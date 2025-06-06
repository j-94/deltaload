---
title: GitHub - cncf/landscapeapp: 🌄Upstream landscape generation application
description: 🌄Upstream landscape generation application. Contribute to cncf/landscapeapp development by creating an account on GitHub.
url: https://github.com/cncf/landscapeapp
timestamp: 2025-01-20T15:30:58.830Z
domain: github.com
path: cncf_landscapeapp
---

# GitHub - cncf/landscapeapp: 🌄Upstream landscape generation application


🌄Upstream landscape generation application. Contribute to cncf/landscapeapp development by creating an account on GitHub.


## Content

Landscapeapp
------------

[](https://github.com/cncf/landscapeapp?screenshot=true#landscapeapp)

[![Image 25: CII Best Practices](https://camo.githubusercontent.com/f31771c78d64995b3e57d302e2f12857caffd2d89db06445257425e5802d03a2/68747470733a2f2f626573747072616374696365732e636f7265696e6672617374727563747572652e6f72672f70726f6a656374732f323433342f6261646765)](https://bestpractices.coreinfrastructure.org/projects/2434) [![Image 26: npm version](https://camo.githubusercontent.com/1ddc9a2f230970491560e654742d2be47f706bf4227de1f857c5c7913b0b915b/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f696e7465726163746976652d6c616e6473636170652e737667)](https://www.npmjs.com/package/interactive-landscape) [![Image 27: Dependency Status](https://camo.githubusercontent.com/3ac0d8722bb25847788a0c255523c4be5603c0bb63709015b73be6080c307e3c/68747470733a2f2f696d672e736869656c64732e696f2f64617669642f636e63662f6c616e6473636170656170702e7376673f7374796c653d666c61742d737175617265)](https://david-dm.org/cncf/landscapeapp) [![Image 28: Netlify Status](https://camo.githubusercontent.com/ec3e14d5da120fc4523fd2eefd1c5d4c1966c42f756ef6c07bb417cff9d268fc/68747470733a2f2f6170692e6e65746c6966792e636f6d2f6170692f76312f6261646765732f35306437363061382d356232312d343331392d616130312d3261643534653435336664362f6465706c6f792d737461747573)](https://app.netlify.com/sites/landscapeapp/deploys)

*   [Adding and managing landscape entries](https://github.com/cncf/landscapeapp?screenshot=true#adding-and-managing-landscape-entries)
    *   [Logos](https://github.com/cncf/landscapeapp?screenshot=true#logos)
        *   [SVGs Can't Include Text](https://github.com/cncf/landscapeapp?screenshot=true#svgs-cant-include-text)
            *   [CloudConvert](https://github.com/cncf/landscapeapp?screenshot=true#cloudconvert)
            *   [Adobe Illustrator](https://github.com/cncf/landscapeapp?screenshot=true#adobe-illustrator)
            *   [Inkscape](https://github.com/cncf/landscapeapp?screenshot=true#inkscape)
        *   [Crunchbase Requirement](https://github.com/cncf/landscapeapp?screenshot=true#crunchbase-requirement)
*   [External Data](https://github.com/cncf/landscapeapp?screenshot=true#external-data)
*   [Creating a New Landscape](https://github.com/cncf/landscapeapp?screenshot=true#creating-a-new-landscape)
    *   [API Keys](https://github.com/cncf/landscapeapp?screenshot=true#api-keys)
    *   [Installing Locally](https://github.com/cncf/landscapeapp?screenshot=true#installing-locally)
    *   [Adding to a google search console](https://github.com/cncf/landscapeapp?screenshot=true#adding-to-a-google-search-console)
*   [Vulnerability reporting](https://github.com/cncf/landscapeapp?screenshot=true#vulnerability-reporting)
*   [Continuous Integration and NPM Publishing](https://github.com/cncf/landscapeapp?screenshot=true#continuous-integration-and-npm-publishing)
    *   [Building an individual landscape](https://github.com/cncf/landscapeapp?screenshot=true#building-an-individual-landscape)
        *   [Running "remotely" on our build server (fast and by default)](https://github.com/cncf/landscapeapp?screenshot=true#running-remotely-on-our-build-server-fast-and-by-default)
        *   [Running "locally" on Netlify instances (if the remote server is broken)](https://github.com/cncf/landscapeapp?screenshot=true#running-locally-on-netlify-instances-if-the-remote-server-is-broken)
    *   [Building this repo, `landscapeapp` on a Netlify](https://github.com/cncf/landscapeapp?screenshot=true#building-this-repo-landscapeapp-on-a-netlify)
    *   [Setting up our build server to speed up Netlify builds](https://github.com/cncf/landscapeapp?screenshot=true#setting-up-our-build-server-to-speed-up-netlify-builds)
*   [Keeping Project Up to Date](https://github.com/cncf/landscapeapp?screenshot=true#keeping-project-up-to-date)
*   [Embed landscape in a web site](https://github.com/cncf/landscapeapp?screenshot=true#embed-landscape-in-a-web-site)
*   [Generating a Guide](https://github.com/cncf/landscapeapp?screenshot=true#generating-a-guide)

The landscapeapp is an upstream NPM [module](https://www.npmjs.com/package/interactive-landscape) that supports building interactive landscape websites such as the [CNCF Cloud Native Landscape](https://landscape.cncf.io/) ([source](https://github.com/cncf/landscape)) and the [LF Artificial Intelligence Landscape](https://landscape.lfai.foundation/) ([source](https://github.com/lfai/lfai-landscape)). The application is under active development by [Andrey Kozlov](https://github.com/AndreyKozlov1984) and [Jordi Noguera](https://jordinl.com/).

In addition to creating fully interactive sites, the landscapeapp builds static images on each update. See examples in [ADOPTERS.md](https://github.com/cncf/landscapeapp/blob/master/ADOPTERS.md). All current [Linux Foundation](https://linuxfoundation.org/) landscapes are listed in [landscapes.yml](https://github.com/cncf/landscapeapp/blob/master/landscapes.yml).

Adding and managing landscape entries
-------------------------------------

[](https://github.com/cncf/landscapeapp?screenshot=true#adding-and-managing-landscape-entries)

When creating new entries, the only 4 required fields are `name`, `homepage_url`, `logo`, and `crunchbase`.

\- item:
  name: <entry name\>
  homepage\_url: <website for entry\>
  # filename in hosted\_logos folder. Put the svg file into the hosted\_logos
  folder and reference its name.
  logo: <logo for entry\> 
  crunchbase: <twitter for entry\>

Additional keys that can be set are defined below:

  # url for the Twitter account; Only add if the value in Crunchbase is incorrect
  twitter: 
  # url to the repo for the project; will fetch stats if it starts with https://github.com/. If you add a \`repo\_url\` the card will be white instead of grey. 
  repo\_url: 
  # url to the GitHub organization for the project; when using \`repo\_url\`, \`project\_org\` can be set pointing to an organization on GitHub, this will have the effect of pulling the information for all the repos belonging to that organization but using \`repo\_url\` for information regarding license and best practices.
  project\_org: 
  # additional repos for the project; will fetch stats if they start with https://github.com/
  additional\_repos: 
  # Stock Ticker for the organization of the project/entry; normally pulls from Crunchbase but can be overridden here. For delisted and many foreign countries, you'll need to add \`stock\_ticker\` with the value to look up on Yahoo Finance to find the market cap.
  stock\_ticker: 
  # description of the entry; if not set pulls from the GitHub repo description
  description: 
  # default branch to reference if not the main one for the repo
  branch: 
  # if the entry is a project hosted by the project, let's you set the maturity level. Should be a value in relations.values.children.id in settings.yml
  project: 
  # url for the CII Best Practices entry if it's not directly mapped to the repo\_url
  url\_for\_bestpractices: 
  # set to false if a repo\_url is given but the entry is a project that isn't open source
  open\_source: 
  # allows multiple entries with the same repo\_url; set for each instance
  allow\_duplicate\_repo: 
  # set to true if you are using an anonymous organization. You will also need anonymous\_organization set in settings.yml
  unnamed\_organization: 

For some of the key, there is some guidance as listed below.

### Logos

[](https://github.com/cncf/landscapeapp?screenshot=true#logos)

The most challenging part of creating a new landscape is finding SVG images for all projects and companies. These landscapes represent a valuable resource to a community in assembling all related projects, creating a taxonomy, and providing up-to-date logos, and unfortunately, there are no shortcuts.

Do _not_ try to convert PNGs to SVGs. You can't automatically go from a low-res to a high-res format, and you'll just waste time and come up with a substandard result. Instead, invest your time finding SVGs and then (when necessary) having a graphic designer recreate images when high res ones are not available.

Tips for finding high quality images:

*   Google images is often the best way to find a good version of the logo (but ensure it's the up-to-date version). Search for [grpc logo filetype:svg](https://www.google.com/search?q=grpc+logo&tbs=ift:svg,imgo:1&tbm=isch) but substitute your project or product name for grpc.
*   Wikipedia also is a good source for high quality logos ( search in either the main [Wikipedia](https://en.wikipedia.org/w/index.php?sort=relevance&search=svg&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns6=1) or [Wikipedia Commons](https://commons.wikimedia.org/w/index.php?sort=relevance&search=svg&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1) ).
*   VectorLogoZone ( [https://www.vectorlogo.zone/](https://www.vectorlogo.zone/) )
*   Also search for 'svg' in the GitHub for the project, as sometimes projects will embed them there.

For new landscapes of any size, you will probably need a graphic artist to rebuild some of the logos for you.

If the project is hosted/sponsored by an organization but doesn't have a logo, best practice is to use that organization's logo with the title of the project underneath ( [example](https://landscape.cncf.io/selected=netflix-eureka) ). You can use a tool such as [Inkscape](https://inkscape.org/) to add the text.

If you get an error with the image that it has a PNG embedded, you will need to find a different SVG that doesn't include a PNG or work with a graphic artist to rebuild the logo.

#### SVGs Can't Include Text

[](https://github.com/cncf/landscapeapp?screenshot=true#svgs-cant-include-text)

SVGs need to not rely on external fonts so that they will render correctly in any web browser, whether or not the correct fonts are installed. That means that all embedded text and tspan elements need to be converted to objects. Use of SVGs with embedded text will fail with an error. You can convert the SVGs as using one of the tools below.

##### CloudConvert

[](https://github.com/cncf/landscapeapp?screenshot=true#cloudconvert)

1.  Go to [https://cloudconvert.com/](https://cloudconvert.com/), and click 'Select File' and select the SVG file.
2.  Next to 'Convert to', click the dropdown and select 'SVG'
3.  There will be wrench icon that appears. Click that.
4.  For the option 'Text To Path', select 'Yes' and then click 'Okay'
5.  Click 'Convert' to do the conversion and the download the converted file.

##### Adobe Illustrator

[](https://github.com/cncf/landscapeapp?screenshot=true#adobe-illustrator)

1.  Select all text
2.  With the text selected, go to Object \> Expand in the top menu
3.  Export file by going to File \> Export \> Export As in top menu
4.  Select SVG from the format drop down and make sure that "Use Artboards" is checked
5.  This will open a SVG options box, make sure to set Decimal to 5 (that is the highest possible, so to ensure that sufficient detail is preserved)
6.  Click Okay to export

##### Inkscape

[](https://github.com/cncf/landscapeapp?screenshot=true#inkscape)

1.  Select the text
2.  Ctrl+K (path combine)
3.  Ctrl+J (dynamic offset)
4.  Save

### Crunchbase Requirement

[](https://github.com/cncf/landscapeapp?screenshot=true#crunchbase-requirement)

We require all landscape entries to include a [Crunchbase](https://www.crunchbase.com/) url. We use the Crunchbase API to fetch the backing organization and headquarters location and (if they exist), Twitter, LinkedIn, funding, parent organization, and stock ticker. For open source, non-affiliated projects, we will just create a nonprofit organization representing the project (if one doesn't already exist), and set the location to the lead developer.

Using an external source for this info saves effort in most cases, because most organizations are already listed. Going forward, the data is being independently maintained and updated over time.

If for certain reason Crunchbase should not be used - we rely on `organization: { name: 'My Organization Name' }` instead of a `crunchbase` field

#### Overriding industries from Crunchbase

[](https://github.com/cncf/landscapeapp?screenshot=true#overriding-industries-from-crunchbase)

To override industries returned from Crunchbase for a specific Crunchbase entry, add it to an `crunchbase_overrides` top-level entry on `landscape.yml`. For instance, the following will set `industries` for Linux Foundation to Linux and Cloud Computing:

crunchbase\_overrides:
  https://www.crunchbase.com/organization/linux-foundation:
    industries:
      - Linux
      - Cloud Computing

`crunchbase_overrides` must be a top-level key on `landscape.yml`, so it should be a sibling of `landscape`. That's to prevent having to override multiple items that share the same Crunchbase URL.

External Data
-------------

[](https://github.com/cncf/landscapeapp?screenshot=true#external-data)

The canonical source for all data is `landscape.yml`. Once a day, the landscapeapp update\_server pulls data for projects and companies from the following sources:

*   Project info from GitHub
*   Funding info from [Crunchbase](https://www.crunchbase.com/)
*   Market cap data from Yahoo Finance
*   CII Best Practices Badge [data](https://bestpractices.coreinfrastructure.org/)

The update server enhances the source data with the fetched data and saves the result in `processed_landscape.yml` and as `data.json`, the latter of which is what the app loads to display data.

Creating a New Landscape
------------------------

[](https://github.com/cncf/landscapeapp?screenshot=true#creating-a-new-landscape)

If you want to create an interactive landscape for your project or organization:

1.  Note ahead of time that the hardest part of building a landscape is getting hi-res images for every project. You _cannot_ convert from a PNG or JPEG into an SVG. You need to get an SVG, AI, or EPS file. When those aren't available, you will need a graphic designer to recreate several images. Don't just use an auto-tracer to try to convert PNG to SVG because there is some artistry involved in making it look good. Please review this [primer](https://www.cncf.io/blog/2019/07/17/what-image-formats-should-you-be-using-in-2019/) on image formats.
2.  Create a repo `youracronym-landscape` so it's distinct from other landscapes stored in the same directory. From inside your new directory, copy over files from a simpler landscape like [https://github.com/graphql/graphql-landscape](https://github.com/graphql/graphql-landscape) with `cp -r ../graphql-landscape/* ../graphql-landscape/.github ../graphql-landscape/.gitignore ../graphql-landscape/.npmrc ../graphql-landscape/.nvmrc .`.
3.  If you're working with the [LF](https://www.linuxfoundation.org/), give admin privileges to the new repo to [dankohn](https://github.com/dankohn) and write privileges to [AndreyKozlov1984](https://github.com/AndreyKozlov1984), [jordinl83](https://github.com/jordinl83), and [CNCF-Bot](https://github.com/CNCF-Bot) and ping Dan after creating an account at [slack.cncf.io](https://slack.cncf.io/). Alex Contini and Dan are available there to help you recreate SVGs based on a PNG of the company's logo, if necessary, and to fix other problems.
4.  Set the repo to only support merge commits and turn off DCO support, since it doesn't work well with the GitHub web interface: [![Image 29: image](https://user-images.githubusercontent.com/3083270/66166276-dd62ad00-e604-11e9-87db-fd9ae7a80d1a.png)](https://user-images.githubusercontent.com/3083270/66166276-dd62ad00-e604-11e9-87db-fd9ae7a80d1a.png)
5.  Edit `settings.yml` and `landscape.yml` for your topic.
6.  [Generate](https://www.qrcode-monkey.com/) a QR code, setting colors to black. Save as SVG and overwrite images/qr.svg.
7.  Run `y reset-tweet-count` to start the count of tweets mentioning your landscape at zero.
8.  Edit [landscapes.yml](https://github.com/cncf/landscapeapp/blob/master/landscapes.yml) to add your project.

### API Keys

[](https://github.com/cncf/landscapeapp?screenshot=true#api-keys)

You want to add the following to your `~/.bash_profile`. If you're with the LF, ask someone on CNCF [Slack](https://slack.cncf.io/) for the Crunchbase and Twitter keys.

For the GitHub key, please go to [https://github.com/settings/tokens](https://github.com/settings/tokens) and create a key (you can call it `personal landscape`) with _no_ permissions. That is, don't click any checkboxes, because you only need to access public repos.

export CRUNCHBASE\_KEY\_4="key-here"
export TWITTER\_KEYS=keys-here
export GITHUB\_KEY=key-here

### Installing Locally

[](https://github.com/cncf/landscapeapp?screenshot=true#installing-locally)

You can administer a landscape without ever needing to install the software locally. However, a local install is helpful for rapid development, as it reduces the 5 minute build time on Netlify to 10 seconds or less locally. In particular, you want a local install when you're reconfiguring the layout. We recommend installing one or more landscapes as sibling directories to the landscapeapp. Then, you want to install the npm modules for landscapeapp but not for any of the landscapes. Here are the [install](https://github.com/cncf/landscapeapp/blob/master/INSTALL.md) directions.

So, if you're in a directory called `dev`, you would do:

dev$ git clone git@github.com:cncf/landscapeapp.git
dev$ git clone git@github.com:cdfoundation/cdf-landscape.git
dev$ cd landscapeapp
dev$ npm install -g yarn@latest
dev$ yarn

### Adding to a google search console

[](https://github.com/cncf/landscapeapp?screenshot=true#adding-to-a-google-search-console)

Go to the google search console, add a new property, enter the url of the given project, for example, [https://landscape.cncf.io](https://landscape.cncf.io/)

Next, google will want to verify that it is your site, thus you need to choose an `html tag verification` option and copy a secret code from it and put it to the `settings.yml` of a given landscape project. Then commit the change to the default branch and wait till Netlify deploys the default branch. The key is named `google_site_veryfication` and it is somewhere around line 14 in settings.yml. After netlify successfully deploys that dashboard, verify the html tag in a google console. Do not forget to add [Dan@linuxfoundation.org](mailto:Dan@linuxfoundation.org) as someone who has a full access from a `Settings` menu for a given search console.

Vulnerability reporting
-----------------------

[](https://github.com/cncf/landscapeapp?screenshot=true#vulnerability-reporting)

Please open an [issue](https://github.com/cncf/landscapeapp/issues/new) or, for sensitive information, email [info@cncf.io](mailto:info@cncf.io).

Continuous Integration and NPM Publishing
-----------------------------------------

[](https://github.com/cncf/landscapeapp?screenshot=true#continuous-integration-and-npm-publishing)

We have a sophisticated build system. We build this landscapeapp repo together with every landscape after each commit to the landscapeapp. A list of landscapes is stored in the landscapes.yml An individual landscape is built on a PR to that landscape.

Details about building a repo on netlify:

### Building an individual landscape

[](https://github.com/cncf/landscapeapp?screenshot=true#building-an-individual-landscape)

To build an individual landscape, we use Netlify. Netlify has certain issues with the performance and their caching algorithm is ineffective, thus in order to produce the fastest build, these steps are done

Note, that script `netlify/landscape.js` from THIS repo is used to run an individual build on every landscape.

A file netlify.toml specifies which commands are used and how to make a build. We start from the `netlify` folder and then download the landscape.js script from the default branch of a landscapeapp repo and then run a `node netlify/landscape.js` script because otherwise, Netlify will run an unnecessary `npm install` In order to make a build as fast as possible, we designed a way to run it on our own build server. The problem is that Netlify uses very slow and cheap amazon virtual machines, while our build server has a lot of CPUs and enough of RAM, that allows further parallelization during build steps.

#### Running "remotely" on our build server (fast and by default)

[](https://github.com/cncf/landscapeapp?screenshot=true#running-remotely-on-our-build-server-fast-and-by-default)

When an environment variable BUILD\_SERVER is set, the following steps will occur:

*   the interactive-landscape package of the latest version is downloaded from npm
*   a current checkout of an individual landscape with a `landscapeapp` in a `package` folder is rsynced and sent to our build server
*   we use a hash of .nvmrc + package.json + npm-shrinkwrap.json from the `landscapeapp` repo as a key to cache `node_modules`, `~/.nvm` and `~/.npm` folders, this way if the hash has not changed - we reuse existing node\_modules without any setup
*   if a hash is different, we install node\_modules and cache `~/.nvm`, `~/.npm` and `node_modules` for further usage
*   finally, we run a build on our remote server via ssh, and when the build is done, the output is returned via rsync

Those extra steps allow us to run a build faster because we avoid an `npm install` step almost every time and extra RAM and CPU allow running npm tasks `renderLandscape`, `checkLandscape` and `jest` in parallel.

Still, if for certain reasons, remote solution stopped to work and we need to restore the Netlify build process as soon as possible, BUILD\_SERVER variable should be set to empty in either a given landscape or in a shared variables section. Usually, the build will fail for all the landscapes, thus renaming the variable to BUILD\_SERVER\_1 in shared variables is the most efficient way.

One of the possible issues why remote builds would stop to work, although let's hope that will never change, would be that a cache folder is broken, therefore `ssh root@${BUILD_SERVER}` and then calling `rm -rf /root/build` on our build server will clear all the caches used for node\_modules. Then you need to trigger a Netlify build again.

#### Running "locally" on Netlify instances (if the remote server is broken)

[](https://github.com/cncf/landscapeapp?screenshot=true#running-locally-on-netlify-instances-if-the-remote-server-is-broken)

Without BUILD\_SERVER variable, the following steps are done, from a file netlify/netlify.sh

*   the interactive-landscape package of the latest version is downloaded from npm
*   we go to that folder
*   we install node\_modules via `npm install`
*   we run `PROJECT_PATH=.. npm run` build from the interactive-landscape package

### Building this repo, `landscapeapp` on a Netlify

[](https://github.com/cncf/landscapeapp?screenshot=true#building-this-repo-landscapeapp-on-a-netlify)

We want to ensure that we are making builds of all the landscapes, defined in `landscapes.yml` Netlify parameters are stored in the `notilfy.toml` file, and it runs the `node netlify/landscapeapp.js` from the `netlify` folder.

First, we check if the hash of `.nvmrc`, `package.json` and `npm-shrinkwrap` file already exists as a key of our cache on our remote server. If it does exist, it means we can use this folder for `node_modules`, `.npm` and `.nvm` folders for every individual landscape. Then we use rsync to send the current checkout of a repo to our remote server Then for every individual landscape, we run a `build.sh` file on a remote server, in each own docker container for every landscape. That is done in parallel. The file `build.sh` checks out the default branch of a given landscape and then runs `npm run build` with a PROJECT\_PATH pointed to the given landscape

When all builds had been finished, the output is returned to the `dist/${landscape.name}` subfolder and logs are shown. Then \_redirects and \_headers files are generated to allow us to view individual landscapes from a Netlify build.

This repo is built only on our build server because Netlify has a 30 minutes timeout and we can not build individual landscapes there in parallel. Still, if every build fails and there are no obvious reasons, it may help to clear a node\_modules cache: `ssh root@${BUILD_SERVER}` and then calling `rm -rf /root/build` and then running a new build on Netlify again

### Setting up our build server to speed up Netlify builds

[](https://github.com/cncf/landscapeapp?screenshot=true#setting-up-our-build-server-to-speed-up-netlify-builds)

If for some reasons our current server is lost or wiped, or we have to rent a different build server, these are required steps

1.  Install docker on a new server. Just the latest docker, nothing else is required
2.  Generate a new pair of ssh keys, and add a public key to the `/root/.ssh/authorized_keys` file
3.  Take a private key without first and last lines, replace \\n with space, and add as a BUILDBOT\_KEY variable to the shared variable on a Netlify website
4.  Update the BUILD\_SERVER shared variable on a Netlify website and provide the IP address of the new build server

To just check that all is fine, go to the `netlify` folder on your computer, checkout any branch you want or even make local changes, and run `node landscapeapp.js`, do not forget to set all required variables, including the BUILDBOT\_KEY and BUILD\_SERVER. The build should finish with the success and copy generated files and folders to the `dist` folder in the root of the repo checkout

Keeping Project Up to Date
--------------------------

[](https://github.com/cncf/landscapeapp?screenshot=true#keeping-project-up-to-date)

We have an issue #75, where we update all out packages. This is how an update is usually done:

1.  Create a new folder like 75-update-2019-10-16
2.  Run `ncu -u` which is same as `npm-check-updates -u`, do not forget to install `npm install -g npm-check-updates`
3.  Run `npm install` , commit and push and make a PR
4.  Check that everything runs locally, i.e. `npm run open:src should still work well`
5.  Check that there are no layout issues on generated landscapes
6.  Do not forget to read README about those npm packages, which are mentioned in a red color, i.e. have a major update. They may require to implement certain changes in our code.

Embed landscape in a web site
-----------------------------

[](https://github.com/cncf/landscapeapp?screenshot=true#embed-landscape-in-a-web-site)

You can embed the landscape in a website in a few different ways...

*   If you want just a full static image of the landscape in landscape mode, you can do:

```
<!-- Embed ASWF landscape as a PNG -->
<img src="https://landscape.aswf.io/images/landscape.png" alt="Academy Software Foundation Landscape Image">
```

*   If you want to embed the card mode for listing a category of entries ( for example members in a foundation or entries in a certain program ), you can do:

```
<!-- Embed list of all Open Mainframe Project members -->  
<iframe src="https://landscape.openmainframeproject.org/category=open-mainframe-project-member-company&amp;format=logo-mode&amp;grouping=category&amp;embed=yes" frameborder="0" id="landscape" scrolling="no" style="width: 1px; min-width: 100%; opacity: 1; visibility: visible; overflow: hidden; height: 1717px;"></iframe>
<script src="https://landscape.openmainframeproject.org/iframeResizer.js"></script>
```

Generating a Guide
------------------

[](https://github.com/cncf/landscapeapp?screenshot=true#generating-a-guide)

A Guide can be generated by adding a file `guide.md`. `guide.md` will be mostly regular markdown with some custom behavior:

### No headings level 1 allowed

[](https://github.com/cncf/landscapeapp?screenshot=true#no-headings-level-1-allowed)

No [Headings](https://www.markdownguide.org/basic-syntax/#headings) level 1 allowed, use level 2 or higher.

### Linking a category from the landscape to a section on the guide

[](https://github.com/cncf/landscapeapp?screenshot=true#linking-a-category-from-the-landscape-to-a-section-on-the-guide)

If a section on the guide refers to a category on the landscape, an info icon will be added on the category on the landscape and such icon will redirect to the entry on the guide for that category.

In order to associate the category and the section on the guide, the section on the guide should be wrapped between `<section data-category="$categoryId">` and `</section>`, where `$categoryId` is the id of the category.

Don't include a title for the section, a level 2 heading will be automatically generated using the name of the category.

### Linking a subcategory from the landscape to a section on the guide

[](https://github.com/cncf/landscapeapp?screenshot=true#linking-a-subcategory-from-the-landscape-to-a-section-on-the-guide)

If a section on the guide refers to a subcategory on the landscape, an info icon will be added on the subcategory on the landscape and such icon will redirect to the entry on the guide for that subcategory.

In order to associate the subcategory and the section on the guide, the section on the guide should be wrapped between `<section data-subcategory="$subcategoryId" data-buzzwords="$buzzword1,$buzzword2">` and `</section>`, where `$subcategoryId` is the id of the subcategory. Buzzwords is a comma-separated list of words that describe the subcategory, a table will be automatically generated at the bottom of the section including those buzzwords and the list of projects hosted by the organization. The cards with all the logos for that subcategory will also be included at the bottom of the section.

Don't include a title for the section, level 3 heading will be automatically generated using the name of the subcategory.

### Automatic generation of guide navigation

[](https://github.com/cncf/landscapeapp?screenshot=true#automatic-generation-of-guide-navigation)

The guide will include a side-navigation generated automatically from all the headings levels 2 and 3 found on the guide. Level 3 headings will be nested under the closest level 2 heading above.

## Metadata

```json
{
  "title": "GitHub - cncf/landscapeapp: 🌄Upstream landscape generation application",
  "description": "🌄Upstream landscape generation application. Contribute to cncf/landscapeapp development by creating an account on GitHub.",
  "url": "https://github.com/cncf/landscapeapp?screenshot=true",
  "content": "Landscapeapp\n------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#landscapeapp)\n\n[![Image 25: CII Best Practices](https://camo.githubusercontent.com/f31771c78d64995b3e57d302e2f12857caffd2d89db06445257425e5802d03a2/68747470733a2f2f626573747072616374696365732e636f7265696e6672617374727563747572652e6f72672f70726f6a656374732f323433342f6261646765)](https://bestpractices.coreinfrastructure.org/projects/2434) [![Image 26: npm version](https://camo.githubusercontent.com/1ddc9a2f230970491560e654742d2be47f706bf4227de1f857c5c7913b0b915b/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f696e7465726163746976652d6c616e6473636170652e737667)](https://www.npmjs.com/package/interactive-landscape) [![Image 27: Dependency Status](https://camo.githubusercontent.com/3ac0d8722bb25847788a0c255523c4be5603c0bb63709015b73be6080c307e3c/68747470733a2f2f696d672e736869656c64732e696f2f64617669642f636e63662f6c616e6473636170656170702e7376673f7374796c653d666c61742d737175617265)](https://david-dm.org/cncf/landscapeapp) [![Image 28: Netlify Status](https://camo.githubusercontent.com/ec3e14d5da120fc4523fd2eefd1c5d4c1966c42f756ef6c07bb417cff9d268fc/68747470733a2f2f6170692e6e65746c6966792e636f6d2f6170692f76312f6261646765732f35306437363061382d356232312d343331392d616130312d3261643534653435336664362f6465706c6f792d737461747573)](https://app.netlify.com/sites/landscapeapp/deploys)\n\n*   [Adding and managing landscape entries](https://github.com/cncf/landscapeapp?screenshot=true#adding-and-managing-landscape-entries)\n    *   [Logos](https://github.com/cncf/landscapeapp?screenshot=true#logos)\n        *   [SVGs Can't Include Text](https://github.com/cncf/landscapeapp?screenshot=true#svgs-cant-include-text)\n            *   [CloudConvert](https://github.com/cncf/landscapeapp?screenshot=true#cloudconvert)\n            *   [Adobe Illustrator](https://github.com/cncf/landscapeapp?screenshot=true#adobe-illustrator)\n            *   [Inkscape](https://github.com/cncf/landscapeapp?screenshot=true#inkscape)\n        *   [Crunchbase Requirement](https://github.com/cncf/landscapeapp?screenshot=true#crunchbase-requirement)\n*   [External Data](https://github.com/cncf/landscapeapp?screenshot=true#external-data)\n*   [Creating a New Landscape](https://github.com/cncf/landscapeapp?screenshot=true#creating-a-new-landscape)\n    *   [API Keys](https://github.com/cncf/landscapeapp?screenshot=true#api-keys)\n    *   [Installing Locally](https://github.com/cncf/landscapeapp?screenshot=true#installing-locally)\n    *   [Adding to a google search console](https://github.com/cncf/landscapeapp?screenshot=true#adding-to-a-google-search-console)\n*   [Vulnerability reporting](https://github.com/cncf/landscapeapp?screenshot=true#vulnerability-reporting)\n*   [Continuous Integration and NPM Publishing](https://github.com/cncf/landscapeapp?screenshot=true#continuous-integration-and-npm-publishing)\n    *   [Building an individual landscape](https://github.com/cncf/landscapeapp?screenshot=true#building-an-individual-landscape)\n        *   [Running \"remotely\" on our build server (fast and by default)](https://github.com/cncf/landscapeapp?screenshot=true#running-remotely-on-our-build-server-fast-and-by-default)\n        *   [Running \"locally\" on Netlify instances (if the remote server is broken)](https://github.com/cncf/landscapeapp?screenshot=true#running-locally-on-netlify-instances-if-the-remote-server-is-broken)\n    *   [Building this repo, `landscapeapp` on a Netlify](https://github.com/cncf/landscapeapp?screenshot=true#building-this-repo-landscapeapp-on-a-netlify)\n    *   [Setting up our build server to speed up Netlify builds](https://github.com/cncf/landscapeapp?screenshot=true#setting-up-our-build-server-to-speed-up-netlify-builds)\n*   [Keeping Project Up to Date](https://github.com/cncf/landscapeapp?screenshot=true#keeping-project-up-to-date)\n*   [Embed landscape in a web site](https://github.com/cncf/landscapeapp?screenshot=true#embed-landscape-in-a-web-site)\n*   [Generating a Guide](https://github.com/cncf/landscapeapp?screenshot=true#generating-a-guide)\n\nThe landscapeapp is an upstream NPM [module](https://www.npmjs.com/package/interactive-landscape) that supports building interactive landscape websites such as the [CNCF Cloud Native Landscape](https://landscape.cncf.io/) ([source](https://github.com/cncf/landscape)) and the [LF Artificial Intelligence Landscape](https://landscape.lfai.foundation/) ([source](https://github.com/lfai/lfai-landscape)). The application is under active development by [Andrey Kozlov](https://github.com/AndreyKozlov1984) and [Jordi Noguera](https://jordinl.com/).\n\nIn addition to creating fully interactive sites, the landscapeapp builds static images on each update. See examples in [ADOPTERS.md](https://github.com/cncf/landscapeapp/blob/master/ADOPTERS.md). All current [Linux Foundation](https://linuxfoundation.org/) landscapes are listed in [landscapes.yml](https://github.com/cncf/landscapeapp/blob/master/landscapes.yml).\n\nAdding and managing landscape entries\n-------------------------------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#adding-and-managing-landscape-entries)\n\nWhen creating new entries, the only 4 required fields are `name`, `homepage_url`, `logo`, and `crunchbase`.\n\n\\- item:\n  name: <entry name\\>\n  homepage\\_url: <website for entry\\>\n  # filename in hosted\\_logos folder. Put the svg file into the hosted\\_logos\n  folder and reference its name.\n  logo: <logo for entry\\> \n  crunchbase: <twitter for entry\\>\n\nAdditional keys that can be set are defined below:\n\n  # url for the Twitter account; Only add if the value in Crunchbase is incorrect\n  twitter: \n  # url to the repo for the project; will fetch stats if it starts with https://github.com/. If you add a \\`repo\\_url\\` the card will be white instead of grey. \n  repo\\_url: \n  # url to the GitHub organization for the project; when using \\`repo\\_url\\`, \\`project\\_org\\` can be set pointing to an organization on GitHub, this will have the effect of pulling the information for all the repos belonging to that organization but using \\`repo\\_url\\` for information regarding license and best practices.\n  project\\_org: \n  # additional repos for the project; will fetch stats if they start with https://github.com/\n  additional\\_repos: \n  # Stock Ticker for the organization of the project/entry; normally pulls from Crunchbase but can be overridden here. For delisted and many foreign countries, you'll need to add \\`stock\\_ticker\\` with the value to look up on Yahoo Finance to find the market cap.\n  stock\\_ticker: \n  # description of the entry; if not set pulls from the GitHub repo description\n  description: \n  # default branch to reference if not the main one for the repo\n  branch: \n  # if the entry is a project hosted by the project, let's you set the maturity level. Should be a value in relations.values.children.id in settings.yml\n  project: \n  # url for the CII Best Practices entry if it's not directly mapped to the repo\\_url\n  url\\_for\\_bestpractices: \n  # set to false if a repo\\_url is given but the entry is a project that isn't open source\n  open\\_source: \n  # allows multiple entries with the same repo\\_url; set for each instance\n  allow\\_duplicate\\_repo: \n  # set to true if you are using an anonymous organization. You will also need anonymous\\_organization set in settings.yml\n  unnamed\\_organization: \n\nFor some of the key, there is some guidance as listed below.\n\n### Logos\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#logos)\n\nThe most challenging part of creating a new landscape is finding SVG images for all projects and companies. These landscapes represent a valuable resource to a community in assembling all related projects, creating a taxonomy, and providing up-to-date logos, and unfortunately, there are no shortcuts.\n\nDo _not_ try to convert PNGs to SVGs. You can't automatically go from a low-res to a high-res format, and you'll just waste time and come up with a substandard result. Instead, invest your time finding SVGs and then (when necessary) having a graphic designer recreate images when high res ones are not available.\n\nTips for finding high quality images:\n\n*   Google images is often the best way to find a good version of the logo (but ensure it's the up-to-date version). Search for [grpc logo filetype:svg](https://www.google.com/search?q=grpc+logo&tbs=ift:svg,imgo:1&tbm=isch) but substitute your project or product name for grpc.\n*   Wikipedia also is a good source for high quality logos ( search in either the main [Wikipedia](https://en.wikipedia.org/w/index.php?sort=relevance&search=svg&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns6=1) or [Wikipedia Commons](https://commons.wikimedia.org/w/index.php?sort=relevance&search=svg&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1) ).\n*   VectorLogoZone ( [https://www.vectorlogo.zone/](https://www.vectorlogo.zone/) )\n*   Also search for 'svg' in the GitHub for the project, as sometimes projects will embed them there.\n\nFor new landscapes of any size, you will probably need a graphic artist to rebuild some of the logos for you.\n\nIf the project is hosted/sponsored by an organization but doesn't have a logo, best practice is to use that organization's logo with the title of the project underneath ( [example](https://landscape.cncf.io/selected=netflix-eureka) ). You can use a tool such as [Inkscape](https://inkscape.org/) to add the text.\n\nIf you get an error with the image that it has a PNG embedded, you will need to find a different SVG that doesn't include a PNG or work with a graphic artist to rebuild the logo.\n\n#### SVGs Can't Include Text\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#svgs-cant-include-text)\n\nSVGs need to not rely on external fonts so that they will render correctly in any web browser, whether or not the correct fonts are installed. That means that all embedded text and tspan elements need to be converted to objects. Use of SVGs with embedded text will fail with an error. You can convert the SVGs as using one of the tools below.\n\n##### CloudConvert\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#cloudconvert)\n\n1.  Go to [https://cloudconvert.com/](https://cloudconvert.com/), and click 'Select File' and select the SVG file.\n2.  Next to 'Convert to', click the dropdown and select 'SVG'\n3.  There will be wrench icon that appears. Click that.\n4.  For the option 'Text To Path', select 'Yes' and then click 'Okay'\n5.  Click 'Convert' to do the conversion and the download the converted file.\n\n##### Adobe Illustrator\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#adobe-illustrator)\n\n1.  Select all text\n2.  With the text selected, go to Object \\> Expand in the top menu\n3.  Export file by going to File \\> Export \\> Export As in top menu\n4.  Select SVG from the format drop down and make sure that \"Use Artboards\" is checked\n5.  This will open a SVG options box, make sure to set Decimal to 5 (that is the highest possible, so to ensure that sufficient detail is preserved)\n6.  Click Okay to export\n\n##### Inkscape\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#inkscape)\n\n1.  Select the text\n2.  Ctrl+K (path combine)\n3.  Ctrl+J (dynamic offset)\n4.  Save\n\n### Crunchbase Requirement\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#crunchbase-requirement)\n\nWe require all landscape entries to include a [Crunchbase](https://www.crunchbase.com/) url. We use the Crunchbase API to fetch the backing organization and headquarters location and (if they exist), Twitter, LinkedIn, funding, parent organization, and stock ticker. For open source, non-affiliated projects, we will just create a nonprofit organization representing the project (if one doesn't already exist), and set the location to the lead developer.\n\nUsing an external source for this info saves effort in most cases, because most organizations are already listed. Going forward, the data is being independently maintained and updated over time.\n\nIf for certain reason Crunchbase should not be used - we rely on `organization: { name: 'My Organization Name' }` instead of a `crunchbase` field\n\n#### Overriding industries from Crunchbase\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#overriding-industries-from-crunchbase)\n\nTo override industries returned from Crunchbase for a specific Crunchbase entry, add it to an `crunchbase_overrides` top-level entry on `landscape.yml`. For instance, the following will set `industries` for Linux Foundation to Linux and Cloud Computing:\n\ncrunchbase\\_overrides:\n  https://www.crunchbase.com/organization/linux-foundation:\n    industries:\n      - Linux\n      - Cloud Computing\n\n`crunchbase_overrides` must be a top-level key on `landscape.yml`, so it should be a sibling of `landscape`. That's to prevent having to override multiple items that share the same Crunchbase URL.\n\nExternal Data\n-------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#external-data)\n\nThe canonical source for all data is `landscape.yml`. Once a day, the landscapeapp update\\_server pulls data for projects and companies from the following sources:\n\n*   Project info from GitHub\n*   Funding info from [Crunchbase](https://www.crunchbase.com/)\n*   Market cap data from Yahoo Finance\n*   CII Best Practices Badge [data](https://bestpractices.coreinfrastructure.org/)\n\nThe update server enhances the source data with the fetched data and saves the result in `processed_landscape.yml` and as `data.json`, the latter of which is what the app loads to display data.\n\nCreating a New Landscape\n------------------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#creating-a-new-landscape)\n\nIf you want to create an interactive landscape for your project or organization:\n\n1.  Note ahead of time that the hardest part of building a landscape is getting hi-res images for every project. You _cannot_ convert from a PNG or JPEG into an SVG. You need to get an SVG, AI, or EPS file. When those aren't available, you will need a graphic designer to recreate several images. Don't just use an auto-tracer to try to convert PNG to SVG because there is some artistry involved in making it look good. Please review this [primer](https://www.cncf.io/blog/2019/07/17/what-image-formats-should-you-be-using-in-2019/) on image formats.\n2.  Create a repo `youracronym-landscape` so it's distinct from other landscapes stored in the same directory. From inside your new directory, copy over files from a simpler landscape like [https://github.com/graphql/graphql-landscape](https://github.com/graphql/graphql-landscape) with `cp -r ../graphql-landscape/* ../graphql-landscape/.github ../graphql-landscape/.gitignore ../graphql-landscape/.npmrc ../graphql-landscape/.nvmrc .`.\n3.  If you're working with the [LF](https://www.linuxfoundation.org/), give admin privileges to the new repo to [dankohn](https://github.com/dankohn) and write privileges to [AndreyKozlov1984](https://github.com/AndreyKozlov1984), [jordinl83](https://github.com/jordinl83), and [CNCF-Bot](https://github.com/CNCF-Bot) and ping Dan after creating an account at [slack.cncf.io](https://slack.cncf.io/). Alex Contini and Dan are available there to help you recreate SVGs based on a PNG of the company's logo, if necessary, and to fix other problems.\n4.  Set the repo to only support merge commits and turn off DCO support, since it doesn't work well with the GitHub web interface: [![Image 29: image](https://user-images.githubusercontent.com/3083270/66166276-dd62ad00-e604-11e9-87db-fd9ae7a80d1a.png)](https://user-images.githubusercontent.com/3083270/66166276-dd62ad00-e604-11e9-87db-fd9ae7a80d1a.png)\n5.  Edit `settings.yml` and `landscape.yml` for your topic.\n6.  [Generate](https://www.qrcode-monkey.com/) a QR code, setting colors to black. Save as SVG and overwrite images/qr.svg.\n7.  Run `y reset-tweet-count` to start the count of tweets mentioning your landscape at zero.\n8.  Edit [landscapes.yml](https://github.com/cncf/landscapeapp/blob/master/landscapes.yml) to add your project.\n\n### API Keys\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#api-keys)\n\nYou want to add the following to your `~/.bash_profile`. If you're with the LF, ask someone on CNCF [Slack](https://slack.cncf.io/) for the Crunchbase and Twitter keys.\n\nFor the GitHub key, please go to [https://github.com/settings/tokens](https://github.com/settings/tokens) and create a key (you can call it `personal landscape`) with _no_ permissions. That is, don't click any checkboxes, because you only need to access public repos.\n\nexport CRUNCHBASE\\_KEY\\_4=\"key-here\"\nexport TWITTER\\_KEYS=keys-here\nexport GITHUB\\_KEY=key-here\n\n### Installing Locally\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#installing-locally)\n\nYou can administer a landscape without ever needing to install the software locally. However, a local install is helpful for rapid development, as it reduces the 5 minute build time on Netlify to 10 seconds or less locally. In particular, you want a local install when you're reconfiguring the layout. We recommend installing one or more landscapes as sibling directories to the landscapeapp. Then, you want to install the npm modules for landscapeapp but not for any of the landscapes. Here are the [install](https://github.com/cncf/landscapeapp/blob/master/INSTALL.md) directions.\n\nSo, if you're in a directory called `dev`, you would do:\n\ndev$ git clone git@github.com:cncf/landscapeapp.git\ndev$ git clone git@github.com:cdfoundation/cdf-landscape.git\ndev$ cd landscapeapp\ndev$ npm install -g yarn@latest\ndev$ yarn\n\n### Adding to a google search console\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#adding-to-a-google-search-console)\n\nGo to the google search console, add a new property, enter the url of the given project, for example, [https://landscape.cncf.io](https://landscape.cncf.io/)\n\nNext, google will want to verify that it is your site, thus you need to choose an `html tag verification` option and copy a secret code from it and put it to the `settings.yml` of a given landscape project. Then commit the change to the default branch and wait till Netlify deploys the default branch. The key is named `google_site_veryfication` and it is somewhere around line 14 in settings.yml. After netlify successfully deploys that dashboard, verify the html tag in a google console. Do not forget to add [Dan@linuxfoundation.org](mailto:Dan@linuxfoundation.org) as someone who has a full access from a `Settings` menu for a given search console.\n\nVulnerability reporting\n-----------------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#vulnerability-reporting)\n\nPlease open an [issue](https://github.com/cncf/landscapeapp/issues/new) or, for sensitive information, email [info@cncf.io](mailto:info@cncf.io).\n\nContinuous Integration and NPM Publishing\n-----------------------------------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#continuous-integration-and-npm-publishing)\n\nWe have a sophisticated build system. We build this landscapeapp repo together with every landscape after each commit to the landscapeapp. A list of landscapes is stored in the landscapes.yml An individual landscape is built on a PR to that landscape.\n\nDetails about building a repo on netlify:\n\n### Building an individual landscape\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#building-an-individual-landscape)\n\nTo build an individual landscape, we use Netlify. Netlify has certain issues with the performance and their caching algorithm is ineffective, thus in order to produce the fastest build, these steps are done\n\nNote, that script `netlify/landscape.js` from THIS repo is used to run an individual build on every landscape.\n\nA file netlify.toml specifies which commands are used and how to make a build. We start from the `netlify` folder and then download the landscape.js script from the default branch of a landscapeapp repo and then run a `node netlify/landscape.js` script because otherwise, Netlify will run an unnecessary `npm install` In order to make a build as fast as possible, we designed a way to run it on our own build server. The problem is that Netlify uses very slow and cheap amazon virtual machines, while our build server has a lot of CPUs and enough of RAM, that allows further parallelization during build steps.\n\n#### Running \"remotely\" on our build server (fast and by default)\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#running-remotely-on-our-build-server-fast-and-by-default)\n\nWhen an environment variable BUILD\\_SERVER is set, the following steps will occur:\n\n*   the interactive-landscape package of the latest version is downloaded from npm\n*   a current checkout of an individual landscape with a `landscapeapp` in a `package` folder is rsynced and sent to our build server\n*   we use a hash of .nvmrc + package.json + npm-shrinkwrap.json from the `landscapeapp` repo as a key to cache `node_modules`, `~/.nvm` and `~/.npm` folders, this way if the hash has not changed - we reuse existing node\\_modules without any setup\n*   if a hash is different, we install node\\_modules and cache `~/.nvm`, `~/.npm` and `node_modules` for further usage\n*   finally, we run a build on our remote server via ssh, and when the build is done, the output is returned via rsync\n\nThose extra steps allow us to run a build faster because we avoid an `npm install` step almost every time and extra RAM and CPU allow running npm tasks `renderLandscape`, `checkLandscape` and `jest` in parallel.\n\nStill, if for certain reasons, remote solution stopped to work and we need to restore the Netlify build process as soon as possible, BUILD\\_SERVER variable should be set to empty in either a given landscape or in a shared variables section. Usually, the build will fail for all the landscapes, thus renaming the variable to BUILD\\_SERVER\\_1 in shared variables is the most efficient way.\n\nOne of the possible issues why remote builds would stop to work, although let's hope that will never change, would be that a cache folder is broken, therefore `ssh root@${BUILD_SERVER}` and then calling `rm -rf /root/build` on our build server will clear all the caches used for node\\_modules. Then you need to trigger a Netlify build again.\n\n#### Running \"locally\" on Netlify instances (if the remote server is broken)\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#running-locally-on-netlify-instances-if-the-remote-server-is-broken)\n\nWithout BUILD\\_SERVER variable, the following steps are done, from a file netlify/netlify.sh\n\n*   the interactive-landscape package of the latest version is downloaded from npm\n*   we go to that folder\n*   we install node\\_modules via `npm install`\n*   we run `PROJECT_PATH=.. npm run` build from the interactive-landscape package\n\n### Building this repo, `landscapeapp` on a Netlify\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#building-this-repo-landscapeapp-on-a-netlify)\n\nWe want to ensure that we are making builds of all the landscapes, defined in `landscapes.yml` Netlify parameters are stored in the `notilfy.toml` file, and it runs the `node netlify/landscapeapp.js` from the `netlify` folder.\n\nFirst, we check if the hash of `.nvmrc`, `package.json` and `npm-shrinkwrap` file already exists as a key of our cache on our remote server. If it does exist, it means we can use this folder for `node_modules`, `.npm` and `.nvm` folders for every individual landscape. Then we use rsync to send the current checkout of a repo to our remote server Then for every individual landscape, we run a `build.sh` file on a remote server, in each own docker container for every landscape. That is done in parallel. The file `build.sh` checks out the default branch of a given landscape and then runs `npm run build` with a PROJECT\\_PATH pointed to the given landscape\n\nWhen all builds had been finished, the output is returned to the `dist/${landscape.name}` subfolder and logs are shown. Then \\_redirects and \\_headers files are generated to allow us to view individual landscapes from a Netlify build.\n\nThis repo is built only on our build server because Netlify has a 30 minutes timeout and we can not build individual landscapes there in parallel. Still, if every build fails and there are no obvious reasons, it may help to clear a node\\_modules cache: `ssh root@${BUILD_SERVER}` and then calling `rm -rf /root/build` and then running a new build on Netlify again\n\n### Setting up our build server to speed up Netlify builds\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#setting-up-our-build-server-to-speed-up-netlify-builds)\n\nIf for some reasons our current server is lost or wiped, or we have to rent a different build server, these are required steps\n\n1.  Install docker on a new server. Just the latest docker, nothing else is required\n2.  Generate a new pair of ssh keys, and add a public key to the `/root/.ssh/authorized_keys` file\n3.  Take a private key without first and last lines, replace \\\\n with space, and add as a BUILDBOT\\_KEY variable to the shared variable on a Netlify website\n4.  Update the BUILD\\_SERVER shared variable on a Netlify website and provide the IP address of the new build server\n\nTo just check that all is fine, go to the `netlify` folder on your computer, checkout any branch you want or even make local changes, and run `node landscapeapp.js`, do not forget to set all required variables, including the BUILDBOT\\_KEY and BUILD\\_SERVER. The build should finish with the success and copy generated files and folders to the `dist` folder in the root of the repo checkout\n\nKeeping Project Up to Date\n--------------------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#keeping-project-up-to-date)\n\nWe have an issue #75, where we update all out packages. This is how an update is usually done:\n\n1.  Create a new folder like 75-update-2019-10-16\n2.  Run `ncu -u` which is same as `npm-check-updates -u`, do not forget to install `npm install -g npm-check-updates`\n3.  Run `npm install` , commit and push and make a PR\n4.  Check that everything runs locally, i.e. `npm run open:src should still work well`\n5.  Check that there are no layout issues on generated landscapes\n6.  Do not forget to read README about those npm packages, which are mentioned in a red color, i.e. have a major update. They may require to implement certain changes in our code.\n\nEmbed landscape in a web site\n-----------------------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#embed-landscape-in-a-web-site)\n\nYou can embed the landscape in a website in a few different ways...\n\n*   If you want just a full static image of the landscape in landscape mode, you can do:\n\n```\n<!-- Embed ASWF landscape as a PNG -->\n<img src=\"https://landscape.aswf.io/images/landscape.png\" alt=\"Academy Software Foundation Landscape Image\">\n```\n\n*   If you want to embed the card mode for listing a category of entries ( for example members in a foundation or entries in a certain program ), you can do:\n\n```\n<!-- Embed list of all Open Mainframe Project members -->  \n<iframe src=\"https://landscape.openmainframeproject.org/category=open-mainframe-project-member-company&amp;format=logo-mode&amp;grouping=category&amp;embed=yes\" frameborder=\"0\" id=\"landscape\" scrolling=\"no\" style=\"width: 1px; min-width: 100%; opacity: 1; visibility: visible; overflow: hidden; height: 1717px;\"></iframe>\n<script src=\"https://landscape.openmainframeproject.org/iframeResizer.js\"></script>\n```\n\nGenerating a Guide\n------------------\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#generating-a-guide)\n\nA Guide can be generated by adding a file `guide.md`. `guide.md` will be mostly regular markdown with some custom behavior:\n\n### No headings level 1 allowed\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#no-headings-level-1-allowed)\n\nNo [Headings](https://www.markdownguide.org/basic-syntax/#headings) level 1 allowed, use level 2 or higher.\n\n### Linking a category from the landscape to a section on the guide\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#linking-a-category-from-the-landscape-to-a-section-on-the-guide)\n\nIf a section on the guide refers to a category on the landscape, an info icon will be added on the category on the landscape and such icon will redirect to the entry on the guide for that category.\n\nIn order to associate the category and the section on the guide, the section on the guide should be wrapped between `<section data-category=\"$categoryId\">` and `</section>`, where `$categoryId` is the id of the category.\n\nDon't include a title for the section, a level 2 heading will be automatically generated using the name of the category.\n\n### Linking a subcategory from the landscape to a section on the guide\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#linking-a-subcategory-from-the-landscape-to-a-section-on-the-guide)\n\nIf a section on the guide refers to a subcategory on the landscape, an info icon will be added on the subcategory on the landscape and such icon will redirect to the entry on the guide for that subcategory.\n\nIn order to associate the subcategory and the section on the guide, the section on the guide should be wrapped between `<section data-subcategory=\"$subcategoryId\" data-buzzwords=\"$buzzword1,$buzzword2\">` and `</section>`, where `$subcategoryId` is the id of the subcategory. Buzzwords is a comma-separated list of words that describe the subcategory, a table will be automatically generated at the bottom of the section including those buzzwords and the list of projects hosted by the organization. The cards with all the logos for that subcategory will also be included at the bottom of the section.\n\nDon't include a title for the section, level 3 heading will be automatically generated using the name of the subcategory.\n\n### Automatic generation of guide navigation\n\n[](https://github.com/cncf/landscapeapp?screenshot=true#automatic-generation-of-guide-navigation)\n\nThe guide will include a side-navigation generated automatically from all the headings levels 2 and 3 found on the guide. Level 3 headings will be nested under the closest level 2 heading above.",
  "usage": {
    "tokens": 7472
  }
}
```
