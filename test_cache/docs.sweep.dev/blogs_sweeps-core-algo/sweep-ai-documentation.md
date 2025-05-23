---
title: Sweep AI Documentation
description: 
url: https://docs.sweep.dev/blogs/sweeps-core-algo
timestamp: 2025-01-20T15:45:11.751Z
domain: docs.sweep.dev
path: blogs_sweeps-core-algo
---

# Sweep AI Documentation



## Content

Sweep's Core Algorithm - Using Retrieval Augmented Generation (RAG) to clear your GitHub Backlog
------------------------------------------------------------------------------------------------

**Kevin Lu** - August 9th, 2023

* * *

At Sweep, our core issue-to-pull-request pipeline resolves around an RAG-based pipeline. This means we retrieve snippets from a corpora (your codebase) and feed it to a language model (GPT-4) to generate code.

In summary, Sweep searches for relevant files and edits the file(s) it thinks requires changes. Sweep then validates its own changes by reading for logical errors and running GitHub Actions on them and finally leaves the pull request for the user to review.

The following is the Sweep’s pipeline that turns an issue like “the app has an error relating to temporary directories on Windows” into a pull request titled “replace all occurrences of `/tmp` with `tempfile.TempDirectory()`” like [this (opens in a new tab)](https://github.com/sweepai/sweep/pull/368/files).

![Image 16](https://docs.sweep.dev/_next/static/media/flowchart.15fed92e.svg)

Inputs[](https://docs.sweep.dev/blogs/sweeps-core-algo#inputs)
--------------------------------------------------------------

Everything starts with the inputs, including everything in the following:

![Image 17](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finputs.94857169.png&w=1920&q=75)

Only the issue, repository and user metadata are useful for now. The context fed to the language model at this point looks like this:

The next step is to use the codebase, but codebases can have up to thousands of files! Thus, we only search for relevant files.

Search[](https://docs.sweep.dev/blogs/sweeps-core-algo#search)
--------------------------------------------------------------

![Image 18](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fsearch.47a41faf.png&w=3840&q=75)

Sweep starts searching for relevant snippets by:

1.  **Query** the title and description against the code snippets as the context and retrieves the top 100 snippets using [MPNet (opens in a new tab)](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) embeddings and a [DeepLake (opens in a new tab)](https://github.com/activeloopai/deeplake) vector store. We chunk the files ahead of time using a custom [CST-based chunker (opens in a new tab)](https://docs.sweep.dev/blogs/chunking-2m-files). We have a more details tour of our search infrastructure at [https://docs.sweep.dev/blogs/search-infra (opens in a new tab)](https://docs.sweep.dev/blogs/search-infra) and [https://docs.sweep.dev/blogs/building-code-search (opens in a new tab)](https://docs.sweep.dev/blogs/building-code-search).
2.  **Re-rank** the snippets using a heuristic based on the commit count and time of the latest commit and pick the top 4. The assumption is that the files with the latest commit and highest commit counts are more likely to be edited again. We also at this point add any files mentioned directly.
3.  **De-duplicate and fuse snippets**. For example, if the snippet `main.py:0-50` and `main.py:51-100` gets fetched, they get fused into `main.py:0-100`. We then extend each snippet by 25 lines in each direction, so `main.py:25-75` becomes `main.py:0-100`.
4.  **Generate a summary** of the repository using [ctag summaries (opens in a new tab)](https://docs.sweep.dev/blogs/understanding-codebase-with-ctags) of the top 10 files from the re-ranking, which is a summary of the variable names and functions declared in the file. This is presented as a directory tree: starting from the root directory all the way to the files and the classes, methods and variables of the files. Only files that are siblings of the top 10 files will be

The final context at this point looks something like the following:

### External Search[](https://docs.sweep.dev/blogs/sweeps-core-algo#external-search)

On top of the code snippet search, we also perform external search:

1.  **Public websites**: leaving a link to a publicly accessible site will make Sweep read the contents of the page.
2.  **Documentation search**: GPT-4, unfortunately, has only been trained until 2022 so it won’t have access to the latest docs, so we set up search indices for docs that update once a day. The current list of docs that get indexed can be found at [https://github.com/sweepai/sweep/blob/main/sweepai/pre\_indexed\_docs.py (opens in a new tab)](https://github.com/sweepai/sweep/blob/main/sweepai/pre_indexed_docs.py), and we’ll write another post describing how we fetch the docs soon. Feel free to create a PR to add docs you would like to see Sweep use!

Planning[](https://docs.sweep.dev/blogs/sweeps-core-algo#planning)
------------------------------------------------------------------

![Image 19](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fplan.9de38eeb.png&w=3840&q=75)

Sweep then curates a list of files it wants to modify and those it wants to create by:

1.  Determining what the root causes of the issues are. E.g. the bug has to do with `/tmp` not existing on Windows.
2.  Determining in natural language an implementation plan using chain-of-thought prompting. E.g. replace all occurrences of `/tmp` with `tempfile.TemporaryDirectory()`.
3.  Specify a list of files to modify, like the following:

We then validate these suggested changes, by changing any “modify”’s to “create” if the files don’t exist and vice versa. In the future, we can use a fuzzy algorithm since we’ve noticed that Sweep sometimes says it wants to modify `src/components/NavBar.tsx` when only the file `src/components/Navbar.tsx` exists (capitalization error), or similar errors for slightly incorrect paths.

Execution[](https://docs.sweep.dev/blogs/sweeps-core-algo#execution)
--------------------------------------------------------------------

![Image 20](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finputs.94857169.png&w=1920&q=75)

Sweep creates each file from scratch (in the case of file creation) or determines which lines it wants to modify. Modification is drastically more complex and involves:

1.  Creating a high-level game plan of what in particular to change. E.g. Use an OS-agnostic alternative to `/tmp` directories by using Python’s `tempfile.gettempdir()`.
2.  Identifies all locations of it and creates a list of natural language descriptions of changes with reference to line numbers. E.g. In `sweepai/app/ui.py`, in the `get_repo()` function replace all occurrences of `/tmp` to `tempfile.gettempdir()`.
3.  Generate search-and-replace pairs, using a [format (opens in a new tab)](https://github.com/sweepai/sweep/blob/d37dda3a626f09dea3b3221dd0254671407ccc1b/sweepai/core/prompts.py#L325-L329) based on `aider`’s prompts, another open-source LLM-powered devtool. This looks something like the following:

We use fuzzy matching for the “search” part of “search-and-replace”, based on heuristics like equal start lines and end lines, since GPT-4 skips comments in the “ORIGINAL” section.

For larger files (\>1000 LOC), we use a streaming method, involving feeding in 600 lines of code at a time (which corresponds to about 15k tokens).

Validation[](https://docs.sweep.dev/blogs/sweeps-core-algo#validation)
----------------------------------------------------------------------

![Image 21](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fvalidation.90ab8fb7.png&w=2048&q=75)

We run both an LLM-based and procedural validation to ensure that there are no errors in the new code and that the generated code reflects the changes summarized by the pull request.

If changes are needed, we re-run the pipeline on the pull request from the beginning, with a few additions. We always include as part of the search all the files that were modified as part of the pull request and we skip the self-review.

### Self-Review[](https://docs.sweep.dev/blogs/sweeps-core-algo#self-review)

Sweep checks the code diffs and the pull request summary using GPT-4 and verifies that nothing is clearly broken. If something is broken, Sweep makes a comment on its own pull request with a summary of things to change.

If it fails again, we do another self-review. We iterate for a maximum of three times.

### GitHub Actions[](https://docs.sweep.dev/blogs/sweeps-core-algo#github-actions)

GitHub Actions is used to check for errors such as type errors, compile-time errors and failed test runs. Failed Action logs get fed to Sweep and get treated like pull request comments.

This is entirely configurable by developers. We use GitHub Actions since there’s a plethora of tools it can use and most developers have GitHub Actions already set up for their team. See more at [https://docs.sweep.dev/blogs/giving-dev-tools (opens in a new tab)](https://docs.sweep.dev/blogs/giving-dev-tools).

User Review[](https://docs.sweep.dev/blogs/sweeps-core-algo#user-review)
------------------------------------------------------------------------

When a user leaves a comment on the pull request, we re-run the entire pipeline, similar to Sweep’s self-reviews or failed GitHub Action runs.

For code comments, Sweep skips to the execution step and only modifies the file the code comment was left on. This is significantly faster, although the scope is limited.

Once again, here’s the final pipeline.

![Image 22](https://docs.sweep.dev/_next/static/media/flowchart.15fed92e.svg)

* * *

⭐ If this interests you, see our [open-source repo (opens in a new tab)](https://github.com/sweepai/sweep)!

[🎓 How our AI junior dev reads all of your documentation](https://docs.sweep.dev/blogs/reading-docs "🎓 How our AI junior dev reads all of your documentation")[⚙️ Generating 50k+ embeddings in 25 seconds using GTE 🧠 and MapReduce 💻](https://docs.sweep.dev/blogs/generating-50k-embeddings-with-gte "⚙️ Generating 50k+ embeddings in 25 seconds using GTE 🧠 and MapReduce 💻")

## Metadata

```json
{
  "title": "Sweep AI Documentation",
  "description": "",
  "url": "https://docs.sweep.dev/blogs/sweeps-core-algo",
  "content": "Sweep's Core Algorithm - Using Retrieval Augmented Generation (RAG) to clear your GitHub Backlog\n------------------------------------------------------------------------------------------------\n\n**Kevin Lu** - August 9th, 2023\n\n* * *\n\nAt Sweep, our core issue-to-pull-request pipeline resolves around an RAG-based pipeline. This means we retrieve snippets from a corpora (your codebase) and feed it to a language model (GPT-4) to generate code.\n\nIn summary, Sweep searches for relevant files and edits the file(s) it thinks requires changes. Sweep then validates its own changes by reading for logical errors and running GitHub Actions on them and finally leaves the pull request for the user to review.\n\nThe following is the Sweep’s pipeline that turns an issue like “the app has an error relating to temporary directories on Windows” into a pull request titled “replace all occurrences of `/tmp` with `tempfile.TempDirectory()`” like [this (opens in a new tab)](https://github.com/sweepai/sweep/pull/368/files).\n\n![Image 16](https://docs.sweep.dev/_next/static/media/flowchart.15fed92e.svg)\n\nInputs[](https://docs.sweep.dev/blogs/sweeps-core-algo#inputs)\n--------------------------------------------------------------\n\nEverything starts with the inputs, including everything in the following:\n\n![Image 17](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finputs.94857169.png&w=1920&q=75)\n\nOnly the issue, repository and user metadata are useful for now. The context fed to the language model at this point looks like this:\n\nThe next step is to use the codebase, but codebases can have up to thousands of files! Thus, we only search for relevant files.\n\nSearch[](https://docs.sweep.dev/blogs/sweeps-core-algo#search)\n--------------------------------------------------------------\n\n![Image 18](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fsearch.47a41faf.png&w=3840&q=75)\n\nSweep starts searching for relevant snippets by:\n\n1.  **Query** the title and description against the code snippets as the context and retrieves the top 100 snippets using [MPNet (opens in a new tab)](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) embeddings and a [DeepLake (opens in a new tab)](https://github.com/activeloopai/deeplake) vector store. We chunk the files ahead of time using a custom [CST-based chunker (opens in a new tab)](https://docs.sweep.dev/blogs/chunking-2m-files). We have a more details tour of our search infrastructure at [https://docs.sweep.dev/blogs/search-infra (opens in a new tab)](https://docs.sweep.dev/blogs/search-infra) and [https://docs.sweep.dev/blogs/building-code-search (opens in a new tab)](https://docs.sweep.dev/blogs/building-code-search).\n2.  **Re-rank** the snippets using a heuristic based on the commit count and time of the latest commit and pick the top 4. The assumption is that the files with the latest commit and highest commit counts are more likely to be edited again. We also at this point add any files mentioned directly.\n3.  **De-duplicate and fuse snippets**. For example, if the snippet `main.py:0-50` and `main.py:51-100` gets fetched, they get fused into `main.py:0-100`. We then extend each snippet by 25 lines in each direction, so `main.py:25-75` becomes `main.py:0-100`.\n4.  **Generate a summary** of the repository using [ctag summaries (opens in a new tab)](https://docs.sweep.dev/blogs/understanding-codebase-with-ctags) of the top 10 files from the re-ranking, which is a summary of the variable names and functions declared in the file. This is presented as a directory tree: starting from the root directory all the way to the files and the classes, methods and variables of the files. Only files that are siblings of the top 10 files will be\n\nThe final context at this point looks something like the following:\n\n### External Search[](https://docs.sweep.dev/blogs/sweeps-core-algo#external-search)\n\nOn top of the code snippet search, we also perform external search:\n\n1.  **Public websites**: leaving a link to a publicly accessible site will make Sweep read the contents of the page.\n2.  **Documentation search**: GPT-4, unfortunately, has only been trained until 2022 so it won’t have access to the latest docs, so we set up search indices for docs that update once a day. The current list of docs that get indexed can be found at [https://github.com/sweepai/sweep/blob/main/sweepai/pre\\_indexed\\_docs.py (opens in a new tab)](https://github.com/sweepai/sweep/blob/main/sweepai/pre_indexed_docs.py), and we’ll write another post describing how we fetch the docs soon. Feel free to create a PR to add docs you would like to see Sweep use!\n\nPlanning[](https://docs.sweep.dev/blogs/sweeps-core-algo#planning)\n------------------------------------------------------------------\n\n![Image 19](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fplan.9de38eeb.png&w=3840&q=75)\n\nSweep then curates a list of files it wants to modify and those it wants to create by:\n\n1.  Determining what the root causes of the issues are. E.g. the bug has to do with `/tmp` not existing on Windows.\n2.  Determining in natural language an implementation plan using chain-of-thought prompting. E.g. replace all occurrences of `/tmp` with `tempfile.TemporaryDirectory()`.\n3.  Specify a list of files to modify, like the following:\n\nWe then validate these suggested changes, by changing any “modify”’s to “create” if the files don’t exist and vice versa. In the future, we can use a fuzzy algorithm since we’ve noticed that Sweep sometimes says it wants to modify `src/components/NavBar.tsx` when only the file `src/components/Navbar.tsx` exists (capitalization error), or similar errors for slightly incorrect paths.\n\nExecution[](https://docs.sweep.dev/blogs/sweeps-core-algo#execution)\n--------------------------------------------------------------------\n\n![Image 20](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Finputs.94857169.png&w=1920&q=75)\n\nSweep creates each file from scratch (in the case of file creation) or determines which lines it wants to modify. Modification is drastically more complex and involves:\n\n1.  Creating a high-level game plan of what in particular to change. E.g. Use an OS-agnostic alternative to `/tmp` directories by using Python’s `tempfile.gettempdir()`.\n2.  Identifies all locations of it and creates a list of natural language descriptions of changes with reference to line numbers. E.g. In `sweepai/app/ui.py`, in the `get_repo()` function replace all occurrences of `/tmp` to `tempfile.gettempdir()`.\n3.  Generate search-and-replace pairs, using a [format (opens in a new tab)](https://github.com/sweepai/sweep/blob/d37dda3a626f09dea3b3221dd0254671407ccc1b/sweepai/core/prompts.py#L325-L329) based on `aider`’s prompts, another open-source LLM-powered devtool. This looks something like the following:\n\nWe use fuzzy matching for the “search” part of “search-and-replace”, based on heuristics like equal start lines and end lines, since GPT-4 skips comments in the “ORIGINAL” section.\n\nFor larger files (\\>1000 LOC), we use a streaming method, involving feeding in 600 lines of code at a time (which corresponds to about 15k tokens).\n\nValidation[](https://docs.sweep.dev/blogs/sweeps-core-algo#validation)\n----------------------------------------------------------------------\n\n![Image 21](https://docs.sweep.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fvalidation.90ab8fb7.png&w=2048&q=75)\n\nWe run both an LLM-based and procedural validation to ensure that there are no errors in the new code and that the generated code reflects the changes summarized by the pull request.\n\nIf changes are needed, we re-run the pipeline on the pull request from the beginning, with a few additions. We always include as part of the search all the files that were modified as part of the pull request and we skip the self-review.\n\n### Self-Review[](https://docs.sweep.dev/blogs/sweeps-core-algo#self-review)\n\nSweep checks the code diffs and the pull request summary using GPT-4 and verifies that nothing is clearly broken. If something is broken, Sweep makes a comment on its own pull request with a summary of things to change.\n\nIf it fails again, we do another self-review. We iterate for a maximum of three times.\n\n### GitHub Actions[](https://docs.sweep.dev/blogs/sweeps-core-algo#github-actions)\n\nGitHub Actions is used to check for errors such as type errors, compile-time errors and failed test runs. Failed Action logs get fed to Sweep and get treated like pull request comments.\n\nThis is entirely configurable by developers. We use GitHub Actions since there’s a plethora of tools it can use and most developers have GitHub Actions already set up for their team. See more at [https://docs.sweep.dev/blogs/giving-dev-tools (opens in a new tab)](https://docs.sweep.dev/blogs/giving-dev-tools).\n\nUser Review[](https://docs.sweep.dev/blogs/sweeps-core-algo#user-review)\n------------------------------------------------------------------------\n\nWhen a user leaves a comment on the pull request, we re-run the entire pipeline, similar to Sweep’s self-reviews or failed GitHub Action runs.\n\nFor code comments, Sweep skips to the execution step and only modifies the file the code comment was left on. This is significantly faster, although the scope is limited.\n\nOnce again, here’s the final pipeline.\n\n![Image 22](https://docs.sweep.dev/_next/static/media/flowchart.15fed92e.svg)\n\n* * *\n\n⭐ If this interests you, see our [open-source repo (opens in a new tab)](https://github.com/sweepai/sweep)!\n\n[🎓 How our AI junior dev reads all of your documentation](https://docs.sweep.dev/blogs/reading-docs \"🎓 How our AI junior dev reads all of your documentation\")[⚙️ Generating 50k+ embeddings in 25 seconds using GTE 🧠 and MapReduce 💻](https://docs.sweep.dev/blogs/generating-50k-embeddings-with-gte \"⚙️ Generating 50k+ embeddings in 25 seconds using GTE 🧠 and MapReduce 💻\")",
  "usage": {
    "tokens": 2388
  }
}
```
