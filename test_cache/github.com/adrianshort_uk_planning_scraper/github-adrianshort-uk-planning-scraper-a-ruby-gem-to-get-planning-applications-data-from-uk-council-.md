---
title: GitHub - adrianshort/uk_planning_scraper: A Ruby gem to get planning applications data from UK council websites.
description: A Ruby gem to get planning applications data from UK council websites. - adrianshort/uk_planning_scraper
url: https://github.com/adrianshort/uk_planning_scraper
timestamp: 2025-01-20T15:30:55.134Z
domain: github.com
path: adrianshort_uk_planning_scraper
---

# GitHub - adrianshort/uk_planning_scraper: A Ruby gem to get planning applications data from UK council websites.


A Ruby gem to get planning applications data from UK council websites. - adrianshort/uk_planning_scraper


## Content

UK Planning Scraper
-------------------

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#uk-planning-scraper)

**PRE-ALPHA: Only works with Idox and Northgate sites and spews a lot of stuff to STDOUT. Not for production use.**

This gem scrapes planning applications data from UK local planning authority websites, eg Westminster City Council. Data is returned as an array of hashes, one hash for each planning application.

This scraper gem doesn't use a database. Storing the output is up to you. It's just a convenient way to get the data.

Currently this only works for Idox and Northgate sites. The ultimate aim is to provide a consistent interface in a single gem for all variants of all planning systems: Idox Public Access, Northgate Planning Explorer, OcellaWeb, Agile Planning and all the one-off systems.

This project is not affiliated with any organisation.

Installation
------------

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#installation)

Add this line to your application's Gemfile:

gem 'uk\_planning\_scraper'

And then execute:

Or install it directly:

```
$ gem install uk_planning_scraper
```

Usage
-----

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#usage)

### First, require your stuff

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#first-require-your-stuff)

require 'uk\_planning\_scraper'
require 'pp'

### Scrape from a council

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#scrape-from-a-council)

Applications in Westminster decided in the last seven days:

pp UKPlanningScraper::Authority.named('Westminster').decided\_days(7).scrape

### Scrape from a bunch of councils

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#scrape-from-a-bunch-of-councils)

Scrape the last week's planning decisions across the whole of London (actually 23 of the 35 authorities right now):

authorities \= UKPlanningScraper::Authority.tagged('london')

authorities.each do |authority|
  applications \= authority.decided\_days(7).scrape
  pp applications
  \# You'll probably want to save \`applications\` to your database here
end

### Satisfy your niche interests

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#satisfy-your-niche-interests)

Launderette applications validated in the last seven days in Scotland:

authorities \= UKPlanningScraper::Authority.tagged('scotland')

authorities.each do |authority|
  applications \= authority.validated\_days(7).keywords('launderette').scrape
  pp applications \# You'll probably want to save \`apps\` to your database here
end

### More scrape parameter methods

Chain as many scrape parameter methods on a `UKPlanningScraper::Authority` object as you like, making sure that `scrape` comes last.

received\_from(Date.parse("1 Jan 2016"))
received\_to(Date.parse("31 Dec 2016"))

\# Received in the last n days (including today)
\# Use instead of received\_to, received\_from
received\_days(7) 

validated\_to(Date.today)
validated\_from(Date.today - 30)
validated\_days(7) \# instead of validated\_to, validated\_from

decided\_to(Date.today)
decided\_from(Date.today - 30)
decided\_days(7) \# instead of decided\_to, decided\_from

\# Check that the systems you're scraping return the
\# results you expect for multiple keywords (AND or OR?)
keywords("hip gable") 

applicant\_name("Mr and Mrs Smith") \# Currently Idox only
application\_type("Householder") \# Currently Idox only
development\_type("") \# Currently Idox only
case\_officer\_code("100000") \# Northgate only
status("Pending Consideration") \# Check valid status codes for each authority

scrape \# runs the scraper

### Save to a SQLite database

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#save-to-a-sqlite-database)

This gem has no interest whatsoever in persistence. What you do with the data it outputs is up to you: relational databases, document stores, VHS and clay tablets are all blissfully none of its business. But using the [ScraperWiki](https://github.com/openaustralia/scraperwiki-ruby) gem is a really easy way to store your data:

require 'scraperwiki' \# Must be installed, of course
ScraperWiki.save\_sqlite(\[:authority\_name, :council\_reference\], applications)

That `applications` param can be a hash or an array of hashes, which is what gets returned by our `Authority.scrape`.

### Find authorities by tag

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#find-authorities-by-tag)

Tags are always lowercase and one word.

london\_auths \= UKPlanningScraper::Authority.tagged('london')

We've got tags for areas:

*   london
*   innerlondon
*   outerlondon
*   northlondon
*   southlondon
*   greatermanchester
*   surrey
*   wales

We also automatically add tags for software systems:

*   idox
*   northgate
*   ocellaweb
*   agileplanning
*   unknownsystem -- for when we can't identify the system

and whatever you'd like to add that would be useful to others.

### WTF is up with London?

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#wtf-is-up-with-london)

London has got 32 London Boroughs, tagged `londonboroughs`. These are the councils under the authority of the Mayor of London and the Greater London Authority.

It has 33 councils: the London Boroughs plus the City of London (named `City of London`). We don't currently have a tag for this, but if you want to add `londoncouncils` please go ahead.

And it's got 35 local planning authorities: the 33 councils plus the two `londondevelopmentcorporations`, named `London Legacy Development Corporation` and `Old Oak and Park Royal Development Corporation`. The tag `london` covers all (and only) the 35 local planning authorities in London.

UKPlanningScraper::Authority.tagged('londonboroughs').size
 \# =\> 32
 
UKPlanningScraper::Authority.tagged('londondevelopmentcorporations').size
 \# =\> 2

UKPlanningScraper::Authority.tagged('london').size
 \# =\> 35

### More fun with Authority tags

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#more-fun-with-authority-tags)

UKPlanningScraper::Authority.named('Merton').tags
 \# =\> \["england", "london", "londonboroughs", "northgate", "outerlondon", "southlondon"\]

UKPlanningScraper::Authority.not\_tagged('london')
 \# =\> \[...\]

UKPlanningScraper::Authority.named('Islington').tagged?('southlondon')
 \# =\> false

### List all authorities

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#list-all-authorities)

UKPlanningScraper::Authority.all.each { |a| puts a.name }

### List all tags

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#list-all-tags)

pp UKPlanningScraper::Authority.tags

Add your favourite local planning authorities
---------------------------------------------

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#add-your-favourite-local-planning-authorities)

The list of authorities is in a CSV file in `/lib/uk_planning_scraper`:

[https://github.com/adrianshort/uk\_planning\_scraper/blob/master/lib/uk\_planning\_scraper/authorities.csv](https://github.com/adrianshort/uk_planning_scraper/blob/master/lib/uk_planning_scraper/authorities.csv)

The easiest way to add to or edit this list is to edit within GitHub (use the pencil icon) and create a new pull request for your changes. If accepted, your changes will be available to everyone with the next version of the gem.

The file format is one line per authority, with comma-separated:

*   Name (omit "the", "council", "borough of", "city of", etc. and write "and" not "&", except for `City of London` which is a special case)
*   URL of the search form (use the advanced search URL if there is one)
*   Tags (use as many comma-separated tags as is reasonable, lowercase and all one word.)

There's no need to manually add tags to the `authorities.csv` file for the software systems like `idox`, `northgate` etc as these are added automatically.

Please check the tag list before you change anything:

pp UKPlanningScraper::Authority.tags

Development
-----------

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#development)

After checking out the repo, run `bin/setup` to install dependencies. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org/).

Contributing
------------

[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#contributing)

Bug reports and pull requests are welcome on GitHub at [https://github.com/adrianshort/uk\_planning\_scraper](https://github.com/adrianshort/uk_planning_scraper).

## Metadata

```json
{
  "title": "GitHub - adrianshort/uk_planning_scraper: A Ruby gem to get planning applications data from UK council websites.",
  "description": "A Ruby gem to get planning applications data from UK council websites. - adrianshort/uk_planning_scraper",
  "url": "https://github.com/adrianshort/uk_planning_scraper?screenshot=true",
  "content": "UK Planning Scraper\n-------------------\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#uk-planning-scraper)\n\n**PRE-ALPHA: Only works with Idox and Northgate sites and spews a lot of stuff to STDOUT. Not for production use.**\n\nThis gem scrapes planning applications data from UK local planning authority websites, eg Westminster City Council. Data is returned as an array of hashes, one hash for each planning application.\n\nThis scraper gem doesn't use a database. Storing the output is up to you. It's just a convenient way to get the data.\n\nCurrently this only works for Idox and Northgate sites. The ultimate aim is to provide a consistent interface in a single gem for all variants of all planning systems: Idox Public Access, Northgate Planning Explorer, OcellaWeb, Agile Planning and all the one-off systems.\n\nThis project is not affiliated with any organisation.\n\nInstallation\n------------\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#installation)\n\nAdd this line to your application's Gemfile:\n\ngem 'uk\\_planning\\_scraper'\n\nAnd then execute:\n\nOr install it directly:\n\n```\n$ gem install uk_planning_scraper\n```\n\nUsage\n-----\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#usage)\n\n### First, require your stuff\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#first-require-your-stuff)\n\nrequire 'uk\\_planning\\_scraper'\nrequire 'pp'\n\n### Scrape from a council\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#scrape-from-a-council)\n\nApplications in Westminster decided in the last seven days:\n\npp UKPlanningScraper::Authority.named('Westminster').decided\\_days(7).scrape\n\n### Scrape from a bunch of councils\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#scrape-from-a-bunch-of-councils)\n\nScrape the last week's planning decisions across the whole of London (actually 23 of the 35 authorities right now):\n\nauthorities \\= UKPlanningScraper::Authority.tagged('london')\n\nauthorities.each do |authority|\n  applications \\= authority.decided\\_days(7).scrape\n  pp applications\n  \\# You'll probably want to save \\`applications\\` to your database here\nend\n\n### Satisfy your niche interests\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#satisfy-your-niche-interests)\n\nLaunderette applications validated in the last seven days in Scotland:\n\nauthorities \\= UKPlanningScraper::Authority.tagged('scotland')\n\nauthorities.each do |authority|\n  applications \\= authority.validated\\_days(7).keywords('launderette').scrape\n  pp applications \\# You'll probably want to save \\`apps\\` to your database here\nend\n\n### More scrape parameter methods\n\nChain as many scrape parameter methods on a `UKPlanningScraper::Authority` object as you like, making sure that `scrape` comes last.\n\nreceived\\_from(Date.parse(\"1 Jan 2016\"))\nreceived\\_to(Date.parse(\"31 Dec 2016\"))\n\n\\# Received in the last n days (including today)\n\\# Use instead of received\\_to, received\\_from\nreceived\\_days(7) \n\nvalidated\\_to(Date.today)\nvalidated\\_from(Date.today - 30)\nvalidated\\_days(7) \\# instead of validated\\_to, validated\\_from\n\ndecided\\_to(Date.today)\ndecided\\_from(Date.today - 30)\ndecided\\_days(7) \\# instead of decided\\_to, decided\\_from\n\n\\# Check that the systems you're scraping return the\n\\# results you expect for multiple keywords (AND or OR?)\nkeywords(\"hip gable\") \n\napplicant\\_name(\"Mr and Mrs Smith\") \\# Currently Idox only\napplication\\_type(\"Householder\") \\# Currently Idox only\ndevelopment\\_type(\"\") \\# Currently Idox only\ncase\\_officer\\_code(\"100000\") \\# Northgate only\nstatus(\"Pending Consideration\") \\# Check valid status codes for each authority\n\nscrape \\# runs the scraper\n\n### Save to a SQLite database\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#save-to-a-sqlite-database)\n\nThis gem has no interest whatsoever in persistence. What you do with the data it outputs is up to you: relational databases, document stores, VHS and clay tablets are all blissfully none of its business. But using the [ScraperWiki](https://github.com/openaustralia/scraperwiki-ruby) gem is a really easy way to store your data:\n\nrequire 'scraperwiki' \\# Must be installed, of course\nScraperWiki.save\\_sqlite(\\[:authority\\_name, :council\\_reference\\], applications)\n\nThat `applications` param can be a hash or an array of hashes, which is what gets returned by our `Authority.scrape`.\n\n### Find authorities by tag\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#find-authorities-by-tag)\n\nTags are always lowercase and one word.\n\nlondon\\_auths \\= UKPlanningScraper::Authority.tagged('london')\n\nWe've got tags for areas:\n\n*   london\n*   innerlondon\n*   outerlondon\n*   northlondon\n*   southlondon\n*   greatermanchester\n*   surrey\n*   wales\n\nWe also automatically add tags for software systems:\n\n*   idox\n*   northgate\n*   ocellaweb\n*   agileplanning\n*   unknownsystem -- for when we can't identify the system\n\nand whatever you'd like to add that would be useful to others.\n\n### WTF is up with London?\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#wtf-is-up-with-london)\n\nLondon has got 32 London Boroughs, tagged `londonboroughs`. These are the councils under the authority of the Mayor of London and the Greater London Authority.\n\nIt has 33 councils: the London Boroughs plus the City of London (named `City of London`). We don't currently have a tag for this, but if you want to add `londoncouncils` please go ahead.\n\nAnd it's got 35 local planning authorities: the 33 councils plus the two `londondevelopmentcorporations`, named `London Legacy Development Corporation` and `Old Oak and Park Royal Development Corporation`. The tag `london` covers all (and only) the 35 local planning authorities in London.\n\nUKPlanningScraper::Authority.tagged('londonboroughs').size\n \\# =\\> 32\n \nUKPlanningScraper::Authority.tagged('londondevelopmentcorporations').size\n \\# =\\> 2\n\nUKPlanningScraper::Authority.tagged('london').size\n \\# =\\> 35\n\n### More fun with Authority tags\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#more-fun-with-authority-tags)\n\nUKPlanningScraper::Authority.named('Merton').tags\n \\# =\\> \\[\"england\", \"london\", \"londonboroughs\", \"northgate\", \"outerlondon\", \"southlondon\"\\]\n\nUKPlanningScraper::Authority.not\\_tagged('london')\n \\# =\\> \\[...\\]\n\nUKPlanningScraper::Authority.named('Islington').tagged?('southlondon')\n \\# =\\> false\n\n### List all authorities\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#list-all-authorities)\n\nUKPlanningScraper::Authority.all.each { |a| puts a.name }\n\n### List all tags\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#list-all-tags)\n\npp UKPlanningScraper::Authority.tags\n\nAdd your favourite local planning authorities\n---------------------------------------------\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#add-your-favourite-local-planning-authorities)\n\nThe list of authorities is in a CSV file in `/lib/uk_planning_scraper`:\n\n[https://github.com/adrianshort/uk\\_planning\\_scraper/blob/master/lib/uk\\_planning\\_scraper/authorities.csv](https://github.com/adrianshort/uk_planning_scraper/blob/master/lib/uk_planning_scraper/authorities.csv)\n\nThe easiest way to add to or edit this list is to edit within GitHub (use the pencil icon) and create a new pull request for your changes. If accepted, your changes will be available to everyone with the next version of the gem.\n\nThe file format is one line per authority, with comma-separated:\n\n*   Name (omit \"the\", \"council\", \"borough of\", \"city of\", etc. and write \"and\" not \"&\", except for `City of London` which is a special case)\n*   URL of the search form (use the advanced search URL if there is one)\n*   Tags (use as many comma-separated tags as is reasonable, lowercase and all one word.)\n\nThere's no need to manually add tags to the `authorities.csv` file for the software systems like `idox`, `northgate` etc as these are added automatically.\n\nPlease check the tag list before you change anything:\n\npp UKPlanningScraper::Authority.tags\n\nDevelopment\n-----------\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#development)\n\nAfter checking out the repo, run `bin/setup` to install dependencies. You can also run `bin/console` for an interactive prompt that will allow you to experiment.\n\nTo install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org/).\n\nContributing\n------------\n\n[](https://github.com/adrianshort/uk_planning_scraper?screenshot=true#contributing)\n\nBug reports and pull requests are welcome on GitHub at [https://github.com/adrianshort/uk\\_planning\\_scraper](https://github.com/adrianshort/uk_planning_scraper).",
  "usage": {
    "tokens": 2229
  }
}
```
