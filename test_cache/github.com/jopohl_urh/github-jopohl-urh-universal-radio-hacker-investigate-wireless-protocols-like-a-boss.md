---
title: GitHub - jopohl/urh: Universal Radio Hacker: Investigate Wireless Protocols Like A Boss
description: Universal Radio Hacker: Investigate Wireless Protocols Like A Boss - jopohl/urh
url: https://github.com/jopohl/urh
timestamp: 2025-01-20T15:30:18.469Z
domain: github.com
path: jopohl_urh
---

# GitHub - jopohl/urh: Universal Radio Hacker: Investigate Wireless Protocols Like A Boss


Universal Radio Hacker: Investigate Wireless Protocols Like A Boss - jopohl/urh


## Content

[![Image 36: URH image](https://raw.githubusercontent.com/jopohl/urh/master/data/icons/banner.png)](https://raw.githubusercontent.com/jopohl/urh/master/data/icons/banner.png)

[![Image 37: CI](https://github.com/jopohl/urh/actions/workflows/ci.yml/badge.svg)](https://github.com/jopohl/urh/actions/workflows/ci.yml) [![Image 38: Code style: black](https://camo.githubusercontent.com/a41c88e230f45ad28a302c9a5e09c79901e172d8d81499fcffc16c191819b5a9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d626c61636b)](https://github.com/psf/black) [![Image 39: PyPI version](https://camo.githubusercontent.com/10290198ee567db71cd8b16349360441cc6771a00573faf530347c60fa64f14d/68747470733a2f2f62616467652e667572792e696f2f70792f7572682e737667)](https://badge.fury.io/py/urh) [![Image 40: Packaging status](https://camo.githubusercontent.com/d520c3624dd8509f24a2f1a6bdcb1e958b5b4d9cb254b496da232ca0eedf4b1b/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f74696e792d7265706f732f7572682e737667)](https://repology.org/project/urh/versions) [![Image 41: Blackhat Arsenal 2017](https://camo.githubusercontent.com/7a20e269a1df3c9df58ecdccfb95d8d7afd201aae0254b68cc5863cf9e883bc9/68747470733a2f2f7261776769742e636f6d2f746f6f6c7377617463682f6261646765732f6d61737465722f617273656e616c2f7573612f323031372e737667)](http://www.toolswatch.org/2017/06/the-black-hat-arsenal-usa-2017-phenomenal-line-up-announced/) [![Image 42: Blackhat Arsenal 2018](https://camo.githubusercontent.com/6894c7f53c44f0103e394b52576780832827e2d701c25b8bd80cabd4a53d1c45/68747470733a2f2f7261776769742e636f6d2f746f6f6c7377617463682f6261646765732f6d61737465722f617273656e616c2f6575726f70652f323031382e737667)](http://www.toolswatch.org/2018/09/black-hat-arsenal-europe-2018-lineup-announced/)

The Universal Radio Hacker (URH) is a complete suite for wireless protocol investigation with native support for [many](https://github.com/jopohl/urh/wiki/Supported-devices) common **Software Defined Radios**. URH allows **easy demodulation** of signals combined with an [automatic](https://dl.acm.org/doi/10.1145/3375894.3375896) detection of modulation parameters making it a breeze to identify the bits and bytes that fly over the air. As data often gets _encoded_ before transmission, URH offers **customizable decodings** to crack even sophisticated encodings like CC1101 data whitening. When it comes to **protocol reverse-engineering**, URH is helpful in two ways. You can either manually assign protocol fields and message types or let URH **automatically infer protocol fields** with a [rule-based intelligence](https://www.usenix.org/conference/woot19/presentation/pohl). Finally, URH entails a **fuzzing component** aimed at stateless protocols and a **simulation environment** for stateful attacks.

### Getting started

[](https://github.com/jopohl/urh?screenshot=true#getting-started)

In order to get started

*   view the [installation instructions](https://github.com/jopohl/urh?screenshot=true#Installation) on this page,
*   download the [official userguide (PDF)](https://github.com/jopohl/urh/releases/download/v2.0.0/userguide.pdf),
*   watch the [demonstration videos (YouTube)](https://www.youtube.com/watch?v=kuubkTDAxwA&index=1&list=PLlKjreY6G-1EKKBs9sucMdk8PwzcFuIPB),
*   check out the [wiki](https://github.com/jopohl/urh/wiki) for more information such as supported devices or
*   read some [articles about URH](https://github.com/jopohl/urh?screenshot=true#Articles) for inspiration.

If you like URH, please ⭐ this repository and [join our Slack channel](https://join.slack.com/t/stralsundsecurity/shared_invite/enQtMjEwOTIxNzMzODc3LTk3NmE4MGVjYjEyYTMzYTdmN2RlNzUzYzg0NTNjNTQ2ODBkMzI3MDZlOWY3MjE4YjBkNTM4ZjJlNTJlZmJhNDg). We appreciate your support!

### Citing URH

[](https://github.com/jopohl/urh?screenshot=true#citing-urh)

We encourage researchers working with URH to cite [this](https://www.usenix.org/conference/woot18/presentation/pohl) WOOT'18 paper or directly use the following BibTeX entry.

**URH BibTeX entry for your research paper**

@inproceedings {220562,
author = {Johannes Pohl and Andreas Noack},
title = {Universal Radio Hacker: A Suite for Analyzing and Attacking Stateful Wireless Protocols},
booktitle = {12th {USENIX} Workshop on Offensive Technologies ({WOOT} 18)},
year = {2018},
address = {Baltimore, MD},
url = {https://www.usenix.org/conference/woot18/presentation/pohl},
publisher = {{USENIX} Association},
}

Installation
------------

[](https://github.com/jopohl/urh?screenshot=true#installation)

URH runs on Windows, Linux and macOS. See below for OS specific installation instructions.

### Windows

[](https://github.com/jopohl/urh?screenshot=true#windows)

On Windows, URH can be installed with its [Installer](https://github.com/jopohl/urh/releases). No further dependencies are required.

If you get an error about missing `api-ms-win-crt-runtime-l1-1-0.dll`, run Windows Update or directly install [KB2999226](https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows).

### Linux

[](https://github.com/jopohl/urh?screenshot=true#linux)

#### Installation with pipx

[](https://github.com/jopohl/urh?screenshot=true#installation-with-pipx)

URH is available on [PyPi](https://pypi.org/project/urh/) so you can install it, for example, with [pipx](https://pypa.github.io/pipx/):

This is the recommended way to install URH on Linux because it comes with **all native extensions** precompiled.

In order to access your SDR as non-root user, install the according **udev rules**. You can find them [in the wiki](https://github.com/jopohl/urh/wiki/SDR-udev-rules).

#### Install via Package Manager

[](https://github.com/jopohl/urh?screenshot=true#install-via-package-manager)

URH is included in the repositories of many linux distributions such as **Arch Linux**, **Gentoo**, **Fedora**, **openSUSE** or **NixOS**. There is also a package for **FreeBSD**. If available, simply use your package manager to install URH.

**Note**: For native support, you must install the according `-dev` package(s) of your SDR(s) such as `hackrf-dev` **before** installing URH.

#### Docker Images

[](https://github.com/jopohl/urh?screenshot=true#docker-images)

The official URH docker image is available [here](https://hub.docker.com/r/jopohl/urh/). It has all native backends included and ready to operate.

### macOS

[](https://github.com/jopohl/urh?screenshot=true#macos)

#### Using DMG

[](https://github.com/jopohl/urh?screenshot=true#using-dmg)

It is recommended to use **at least macOS 13** when using the DMG available [here](https://github.com/jopohl/urh/releases).

#### With brew

[](https://github.com/jopohl/urh?screenshot=true#with-brew)

URH is available as a [homebrew formula](https://formulae.brew.sh/formula/urh) so you can install it with

### Running from source (OS-agnostic)

[](https://github.com/jopohl/urh?screenshot=true#running-from-source-os-agnostic)

#### Without installation

[](https://github.com/jopohl/urh?screenshot=true#without-installation)

To execute the Universal Radio Hacker without installation, just run:

```
git clone https://github.com/jopohl/urh/
cd urh/src/urh
./main.py
```

Note, before first usage the C++ extensions will be built.

#### Installing from source

[](https://github.com/jopohl/urh?screenshot=true#installing-from-source)

To install URH from source you need to have `python-setuptools` installed. You can get them with `python3 -m pip install setuptools`. Once the setuptools are installed execute:

```
git clone https://github.com/jopohl/urh/
cd urh
python setup.py install
```

And start the application by typing `urh` in a terminal.

Articles
--------

[](https://github.com/jopohl/urh?screenshot=true#articles)

### Hacking stuff with URH

[](https://github.com/jopohl/urh?screenshot=true#hacking-stuff-with-urh)

*   [Hacking Burger Pagers](https://www.rtl-sdr.com/using-a-hackrf-to-reverse-engineer-and-control-restaurant-pagers/)
*   [Reverse-engineer and Clone a Remote Control](https://www.rtl-sdr.com/video-tutorial-using-universal-radio-hacker-an-rtl-sdr-and-a-microcontroller-to-clone-433-mhz-remotes/)
*   [Reverse-engineering Weather Station RF Signals](https://www.rtl-sdr.com/tag/universal-radio-hacker/)
*   [Reverse-engineering Wireless Blinds](https://www.rtl-sdr.com/reverse-engineering-wireless-blinds-with-an-rtl-sdr-and-controlling-them-with-amazon-alexa/)
*   [Attacking Logitech Wireless Presenters (German Article)](https://www.heise.de/security/meldung/Wireless-Presenter-von-Logitech-und-Inateck-anfaellig-fuer-Angriffe-ueber-Funk-4439795.html)
*   [Attacking Wireless Keyboards](https://threatpost.com/fujitsu-wireless-keyboard-unpatched-flaws/149477/)
*   [Reverse-engineering a 433MHz Remote-controlled Power Socket for use with Arduino](http://www.ignorantofthings.com/2018/11/reverse-engineering-433mhz-remote.html)

### General presentations and tutorials on URH

[](https://github.com/jopohl/urh?screenshot=true#general-presentations-and-tutorials-on-urh)

*   [Hackaday Article](https://hackaday.com/2017/02/23/universal-radio-hacker/)
*   [RTL-SDR.com Article](https://www.rtl-sdr.com/reverse-engineering-signals-universal-radio-hacker-software/)
*   [Short Tutorial on URH with LimeSDR Mini](https://www.crowdsupply.com/lime-micro/limesdr-mini/updates/investigating-wireless-protocols-with-universal-radio-hacker)
*   [Brute-forcing a RF Device: a Step-by-step Guide](https://pandwarf.com/news/brute-forcing-a-new-device-a-step-by-step-guide/)
*   [Hacking wireless sockets like a NOOB](https://olof-astrand.medium.com/hacking-wireless-sockets-like-a-noob-b57d4b4812d5)

External decodings
------------------

[](https://github.com/jopohl/urh?screenshot=true#external-decodings)

See [wiki](https://github.com/jopohl/urh/wiki/External-decodings) for a list of external decodings provided by our community! Thanks for that!

Screenshots
-----------

[](https://github.com/jopohl/urh?screenshot=true#screenshots)

### Get the data out of raw signals

[](https://github.com/jopohl/urh?screenshot=true#get-the-data-out-of-raw-signals)

[![Image 43: Interpretation phase](https://camo.githubusercontent.com/a135c200210d7c7445b9fc3cd07d31bc896a6a392a1ed596d1e95fc15a05331e/687474703a2f2f692e696d6775722e636f6d2f577931375a76332e706e67)](https://camo.githubusercontent.com/a135c200210d7c7445b9fc3cd07d31bc896a6a392a1ed596d1e95fc15a05331e/687474703a2f2f692e696d6775722e636f6d2f577931375a76332e706e67)

### Keep an overview even on complex protocols

[](https://github.com/jopohl/urh?screenshot=true#keep-an-overview-even-on-complex-protocols)

[![Image 44: Analysis phase](https://camo.githubusercontent.com/7d9061753c1285b7e50a073cc95803cdba5d91b6cdc69fa7caf47f23beb87904/687474703a2f2f692e696d6775722e636f6d2f7562414c3370452e706e67)](https://camo.githubusercontent.com/7d9061753c1285b7e50a073cc95803cdba5d91b6cdc69fa7caf47f23beb87904/687474703a2f2f692e696d6775722e636f6d2f7562414c3370452e706e67)

### Record and send signals

[](https://github.com/jopohl/urh?screenshot=true#record-and-send-signals)

[![Image 45: Record](https://camo.githubusercontent.com/cc825e4d698238b30357414a901bec2d5cbfb04de1dc7beaf60c5392a1d98828/687474703a2f2f692e696d6775722e636f6d2f426651706732332e706e67)](https://camo.githubusercontent.com/cc825e4d698238b30357414a901bec2d5cbfb04de1dc7beaf60c5392a1d98828/687474703a2f2f692e696d6775722e636f6d2f426651706732332e706e67)

## Metadata

```json
{
  "title": "GitHub - jopohl/urh: Universal Radio Hacker: Investigate Wireless Protocols Like A Boss",
  "description": "Universal Radio Hacker: Investigate Wireless Protocols Like A Boss - jopohl/urh",
  "url": "https://github.com/jopohl/urh?screenshot=true",
  "content": "[![Image 36: URH image](https://raw.githubusercontent.com/jopohl/urh/master/data/icons/banner.png)](https://raw.githubusercontent.com/jopohl/urh/master/data/icons/banner.png)\n\n[![Image 37: CI](https://github.com/jopohl/urh/actions/workflows/ci.yml/badge.svg)](https://github.com/jopohl/urh/actions/workflows/ci.yml) [![Image 38: Code style: black](https://camo.githubusercontent.com/a41c88e230f45ad28a302c9a5e09c79901e172d8d81499fcffc16c191819b5a9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d626c61636b)](https://github.com/psf/black) [![Image 39: PyPI version](https://camo.githubusercontent.com/10290198ee567db71cd8b16349360441cc6771a00573faf530347c60fa64f14d/68747470733a2f2f62616467652e667572792e696f2f70792f7572682e737667)](https://badge.fury.io/py/urh) [![Image 40: Packaging status](https://camo.githubusercontent.com/d520c3624dd8509f24a2f1a6bdcb1e958b5b4d9cb254b496da232ca0eedf4b1b/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f74696e792d7265706f732f7572682e737667)](https://repology.org/project/urh/versions) [![Image 41: Blackhat Arsenal 2017](https://camo.githubusercontent.com/7a20e269a1df3c9df58ecdccfb95d8d7afd201aae0254b68cc5863cf9e883bc9/68747470733a2f2f7261776769742e636f6d2f746f6f6c7377617463682f6261646765732f6d61737465722f617273656e616c2f7573612f323031372e737667)](http://www.toolswatch.org/2017/06/the-black-hat-arsenal-usa-2017-phenomenal-line-up-announced/) [![Image 42: Blackhat Arsenal 2018](https://camo.githubusercontent.com/6894c7f53c44f0103e394b52576780832827e2d701c25b8bd80cabd4a53d1c45/68747470733a2f2f7261776769742e636f6d2f746f6f6c7377617463682f6261646765732f6d61737465722f617273656e616c2f6575726f70652f323031382e737667)](http://www.toolswatch.org/2018/09/black-hat-arsenal-europe-2018-lineup-announced/)\n\nThe Universal Radio Hacker (URH) is a complete suite for wireless protocol investigation with native support for [many](https://github.com/jopohl/urh/wiki/Supported-devices) common **Software Defined Radios**. URH allows **easy demodulation** of signals combined with an [automatic](https://dl.acm.org/doi/10.1145/3375894.3375896) detection of modulation parameters making it a breeze to identify the bits and bytes that fly over the air. As data often gets _encoded_ before transmission, URH offers **customizable decodings** to crack even sophisticated encodings like CC1101 data whitening. When it comes to **protocol reverse-engineering**, URH is helpful in two ways. You can either manually assign protocol fields and message types or let URH **automatically infer protocol fields** with a [rule-based intelligence](https://www.usenix.org/conference/woot19/presentation/pohl). Finally, URH entails a **fuzzing component** aimed at stateless protocols and a **simulation environment** for stateful attacks.\n\n### Getting started\n\n[](https://github.com/jopohl/urh?screenshot=true#getting-started)\n\nIn order to get started\n\n*   view the [installation instructions](https://github.com/jopohl/urh?screenshot=true#Installation) on this page,\n*   download the [official userguide (PDF)](https://github.com/jopohl/urh/releases/download/v2.0.0/userguide.pdf),\n*   watch the [demonstration videos (YouTube)](https://www.youtube.com/watch?v=kuubkTDAxwA&index=1&list=PLlKjreY6G-1EKKBs9sucMdk8PwzcFuIPB),\n*   check out the [wiki](https://github.com/jopohl/urh/wiki) for more information such as supported devices or\n*   read some [articles about URH](https://github.com/jopohl/urh?screenshot=true#Articles) for inspiration.\n\nIf you like URH, please ⭐ this repository and [join our Slack channel](https://join.slack.com/t/stralsundsecurity/shared_invite/enQtMjEwOTIxNzMzODc3LTk3NmE4MGVjYjEyYTMzYTdmN2RlNzUzYzg0NTNjNTQ2ODBkMzI3MDZlOWY3MjE4YjBkNTM4ZjJlNTJlZmJhNDg). We appreciate your support!\n\n### Citing URH\n\n[](https://github.com/jopohl/urh?screenshot=true#citing-urh)\n\nWe encourage researchers working with URH to cite [this](https://www.usenix.org/conference/woot18/presentation/pohl) WOOT'18 paper or directly use the following BibTeX entry.\n\n**URH BibTeX entry for your research paper**\n\n@inproceedings {220562,\nauthor = {Johannes Pohl and Andreas Noack},\ntitle = {Universal Radio Hacker: A Suite for Analyzing and Attacking Stateful Wireless Protocols},\nbooktitle = {12th {USENIX} Workshop on Offensive Technologies ({WOOT} 18)},\nyear = {2018},\naddress = {Baltimore, MD},\nurl = {https://www.usenix.org/conference/woot18/presentation/pohl},\npublisher = {{USENIX} Association},\n}\n\nInstallation\n------------\n\n[](https://github.com/jopohl/urh?screenshot=true#installation)\n\nURH runs on Windows, Linux and macOS. See below for OS specific installation instructions.\n\n### Windows\n\n[](https://github.com/jopohl/urh?screenshot=true#windows)\n\nOn Windows, URH can be installed with its [Installer](https://github.com/jopohl/urh/releases). No further dependencies are required.\n\nIf you get an error about missing `api-ms-win-crt-runtime-l1-1-0.dll`, run Windows Update or directly install [KB2999226](https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows).\n\n### Linux\n\n[](https://github.com/jopohl/urh?screenshot=true#linux)\n\n#### Installation with pipx\n\n[](https://github.com/jopohl/urh?screenshot=true#installation-with-pipx)\n\nURH is available on [PyPi](https://pypi.org/project/urh/) so you can install it, for example, with [pipx](https://pypa.github.io/pipx/):\n\nThis is the recommended way to install URH on Linux because it comes with **all native extensions** precompiled.\n\nIn order to access your SDR as non-root user, install the according **udev rules**. You can find them [in the wiki](https://github.com/jopohl/urh/wiki/SDR-udev-rules).\n\n#### Install via Package Manager\n\n[](https://github.com/jopohl/urh?screenshot=true#install-via-package-manager)\n\nURH is included in the repositories of many linux distributions such as **Arch Linux**, **Gentoo**, **Fedora**, **openSUSE** or **NixOS**. There is also a package for **FreeBSD**. If available, simply use your package manager to install URH.\n\n**Note**: For native support, you must install the according `-dev` package(s) of your SDR(s) such as `hackrf-dev` **before** installing URH.\n\n#### Docker Images\n\n[](https://github.com/jopohl/urh?screenshot=true#docker-images)\n\nThe official URH docker image is available [here](https://hub.docker.com/r/jopohl/urh/). It has all native backends included and ready to operate.\n\n### macOS\n\n[](https://github.com/jopohl/urh?screenshot=true#macos)\n\n#### Using DMG\n\n[](https://github.com/jopohl/urh?screenshot=true#using-dmg)\n\nIt is recommended to use **at least macOS 13** when using the DMG available [here](https://github.com/jopohl/urh/releases).\n\n#### With brew\n\n[](https://github.com/jopohl/urh?screenshot=true#with-brew)\n\nURH is available as a [homebrew formula](https://formulae.brew.sh/formula/urh) so you can install it with\n\n### Running from source (OS-agnostic)\n\n[](https://github.com/jopohl/urh?screenshot=true#running-from-source-os-agnostic)\n\n#### Without installation\n\n[](https://github.com/jopohl/urh?screenshot=true#without-installation)\n\nTo execute the Universal Radio Hacker without installation, just run:\n\n```\ngit clone https://github.com/jopohl/urh/\ncd urh/src/urh\n./main.py\n```\n\nNote, before first usage the C++ extensions will be built.\n\n#### Installing from source\n\n[](https://github.com/jopohl/urh?screenshot=true#installing-from-source)\n\nTo install URH from source you need to have `python-setuptools` installed. You can get them with `python3 -m pip install setuptools`. Once the setuptools are installed execute:\n\n```\ngit clone https://github.com/jopohl/urh/\ncd urh\npython setup.py install\n```\n\nAnd start the application by typing `urh` in a terminal.\n\nArticles\n--------\n\n[](https://github.com/jopohl/urh?screenshot=true#articles)\n\n### Hacking stuff with URH\n\n[](https://github.com/jopohl/urh?screenshot=true#hacking-stuff-with-urh)\n\n*   [Hacking Burger Pagers](https://www.rtl-sdr.com/using-a-hackrf-to-reverse-engineer-and-control-restaurant-pagers/)\n*   [Reverse-engineer and Clone a Remote Control](https://www.rtl-sdr.com/video-tutorial-using-universal-radio-hacker-an-rtl-sdr-and-a-microcontroller-to-clone-433-mhz-remotes/)\n*   [Reverse-engineering Weather Station RF Signals](https://www.rtl-sdr.com/tag/universal-radio-hacker/)\n*   [Reverse-engineering Wireless Blinds](https://www.rtl-sdr.com/reverse-engineering-wireless-blinds-with-an-rtl-sdr-and-controlling-them-with-amazon-alexa/)\n*   [Attacking Logitech Wireless Presenters (German Article)](https://www.heise.de/security/meldung/Wireless-Presenter-von-Logitech-und-Inateck-anfaellig-fuer-Angriffe-ueber-Funk-4439795.html)\n*   [Attacking Wireless Keyboards](https://threatpost.com/fujitsu-wireless-keyboard-unpatched-flaws/149477/)\n*   [Reverse-engineering a 433MHz Remote-controlled Power Socket for use with Arduino](http://www.ignorantofthings.com/2018/11/reverse-engineering-433mhz-remote.html)\n\n### General presentations and tutorials on URH\n\n[](https://github.com/jopohl/urh?screenshot=true#general-presentations-and-tutorials-on-urh)\n\n*   [Hackaday Article](https://hackaday.com/2017/02/23/universal-radio-hacker/)\n*   [RTL-SDR.com Article](https://www.rtl-sdr.com/reverse-engineering-signals-universal-radio-hacker-software/)\n*   [Short Tutorial on URH with LimeSDR Mini](https://www.crowdsupply.com/lime-micro/limesdr-mini/updates/investigating-wireless-protocols-with-universal-radio-hacker)\n*   [Brute-forcing a RF Device: a Step-by-step Guide](https://pandwarf.com/news/brute-forcing-a-new-device-a-step-by-step-guide/)\n*   [Hacking wireless sockets like a NOOB](https://olof-astrand.medium.com/hacking-wireless-sockets-like-a-noob-b57d4b4812d5)\n\nExternal decodings\n------------------\n\n[](https://github.com/jopohl/urh?screenshot=true#external-decodings)\n\nSee [wiki](https://github.com/jopohl/urh/wiki/External-decodings) for a list of external decodings provided by our community! Thanks for that!\n\nScreenshots\n-----------\n\n[](https://github.com/jopohl/urh?screenshot=true#screenshots)\n\n### Get the data out of raw signals\n\n[](https://github.com/jopohl/urh?screenshot=true#get-the-data-out-of-raw-signals)\n\n[![Image 43: Interpretation phase](https://camo.githubusercontent.com/a135c200210d7c7445b9fc3cd07d31bc896a6a392a1ed596d1e95fc15a05331e/687474703a2f2f692e696d6775722e636f6d2f577931375a76332e706e67)](https://camo.githubusercontent.com/a135c200210d7c7445b9fc3cd07d31bc896a6a392a1ed596d1e95fc15a05331e/687474703a2f2f692e696d6775722e636f6d2f577931375a76332e706e67)\n\n### Keep an overview even on complex protocols\n\n[](https://github.com/jopohl/urh?screenshot=true#keep-an-overview-even-on-complex-protocols)\n\n[![Image 44: Analysis phase](https://camo.githubusercontent.com/7d9061753c1285b7e50a073cc95803cdba5d91b6cdc69fa7caf47f23beb87904/687474703a2f2f692e696d6775722e636f6d2f7562414c3370452e706e67)](https://camo.githubusercontent.com/7d9061753c1285b7e50a073cc95803cdba5d91b6cdc69fa7caf47f23beb87904/687474703a2f2f692e696d6775722e636f6d2f7562414c3370452e706e67)\n\n### Record and send signals\n\n[](https://github.com/jopohl/urh?screenshot=true#record-and-send-signals)\n\n[![Image 45: Record](https://camo.githubusercontent.com/cc825e4d698238b30357414a901bec2d5cbfb04de1dc7beaf60c5392a1d98828/687474703a2f2f692e696d6775722e636f6d2f426651706732332e706e67)](https://camo.githubusercontent.com/cc825e4d698238b30357414a901bec2d5cbfb04de1dc7beaf60c5392a1d98828/687474703a2f2f692e696d6775722e636f6d2f426651706732332e706e67)",
  "usage": {
    "tokens": 3561
  }
}
```
