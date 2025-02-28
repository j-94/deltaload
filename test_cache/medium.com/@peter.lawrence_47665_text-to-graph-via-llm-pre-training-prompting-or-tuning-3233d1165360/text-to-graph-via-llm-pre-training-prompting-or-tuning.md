---
title: Text-to-Graph via LLM: pre-training, prompting, or tuning?
description: Can unstructured text be translated into structured Knowledge Graphs using LLMs?  Yes, but what is the most efficient and accurate approach: prompting, training, tuning, or hybrid? This article demonstrates each approach and suggests pros/cons for each.
url: https://medium.com/@peter.lawrence_47665/text-to-graph-via-llm-pre-training-prompting-or-tuning-3233d1165360
timestamp: 2025-01-20T15:56:43.965Z
domain: medium.com
path: @peter.lawrence_47665_text-to-graph-via-llm-pre-training-prompting-or-tuning-3233d1165360
---

# Text-to-Graph via LLM: pre-training, prompting, or tuning?


Can unstructured text be translated into structured Knowledge Graphs using LLMs?  Yes, but what is the most efficient and accurate approach: prompting, training, tuning, or hybrid? This article demonstrates each approach and suggests pros/cons for each.


## Content

[![Image 17: Peter Lawrence, answering users' data questions](https://miro.medium.com/v2/resize:fill:88:88/1*Xx1hr19jFcXPzXWi4FMhWA.png)](https://medium.com/@peter.lawrence_47665?source=post_page---byline--3233d1165360--------------------------------)

![Image 18](https://miro.medium.com/v2/resize:fit:700/1*6ZV-b-qXvnQeuHHGiiBWrQ.gif)

Knowledge Graphs are, IMHO, the best way to structure data for any subsequent analysis. The problem is that the majority of data that is available today is in the form of unstructured text.

LLMs have shown their ability to transform unstructured text into a Knowledge Graph. However, the majority of examples I have seen allow the LLM to decide what ontology/schema to use. Some have added restrictions on what properties to use. I want to create graphs that conform to a specific ontology/schema for the following reasons:

*   I will want to create a variety of different queries over the resulting graph. Creating queries without knowledge of the schema is close to impossible.
*   I will want to create graphs from a large number of documents, so large that they cannot be processed as a single prompt despite the increasing size of allowable prompts. I will want all graph responses to conform to the same ontology.

In the past NLP tools were available to extract a graph from unstructured text, but these tools were not easily accessible for casual use.

Previously I demonstrated that this can be done by prompting an LLM with the ontology, but this is token-expensive.

Using LLM to transform unstructured text to KG
----------------------------------------------

I want to describe and compare four approaches that use an LLM to transform unstructured text, responding with a KG that conforms to a pre-defined ontology:

1.  Text-to-Graph using an LLM with pre-trained ontologies
2.  Text-to-Graph prompted an LLM with an ontology
3.  Text-to-Graph using an LLM fine-tuned with an ontology
4.  Text-to-Graph using a hybrid of a fine-tuned and pre-trained LLM

Approach 1: LLM with pre-trained ontologies
-------------------------------------------

![Image 19](https://miro.medium.com/v2/resize:fit:700/1*wICPdF30Z5KPmKTF1ekVEQ.png)

Text-to-Graph Translation using LLM with pre-trained ontologies

LLMs seem to have been pre-trained on a variety of standard ontologies, such as SCHEMA.ORG, FOAF, SKOS, RDF, RDFS, OWL, etc. Thus with a suitable system-prompt that instructs the use of this pre-trained ontology, together with a user-prompt containing the unstructured text we can obtain the transformed graph that we want.

A pre-trained-ontology system-prompt would state:

*   _It should translate the supplied text using the named ontologies_
*   _It follows specific instructions regarding prefixes_

The actual system-prompt is as follows:

Translate the following user text to an RDF graph using the RDF, RDFS, and OWL ontologies formatted as TTL.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.

This system-prompt uses ~41 tokens.

The corresponding user-prompt provides:

*   _<the unstructured text that we want to be transformed into the ontology specified in the system prompt\>_

For example, the user-prompt I shall use as an example is:

Peter Jones and Beth Hampton studied at Brunel University, then married, and had three children: George, James, and Harold.

This user-prompt uses ~26 tokens.

The LLM responds with the following:

@prefix ex: <http://example.com/\> .  
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#\> .  
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#\> .  
@prefix owl: <http://www.w3.org/2002/07/owl#\> .  
ex:PeterJones rdf:type ex:Person ;  
  rdf:label "Peter Jones" .  
ex:BethHampton rdf:type ex:Person ;  
  rdf:label "Beth Hampton" .  
ex:BrunelUniversity rdf:type ex:University ;  
  rdf:label "Brunel University" .  
ex:George rdf:type ex:Person ;  
  rdf:label "George" .  
ex:James rdf:type ex:Person ;  
  rdf:label "James" .  
ex:Harold rdf:type ex:Person ;  
  rdf:label "Harold" .  
ex:PeterJones ex:studiedAt ex:BrunelUniversity ;  
  ex:marriedTo ex:BethHampton ;  
  ex:hasChild ex:George, ex:James, ex:Harold .

Note that the LLM (gpt-3.5-turbo in this case) has no problems creating new properties.

If we modify the system-prompt to suggest the use of only, say, SCHEMA.ORG

Translate the following user text to an RDF graph using the SCHEMA.ORG ontologies formatted as TTL.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.

The LLMs’ assistant-response uses the correct schema classes and properties where possible:

@prefix ex: <http://example.com/\> .  
@prefix schema: <https://schema.org/\> .ex:PeterJones a schema:Person ;  
  schema:spouse ex:BethHampton ;  
  schema:alumniOf ex:BrunelUniversity .

ex:BethHampton a schema:Person ;  
  schema:spouse ex:PeterJones .  
  ex:BrunelUniversity a schema:EducationalOrganization .

ex:George a schema:Person .  
ex:James a schema:Person .  
ex:Harold a schema:Person .

ex:PeterJones schema:children ex:George, ex:James, ex:Harold .  
ex:BethHampton schema:children ex:George, ex:James, ex:Harold .

Pro:
----

*   Depending on the ontologies suggested in the system prompt, the LLM will use defined classes and properties or create (and define) its own.
*   The system prompt can be very concise (~41 tokens), so most of the token cost comprises the unstructured text to be transformed.

Con:
----

*   Transformation is limited to those ‘standard’ ontologies in which the LLM has been pre-trained.  
    \-​​​ ​ ​​​ ​ ​​​ ​I’ve tried asking politely what standard ontologies ChatGPT has been trained on, but the answer was, shall we say, evasive.
*   Entities that are generated in a text-to-graph translation need to be aligned between graphs

Approach 2: LLM prompted with an ontology
-----------------------------------------

![Image 20](https://miro.medium.com/v2/resize:fit:700/1*bbDJqUbmOnNTm511KSti1Q.png)

Text-to-Graph Translation prompting LLM with ontology

There are many situations in which we want to use a non-standard or custom ontology. It is unlikely that the LLM will have been pre-trained on such an ontology, so we will need to include the full ontology in the system-prompt.

A prompted-ontology system-prompt would state:

*   _It translates using the included ontology_
*   _It follows specific instructions regarding prefixes_
*   _It follows instructions to use only pre-defined properties and classes in prompted-ontology (this is to avoid the LLM creating its own)_
*   _Includes the full ontology in TTL format_

The following is a truncated version of this system-prompt. The actual system-prompt includes the full ontology.

Translate the following user text to an RDF graph using the following schema1: <http://inova8.com/schema/1/\> ontologies formatted as TTL.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.  
Only use pre-defined classes and properties from the schema1: <http://inova8.com/schema/1/\> ontology.  
Use the properties and classes in the schema1: ontology.  
Include individuals, their data, and relationships.... the full ontology in TTL format ...

Immediately we see that even this modest ontology greatly increases the system prompt token count to ~3567

With the same user-prompt as before, the LLM does a great job of transforming the text as shown in the assistant-response below:

ex:PeterJones rdf:type schema1:CC ;  
  :dc "Peter" ;  
  :de "Jones" ;  
  :oa ex:BrunelUniversity ;  
  :oh ex:BethHampton ;  
  :of ex:business .  
ex:BethHampton rdf:type schema1:CC ;  
  :dc "Beth" ;  
  :de "Hampton" ;  
  :oa ex:BrunelUniversity ;  
  :oh ex:PeterJones ;  
  :of ex:business .  
ex:BrunelUniversity rdf:type schema1:CA ;  
  rdfs:label "Brunel University" .  
ex:George rdf:type schema1:CC ;  
  rdfs:label "George" ;  
  :od ex:PeterJones ;  
  :od ex:BethHampton .  
ex:James rdf:type schema1:CC ;  
  rdfs:label "James" ;  
  :od ex:PeterJones ;  
  :od ex:BethHampton .  
ex:Harold rdf:type schema1:CC ;  
  rdfs:label "Harold" ;  
  :od ex:PeterJones ;  
  :od ex:BethHampton .  
ex:PeterJones :oh ex:BethHampton .  
ex:BethHampton :oh ex:PeterJones .

Some notes about this ontology:

*   Anonymized qNames were used for properties and classes to avoid the LLM making incorrect deductions about a concept solely from the qName. For example, :CA is a ‘college’, :CC is a Person, etc
*   The ontology included a rdfs:label and a meaningful rdfs:comment for each concept.
*   Shortened qNames were used so that they were tokenized to a single token. For example, CC was used instead of, say, C-3. The former tokenises to 1 token whilst the latter tokenises to 3.

Pro:
----

*   The LLM seems to understand an ontology expressed in RDF, RDFS, and OWL when it is included in the system-prompt.
*   The LLM competently transforms the unstructured text into the custom ontology.  
    \- However, a more ‘advanced’ LLM such as GPT-4 does a better job at creating the second-order (many-to-many) concept of a marriage

Con:
----

*   The system prompt is now very verbose as it has to include all of the custom ontology.
*   There is a significant system-prompt token overhead since the full ontology needs to be included for each fragment of unstructured text in the user-prompt.  
    \- This will increase costs, as cost is proportional to the tokens processed  
    \- This will slow response time, as time is proportional to the tokens to be processed.
*   Entities that are generated in a text-to-graph translation need to be aligned between graphs

Approach 3: LLM fine-tuned with an ontology
-------------------------------------------

![Image 21](https://miro.medium.com/v2/resize:fit:700/1*HEu3y8wDyCmNflTDVBWe2w.png)

Text-to-Graph Translation using LLM fine-tuned with ontology

Being limited to pre-trained ontologies, or having the token overhead when including the custom ontology in the system prompt are significant problems with the previous two approaches.

We know that a well-instructed LLM understands ontologies, and the LLM can use this understanding to transform unstructured text. Therefore it should be possible to train an LLM on other ontologies. Unfortunately, my budget does not stretch to full training, but fine-tuning is well within my reach. However, this creates the problem of creating a suitable tuning dataset.

In previous papers [Knowledge Graphs + Large Language Models = The ability for users to ask their own questions?](https://medium.com/@peter.lawrence_47665/knowledge-graphs-large-language-models-the-ability-for-users-to-ask-their-own-questions-e4afc348fa72), and [Large Language Model = Knowledge Graph Store? Yes, by Fine-Tuning LLM With KG](https://medium.com/better-programming/large-language-model-knowledge-graph-store-yes-by-fine-tuning-llm-with-kg-f88b556959e6) I showed how easily an LLM can be fine-tuned with a graph. In essence a triple from the graph:

{:subject :predicate :object}

Can be mapped to the following system-user-assistant prompts for training. These can be automatically generated from the graph.

{“messages”: \[  
  {"role": "system", "content": "Complete the following graph edge"},  
  {"role": "user", "content": "What is <:subject\> <predicate\>?"},  
  {"role": "assistant", "content": " <:subject\> is <:predicate\> <:object\>."}\]  
}  
…

Our problem is not that of completing the edges of a graph to answer graph queries but is to transform unstructured text into a graph conforming to the custom ontology. This problem is closer to training an LLM to translate from one language (unstructured English text) to another (highly structured RDF-graph using the semantics of the fine-tuned ontology).

Using the examples of language translation datasets that have been used elsewhere, I need to create a dataset with suitable content, such as the following:

> sample system-prompt: “Translate the following user text to an RDF graph using the Schema1 ontology.”
> 
> sample user-prompt:“**{example unstructured text}**”
> 
> sample assistant-response:“**{RDF graph using custom Schema1 ontology semantics}**”

Or in training message format:

messages”: \[  
  {"role": "system", "content": "Translate the following user text to an RDF graph using the Schema1 ontology."},  
  {"role": "user", "content": "{example unstructured text}"},  
  {"role": "assistant", "content": "{RDF graph using custom Schema1 ontology semantics}"}\]  
}  
…

So the challenge is to create a representative set (100~200) of examples and translations to RDF. My journey to successfully create an example dataset is described in the next two sections.

> Plot-spoiler: the first attempt fails dismally

Fine-tuning dataset generator: using ontology templates
-------------------------------------------------------

Reverting to my roots, my first approach was to algorithmically generate unstructured text from a ‘fragment’ of the ontology.

For example, from the following object property ‘fragment’

:of  
  rdf:type owl:ObjectProperty ;  
  rdfs:domain :CC ;  
  rdfs:label "has profession" ;  
  rdfs:comment "The people who do a particular type of work, considered as a group.  
Any type of work that needs special training or a particular skill, often one that is respected because it involves a high level of education" ;  
  rdfs:range :CF .

The following user ‘unstructured’ text was generated with the following template.

{randomDomainInstance},   
  which is a {synonymDomainLabel},   
  has {synonymPropertyLabel} {randonRangeInstance},   
  which is a {synonymRangeLabel}.

An actual example of the algorithmically generated user-text is as follows:

EpentheticShowed,   
  which is a Person,  
  has profession ShelffulKnuckleheads,  
  which is a Profession.

Becomes the following synthesized RDF sample assistant response using the following template:

ex:{randomDomainInstance} rdf:type {domain} ;  
  rdfs:label {randomDomainInstance}  
  {property} ex:{randonRangeInstance} .  
ex:{randonRangeInstance} rdf:type {range} ;  
  rdfs:label {randomRangeInstance} .  
{domain} rdfs:label {domainLabel} .  
{range} rdfs:label {rangeLabel} .  
{property} rdfs:label {propertyLabel} .

An actual example of the algorithmically generated assistant-text is as follows:

ex:EpentheticShowed a :CC ;  
  rdfs:label "EpentheticShowed" ;  
  :of ex:ShelffulKnuckleheads .  
ex:ShelffulKnuckleheads a :CF ;  
  rdfs:label "ShelffulKnuckleheads" ;  
:CC rdfs:label "Person" .  
:CF rdfs:label "Profession" .  
:of rdfs:label "has profession" .

A sample of the dataset that was created can be found here: [https://huggingface.co/datasets/PeterLawrence/inova8.schema.1](https://huggingface.co/datasets/PeterLawrence/inova8.schema.1)

This was used to fine-tune gpt-4, using 3, 10 and 15 epochs. The results in all cases were **very disappointing, and not worth repeating**!

Algorithmic Tuning Dataset Generation Conclusions
-------------------------------------------------

Given the poor results, what was the point in presenting the approach here? Well, even failures are a learning opportunity. Reviewing the sample dataset, the generated text is syntactically correct in that it is correctly structured English. However, it could be more semantically meaningful. For example, I would never guess that **_EpentheticShowed_** or **_ShelffulKnuckleheads_** are the names of people and professions respectively😊. Therefore why should I expect that an LLM can deduce that they are likely to be people and professions?

I conclude that

EpentheticShowed,   
  which is a Person,  
  has profession ShelffulKnuckleheads,  
  which is a Profession.

is too large a distance from a more meaningful tuning example of:

Peter,   
  who is a Person,   
  has a profession Developer,   
  which is a Profession.

Fine-tuning dataset generator: asking an LLM
--------------------------------------------

So my algorithmic approach failed. How can I create meaningful examples from the ontology? Well, the answer was staring me in the face: **ask the LLM!** The request to generate suitable tuning examples was formulated as follows:

The system-prompt contains the role we want the LLM to perform, that is the role of translater of text to graph and includes the ontology, in RDF TTL, to which we want the LLM to be tuned.

So the system-prompt used was (not including the full text of the ontology):

You are a helpful assistant who will use the :Schema1 ontology that follows.   
This schema is called :Schema1 with IRI <http://inova8.com/schema/1/\>…. ontology in TTL ….

The user-prompt tells the LLM that we wish to fine-tune an LLM, and we want example user texts together with the RDF graph into which it would be translated.

I want to fine-tune an LLM on this Schema1 ontology.   
This training aims to take an example user text and the assistant translates it into an RDF graph based on the Schema1 ontology.   
Please create a comprehensive set of 50 example system, user, and assistant messages in JSONL message conversational chat format format for fine-tuning an LLM to translate text to Schema1 ontology RDF.  
The system content should be the instruction to translate the user text to the assistant RDF graph response using Sxchema1 ontology.  
The user text should be examples that cover all the concepts within the Schema1 ontology.  
The assistant content should be an RDF graph using the Schema1 ontology of the translation of the user text examples.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.  
Use the message format as follows:  
  {"messages": \[  
    {"role": "system", "content": "<system\_content\>"},   
    {"role": "user", "content": "<user\_content\>},   
    {"role": "assistant", "content": "<assistant\_content\>"}  
  \]}

As hoped for, the LLM responds with fine-tuning examples as requested. Not only that, the LLM responded in the correct format.

{“messages”: \[  
  {“role”: “system”, “content”: “  
      Translate the following user text to an RDF graph using the Schema1 ontology.”},   
  {“role”: “user”, “content”: “  
      John Smith is a professor who graduated from a reputed college.”},   
  {“role”: “assistant”, “content”: “  
      @prefix ex: <http://example.com/\> .  
      @prefix schema1: <http://inova8.com/schema/1/\> .  
      ex:JohnSmith rdf:type schema1:CC ;  
        schema1:dc \\”John\\” ;  
        schema1:de \\”Smith\\” ;  
        schema1:of schema1:professor ;  
        schema1:oa ex:ReputedCollege .  
      ex:ReputedCollege rdf:type schema1:CA .”}\]}… and so on

Using this I was able to generate a decent-sized (160) translation tuning dataset. With this dataset, I then fine-tuned the LLM using both 3 and 10 epochs.

Questioning the fine-tuned LLM
------------------------------

The proof of any pudding is in the eating. Submitting the same request to translate a fragment of unstructured text to this fine-tuned LLM produces the results that we would expect. Success!

System-prompt (34 tokens):

Translate the following user text to an RDF graph using the Schema1 ontology.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.

User-prompt (28 tokens):

Peter Jones and Beth Hampton both studied at Brunel University, then got married, and have three children: George, James, and Harold.

The LLM’s assistant-response is the translation we had expected:

@prefix ex: <http://example.com/\> .  
ex:PeterJones a schema1:CC ;  
  schema1:dc "Peter" ;  
  schema1:de "Jones" ;  
  schema1:of schema1:student .  
ex:BethHampton a schema1:CC ;  
  schema1:dc "Beth" ;  
  schema1:de "Hampton" ;  
  schema1:of schema1:student .  
ex:JonesHamptonMarriage a schema1:CG ;  
  schema1:og ex:PeterJones ;  
  schema1:oh ex:BethHampton .  
ex:GeorgeJones a schema1:CD ;  
  schema1:dc "George" ;  
  schema1:od ex:PeterJones ;  
  schema1:of ex:BethHampton .  
ex:JamesJones a schema1:CD ;  
  schema1:dc "James" ;  
  schema1:od ex:PeterJones ;  
  schema1:of ex:BethHampton .  
ex:HaroldJones a schema1:CD ;  
  schema1:dc "Harold" ;  
  schema1:od ex:PeterJones ;  
  schema1:of ex:BethHampton .

Note that there seemed to be, qualitatively at least, little difference in the quality of the translations between the 3 and 10-epoch fine-tuned LLM. This is good to know as we do not want to get into the territory of ‘[catastrophic forgetting](https://doi.org/10.48550/arXiv.2308.08747)’ by over-tuning.

Pro:
----

*   An LLM can generate the fine-tuning dataset corresponding to the custom ontology
*   An LLM can be fine-tuned with a custom ontology
*   The system-prompt for a fine-tuned LLM can be very concise (~41 tokens), so most of the token cost is made up of the unstructured text to be transformed.

Con:
----

*   Fine-tuning prompts need to be generated
*   The LLM needs to be fine-tuned
*   We need metrics that measure the LLMs’ accuracy in understanding the custom ontology, and the accuracy of graph translation
*   Entities that are generated in a text-to-graph translation need to be aligned between graphs

Approach 4: Hybrid of fine-tuned and pre-trained
------------------------------------------------

It is often the case that a single ontology/schema is insufficient to capture the full semantics of the text. Therefore we might want to use two or more ontologies. Fortunately, it appears that fine-tuning the LLM with the custom ontology has not caused it to forget the pre-trained ontologies such as FOAF as the following example reveals.

System-prompt, now referring to both pre-trained and fine-tuned ontologies:

Translate the following user text to an RDF graph using both the FOAF, and Schema1 ontologies.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.

User-prompt:

Peter Jones and Beth Hampton both studied at Brunel University, then got married, and have three children: George, James, and Harold.   
Peter, email address peter.jones@inova8.com, has been friends with Paul Williams because of their shared interest in ornithology.

And the LLMs assistant-response uses both ontologies:

@prefix ex: <http://example.com/\> .  
ex:PeterJones a schema1:Thing, foaf:Person ;  
  schema1:email "peter.jones@inova8.com" ;  
  foaf:name "Peter Jones" ;  
  foaf:interest ex:Ornithology .  
ex:BethHampton a schema1:Thing, foaf:Person ;  
  foaf:name "Beth Hampton" .  
ex:GeorgeJones a schema1:Thing, foaf:Person ;  
  foaf:name "George Jones" ;  
  foaf:maker ex:PeterJones .  
ex:JamesJones a schema1:Thing, foaf:Person ;  
  foaf:name "James Jones" ;  
  foaf:maker ex:PeterJones .  
ex:HaroldJones a schema1:Thing, foaf:Person ;  
  foaf:name "Harold Jones" ;  
  foaf:maker ex:PeterJones .  
ex:BrunelUniversity a schema1:Thing, foaf:Document ;  
  foaf:name "Brunel University" .  
ex:JonesHamptonMarriage a schema1:Thing ;  
  schema1:spouse ex:PeterJones, ex:BethHampton .  
ex:JonesHamptonFamily a schema1:Thing ;  
  schema1:parent ex:PeterJones, ex:BethHampton ;  
  schema1:child ex:GeorgeJones, ex:JamesJones, ex:HaroldJones .  
ex:PeterJones foaf:knows ex:PaulWilliams .  
ex:PaulWilliams a schema1:Thing, foaf:Person ;  
  foaf:name "Paul Williams" .

Pro:
----

*   An LLM that is fine-tuned with a custom ontology does not forget its pre-trained ontologies
*   Text-to-graph translation can use a combination of pre-trained and fine-tuned ontologies

Con:
----

*   When concepts overlap between ontologies, we need to control which translation the LLM will use
*   Entities that are generated in a text-to-graph translation need to be aligned between graphs

What have we learnt?
--------------------

*   LLMs can effectively transform unstructured text into an RDF graph.  
    \- Using pre-trained ontologies such as FOAF, and SCHEMA.ORG  
    \- Using custom ontologies in the prompt  
    \- Fine-tuning the LLM with a custom ontology  
    \- A hybrid of pre-trained and fine-tuned ontologies.
*   An LLM can successfully create fine-tuning examples given the ontology in RDF TTL format.
*   Fine-tuning with ~160 examples can be completed in 3 epochs  
    \- This reduces tuning costs  
    \- It also reduces the risk of catastrophic forgetting
*   A custom-ontology fine-tuned model is far more token-efficient as it does not need the overhead of the complete ontology in the prompt with each translation request  
    \- This reduces translation costs in a production environment when multiple texts are to be transformed  
    \- It also improves translation performance.

What have we yet to learn?
--------------------------

*   What is the number of tuning examples and tuning epochs to ‘optimise’ the fine-tuning?
*   Can we establish a text-to-graph transformation ‘accuracy’ test so that we can perform some quantitative tests?
*   The transformed text will include newly created entities. These will have to be aligned across multiple responses.  
    \- Is this a task for existing entity alignment tools like [SILK](http://silkframework.org/)?  
    \- Is this something we can ask the LLM to do as part of the graph post-processing?

Where to next?
--------------

*   The LLM capabilities of transforming text to RDF graphs have been explored using state-of-the-art LLMs.  
    \- We need to take these learnings and apply them to open-source and smaller LLMs such as Mistral-7B and OpenHermes. Initial results look very promising.
*   It would be nice to have **quantitative** measures of text-to-graph transformation performance. For example:  
    \- How many samples per ontology concept ( 160/54 in these examples) are required for fine-tuning?  
    \- How many epochs are required (3 and 10 used in these examples)?  
    \- How does the response token rate vary between pre-trained, fine-tuned, and prompted?

Summary
-------

![Image 22](https://miro.medium.com/v2/resize:fit:700/1*mAfQJ-FCRrHF9zXtuzQqtA.png)

Prompt Details
--------------

Including the LLM prompts and responses within the body of this article makes it difficult to read. Therefore I have included the prompts here, leaving a description of the prompt within the main text.

Approach 1: LLM with pre-trained ontologies
-------------------------------------------

Request for Text-to-Graph Translation using RDF, RDFS, and OWL Ontologies
-------------------------------------------------------------------------

RDF, RDFS, and OWL System Prompt
--------------------------------

Translate the following user text to an RDF graph using the RDF, RDFS, and OWL ontologies formatted as TTL.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.

RDF, RDFS, and OWL User Prompt
------------------------------

Peter Jones and Beth Hampton studied at Brunel University, then married, and had three children: George, James, and Harold.

RDF, RDFS, and OWL Assistant Response
-------------------------------------

@prefix ex: <http://example.com/\> .  
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#\> .  
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#\> .  
@prefix owl: <http://www.w3.org/2002/07/owl#\> .  
ex:PeterJones rdf:type ex:Person ;  
rdf:label "Peter Jones" .  
ex:BethHampton rdf:type ex:Person ;  
rdf:label "Beth Hampton" .  
ex:BrunelUniversity rdf:type ex:University ;  
rdf:label "Brunel University" .  
ex:George rdf:type ex:Person ;  
rdf:label "George" .  
ex:James rdf:type ex:Person ;  
rdf:label "James" .  
ex:Harold rdf:type ex:Person ;  
rdf:label "Harold" .  
ex:PeterJones ex:studiedAt ex:BrunelUniversity ;  
ex:marriedTo ex:BethHampton ;  
ex:hasChild ex:George, ex:James, ex:Harold .

Request for Text-to-Graph Translation using SCHEMA.ORG
------------------------------------------------------

SCHEMA.ORG System Prompt
------------------------

Translate the following user text to an RDF graph using the SCHEMA.ORG ontologies formatted as TTL.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.

SCHEMA.ORG User Prompt
----------------------

Peter Jones and Beth Hampton studied at Brunel University, then married, and had three children: George, James, and Harold.

SCHEMA.ORG Assistant Response
-----------------------------

@prefix ex: <http://example.com/\> .  
@prefix schema: <https://schema.org/\> .  
ex:PeterJones a schema:Person ;  
schema:spouse ex:BethHampton ;  
schema:alumniOf ex:BrunelUniversity .  
ex:BethHampton a schema:Person ;  
schema:spouse ex:PeterJones .  
ex:BrunelUniversity a schema:EducationalOrganization .  
ex:George a schema:Person .  
ex:James a schema:Person .  
ex:Harold a schema:Person .  
ex:PeterJones schema:children ex:George, ex:James, ex:Harold .  
ex:BethHampton schema:children ex:George, ex:James, ex:Harold .

Approach 2: LLM prompted with an ontology
-----------------------------------------

Request for Text-to-Graph Translation providing an ontology
-----------------------------------------------------------

Provided Ontology System Prompt
-------------------------------

Translate the following user text to an RDF graph using the following schema1: <http://inova8.com/schema/1/\> ontologies formatted as TTL.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.  
Only use pre-defined classes and properties from the schema1: <http://inova8.com/schema/1/\> ontology.  
Use the properties and classes in the schema1: ontology.  
Include individuals, their data, and relationships.  
@prefix : <http://inova8.com/schema/1/\> .  
@prefix owl: <http://www.w3.org/2002/07/owl#\> .  
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#\> .  
@prefix xml: <http://www.w3.org/XML/1998/namespace\> .  
@prefix xsd: <http://www.w3.org/2001/XMLSchema#\> .  
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#\> .  
@prefix schema1: <http://inova8.com/schema/1/\> .  
@base <http://inova8.com/schema/1/\> .  
<http://inova8.com/schema/1/\> rdf:type owl:Ontology .  
#################################################################  
\# Object Properties  
#################################################################  
\### http://inova8.com/schema/1/oa  
schema1:oa rdf:type owl:ObjectProperty ;  
  rdfs:domain schema1:CC ;  
  rdfs:range schema1:CA ;  
  rdfs:comment """The university, school, or college that one formerly attended.  
\\"he started teaching at his alma mater\\"""" ;  
  rdfs:label "alma mater" .  
\### http://inova8.com/schema/1/ob  
schema1:ob rdf:type owl:ObjectProperty ;  
  rdfs:domain schema1:CC ;  
  rdfs:range schema1:CC ;  
  rdfs:comment "Inverse of 'parent'" ;  
  rdfs:label "child" .  
…  
#################################################################  
\# Data properties  
#################################################################  
\### http://inova8.com/schema/1/da  
schema1:da rdf:type owl:DatatypeProperty ;  
  rdfs:domain schema1:CC ;  
  rdfs:range xsd:int ;  
  rdfs:comment "The day they were born, shown in numbers, or words and numbers" ;  
  rdfs:label "year of birth" .  
\### http://inova8.com/schema/1/db  
schema1:db rdf:type owl:DatatypeProperty ;  
  rdfs:domain schema1:CC ;  
  rdfs:range xsd:int ;  
  rdfs:comment "The day they died, shown in numbers, or words and numbers" ;  
  rdfs:label "year of death" .  
\### http://inova8.com/schema/1/dc  
schema1:dc rdf:type owl:DatatypeProperty ;  
  rdfs:domain schema1:CC ;  
  rdfs:range xsd:string ;  
  rdfs:comment "The name that was given to you when you were born and that comes before your family name:" ;  
  rdfs:label "first name" .  
…  
#################################################################  
\# Classes  
#################################################################  
\### http://inova8.com/schema/1/CA  
schema1:CA rdf:type owl:Class ;  
  rdfs:subClassOf owl:Thing ;  
  rdfs:label "College" .  
…  
\### http://inova8.com/schema/1/CF  
schema1:CF rdf:type owl:Class ;  
  rdfs:subClassOf owl:Thing ;  
  rdfs:label "Profession" .  
\### http://inova8.com/schema/1/CG  
schema1:CG rdf:type owl:Class ;  
  rdfs:subClassOf owl:Thing ;  
  rdfs:label "Marriage" .  
#################################################################  
\# Individuals  
#################################################################  
\### http://inova8.com/schema/1/Lt-governor  
schema1:Lt-governor rdf:type owl:NamedIndividual ,  
  schema1:CF ;  
  rdfs:label "Lt-governor" .  
\### http://inova8.com/schema/1/PR  
schema1:PR rdf:type owl:NamedIndividual ,  
…  
  schema1:CF ;  
  rdfs:label "PR" .

Provided Ontology User Prompt
-----------------------------

Peter Jones and Beth Hampton studied at Brunel University, then married, and had three children: George, James, and Harold.

Provided Ontology Assistant Response
------------------------------------

ex:PeterJones rdf:type schema1:CC ;  
  :dc "Peter" ;  
  :de "Jones" ;  
  :oa ex:BrunelUniversity ;  
  :oh ex:BethHampton ;  
  :of ex:business .  
ex:BethHampton rdf:type schema1:CC ;  
  :dc "Beth" ;  
  :de "Hampton" ;  
  :oa ex:BrunelUniversity ;  
  :oh ex:PeterJones ;  
  :of ex:business .  
ex:BrunelUniversity rdf:type schema1:CA ;  
  rdfs:label "Brunel University" .  
ex:George rdf:type schema1:CC ;  
  rdfs:label "George" ;  
  :od ex:PeterJones ;  
  :od ex:BethHampton .  
ex:James rdf:type schema1:CC ;  
  rdfs:label "James" ;  
  :od ex:PeterJones ;  
  :od ex:BethHampton .  
ex:Harold rdf:type schema1:CC ;  
  rdfs:label "Harold" ;  
  :od ex:PeterJones ;  
  :od ex:BethHampton .  
ex:PeterJones :oh ex:BethHampton .  
ex:BethHampton :oh ex:PeterJones .

Approach 3: LLM fine-tuned with an ontology
-------------------------------------------

Request for Fine-Tuning Examples
--------------------------------

Tuning Example Request System Prompt
------------------------------------

You are a helpful assistant who will use the :Schema1 ontology that follows. This schema is called  
:Schema1 with IRI <http://inova8.com/schema/1/\>  
…. ontology in TTL …. 

Tuning Example Request User Prompt
----------------------------------

I want to fine-tune an LLM on this Schema1 ontology. This training aims to take an example user text and the assistant translates it into an RDF graph based on the Schema1 ontology. Please create a comprehensive set of 50 example system, user, and assistant messages in JSONL message conversational chat format format for fine-tuning an LLM to translate text to Schema1 ontology RDF.  
The system content should be the instruction to translate the user text to the assistant RDF graph response using Sxchema1 ontology.  
The user text should be examples that cover all the concepts within the Schema1 ontology.  
The assistant content should be an RDF graph using the Schema1 ontology of the translation of the user text examples.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.  
Use the message format as follows:  
{"messages": \[{"role": "system", "content": "<system\_content\>"}, {"role": "user", "content": "<user\_content\>}, {"role": "assistant", "content": "<assistant\_content\>"}\]}

Tuning Example Request Assistant Response
-----------------------------------------

{“messages”: \[  
  {“role”: “system”, “content”: “Translate the following user text to an RDF graph using the Schema1 ontology.”},   
  {“role”: “user”, “content”: “John Smith is a professor who graduated from a reputed college.”},   
  {“role”: “assistant”, “content”: “@prefix ex: <http://example.com/\> .\\n@prefix schema1: <http://inova8.com/schema/1/\> .\\nex:JohnSmith rdf:type schema1:CC ;\\nschema1:dc \\”John\\” ;\\nschema1:de \\”Smith\\” ;\\nschema1:of schema1:professor ;\\nschema1:oa ex:ReputedCollege .\\nex:ReputedCollege rdf:type schema1:CA .”}  
  \]  
}  
… and so on

Request for Text-to-Graph Translation using fine-tuned LLM
----------------------------------------------------------

Fine-tuned Ontology System Prompt
---------------------------------

Translate the following user text to an RDF graph using the Schema1 ontology.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.

Fine-tuned Ontology User Prompt
-------------------------------

Peter Jones and Beth Hampton both studied at Brunel University, then got married, and have three children: George, James, and Harold.

Fine-tuned Ontology Assistant Response
--------------------------------------

@prefix ex: <http://example.com/\> .  
ex:PeterJones a schema1:CC ;  
  schema1:dc "Peter" ;  
  schema1:de "Jones" ;  
  schema1:of schema1:student .  
ex:BethHampton a schema1:CC ;  
  schema1:dc "Beth" ;  
  schema1:de "Hampton" ;  
  schema1:of schema1:student .  
ex:JonesHamptonMarriage a schema1:CG ;  
  schema1:og ex:PeterJones ;  
  schema1:oh ex:BethHampton .  
ex:GeorgeJones a schema1:CD ;  
  schema1:dc "George" ;  
  schema1:od ex:PeterJones ;  
  schema1:of ex:BethHampton .  
ex:JamesJones a schema1:CD ;  
  schema1:dc "James" ;  
  schema1:od ex:PeterJones ;  
  schema1:of ex:BethHampton .  
ex:HaroldJones a schema1:CD ;  
  schema1:dc "Harold" ;  
  schema1:od ex:PeterJones ;  
  schema1:of ex:BethHampton

Approach 4: Hybrid of fine-tuned and pre-trained
------------------------------------------------

Request for Text-to-Graph Translation using fine-tuned LLM and FOAF
-------------------------------------------------------------------

Hybrid System Prompt
--------------------

Translate the following user text to an RDF graph using both the FOAF, and Schema1 ontologies.  
Use the prefix ex: with IRI <http://example.com/\> for any created entities.

Hybrid User Prompt
------------------

Peter Jones and Beth Hampton both studied at Brunel University, then got married, and have three children: George, James, and Harold.   
Peter, email address peter.jones@inova8.com, has been friends with Paul Williams because of their shared interest in ornithology.

Hybrid Assistant Response
-------------------------

@prefix ex: <http://example.com/\> .  
ex:PeterJones a schema1:Thing, foaf:Person ;  
  schema1:email "peter.jones@inova8.com" ;  
  foaf:name "Peter Jones" ;  
  foaf:interest ex:Ornithology .  
ex:BethHampton a schema1:Thing, foaf:Person ;  
  foaf:name "Beth Hampton" .  
ex:GeorgeJones a schema1:Thing, foaf:Person ;  
  foaf:name "George Jones" ;  
  foaf:maker ex:PeterJones .  
ex:JamesJones a schema1:Thing, foaf:Person ;  
  foaf:name "James Jones" ;   
  foaf:maker ex:PeterJones .  
ex:HaroldJones a schema1:Thing, foaf:Person ;  
  foaf:name "Harold Jones" ;  
  foaf:maker ex:PeterJones .  
  ex:BrunelUniversity a schema1:Thing, foaf:Document ;  
foaf:name "Brunel University" .  
ex:JonesHamptonMarriage a schema1:Thing ;  
  schema1:spouse ex:PeterJones, ex:BethHampton .  
  ex:JonesHamptonFamily a schema1:Thing ;  
  schema1:parent ex:PeterJones, ex:BethHampton ;  
  schema1:child ex:GeorgeJones, ex:JamesJones, ex:HaroldJones .  
ex:PeterJones foaf:knows ex:PaulWilliams .  
ex:PaulWilliams a schema1:Thing, foaf:Person ;  
  foaf:name "Paul Williams" .

## Metadata

```json
{
  "title": "Text-to-Graph via LLM: pre-training, prompting, or tuning?",
  "description": "Can unstructured text be translated into structured Knowledge Graphs using LLMs?  Yes, but what is the most efficient and accurate approach: prompting, training, tuning, or hybrid? This article demonstrates each approach and suggests pros/cons for each.",
  "url": "https://medium.com/@peter.lawrence_47665/text-to-graph-via-llm-pre-training-prompting-or-tuning-3233d1165360",
  "content": "[![Image 17: Peter Lawrence, answering users' data questions](https://miro.medium.com/v2/resize:fill:88:88/1*Xx1hr19jFcXPzXWi4FMhWA.png)](https://medium.com/@peter.lawrence_47665?source=post_page---byline--3233d1165360--------------------------------)\n\n![Image 18](https://miro.medium.com/v2/resize:fit:700/1*6ZV-b-qXvnQeuHHGiiBWrQ.gif)\n\nKnowledge Graphs are, IMHO, the best way to structure data for any subsequent analysis. The problem is that the majority of data that is available today is in the form of unstructured text.\n\nLLMs have shown their ability to transform unstructured text into a Knowledge Graph. However, the majority of examples I have seen allow the LLM to decide what ontology/schema to use. Some have added restrictions on what properties to use. I want to create graphs that conform to a specific ontology/schema for the following reasons:\n\n*   I will want to create a variety of different queries over the resulting graph. Creating queries without knowledge of the schema is close to impossible.\n*   I will want to create graphs from a large number of documents, so large that they cannot be processed as a single prompt despite the increasing size of allowable prompts. I will want all graph responses to conform to the same ontology.\n\nIn the past NLP tools were available to extract a graph from unstructured text, but these tools were not easily accessible for casual use.\n\nPreviously I demonstrated that this can be done by prompting an LLM with the ontology, but this is token-expensive.\n\nUsing LLM to transform unstructured text to KG\n----------------------------------------------\n\nI want to describe and compare four approaches that use an LLM to transform unstructured text, responding with a KG that conforms to a pre-defined ontology:\n\n1.  Text-to-Graph using an LLM with pre-trained ontologies\n2.  Text-to-Graph prompted an LLM with an ontology\n3.  Text-to-Graph using an LLM fine-tuned with an ontology\n4.  Text-to-Graph using a hybrid of a fine-tuned and pre-trained LLM\n\nApproach 1: LLM with pre-trained ontologies\n-------------------------------------------\n\n![Image 19](https://miro.medium.com/v2/resize:fit:700/1*wICPdF30Z5KPmKTF1ekVEQ.png)\n\nText-to-Graph Translation using LLM with pre-trained ontologies\n\nLLMs seem to have been pre-trained on a variety of standard ontologies, such as SCHEMA.ORG, FOAF, SKOS, RDF, RDFS, OWL, etc. Thus with a suitable system-prompt that instructs the use of this pre-trained ontology, together with a user-prompt containing the unstructured text we can obtain the transformed graph that we want.\n\nA pre-trained-ontology system-prompt would state:\n\n*   _It should translate the supplied text using the named ontologies_\n*   _It follows specific instructions regarding prefixes_\n\nThe actual system-prompt is as follows:\n\nTranslate the following user text to an RDF graph using the RDF, RDFS, and OWL ontologies formatted as TTL.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.\n\nThis system-prompt uses ~41 tokens.\n\nThe corresponding user-prompt provides:\n\n*   _<the unstructured text that we want to be transformed into the ontology specified in the system prompt\\>_\n\nFor example, the user-prompt I shall use as an example is:\n\nPeter Jones and Beth Hampton studied at Brunel University, then married, and had three children: George, James, and Harold.\n\nThis user-prompt uses ~26 tokens.\n\nThe LLM responds with the following:\n\n@prefix ex: <http://example.com/\\> .  \n@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#\\> .  \n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#\\> .  \n@prefix owl: <http://www.w3.org/2002/07/owl#\\> .  \nex:PeterJones rdf:type ex:Person ;  \n  rdf:label \"Peter Jones\" .  \nex:BethHampton rdf:type ex:Person ;  \n  rdf:label \"Beth Hampton\" .  \nex:BrunelUniversity rdf:type ex:University ;  \n  rdf:label \"Brunel University\" .  \nex:George rdf:type ex:Person ;  \n  rdf:label \"George\" .  \nex:James rdf:type ex:Person ;  \n  rdf:label \"James\" .  \nex:Harold rdf:type ex:Person ;  \n  rdf:label \"Harold\" .  \nex:PeterJones ex:studiedAt ex:BrunelUniversity ;  \n  ex:marriedTo ex:BethHampton ;  \n  ex:hasChild ex:George, ex:James, ex:Harold .\n\nNote that the LLM (gpt-3.5-turbo in this case) has no problems creating new properties.\n\nIf we modify the system-prompt to suggest the use of only, say, SCHEMA.ORG\n\nTranslate the following user text to an RDF graph using the SCHEMA.ORG ontologies formatted as TTL.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.\n\nThe LLMs’ assistant-response uses the correct schema classes and properties where possible:\n\n@prefix ex: <http://example.com/\\> .  \n@prefix schema: <https://schema.org/\\> .ex:PeterJones a schema:Person ;  \n  schema:spouse ex:BethHampton ;  \n  schema:alumniOf ex:BrunelUniversity .\n\nex:BethHampton a schema:Person ;  \n  schema:spouse ex:PeterJones .  \n  ex:BrunelUniversity a schema:EducationalOrganization .\n\nex:George a schema:Person .  \nex:James a schema:Person .  \nex:Harold a schema:Person .\n\nex:PeterJones schema:children ex:George, ex:James, ex:Harold .  \nex:BethHampton schema:children ex:George, ex:James, ex:Harold .\n\nPro:\n----\n\n*   Depending on the ontologies suggested in the system prompt, the LLM will use defined classes and properties or create (and define) its own.\n*   The system prompt can be very concise (~41 tokens), so most of the token cost comprises the unstructured text to be transformed.\n\nCon:\n----\n\n*   Transformation is limited to those ‘standard’ ontologies in which the LLM has been pre-trained.  \n    \\-​​​ ​ ​​​ ​ ​​​ ​I’ve tried asking politely what standard ontologies ChatGPT has been trained on, but the answer was, shall we say, evasive.\n*   Entities that are generated in a text-to-graph translation need to be aligned between graphs\n\nApproach 2: LLM prompted with an ontology\n-----------------------------------------\n\n![Image 20](https://miro.medium.com/v2/resize:fit:700/1*bbDJqUbmOnNTm511KSti1Q.png)\n\nText-to-Graph Translation prompting LLM with ontology\n\nThere are many situations in which we want to use a non-standard or custom ontology. It is unlikely that the LLM will have been pre-trained on such an ontology, so we will need to include the full ontology in the system-prompt.\n\nA prompted-ontology system-prompt would state:\n\n*   _It translates using the included ontology_\n*   _It follows specific instructions regarding prefixes_\n*   _It follows instructions to use only pre-defined properties and classes in prompted-ontology (this is to avoid the LLM creating its own)_\n*   _Includes the full ontology in TTL format_\n\nThe following is a truncated version of this system-prompt. The actual system-prompt includes the full ontology.\n\nTranslate the following user text to an RDF graph using the following schema1: <http://inova8.com/schema/1/\\> ontologies formatted as TTL.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.  \nOnly use pre-defined classes and properties from the schema1: <http://inova8.com/schema/1/\\> ontology.  \nUse the properties and classes in the schema1: ontology.  \nInclude individuals, their data, and relationships.... the full ontology in TTL format ...\n\nImmediately we see that even this modest ontology greatly increases the system prompt token count to ~3567\n\nWith the same user-prompt as before, the LLM does a great job of transforming the text as shown in the assistant-response below:\n\nex:PeterJones rdf:type schema1:CC ;  \n  :dc \"Peter\" ;  \n  :de \"Jones\" ;  \n  :oa ex:BrunelUniversity ;  \n  :oh ex:BethHampton ;  \n  :of ex:business .  \nex:BethHampton rdf:type schema1:CC ;  \n  :dc \"Beth\" ;  \n  :de \"Hampton\" ;  \n  :oa ex:BrunelUniversity ;  \n  :oh ex:PeterJones ;  \n  :of ex:business .  \nex:BrunelUniversity rdf:type schema1:CA ;  \n  rdfs:label \"Brunel University\" .  \nex:George rdf:type schema1:CC ;  \n  rdfs:label \"George\" ;  \n  :od ex:PeterJones ;  \n  :od ex:BethHampton .  \nex:James rdf:type schema1:CC ;  \n  rdfs:label \"James\" ;  \n  :od ex:PeterJones ;  \n  :od ex:BethHampton .  \nex:Harold rdf:type schema1:CC ;  \n  rdfs:label \"Harold\" ;  \n  :od ex:PeterJones ;  \n  :od ex:BethHampton .  \nex:PeterJones :oh ex:BethHampton .  \nex:BethHampton :oh ex:PeterJones .\n\nSome notes about this ontology:\n\n*   Anonymized qNames were used for properties and classes to avoid the LLM making incorrect deductions about a concept solely from the qName. For example, :CA is a ‘college’, :CC is a Person, etc\n*   The ontology included a rdfs:label and a meaningful rdfs:comment for each concept.\n*   Shortened qNames were used so that they were tokenized to a single token. For example, CC was used instead of, say, C-3. The former tokenises to 1 token whilst the latter tokenises to 3.\n\nPro:\n----\n\n*   The LLM seems to understand an ontology expressed in RDF, RDFS, and OWL when it is included in the system-prompt.\n*   The LLM competently transforms the unstructured text into the custom ontology.  \n    \\- However, a more ‘advanced’ LLM such as GPT-4 does a better job at creating the second-order (many-to-many) concept of a marriage\n\nCon:\n----\n\n*   The system prompt is now very verbose as it has to include all of the custom ontology.\n*   There is a significant system-prompt token overhead since the full ontology needs to be included for each fragment of unstructured text in the user-prompt.  \n    \\- This will increase costs, as cost is proportional to the tokens processed  \n    \\- This will slow response time, as time is proportional to the tokens to be processed.\n*   Entities that are generated in a text-to-graph translation need to be aligned between graphs\n\nApproach 3: LLM fine-tuned with an ontology\n-------------------------------------------\n\n![Image 21](https://miro.medium.com/v2/resize:fit:700/1*HEu3y8wDyCmNflTDVBWe2w.png)\n\nText-to-Graph Translation using LLM fine-tuned with ontology\n\nBeing limited to pre-trained ontologies, or having the token overhead when including the custom ontology in the system prompt are significant problems with the previous two approaches.\n\nWe know that a well-instructed LLM understands ontologies, and the LLM can use this understanding to transform unstructured text. Therefore it should be possible to train an LLM on other ontologies. Unfortunately, my budget does not stretch to full training, but fine-tuning is well within my reach. However, this creates the problem of creating a suitable tuning dataset.\n\nIn previous papers [Knowledge Graphs + Large Language Models = The ability for users to ask their own questions?](https://medium.com/@peter.lawrence_47665/knowledge-graphs-large-language-models-the-ability-for-users-to-ask-their-own-questions-e4afc348fa72), and [Large Language Model = Knowledge Graph Store? Yes, by Fine-Tuning LLM With KG](https://medium.com/better-programming/large-language-model-knowledge-graph-store-yes-by-fine-tuning-llm-with-kg-f88b556959e6) I showed how easily an LLM can be fine-tuned with a graph. In essence a triple from the graph:\n\n{:subject :predicate :object}\n\nCan be mapped to the following system-user-assistant prompts for training. These can be automatically generated from the graph.\n\n{“messages”: \\[  \n  {\"role\": \"system\", \"content\": \"Complete the following graph edge\"},  \n  {\"role\": \"user\", \"content\": \"What is <:subject\\> <predicate\\>?\"},  \n  {\"role\": \"assistant\", \"content\": \" <:subject\\> is <:predicate\\> <:object\\>.\"}\\]  \n}  \n…\n\nOur problem is not that of completing the edges of a graph to answer graph queries but is to transform unstructured text into a graph conforming to the custom ontology. This problem is closer to training an LLM to translate from one language (unstructured English text) to another (highly structured RDF-graph using the semantics of the fine-tuned ontology).\n\nUsing the examples of language translation datasets that have been used elsewhere, I need to create a dataset with suitable content, such as the following:\n\n> sample system-prompt: “Translate the following user text to an RDF graph using the Schema1 ontology.”\n> \n> sample user-prompt:“**{example unstructured text}**”\n> \n> sample assistant-response:“**{RDF graph using custom Schema1 ontology semantics}**”\n\nOr in training message format:\n\nmessages”: \\[  \n  {\"role\": \"system\", \"content\": \"Translate the following user text to an RDF graph using the Schema1 ontology.\"},  \n  {\"role\": \"user\", \"content\": \"{example unstructured text}\"},  \n  {\"role\": \"assistant\", \"content\": \"{RDF graph using custom Schema1 ontology semantics}\"}\\]  \n}  \n…\n\nSo the challenge is to create a representative set (100~200) of examples and translations to RDF. My journey to successfully create an example dataset is described in the next two sections.\n\n> Plot-spoiler: the first attempt fails dismally\n\nFine-tuning dataset generator: using ontology templates\n-------------------------------------------------------\n\nReverting to my roots, my first approach was to algorithmically generate unstructured text from a ‘fragment’ of the ontology.\n\nFor example, from the following object property ‘fragment’\n\n:of  \n  rdf:type owl:ObjectProperty ;  \n  rdfs:domain :CC ;  \n  rdfs:label \"has profession\" ;  \n  rdfs:comment \"The people who do a particular type of work, considered as a group.  \nAny type of work that needs special training or a particular skill, often one that is respected because it involves a high level of education\" ;  \n  rdfs:range :CF .\n\nThe following user ‘unstructured’ text was generated with the following template.\n\n{randomDomainInstance},   \n  which is a {synonymDomainLabel},   \n  has {synonymPropertyLabel} {randonRangeInstance},   \n  which is a {synonymRangeLabel}.\n\nAn actual example of the algorithmically generated user-text is as follows:\n\nEpentheticShowed,   \n  which is a Person,  \n  has profession ShelffulKnuckleheads,  \n  which is a Profession.\n\nBecomes the following synthesized RDF sample assistant response using the following template:\n\nex:{randomDomainInstance} rdf:type {domain} ;  \n  rdfs:label {randomDomainInstance}  \n  {property} ex:{randonRangeInstance} .  \nex:{randonRangeInstance} rdf:type {range} ;  \n  rdfs:label {randomRangeInstance} .  \n{domain} rdfs:label {domainLabel} .  \n{range} rdfs:label {rangeLabel} .  \n{property} rdfs:label {propertyLabel} .\n\nAn actual example of the algorithmically generated assistant-text is as follows:\n\nex:EpentheticShowed a :CC ;  \n  rdfs:label \"EpentheticShowed\" ;  \n  :of ex:ShelffulKnuckleheads .  \nex:ShelffulKnuckleheads a :CF ;  \n  rdfs:label \"ShelffulKnuckleheads\" ;  \n:CC rdfs:label \"Person\" .  \n:CF rdfs:label \"Profession\" .  \n:of rdfs:label \"has profession\" .\n\nA sample of the dataset that was created can be found here: [https://huggingface.co/datasets/PeterLawrence/inova8.schema.1](https://huggingface.co/datasets/PeterLawrence/inova8.schema.1)\n\nThis was used to fine-tune gpt-4, using 3, 10 and 15 epochs. The results in all cases were **very disappointing, and not worth repeating**!\n\nAlgorithmic Tuning Dataset Generation Conclusions\n-------------------------------------------------\n\nGiven the poor results, what was the point in presenting the approach here? Well, even failures are a learning opportunity. Reviewing the sample dataset, the generated text is syntactically correct in that it is correctly structured English. However, it could be more semantically meaningful. For example, I would never guess that **_EpentheticShowed_** or **_ShelffulKnuckleheads_** are the names of people and professions respectively😊. Therefore why should I expect that an LLM can deduce that they are likely to be people and professions?\n\nI conclude that\n\nEpentheticShowed,   \n  which is a Person,  \n  has profession ShelffulKnuckleheads,  \n  which is a Profession.\n\nis too large a distance from a more meaningful tuning example of:\n\nPeter,   \n  who is a Person,   \n  has a profession Developer,   \n  which is a Profession.\n\nFine-tuning dataset generator: asking an LLM\n--------------------------------------------\n\nSo my algorithmic approach failed. How can I create meaningful examples from the ontology? Well, the answer was staring me in the face: **ask the LLM!** The request to generate suitable tuning examples was formulated as follows:\n\nThe system-prompt contains the role we want the LLM to perform, that is the role of translater of text to graph and includes the ontology, in RDF TTL, to which we want the LLM to be tuned.\n\nSo the system-prompt used was (not including the full text of the ontology):\n\nYou are a helpful assistant who will use the :Schema1 ontology that follows.   \nThis schema is called :Schema1 with IRI <http://inova8.com/schema/1/\\>…. ontology in TTL ….\n\nThe user-prompt tells the LLM that we wish to fine-tune an LLM, and we want example user texts together with the RDF graph into which it would be translated.\n\nI want to fine-tune an LLM on this Schema1 ontology.   \nThis training aims to take an example user text and the assistant translates it into an RDF graph based on the Schema1 ontology.   \nPlease create a comprehensive set of 50 example system, user, and assistant messages in JSONL message conversational chat format format for fine-tuning an LLM to translate text to Schema1 ontology RDF.  \nThe system content should be the instruction to translate the user text to the assistant RDF graph response using Sxchema1 ontology.  \nThe user text should be examples that cover all the concepts within the Schema1 ontology.  \nThe assistant content should be an RDF graph using the Schema1 ontology of the translation of the user text examples.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.  \nUse the message format as follows:  \n  {\"messages\": \\[  \n    {\"role\": \"system\", \"content\": \"<system\\_content\\>\"},   \n    {\"role\": \"user\", \"content\": \"<user\\_content\\>},   \n    {\"role\": \"assistant\", \"content\": \"<assistant\\_content\\>\"}  \n  \\]}\n\nAs hoped for, the LLM responds with fine-tuning examples as requested. Not only that, the LLM responded in the correct format.\n\n{“messages”: \\[  \n  {“role”: “system”, “content”: “  \n      Translate the following user text to an RDF graph using the Schema1 ontology.”},   \n  {“role”: “user”, “content”: “  \n      John Smith is a professor who graduated from a reputed college.”},   \n  {“role”: “assistant”, “content”: “  \n      @prefix ex: <http://example.com/\\> .  \n      @prefix schema1: <http://inova8.com/schema/1/\\> .  \n      ex:JohnSmith rdf:type schema1:CC ;  \n        schema1:dc \\\\”John\\\\” ;  \n        schema1:de \\\\”Smith\\\\” ;  \n        schema1:of schema1:professor ;  \n        schema1:oa ex:ReputedCollege .  \n      ex:ReputedCollege rdf:type schema1:CA .”}\\]}… and so on\n\nUsing this I was able to generate a decent-sized (160) translation tuning dataset. With this dataset, I then fine-tuned the LLM using both 3 and 10 epochs.\n\nQuestioning the fine-tuned LLM\n------------------------------\n\nThe proof of any pudding is in the eating. Submitting the same request to translate a fragment of unstructured text to this fine-tuned LLM produces the results that we would expect. Success!\n\nSystem-prompt (34 tokens):\n\nTranslate the following user text to an RDF graph using the Schema1 ontology.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.\n\nUser-prompt (28 tokens):\n\nPeter Jones and Beth Hampton both studied at Brunel University, then got married, and have three children: George, James, and Harold.\n\nThe LLM’s assistant-response is the translation we had expected:\n\n@prefix ex: <http://example.com/\\> .  \nex:PeterJones a schema1:CC ;  \n  schema1:dc \"Peter\" ;  \n  schema1:de \"Jones\" ;  \n  schema1:of schema1:student .  \nex:BethHampton a schema1:CC ;  \n  schema1:dc \"Beth\" ;  \n  schema1:de \"Hampton\" ;  \n  schema1:of schema1:student .  \nex:JonesHamptonMarriage a schema1:CG ;  \n  schema1:og ex:PeterJones ;  \n  schema1:oh ex:BethHampton .  \nex:GeorgeJones a schema1:CD ;  \n  schema1:dc \"George\" ;  \n  schema1:od ex:PeterJones ;  \n  schema1:of ex:BethHampton .  \nex:JamesJones a schema1:CD ;  \n  schema1:dc \"James\" ;  \n  schema1:od ex:PeterJones ;  \n  schema1:of ex:BethHampton .  \nex:HaroldJones a schema1:CD ;  \n  schema1:dc \"Harold\" ;  \n  schema1:od ex:PeterJones ;  \n  schema1:of ex:BethHampton .\n\nNote that there seemed to be, qualitatively at least, little difference in the quality of the translations between the 3 and 10-epoch fine-tuned LLM. This is good to know as we do not want to get into the territory of ‘[catastrophic forgetting](https://doi.org/10.48550/arXiv.2308.08747)’ by over-tuning.\n\nPro:\n----\n\n*   An LLM can generate the fine-tuning dataset corresponding to the custom ontology\n*   An LLM can be fine-tuned with a custom ontology\n*   The system-prompt for a fine-tuned LLM can be very concise (~41 tokens), so most of the token cost is made up of the unstructured text to be transformed.\n\nCon:\n----\n\n*   Fine-tuning prompts need to be generated\n*   The LLM needs to be fine-tuned\n*   We need metrics that measure the LLMs’ accuracy in understanding the custom ontology, and the accuracy of graph translation\n*   Entities that are generated in a text-to-graph translation need to be aligned between graphs\n\nApproach 4: Hybrid of fine-tuned and pre-trained\n------------------------------------------------\n\nIt is often the case that a single ontology/schema is insufficient to capture the full semantics of the text. Therefore we might want to use two or more ontologies. Fortunately, it appears that fine-tuning the LLM with the custom ontology has not caused it to forget the pre-trained ontologies such as FOAF as the following example reveals.\n\nSystem-prompt, now referring to both pre-trained and fine-tuned ontologies:\n\nTranslate the following user text to an RDF graph using both the FOAF, and Schema1 ontologies.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.\n\nUser-prompt:\n\nPeter Jones and Beth Hampton both studied at Brunel University, then got married, and have three children: George, James, and Harold.   \nPeter, email address peter.jones@inova8.com, has been friends with Paul Williams because of their shared interest in ornithology.\n\nAnd the LLMs assistant-response uses both ontologies:\n\n@prefix ex: <http://example.com/\\> .  \nex:PeterJones a schema1:Thing, foaf:Person ;  \n  schema1:email \"peter.jones@inova8.com\" ;  \n  foaf:name \"Peter Jones\" ;  \n  foaf:interest ex:Ornithology .  \nex:BethHampton a schema1:Thing, foaf:Person ;  \n  foaf:name \"Beth Hampton\" .  \nex:GeorgeJones a schema1:Thing, foaf:Person ;  \n  foaf:name \"George Jones\" ;  \n  foaf:maker ex:PeterJones .  \nex:JamesJones a schema1:Thing, foaf:Person ;  \n  foaf:name \"James Jones\" ;  \n  foaf:maker ex:PeterJones .  \nex:HaroldJones a schema1:Thing, foaf:Person ;  \n  foaf:name \"Harold Jones\" ;  \n  foaf:maker ex:PeterJones .  \nex:BrunelUniversity a schema1:Thing, foaf:Document ;  \n  foaf:name \"Brunel University\" .  \nex:JonesHamptonMarriage a schema1:Thing ;  \n  schema1:spouse ex:PeterJones, ex:BethHampton .  \nex:JonesHamptonFamily a schema1:Thing ;  \n  schema1:parent ex:PeterJones, ex:BethHampton ;  \n  schema1:child ex:GeorgeJones, ex:JamesJones, ex:HaroldJones .  \nex:PeterJones foaf:knows ex:PaulWilliams .  \nex:PaulWilliams a schema1:Thing, foaf:Person ;  \n  foaf:name \"Paul Williams\" .\n\nPro:\n----\n\n*   An LLM that is fine-tuned with a custom ontology does not forget its pre-trained ontologies\n*   Text-to-graph translation can use a combination of pre-trained and fine-tuned ontologies\n\nCon:\n----\n\n*   When concepts overlap between ontologies, we need to control which translation the LLM will use\n*   Entities that are generated in a text-to-graph translation need to be aligned between graphs\n\nWhat have we learnt?\n--------------------\n\n*   LLMs can effectively transform unstructured text into an RDF graph.  \n    \\- Using pre-trained ontologies such as FOAF, and SCHEMA.ORG  \n    \\- Using custom ontologies in the prompt  \n    \\- Fine-tuning the LLM with a custom ontology  \n    \\- A hybrid of pre-trained and fine-tuned ontologies.\n*   An LLM can successfully create fine-tuning examples given the ontology in RDF TTL format.\n*   Fine-tuning with ~160 examples can be completed in 3 epochs  \n    \\- This reduces tuning costs  \n    \\- It also reduces the risk of catastrophic forgetting\n*   A custom-ontology fine-tuned model is far more token-efficient as it does not need the overhead of the complete ontology in the prompt with each translation request  \n    \\- This reduces translation costs in a production environment when multiple texts are to be transformed  \n    \\- It also improves translation performance.\n\nWhat have we yet to learn?\n--------------------------\n\n*   What is the number of tuning examples and tuning epochs to ‘optimise’ the fine-tuning?\n*   Can we establish a text-to-graph transformation ‘accuracy’ test so that we can perform some quantitative tests?\n*   The transformed text will include newly created entities. These will have to be aligned across multiple responses.  \n    \\- Is this a task for existing entity alignment tools like [SILK](http://silkframework.org/)?  \n    \\- Is this something we can ask the LLM to do as part of the graph post-processing?\n\nWhere to next?\n--------------\n\n*   The LLM capabilities of transforming text to RDF graphs have been explored using state-of-the-art LLMs.  \n    \\- We need to take these learnings and apply them to open-source and smaller LLMs such as Mistral-7B and OpenHermes. Initial results look very promising.\n*   It would be nice to have **quantitative** measures of text-to-graph transformation performance. For example:  \n    \\- How many samples per ontology concept ( 160/54 in these examples) are required for fine-tuning?  \n    \\- How many epochs are required (3 and 10 used in these examples)?  \n    \\- How does the response token rate vary between pre-trained, fine-tuned, and prompted?\n\nSummary\n-------\n\n![Image 22](https://miro.medium.com/v2/resize:fit:700/1*mAfQJ-FCRrHF9zXtuzQqtA.png)\n\nPrompt Details\n--------------\n\nIncluding the LLM prompts and responses within the body of this article makes it difficult to read. Therefore I have included the prompts here, leaving a description of the prompt within the main text.\n\nApproach 1: LLM with pre-trained ontologies\n-------------------------------------------\n\nRequest for Text-to-Graph Translation using RDF, RDFS, and OWL Ontologies\n-------------------------------------------------------------------------\n\nRDF, RDFS, and OWL System Prompt\n--------------------------------\n\nTranslate the following user text to an RDF graph using the RDF, RDFS, and OWL ontologies formatted as TTL.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.\n\nRDF, RDFS, and OWL User Prompt\n------------------------------\n\nPeter Jones and Beth Hampton studied at Brunel University, then married, and had three children: George, James, and Harold.\n\nRDF, RDFS, and OWL Assistant Response\n-------------------------------------\n\n@prefix ex: <http://example.com/\\> .  \n@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#\\> .  \n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#\\> .  \n@prefix owl: <http://www.w3.org/2002/07/owl#\\> .  \nex:PeterJones rdf:type ex:Person ;  \nrdf:label \"Peter Jones\" .  \nex:BethHampton rdf:type ex:Person ;  \nrdf:label \"Beth Hampton\" .  \nex:BrunelUniversity rdf:type ex:University ;  \nrdf:label \"Brunel University\" .  \nex:George rdf:type ex:Person ;  \nrdf:label \"George\" .  \nex:James rdf:type ex:Person ;  \nrdf:label \"James\" .  \nex:Harold rdf:type ex:Person ;  \nrdf:label \"Harold\" .  \nex:PeterJones ex:studiedAt ex:BrunelUniversity ;  \nex:marriedTo ex:BethHampton ;  \nex:hasChild ex:George, ex:James, ex:Harold .\n\nRequest for Text-to-Graph Translation using SCHEMA.ORG\n------------------------------------------------------\n\nSCHEMA.ORG System Prompt\n------------------------\n\nTranslate the following user text to an RDF graph using the SCHEMA.ORG ontologies formatted as TTL.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.\n\nSCHEMA.ORG User Prompt\n----------------------\n\nPeter Jones and Beth Hampton studied at Brunel University, then married, and had three children: George, James, and Harold.\n\nSCHEMA.ORG Assistant Response\n-----------------------------\n\n@prefix ex: <http://example.com/\\> .  \n@prefix schema: <https://schema.org/\\> .  \nex:PeterJones a schema:Person ;  \nschema:spouse ex:BethHampton ;  \nschema:alumniOf ex:BrunelUniversity .  \nex:BethHampton a schema:Person ;  \nschema:spouse ex:PeterJones .  \nex:BrunelUniversity a schema:EducationalOrganization .  \nex:George a schema:Person .  \nex:James a schema:Person .  \nex:Harold a schema:Person .  \nex:PeterJones schema:children ex:George, ex:James, ex:Harold .  \nex:BethHampton schema:children ex:George, ex:James, ex:Harold .\n\nApproach 2: LLM prompted with an ontology\n-----------------------------------------\n\nRequest for Text-to-Graph Translation providing an ontology\n-----------------------------------------------------------\n\nProvided Ontology System Prompt\n-------------------------------\n\nTranslate the following user text to an RDF graph using the following schema1: <http://inova8.com/schema/1/\\> ontologies formatted as TTL.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.  \nOnly use pre-defined classes and properties from the schema1: <http://inova8.com/schema/1/\\> ontology.  \nUse the properties and classes in the schema1: ontology.  \nInclude individuals, their data, and relationships.  \n@prefix : <http://inova8.com/schema/1/\\> .  \n@prefix owl: <http://www.w3.org/2002/07/owl#\\> .  \n@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#\\> .  \n@prefix xml: <http://www.w3.org/XML/1998/namespace\\> .  \n@prefix xsd: <http://www.w3.org/2001/XMLSchema#\\> .  \n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#\\> .  \n@prefix schema1: <http://inova8.com/schema/1/\\> .  \n@base <http://inova8.com/schema/1/\\> .  \n<http://inova8.com/schema/1/\\> rdf:type owl:Ontology .  \n#################################################################  \n\\# Object Properties  \n#################################################################  \n\\### http://inova8.com/schema/1/oa  \nschema1:oa rdf:type owl:ObjectProperty ;  \n  rdfs:domain schema1:CC ;  \n  rdfs:range schema1:CA ;  \n  rdfs:comment \"\"\"The university, school, or college that one formerly attended.  \n\\\\\"he started teaching at his alma mater\\\\\"\"\"\" ;  \n  rdfs:label \"alma mater\" .  \n\\### http://inova8.com/schema/1/ob  \nschema1:ob rdf:type owl:ObjectProperty ;  \n  rdfs:domain schema1:CC ;  \n  rdfs:range schema1:CC ;  \n  rdfs:comment \"Inverse of 'parent'\" ;  \n  rdfs:label \"child\" .  \n…  \n#################################################################  \n\\# Data properties  \n#################################################################  \n\\### http://inova8.com/schema/1/da  \nschema1:da rdf:type owl:DatatypeProperty ;  \n  rdfs:domain schema1:CC ;  \n  rdfs:range xsd:int ;  \n  rdfs:comment \"The day they were born, shown in numbers, or words and numbers\" ;  \n  rdfs:label \"year of birth\" .  \n\\### http://inova8.com/schema/1/db  \nschema1:db rdf:type owl:DatatypeProperty ;  \n  rdfs:domain schema1:CC ;  \n  rdfs:range xsd:int ;  \n  rdfs:comment \"The day they died, shown in numbers, or words and numbers\" ;  \n  rdfs:label \"year of death\" .  \n\\### http://inova8.com/schema/1/dc  \nschema1:dc rdf:type owl:DatatypeProperty ;  \n  rdfs:domain schema1:CC ;  \n  rdfs:range xsd:string ;  \n  rdfs:comment \"The name that was given to you when you were born and that comes before your family name:\" ;  \n  rdfs:label \"first name\" .  \n…  \n#################################################################  \n\\# Classes  \n#################################################################  \n\\### http://inova8.com/schema/1/CA  \nschema1:CA rdf:type owl:Class ;  \n  rdfs:subClassOf owl:Thing ;  \n  rdfs:label \"College\" .  \n…  \n\\### http://inova8.com/schema/1/CF  \nschema1:CF rdf:type owl:Class ;  \n  rdfs:subClassOf owl:Thing ;  \n  rdfs:label \"Profession\" .  \n\\### http://inova8.com/schema/1/CG  \nschema1:CG rdf:type owl:Class ;  \n  rdfs:subClassOf owl:Thing ;  \n  rdfs:label \"Marriage\" .  \n#################################################################  \n\\# Individuals  \n#################################################################  \n\\### http://inova8.com/schema/1/Lt-governor  \nschema1:Lt-governor rdf:type owl:NamedIndividual ,  \n  schema1:CF ;  \n  rdfs:label \"Lt-governor\" .  \n\\### http://inova8.com/schema/1/PR  \nschema1:PR rdf:type owl:NamedIndividual ,  \n…  \n  schema1:CF ;  \n  rdfs:label \"PR\" .\n\nProvided Ontology User Prompt\n-----------------------------\n\nPeter Jones and Beth Hampton studied at Brunel University, then married, and had three children: George, James, and Harold.\n\nProvided Ontology Assistant Response\n------------------------------------\n\nex:PeterJones rdf:type schema1:CC ;  \n  :dc \"Peter\" ;  \n  :de \"Jones\" ;  \n  :oa ex:BrunelUniversity ;  \n  :oh ex:BethHampton ;  \n  :of ex:business .  \nex:BethHampton rdf:type schema1:CC ;  \n  :dc \"Beth\" ;  \n  :de \"Hampton\" ;  \n  :oa ex:BrunelUniversity ;  \n  :oh ex:PeterJones ;  \n  :of ex:business .  \nex:BrunelUniversity rdf:type schema1:CA ;  \n  rdfs:label \"Brunel University\" .  \nex:George rdf:type schema1:CC ;  \n  rdfs:label \"George\" ;  \n  :od ex:PeterJones ;  \n  :od ex:BethHampton .  \nex:James rdf:type schema1:CC ;  \n  rdfs:label \"James\" ;  \n  :od ex:PeterJones ;  \n  :od ex:BethHampton .  \nex:Harold rdf:type schema1:CC ;  \n  rdfs:label \"Harold\" ;  \n  :od ex:PeterJones ;  \n  :od ex:BethHampton .  \nex:PeterJones :oh ex:BethHampton .  \nex:BethHampton :oh ex:PeterJones .\n\nApproach 3: LLM fine-tuned with an ontology\n-------------------------------------------\n\nRequest for Fine-Tuning Examples\n--------------------------------\n\nTuning Example Request System Prompt\n------------------------------------\n\nYou are a helpful assistant who will use the :Schema1 ontology that follows. This schema is called  \n:Schema1 with IRI <http://inova8.com/schema/1/\\>  \n…. ontology in TTL …. \n\nTuning Example Request User Prompt\n----------------------------------\n\nI want to fine-tune an LLM on this Schema1 ontology. This training aims to take an example user text and the assistant translates it into an RDF graph based on the Schema1 ontology. Please create a comprehensive set of 50 example system, user, and assistant messages in JSONL message conversational chat format format for fine-tuning an LLM to translate text to Schema1 ontology RDF.  \nThe system content should be the instruction to translate the user text to the assistant RDF graph response using Sxchema1 ontology.  \nThe user text should be examples that cover all the concepts within the Schema1 ontology.  \nThe assistant content should be an RDF graph using the Schema1 ontology of the translation of the user text examples.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.  \nUse the message format as follows:  \n{\"messages\": \\[{\"role\": \"system\", \"content\": \"<system\\_content\\>\"}, {\"role\": \"user\", \"content\": \"<user\\_content\\>}, {\"role\": \"assistant\", \"content\": \"<assistant\\_content\\>\"}\\]}\n\nTuning Example Request Assistant Response\n-----------------------------------------\n\n{“messages”: \\[  \n  {“role”: “system”, “content”: “Translate the following user text to an RDF graph using the Schema1 ontology.”},   \n  {“role”: “user”, “content”: “John Smith is a professor who graduated from a reputed college.”},   \n  {“role”: “assistant”, “content”: “@prefix ex: <http://example.com/\\> .\\\\n@prefix schema1: <http://inova8.com/schema/1/\\> .\\\\nex:JohnSmith rdf:type schema1:CC ;\\\\nschema1:dc \\\\”John\\\\” ;\\\\nschema1:de \\\\”Smith\\\\” ;\\\\nschema1:of schema1:professor ;\\\\nschema1:oa ex:ReputedCollege .\\\\nex:ReputedCollege rdf:type schema1:CA .”}  \n  \\]  \n}  \n… and so on\n\nRequest for Text-to-Graph Translation using fine-tuned LLM\n----------------------------------------------------------\n\nFine-tuned Ontology System Prompt\n---------------------------------\n\nTranslate the following user text to an RDF graph using the Schema1 ontology.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.\n\nFine-tuned Ontology User Prompt\n-------------------------------\n\nPeter Jones and Beth Hampton both studied at Brunel University, then got married, and have three children: George, James, and Harold.\n\nFine-tuned Ontology Assistant Response\n--------------------------------------\n\n@prefix ex: <http://example.com/\\> .  \nex:PeterJones a schema1:CC ;  \n  schema1:dc \"Peter\" ;  \n  schema1:de \"Jones\" ;  \n  schema1:of schema1:student .  \nex:BethHampton a schema1:CC ;  \n  schema1:dc \"Beth\" ;  \n  schema1:de \"Hampton\" ;  \n  schema1:of schema1:student .  \nex:JonesHamptonMarriage a schema1:CG ;  \n  schema1:og ex:PeterJones ;  \n  schema1:oh ex:BethHampton .  \nex:GeorgeJones a schema1:CD ;  \n  schema1:dc \"George\" ;  \n  schema1:od ex:PeterJones ;  \n  schema1:of ex:BethHampton .  \nex:JamesJones a schema1:CD ;  \n  schema1:dc \"James\" ;  \n  schema1:od ex:PeterJones ;  \n  schema1:of ex:BethHampton .  \nex:HaroldJones a schema1:CD ;  \n  schema1:dc \"Harold\" ;  \n  schema1:od ex:PeterJones ;  \n  schema1:of ex:BethHampton\n\nApproach 4: Hybrid of fine-tuned and pre-trained\n------------------------------------------------\n\nRequest for Text-to-Graph Translation using fine-tuned LLM and FOAF\n-------------------------------------------------------------------\n\nHybrid System Prompt\n--------------------\n\nTranslate the following user text to an RDF graph using both the FOAF, and Schema1 ontologies.  \nUse the prefix ex: with IRI <http://example.com/\\> for any created entities.\n\nHybrid User Prompt\n------------------\n\nPeter Jones and Beth Hampton both studied at Brunel University, then got married, and have three children: George, James, and Harold.   \nPeter, email address peter.jones@inova8.com, has been friends with Paul Williams because of their shared interest in ornithology.\n\nHybrid Assistant Response\n-------------------------\n\n@prefix ex: <http://example.com/\\> .  \nex:PeterJones a schema1:Thing, foaf:Person ;  \n  schema1:email \"peter.jones@inova8.com\" ;  \n  foaf:name \"Peter Jones\" ;  \n  foaf:interest ex:Ornithology .  \nex:BethHampton a schema1:Thing, foaf:Person ;  \n  foaf:name \"Beth Hampton\" .  \nex:GeorgeJones a schema1:Thing, foaf:Person ;  \n  foaf:name \"George Jones\" ;  \n  foaf:maker ex:PeterJones .  \nex:JamesJones a schema1:Thing, foaf:Person ;  \n  foaf:name \"James Jones\" ;   \n  foaf:maker ex:PeterJones .  \nex:HaroldJones a schema1:Thing, foaf:Person ;  \n  foaf:name \"Harold Jones\" ;  \n  foaf:maker ex:PeterJones .  \n  ex:BrunelUniversity a schema1:Thing, foaf:Document ;  \nfoaf:name \"Brunel University\" .  \nex:JonesHamptonMarriage a schema1:Thing ;  \n  schema1:spouse ex:PeterJones, ex:BethHampton .  \n  ex:JonesHamptonFamily a schema1:Thing ;  \n  schema1:parent ex:PeterJones, ex:BethHampton ;  \n  schema1:child ex:GeorgeJones, ex:JamesJones, ex:HaroldJones .  \nex:PeterJones foaf:knows ex:PaulWilliams .  \nex:PaulWilliams a schema1:Thing, foaf:Person ;  \n  foaf:name \"Paul Williams\" .",
  "publishedTime": "2024-01-16T05:59:17.564Z",
  "usage": {
    "tokens": 9989
  }
}
```
