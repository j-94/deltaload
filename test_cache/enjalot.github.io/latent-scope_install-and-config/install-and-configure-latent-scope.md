---
title: Install and Configure | Latent Scope
description: 
url: https://enjalot.github.io/latent-scope/install-and-config
timestamp: 2025-01-20T16:17:05.284Z
domain: enjalot.github.io
path: latent-scope_install-and-config
---

# Install and Configure | Latent Scope



## Content

To process your own data you'll need to install the python module and run it. It's recommended to create a folder where the library can store it's data. This is also a convenient place to make a virtual environment.

Latent Scope works on Mac, Linux and Windows. Python 3.12 is the recommended python version.

```
# make a directory for your data to live
mkdir ~/latent-scope-data
cd ~/latent-scope-data

# create & activate virtual environment
python -m venv lsenv
source lsenv/bin/activate

# install the module
pip install latentscope
# run the module, specifying the data directory and optionally a port to run on
ls-serve ~/latent-scope-data --port 5001
```

This will start a local webserver from which you can access the tool at [http://localhost:5001](http://localhost:5001/)

The next time you want to run Latent Scope you can simply do:

```
cd ~/latent-scope-data
ls-serve
```

[Configure](https://enjalot.github.io/latent-scope/install-and-config#configure)
--------------------------------------------------------------------------------

There are a few settings Latent Scope uses to run, they are stored in a `.env` file where you run `ls-serve` so if you followed the above example you could look in  
`~/latent-scope-data/.env`

You can also see the settings in the web UI at [http://localhost:5001/settings](http://localhost:5001/settings)

[Third Party API keys](https://enjalot.github.io/latent-scope/install-and-config#third-party-api-keys)
------------------------------------------------------------------------------------------------------

You may want to use third party APIs like OpenAI to run parts of the latent scope process. You can do so by setting the API keys in [http://localhost:5001/settings](http://localhost:5001/settings)

![Image 3: Settings API Keys](https://enjalot.github.io/latent-scope/_file/assets/install/settings-api-keys.6e66515d.png)or by manually adding them to `.env`:

```
OPENAI_API_KEY=XXX
TOGETHER_API_KEY=XXX
MISTRAL_API_KEY=XXX
VOYAGE_API_KEY=XXX
COHERE_API_KEY=XXX
```

## Metadata

```json
{
  "title": "Install and Configure | Latent Scope",
  "description": "",
  "url": "https://enjalot.github.io/latent-scope/install-and-config",
  "content": "To process your own data you'll need to install the python module and run it. It's recommended to create a folder where the library can store it's data. This is also a convenient place to make a virtual environment.\n\nLatent Scope works on Mac, Linux and Windows. Python 3.12 is the recommended python version.\n\n```\n# make a directory for your data to live\nmkdir ~/latent-scope-data\ncd ~/latent-scope-data\n\n# create & activate virtual environment\npython -m venv lsenv\nsource lsenv/bin/activate\n\n# install the module\npip install latentscope\n# run the module, specifying the data directory and optionally a port to run on\nls-serve ~/latent-scope-data --port 5001\n```\n\nThis will start a local webserver from which you can access the tool at [http://localhost:5001](http://localhost:5001/)\n\nThe next time you want to run Latent Scope you can simply do:\n\n```\ncd ~/latent-scope-data\nls-serve\n```\n\n[Configure](https://enjalot.github.io/latent-scope/install-and-config#configure)\n--------------------------------------------------------------------------------\n\nThere are a few settings Latent Scope uses to run, they are stored in a `.env` file where you run `ls-serve` so if you followed the above example you could look in  \n`~/latent-scope-data/.env`\n\nYou can also see the settings in the web UI at [http://localhost:5001/settings](http://localhost:5001/settings)\n\n[Third Party API keys](https://enjalot.github.io/latent-scope/install-and-config#third-party-api-keys)\n------------------------------------------------------------------------------------------------------\n\nYou may want to use third party APIs like OpenAI to run parts of the latent scope process. You can do so by setting the API keys in [http://localhost:5001/settings](http://localhost:5001/settings)\n\n![Image 3: Settings API Keys](https://enjalot.github.io/latent-scope/_file/assets/install/settings-api-keys.6e66515d.png)or by manually adding them to `.env`:\n\n```\nOPENAI_API_KEY=XXX\nTOGETHER_API_KEY=XXX\nMISTRAL_API_KEY=XXX\nVOYAGE_API_KEY=XXX\nCOHERE_API_KEY=XXX\n```",
  "usage": {
    "tokens": 481
  }
}
```
