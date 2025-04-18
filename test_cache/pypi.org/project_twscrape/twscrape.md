---
title: twscrape
description: Twitter GraphQL and Search API implementation with SNScrape data models
url: https://pypi.org/project/twscrape/
timestamp: 2025-01-20T16:02:45.386Z
domain: pypi.org
path: project_twscrape
---

# twscrape


Twitter GraphQL and Search API implementation with SNScrape data models


## Content

[![Image 46: version](https://pypi-camo.freetls.fastly.net/36d31c2526732b71da4e83b106c0de7c0c279824/68747470733a2f2f62616467656e2e6e65742f707970692f762f7477736372617065)](https://pypi.org/project/twscrape) [![Image 47: py versions](https://pypi-camo.freetls.fastly.net/4aa3612c04847d1c6c855a0474162614a01edf18/68747470733a2f2f62616467656e2e6e65742f707970692f707974686f6e2f7477736372617065)](https://pypi.org/project/twscrape) [![Image 48: downloads](https://pypi-camo.freetls.fastly.net/4394efa867eaf02886475e3eb00af5220d7f7116/68747470733a2f2f62616467656e2e6e65742f707970692f646d2f7477736372617065)](https://pypi.org/project/twscrape) [![Image 49: license](https://pypi-camo.freetls.fastly.net/3845b62f2987ff462dcef9a3313855e11b4734a3/68747470733a2f2f62616467656e2e6e65742f6769746875622f6c6963656e73652f766c61646b656e732f7477736372617065)](https://github.com/vladkens/twscrape/blob/main/LICENSE) [![Image 50: donate](https://pypi-camo.freetls.fastly.net/4f4106408d292c5e4eef46ea5f09b447a78369e4/68747470733a2f2f62616467656e2e6e65742f7374617469632f2d2f6275792532306d6525323061253230636f666665652f6666383133663f69636f6e3d6275796d6561636f66666565266c6162656c)](https://buymeacoffee.com/vladkens)

Twitter GraphQL API implementation with [SNScrape](https://github.com/JustAnotherArchivist/snscrape) data models.

![Image 51: example of cli usage](https://pypi-camo.freetls.fastly.net/ff4ee9cb5c33e32385958665ae5058a6e9adc3ac/2e6769746875622f6578616d706c652e706e67)

Install
-------

pip install twscrape

Or development version:

pip install git+https://github.com/vladkens/twscrape.git

Features
--------

*   Support both Search & GraphQL Twitter API
*   Async/Await functions (can run multiple scrapers in parallel at the same time)
*   Login flow (with receiving verification code from email)
*   Saving/restoring account sessions
*   Raw Twitter API responses & SNScrape models
*   Automatic account switching to smooth Twitter API rate limits

Usage
-----

Since this project works through an authorized API, accounts need to be added. You can register and add an account yourself. You can also google sites that provide these things.

The email password is needed to get the code to log in to the account automatically (via imap protocol).

Data models:

*   [User](https://github.com/vladkens/twscrape/blob/main/twscrape/models.py#L87)
*   [Tweet](https://github.com/vladkens/twscrape/blob/main/twscrape/models.py#L136)

import asyncio
from twscrape import API, gather
from twscrape.logger import set\_log\_level

async def main():
    api \= API()  \# or API("path-to.db") - default is \`accounts.db\`

    \# ADD ACCOUNTS (for CLI usage see BELOW)
    await api.pool.add\_account("user1", "pass1", "u1@example.com", "mail\_pass1")
    await api.pool.add\_account("user2", "pass2", "u2@example.com", "mail\_pass2")
    await api.pool.login\_all()

    \# or add account with COOKIES (with cookies login not required)
    cookies \= "abc=12; ct0=xyz"  \# or '{"abc": "12", "ct0": "xyz"}'
    await api.pool.add\_account("user3", "pass3", "u3@mail.com", "mail\_pass3", cookies\=cookies)

    \# API USAGE

    \# search (latest tab)
    await gather(api.search("elon musk", limit\=20))  \# list\[Tweet\]
    \# change search tab (product), can be: Top, Latest (default), Media
    await gather(api.search("elon musk", limit\=20, kv\={"product": "Top"}))

    \# tweet info
    tweet\_id \= 20
    await api.tweet\_details(tweet\_id)  \# Tweet
    await gather(api.retweeters(tweet\_id, limit\=20))  \# list\[User\]

    \# Note: this method have small pagination from X side, like 5 tweets per query
    await gather(api.tweet\_replies(tweet\_id, limit\=20))  \# list\[Tweet\]

    \# get user by login
    user\_login \= "xdevelopers"
    await api.user\_by\_login(user\_login)  \# User

    \# user info
    user\_id \= 2244994945
    await api.user\_by\_id(user\_id)  \# User
    await gather(api.following(user\_id, limit\=20))  \# list\[User\]
    await gather(api.followers(user\_id, limit\=20))  \# list\[User\]
    await gather(api.verified\_followers(user\_id, limit\=20))  \# list\[User\]
    await gather(api.subscriptions(user\_id, limit\=20))  \# list\[User\]
    await gather(api.user\_tweets(user\_id, limit\=20))  \# list\[Tweet\]
    await gather(api.user\_tweets\_and\_replies(user\_id, limit\=20))  \# list\[Tweet\]
    await gather(api.user\_media(user\_id, limit\=20))  \# list\[Tweet\]

    \# list info
    list\_id \= 123456789
    await gather(api.list\_timeline(list\_id))

    \# NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    async for tweet in api.search("elon musk"):
        print(tweet.id, tweet.user.username, tweet.rawContent)  \# tweet is \`Tweet\` object

    \# NOTE 2: all methods have \`raw\` version (returns \`httpx.Response\` object):
    async for rep in api.search\_raw("elon musk"):
        print(rep.status\_code, rep.json())  \# rep is \`httpx.Response\` object

    \# change log level, default info
    set\_log\_level("DEBUG")

    \# Tweet & User model can be converted to regular dict or json, e.g.:
    doc \= await api.user\_by\_id(user\_id)  \# User
    doc.dict()  \# -\> python dict
    doc.json()  \# -\> json string

if \_\_name\_\_ \== "\_\_main\_\_":
    asyncio.run(main())

### Depraceted API methods (no more available in X)

*   favoriters ([ref](https://x.com/XDevelopers/status/1800675411086409765))
*   liked\_tweets ([ref](https://x.com/XDevelopers/status/1800675411086409765))

### Stoping iteration with break

In order to correctly release an account in case of `break` in loop, a special syntax must be used. Otherwise, Python's events loop will release lock on the account sometime in the future. See explanation [here](https://github.com/vladkens/twscrape/issues/27#issuecomment-1623395424).

from contextlib import aclosing

async with aclosing(api.search("elon musk")) as gen:
    async for tweet in gen:
        if tweet.id < 200:
            break

CLI
---

### Get help on CLI commands

\# show all commands
twscrape

\# help on specific comand
twscrape search \--help

### Add accounts

To add accounts use `add_accounts` command. Command syntax is:

twscrape add\_accounts <file\_path\> <line\_format\>

Where: `<line_format>` is format of line if accounts file splited by delimeter. Possible tokens:

*   `username` – required
*   `password` – required
*   `email` – required
*   `email_password` – to receive email code (you can use `--manual` mode to get code)
*   `cookies` – can be any parsable format (string, json, base64 string, etc)
*   `_` – skip column from parse

Tokens should be splited by delimeter, usually "`:`" used.

Example:

I have account files named `order-12345.txt` with format:

username:password:email:email password:user\_agent:cookies

Command to add accounts will be (user\_agent column skiped with `_`):

twscrape add\_accounts ./order-12345.txt username:password:email:email\_password:\_:cookies

### Login accounts

_Note:_ If you added accounts with cookies, login not required.

Run:

twscrape login\_accounts

`twscrape` will start login flow for each new account. If X will ask to verify email and you provided `email_password` in `add_account`, then `twscrape` will try to receive verification code by IMAP protocol. After success login account cookies will be saved to db file for future use.

#### Manual email verification

In case your email provider not support IMAP protocol (ProtonMail, Tutanota, etc) or IMAP is disabled in settings, you can enter email verification code manually. To do this run login command with `--manual` flag.

Example:

twscrape login\_accounts \--manual
twscrape relogin user1 user2 \--manual
twscrape relogin\_failed \--manual

### Get list of accounts and their statuses

twscrape accounts

\# Output:
\# username  logged\_in  active  last\_used            total\_req  error\_msg
\# user1     True       True    2023-05-20 03:20:40  100        None
\# user2     True       True    2023-05-20 03:25:45  120        None
\# user3     False      False   None                 120        Login error

### Re-login accounts

It is possible to re-login specific accounts:

twscrape relogin user1 user2

Or retry login for all failed logins:

twscrape relogin\_failed

### Use different accounts file

Useful if using a different set of accounts for different actions

```
twscrape --db test-accounts.db <command>
```

### Search commands

twscrape search "QUERY" \--limit\=20
twscrape tweet\_details TWEET\_ID
twscrape tweet\_replies TWEET\_ID \--limit\=20
twscrape retweeters TWEET\_ID \--limit\=20
twscrape user\_by\_id USER\_ID
twscrape user\_by\_login USERNAME
twscrape user\_media USER\_ID \--limit\=20
twscrape following USER\_ID \--limit\=20
twscrape followers USER\_ID \--limit\=20
twscrape verified\_followers USER\_ID \--limit\=20
twscrape subscriptions USER\_ID \--limit\=20
twscrape user\_tweets USER\_ID \--limit\=20
twscrape user\_tweets\_and\_replies USER\_ID \--limit\=20

The default output is in the console (stdout), one document per line. So it can be redirected to the file.

twscrape search "elon mask lang:es" \--limit\=20 \> data.txt

By default, parsed data is returned. The original tweet responses can be retrieved with `--raw` flag.

twscrape search "elon mask lang:es" \--limit\=20 \--raw

### About `limit` param

X API works through pagination, each API method can have different defaults for per page parameter (and this parameter can't be changed by caller). So `limit` param in `twscrape` is the desired number of objects (tweets or users, depending on the method). `twscrape` tries to return NO LESS objects than requested. If the X API returns less or more objects, `twscrape` will return whatever X gives.

Proxy
-----

There are few options to use proxies.

1.  You can add proxy per account

proxy \= "http://login:pass@example.com:8080"
await api.pool.add\_account("user4", "pass4", "u4@mail.com", "mail\_pass4", proxy\=proxy)

2.  You can use global proxy for all accounts

proxy \= "http://login:pass@example.com:8080"
api \= API(proxy\=proxy)
doc \= await api.user\_by\_login("elonmusk")

3.  Use can set proxy with environemt variable `TWS_RPOXY`:

TWS\_PROXY\=socks5://user:pass@127.0.0.1:1080 twscrape user\_by\_login elonmusk

4.  You can change proxy any time like:

api.proxy \= "socks5://user:pass@127.0.0.1:1080"
doc \= await api.user\_by\_login("elonmusk")  \# new proxy will be used
api.proxy \= None
doc \= await api.user\_by\_login("elonmusk")  \# no proxy used

5.  Proxy priorities

*   `api.proxy` have top priority
*   `env.proxy` will be used if `api.proxy` is None
*   `acc.proxy` have lowest priotity

So if you want to use proxy PER ACCOUNT, do NOT override proxy with env variable or by passing proxy param to API.

_Note:_ If proxy not working, exception will be raised from API class.

Environment variables
---------------------

*   `TWS_WAIT_EMAIL_CODE` – timeout for email verification code during login (default: `30`, in seconds)
*   `TWS_RAISE_WHEN_NO_ACCOUNT` – raise `NoAccountError` exception when no available accounts right now, instead of waiting for availability (default: `false`, possible value: `false` / `0` / `true` / `1`)

Limitations
-----------

After 1 July 2023 Twitter [introduced new limits](https://x.com/elonmusk/status/1675187969420828672) and still continue to update it periodically.

The basic behaviour is as follows:

*   the request limit is updated every 15 minutes for each endpoint individually
*   e.g. each account have 50 search requests / 15 min, 50 profile requests / 15 min, etc.

API data limits:

*   `user_tweets` & `user_tweets_and_replies` – can return ~3200 tweets maximum

Articles
--------

*   [How to still scrape millions of tweets in 2023](https://medium.com/@vladkens/how-to-still-scrape-millions-of-tweets-in-2023-using-twscrape-97f5d3881434)
*   [_(Add Article)_](https://github.com/vladkens/twscrape/edit/main/readme.md)

See also
--------

*   [twitter-advanced-search](https://github.com/igorbrigadir/twitter-advanced-search) – guide on search filters
*   [twitter-api-client](https://github.com/trevorhobenshield/twitter-api-client) – Implementation of Twitter's v1, v2, and GraphQL APIs
*   [snscrape](https://github.com/JustAnotherArchivist/snscrape) – is a scraper for social networking services (SNS)
*   [twint](https://github.com/twintproject/twint) – Twitter Intelligence Tool

## Metadata

```json
{
  "title": "twscrape",
  "description": "Twitter GraphQL and Search API implementation with SNScrape data models",
  "url": "https://pypi.org/project/twscrape/",
  "content": "[![Image 46: version](https://pypi-camo.freetls.fastly.net/36d31c2526732b71da4e83b106c0de7c0c279824/68747470733a2f2f62616467656e2e6e65742f707970692f762f7477736372617065)](https://pypi.org/project/twscrape) [![Image 47: py versions](https://pypi-camo.freetls.fastly.net/4aa3612c04847d1c6c855a0474162614a01edf18/68747470733a2f2f62616467656e2e6e65742f707970692f707974686f6e2f7477736372617065)](https://pypi.org/project/twscrape) [![Image 48: downloads](https://pypi-camo.freetls.fastly.net/4394efa867eaf02886475e3eb00af5220d7f7116/68747470733a2f2f62616467656e2e6e65742f707970692f646d2f7477736372617065)](https://pypi.org/project/twscrape) [![Image 49: license](https://pypi-camo.freetls.fastly.net/3845b62f2987ff462dcef9a3313855e11b4734a3/68747470733a2f2f62616467656e2e6e65742f6769746875622f6c6963656e73652f766c61646b656e732f7477736372617065)](https://github.com/vladkens/twscrape/blob/main/LICENSE) [![Image 50: donate](https://pypi-camo.freetls.fastly.net/4f4106408d292c5e4eef46ea5f09b447a78369e4/68747470733a2f2f62616467656e2e6e65742f7374617469632f2d2f6275792532306d6525323061253230636f666665652f6666383133663f69636f6e3d6275796d6561636f66666565266c6162656c)](https://buymeacoffee.com/vladkens)\n\nTwitter GraphQL API implementation with [SNScrape](https://github.com/JustAnotherArchivist/snscrape) data models.\n\n![Image 51: example of cli usage](https://pypi-camo.freetls.fastly.net/ff4ee9cb5c33e32385958665ae5058a6e9adc3ac/2e6769746875622f6578616d706c652e706e67)\n\nInstall\n-------\n\npip install twscrape\n\nOr development version:\n\npip install git+https://github.com/vladkens/twscrape.git\n\nFeatures\n--------\n\n*   Support both Search & GraphQL Twitter API\n*   Async/Await functions (can run multiple scrapers in parallel at the same time)\n*   Login flow (with receiving verification code from email)\n*   Saving/restoring account sessions\n*   Raw Twitter API responses & SNScrape models\n*   Automatic account switching to smooth Twitter API rate limits\n\nUsage\n-----\n\nSince this project works through an authorized API, accounts need to be added. You can register and add an account yourself. You can also google sites that provide these things.\n\nThe email password is needed to get the code to log in to the account automatically (via imap protocol).\n\nData models:\n\n*   [User](https://github.com/vladkens/twscrape/blob/main/twscrape/models.py#L87)\n*   [Tweet](https://github.com/vladkens/twscrape/blob/main/twscrape/models.py#L136)\n\nimport asyncio\nfrom twscrape import API, gather\nfrom twscrape.logger import set\\_log\\_level\n\nasync def main():\n    api \\= API()  \\# or API(\"path-to.db\") - default is \\`accounts.db\\`\n\n    \\# ADD ACCOUNTS (for CLI usage see BELOW)\n    await api.pool.add\\_account(\"user1\", \"pass1\", \"u1@example.com\", \"mail\\_pass1\")\n    await api.pool.add\\_account(\"user2\", \"pass2\", \"u2@example.com\", \"mail\\_pass2\")\n    await api.pool.login\\_all()\n\n    \\# or add account with COOKIES (with cookies login not required)\n    cookies \\= \"abc=12; ct0=xyz\"  \\# or '{\"abc\": \"12\", \"ct0\": \"xyz\"}'\n    await api.pool.add\\_account(\"user3\", \"pass3\", \"u3@mail.com\", \"mail\\_pass3\", cookies\\=cookies)\n\n    \\# API USAGE\n\n    \\# search (latest tab)\n    await gather(api.search(\"elon musk\", limit\\=20))  \\# list\\[Tweet\\]\n    \\# change search tab (product), can be: Top, Latest (default), Media\n    await gather(api.search(\"elon musk\", limit\\=20, kv\\={\"product\": \"Top\"}))\n\n    \\# tweet info\n    tweet\\_id \\= 20\n    await api.tweet\\_details(tweet\\_id)  \\# Tweet\n    await gather(api.retweeters(tweet\\_id, limit\\=20))  \\# list\\[User\\]\n\n    \\# Note: this method have small pagination from X side, like 5 tweets per query\n    await gather(api.tweet\\_replies(tweet\\_id, limit\\=20))  \\# list\\[Tweet\\]\n\n    \\# get user by login\n    user\\_login \\= \"xdevelopers\"\n    await api.user\\_by\\_login(user\\_login)  \\# User\n\n    \\# user info\n    user\\_id \\= 2244994945\n    await api.user\\_by\\_id(user\\_id)  \\# User\n    await gather(api.following(user\\_id, limit\\=20))  \\# list\\[User\\]\n    await gather(api.followers(user\\_id, limit\\=20))  \\# list\\[User\\]\n    await gather(api.verified\\_followers(user\\_id, limit\\=20))  \\# list\\[User\\]\n    await gather(api.subscriptions(user\\_id, limit\\=20))  \\# list\\[User\\]\n    await gather(api.user\\_tweets(user\\_id, limit\\=20))  \\# list\\[Tweet\\]\n    await gather(api.user\\_tweets\\_and\\_replies(user\\_id, limit\\=20))  \\# list\\[Tweet\\]\n    await gather(api.user\\_media(user\\_id, limit\\=20))  \\# list\\[Tweet\\]\n\n    \\# list info\n    list\\_id \\= 123456789\n    await gather(api.list\\_timeline(list\\_id))\n\n    \\# NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:\n    async for tweet in api.search(\"elon musk\"):\n        print(tweet.id, tweet.user.username, tweet.rawContent)  \\# tweet is \\`Tweet\\` object\n\n    \\# NOTE 2: all methods have \\`raw\\` version (returns \\`httpx.Response\\` object):\n    async for rep in api.search\\_raw(\"elon musk\"):\n        print(rep.status\\_code, rep.json())  \\# rep is \\`httpx.Response\\` object\n\n    \\# change log level, default info\n    set\\_log\\_level(\"DEBUG\")\n\n    \\# Tweet & User model can be converted to regular dict or json, e.g.:\n    doc \\= await api.user\\_by\\_id(user\\_id)  \\# User\n    doc.dict()  \\# -\\> python dict\n    doc.json()  \\# -\\> json string\n\nif \\_\\_name\\_\\_ \\== \"\\_\\_main\\_\\_\":\n    asyncio.run(main())\n\n### Depraceted API methods (no more available in X)\n\n*   favoriters ([ref](https://x.com/XDevelopers/status/1800675411086409765))\n*   liked\\_tweets ([ref](https://x.com/XDevelopers/status/1800675411086409765))\n\n### Stoping iteration with break\n\nIn order to correctly release an account in case of `break` in loop, a special syntax must be used. Otherwise, Python's events loop will release lock on the account sometime in the future. See explanation [here](https://github.com/vladkens/twscrape/issues/27#issuecomment-1623395424).\n\nfrom contextlib import aclosing\n\nasync with aclosing(api.search(\"elon musk\")) as gen:\n    async for tweet in gen:\n        if tweet.id < 200:\n            break\n\nCLI\n---\n\n### Get help on CLI commands\n\n\\# show all commands\ntwscrape\n\n\\# help on specific comand\ntwscrape search \\--help\n\n### Add accounts\n\nTo add accounts use `add_accounts` command. Command syntax is:\n\ntwscrape add\\_accounts <file\\_path\\> <line\\_format\\>\n\nWhere: `<line_format>` is format of line if accounts file splited by delimeter. Possible tokens:\n\n*   `username` – required\n*   `password` – required\n*   `email` – required\n*   `email_password` – to receive email code (you can use `--manual` mode to get code)\n*   `cookies` – can be any parsable format (string, json, base64 string, etc)\n*   `_` – skip column from parse\n\nTokens should be splited by delimeter, usually \"`:`\" used.\n\nExample:\n\nI have account files named `order-12345.txt` with format:\n\nusername:password:email:email password:user\\_agent:cookies\n\nCommand to add accounts will be (user\\_agent column skiped with `_`):\n\ntwscrape add\\_accounts ./order-12345.txt username:password:email:email\\_password:\\_:cookies\n\n### Login accounts\n\n_Note:_ If you added accounts with cookies, login not required.\n\nRun:\n\ntwscrape login\\_accounts\n\n`twscrape` will start login flow for each new account. If X will ask to verify email and you provided `email_password` in `add_account`, then `twscrape` will try to receive verification code by IMAP protocol. After success login account cookies will be saved to db file for future use.\n\n#### Manual email verification\n\nIn case your email provider not support IMAP protocol (ProtonMail, Tutanota, etc) or IMAP is disabled in settings, you can enter email verification code manually. To do this run login command with `--manual` flag.\n\nExample:\n\ntwscrape login\\_accounts \\--manual\ntwscrape relogin user1 user2 \\--manual\ntwscrape relogin\\_failed \\--manual\n\n### Get list of accounts and their statuses\n\ntwscrape accounts\n\n\\# Output:\n\\# username  logged\\_in  active  last\\_used            total\\_req  error\\_msg\n\\# user1     True       True    2023-05-20 03:20:40  100        None\n\\# user2     True       True    2023-05-20 03:25:45  120        None\n\\# user3     False      False   None                 120        Login error\n\n### Re-login accounts\n\nIt is possible to re-login specific accounts:\n\ntwscrape relogin user1 user2\n\nOr retry login for all failed logins:\n\ntwscrape relogin\\_failed\n\n### Use different accounts file\n\nUseful if using a different set of accounts for different actions\n\n```\ntwscrape --db test-accounts.db <command>\n```\n\n### Search commands\n\ntwscrape search \"QUERY\" \\--limit\\=20\ntwscrape tweet\\_details TWEET\\_ID\ntwscrape tweet\\_replies TWEET\\_ID \\--limit\\=20\ntwscrape retweeters TWEET\\_ID \\--limit\\=20\ntwscrape user\\_by\\_id USER\\_ID\ntwscrape user\\_by\\_login USERNAME\ntwscrape user\\_media USER\\_ID \\--limit\\=20\ntwscrape following USER\\_ID \\--limit\\=20\ntwscrape followers USER\\_ID \\--limit\\=20\ntwscrape verified\\_followers USER\\_ID \\--limit\\=20\ntwscrape subscriptions USER\\_ID \\--limit\\=20\ntwscrape user\\_tweets USER\\_ID \\--limit\\=20\ntwscrape user\\_tweets\\_and\\_replies USER\\_ID \\--limit\\=20\n\nThe default output is in the console (stdout), one document per line. So it can be redirected to the file.\n\ntwscrape search \"elon mask lang:es\" \\--limit\\=20 \\> data.txt\n\nBy default, parsed data is returned. The original tweet responses can be retrieved with `--raw` flag.\n\ntwscrape search \"elon mask lang:es\" \\--limit\\=20 \\--raw\n\n### About `limit` param\n\nX API works through pagination, each API method can have different defaults for per page parameter (and this parameter can't be changed by caller). So `limit` param in `twscrape` is the desired number of objects (tweets or users, depending on the method). `twscrape` tries to return NO LESS objects than requested. If the X API returns less or more objects, `twscrape` will return whatever X gives.\n\nProxy\n-----\n\nThere are few options to use proxies.\n\n1.  You can add proxy per account\n\nproxy \\= \"http://login:pass@example.com:8080\"\nawait api.pool.add\\_account(\"user4\", \"pass4\", \"u4@mail.com\", \"mail\\_pass4\", proxy\\=proxy)\n\n2.  You can use global proxy for all accounts\n\nproxy \\= \"http://login:pass@example.com:8080\"\napi \\= API(proxy\\=proxy)\ndoc \\= await api.user\\_by\\_login(\"elonmusk\")\n\n3.  Use can set proxy with environemt variable `TWS_RPOXY`:\n\nTWS\\_PROXY\\=socks5://user:pass@127.0.0.1:1080 twscrape user\\_by\\_login elonmusk\n\n4.  You can change proxy any time like:\n\napi.proxy \\= \"socks5://user:pass@127.0.0.1:1080\"\ndoc \\= await api.user\\_by\\_login(\"elonmusk\")  \\# new proxy will be used\napi.proxy \\= None\ndoc \\= await api.user\\_by\\_login(\"elonmusk\")  \\# no proxy used\n\n5.  Proxy priorities\n\n*   `api.proxy` have top priority\n*   `env.proxy` will be used if `api.proxy` is None\n*   `acc.proxy` have lowest priotity\n\nSo if you want to use proxy PER ACCOUNT, do NOT override proxy with env variable or by passing proxy param to API.\n\n_Note:_ If proxy not working, exception will be raised from API class.\n\nEnvironment variables\n---------------------\n\n*   `TWS_WAIT_EMAIL_CODE` – timeout for email verification code during login (default: `30`, in seconds)\n*   `TWS_RAISE_WHEN_NO_ACCOUNT` – raise `NoAccountError` exception when no available accounts right now, instead of waiting for availability (default: `false`, possible value: `false` / `0` / `true` / `1`)\n\nLimitations\n-----------\n\nAfter 1 July 2023 Twitter [introduced new limits](https://x.com/elonmusk/status/1675187969420828672) and still continue to update it periodically.\n\nThe basic behaviour is as follows:\n\n*   the request limit is updated every 15 minutes for each endpoint individually\n*   e.g. each account have 50 search requests / 15 min, 50 profile requests / 15 min, etc.\n\nAPI data limits:\n\n*   `user_tweets` & `user_tweets_and_replies` – can return ~3200 tweets maximum\n\nArticles\n--------\n\n*   [How to still scrape millions of tweets in 2023](https://medium.com/@vladkens/how-to-still-scrape-millions-of-tweets-in-2023-using-twscrape-97f5d3881434)\n*   [_(Add Article)_](https://github.com/vladkens/twscrape/edit/main/readme.md)\n\nSee also\n--------\n\n*   [twitter-advanced-search](https://github.com/igorbrigadir/twitter-advanced-search) – guide on search filters\n*   [twitter-api-client](https://github.com/trevorhobenshield/twitter-api-client) – Implementation of Twitter's v1, v2, and GraphQL APIs\n*   [snscrape](https://github.com/JustAnotherArchivist/snscrape) – is a scraper for social networking services (SNS)\n*   [twint](https://github.com/twintproject/twint) – Twitter Intelligence Tool",
  "usage": {
    "tokens": 3710
  }
}
```
