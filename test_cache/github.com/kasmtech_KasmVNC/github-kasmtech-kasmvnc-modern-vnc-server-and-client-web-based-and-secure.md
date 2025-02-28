---
title: GitHub - kasmtech/KasmVNC: Modern VNC Server and client, web based and secure
description: Modern VNC Server and client, web based and secure - kasmtech/KasmVNC
url: https://github.com/kasmtech/KasmVNC
timestamp: 2025-01-20T15:32:03.115Z
domain: github.com
path: kasmtech_KasmVNC
---

# GitHub - kasmtech/KasmVNC: Modern VNC Server and client, web based and secure


Modern VNC Server and client, web based and secure - kasmtech/KasmVNC


## Content

KasmVNC - Linux Web Remote Desktop
----------------------------------

[](https://github.com/kasmtech/KasmVNC?screenshot=true#kasmvnc---linux-web-remote-desktop)

[![Image 17](https://camo.githubusercontent.com/6ee9266970dc528af88a597e78f08253114d4e947a29544f74dc4fc43eb3763f/68747470733a2f2f6b61736d2d7374617469632d636f6e74656e742e73332e616d617a6f6e6177732e636f6d2f6c6f676f5f6b61736d2e706e67)](https://kasmweb.com/)

KasmVNC provides remote web-based access to a Desktop or application. While VNC is in the name, KasmVNC differs from other VNC variants such as TigerVNC, RealVNC, and TurboVNC. KasmVNC has broken from the RFB specification which defines VNC, in order to support modern technologies and increase security. KasmVNC is accessed by users from any modern browser and does not support legacy VNC viewer applications. KasmVNC uses a modern YAML based configuration at the server and user level, allowing for ease of management.

[Kasm Technologies](https://www.kasmweb.com/) developed Kasm Workspaces, the Containerized Streaming Platform. Kasm has open-sourced the Workspace docker images, which include containerized [full desktops and apps](https://github.com/kasmtech/workspaces-images) and [base images](https://github.com/kasmtech/workspaces-core-images) intended for developers to create customized streaming containers. These containers can be used standalone or within the [Kasm Workspaces Platform](https://www.kasmweb.com/) which provides a full Enterprise feature set.

Documentation
-------------

[](https://github.com/kasmtech/KasmVNC?screenshot=true#documentation)

**Do not use the README from the master branch**, unless you are compiling KasmVNC yourself from the tip of master. Use the documentation for your specific release.

*   [KasmVNC 1.0.0 Documentation](https://www.kasmweb.com/kasmvnc/docs/1.0.0/index.html)

For beta releases prior to version 1.0.0, use the README in this github project on the tagged commit for that release.

Installation
------------

[](https://github.com/kasmtech/KasmVNC?screenshot=true#installation)

**You must disconnect and reconnect to the server after installation, for the group membership to apply.**

### Debian/Ubuntu/Kali

[](https://github.com/kasmtech/KasmVNC?screenshot=true#debianubuntukali)

# Please choose the package for your distro here (under Assets):
# https://github.com/kasmtech/KasmVNC/releases
wget <package\_url\>

sudo apt-get install ./kasmvncserver\_\*.deb

# Add your user to the ssl-cert group
sudo adduser $USER ssl-cert

### Oracle 8

[](https://github.com/kasmtech/KasmVNC?screenshot=true#oracle-8)

# Please choose the package for your distro here (under Assets):
# https://github.com/kasmtech/KasmVNC/releases
wget <package\_url\>

# Ensure KasmVNC dependencies are available
sudo dnf config-manager --set-enabled ol8\_codeready\_builder
sudo dnf install oracle-epel-release-el8

sudo dnf localinstall ./kasmvncserver\_\*.rpm

# Add your user to the kasmvnc-cert group
sudo usermod -a -G kasmvnc-cert $USER

### CentOS 7

[](https://github.com/kasmtech/KasmVNC?screenshot=true#centos-7)

# Please choose the package for your distro here (under Assets):
# https://github.com/kasmtech/KasmVNC/releases
wget <package\_url\>

# Ensure KasmVNC dependencies are available
sudo yum install epel-release

sudo yum install ./kasmvncserver\_\*.rpm

# Add your user to the kasmvnc-cert group
sudo usermod -a -G kasmvnc-cert $USER

Getting Started
---------------

[](https://github.com/kasmtech/KasmVNC?screenshot=true#getting-started)

The following examples provide basic usage of KasmVNC with the tools provided. For full documentation on all the utilities and the runtime environment, see our [KasmVNC Documentation](https://www.kasmweb.com/kasmvnc/docs/latest/index.html)

# Start a session and be guided to setup a user and select a default desktop environment
vncserver

# Start a session with the mate desktop environment
vncserver -select-de mate

# Add a new user with read/write permissions
vncpasswd -u my\_username -w -r

# Tail the logs
tail -f ~/.vnc/\*.log

# Get a list of current sessions with display IDs
vncserver -list

# Kill the VNC session with display ID :2
vncserver -kill :2

Configuration
-------------

[](https://github.com/kasmtech/KasmVNC?screenshot=true#configuration)

KasmVNC is configured via YAML based configurations. The server level configuration is at `/etc/kasmvnc/kasmvnc.yaml`. Edits to this file apply to all users. Individual users can override server global configurations by specifying them in their configuration file at `~/.vnc/kasmvnc.yaml`.

The following configuration shows all default settings. Many of the encoding settings can be overridden by the client, unless the `runtime_configuration.allow_client_to_override_kasm_server_settings` setting is set tot false. By default the client is allowed to modify encoding settings.

For a full description of each setting see the [configuration reference](https://www.kasmweb.com/kasmvnc/docs/latest/configuration.html).

desktop:
  resolution:
    width: 1024
    height: 768
  allow\_resize: true
  pixel\_depth: 24
  gpu:
    hw3d: false
    drinode: /dev/dri/renderD128

network:
  protocol: http
  interface: 0.0.0.0
  websocket\_port: auto
  use\_ipv4: true
  use\_ipv6: true
  udp:
    public\_ip: auto
    port: auto
    stun\_server: auto
  ssl:
    pem\_certificate: /etc/ssl/certs/ssl-cert-snakeoil.pem
    pem\_key: /etc/ssl/private/ssl-cert-snakeoil.key
    require\_ssl: true

user\_session:
  new\_session\_disconnects\_existing\_exclusive\_session: false
  concurrent\_connections\_prompt: false
  concurrent\_connections\_prompt\_timeout: 10
  idle\_timeout: never

keyboard:
  remap\_keys:
  ignore\_numlock: false
  raw\_keyboard: false

pointer:
  enabled: true

runtime\_configuration:
  allow\_client\_to\_override\_kasm\_server\_settings: true
  allow\_override\_standard\_vnc\_server\_settings: true
  allow\_override\_list:
    - pointer.enabled
    - data\_loss\_prevention.clipboard.server\_to\_client.enabled
    - data\_loss\_prevention.clipboard.client\_to\_server.enabled
    - data\_loss\_prevention.clipboard.server\_to\_client.primary\_clipboard\_enabled

logging:
  log\_writer\_name: all
  log\_dest: logfile
  level: 30

security:
  brute\_force\_protection:
    blacklist\_threshold: 5
    blacklist\_timeout: 10

data\_loss\_prevention:
  visible\_region:
    # top: 10
    # left: 10
    # right: 40
    # bottom: 40
    concealed\_region:
      allow\_click\_down: false
      allow\_click\_release: false
  clipboard:
    delay\_between\_operations: none
    allow\_mimetypes:
      - chromium/x-web-custom-data
      - text/html
      - image/png
    server\_to\_client:
      enabled: true
      size: unlimited
      primary\_clipboard\_enabled: false
    client\_to\_server:
      enabled: true
      size: unlimited
  keyboard:
    enabled: true
    rate\_limit: unlimited
  logging:
    level: off

encoding:
  max\_frame\_rate: 60
  full\_frame\_updates: none
  rect\_encoding\_mode:
    min\_quality: 7
    max\_quality: 8
    consider\_lossless\_quality: 10
    rectangle\_compress\_threads: auto

  video\_encoding\_mode:
    jpeg\_quality: \-1
    webp\_quality: \-1
    max\_resolution:
      width: 1920
      height: 1080
    enter\_video\_encoding\_mode:
      time\_threshold: 5
      area\_threshold: 45%
    exit\_video\_encoding\_mode:
      time\_threshold: 3
    logging:
      level: off
    scaling\_algorithm: progressive\_bilinear

  compare\_framebuffer: auto
  zrle\_zlib\_level: auto
  hextile\_improved\_compression: true

server:
  http:
    headers:
      - Cross-Origin-Embedder-Policy=require-corp
      - Cross-Origin-Opener-Policy=same-origin
    httpd\_directory: /usr/share/kasmvnc/www
  advanced:
    x\_font\_path: auto
    kasm\_password\_file: ${HOME}/.kasmpasswd
    x\_authority\_file: auto
  auto\_shutdown:
    no\_user\_session\_timeout: never
    active\_user\_session\_timeout: never
    inactive\_user\_session\_timeout: never

command\_line:
  prompt: true

New Features!
-------------

[](https://github.com/kasmtech/KasmVNC?screenshot=true#new-features)

*   Faster jpeg compression (via statically linked libjpeg-turbo)
*   Webp image compression for better bandwidth usage
*   Automatic mixing of webp and jpeg based on CPU availability on server
*   Multi-threaded image encoding for smoother frame rate for servers with more cores
*   WebRTC UDP Transit
*   Lossless QOI Image format for Local LAN
*   [Full screen video detection](https://github.com/kasmtech/KasmVNC/wiki/Video-Rendering-Options#video-mode), goes into configurable video mode for better full screen videoo playback performance.
*   [Dynamic jpeg/webp image coompression](https://github.com/kasmtech/KasmVNC/wiki/Video-Rendering-Options#dynamic-image-quality) quality settings based on screen change rates
*   Seemless clipboard support (on Chromium based browsers)
*   Binary clipboard support for text, images, and formatted text (on Chromium based browsers)
*   Allow client to set/change most configuration settings
*   [Data Loss Prevention features](https://github.com/kasmtech/KasmVNC/wiki/Data-Loss-Prevention)
    *   Key stroke logging
    *   Clipboard logging
    *   Max clipboard transfer size up and down
    *   Min time between clipboard operations required
    *   Keyboard input rate limit
    *   Screen region selection
*   Deb packages for Debian, Ubuntu, and Kali Linux included in release.
*   RPM packages for CentOS, Oracle, OpenSUSE, Fedora. RPM packages are currently not updatable and not released, though you can build and install them. See build documentation.
*   Web [API](https://github.com/kasmtech/KasmVNC/wiki/API) added for remotely controlling and getting information from KasmVNC
*   Multi-User support with permissions that can be changed via the API
*   Web UI uses a webpack for faster load times.
*   Network and CPU bottleneck statistics
*   Relative cursor support (game pointer mode)
*   Cursor lock
*   IME support for languages with extended characters
*   Better mobile support
*   DRI3 GPU acceleration with open source drivers (AMDGPU,Intel,ATI,ARM)

Future Goals:

*   H264 encoding

### Compiling From Source

[](https://github.com/kasmtech/KasmVNC?screenshot=true#compiling-from-source)

See the [builder/README.md](https://github.com/kasmtech/KasmVNC/blob/master/builder/README.md). We containerize our build systems to ensure highly repeatable builds.

### License and Acknowledgements

[](https://github.com/kasmtech/KasmVNC?screenshot=true#license-and-acknowledgements)

See the [LICENSE.TXT](https://github.com/kasmtech/KasmVNC/blob/master/LICENSE.TXT) and [ACKNOWLEDGEMENTS.md](https://github.com/kasmtech/KasmVNC/blob/master/ACKNOWLEDGEMENTS.md)

## Metadata

```json
{
  "title": "GitHub - kasmtech/KasmVNC: Modern VNC Server and client, web based and secure",
  "description": "Modern VNC Server and client, web based and secure - kasmtech/KasmVNC",
  "url": "https://github.com/kasmtech/KasmVNC?screenshot=true",
  "content": "KasmVNC - Linux Web Remote Desktop\n----------------------------------\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#kasmvnc---linux-web-remote-desktop)\n\n[![Image 17](https://camo.githubusercontent.com/6ee9266970dc528af88a597e78f08253114d4e947a29544f74dc4fc43eb3763f/68747470733a2f2f6b61736d2d7374617469632d636f6e74656e742e73332e616d617a6f6e6177732e636f6d2f6c6f676f5f6b61736d2e706e67)](https://kasmweb.com/)\n\nKasmVNC provides remote web-based access to a Desktop or application. While VNC is in the name, KasmVNC differs from other VNC variants such as TigerVNC, RealVNC, and TurboVNC. KasmVNC has broken from the RFB specification which defines VNC, in order to support modern technologies and increase security. KasmVNC is accessed by users from any modern browser and does not support legacy VNC viewer applications. KasmVNC uses a modern YAML based configuration at the server and user level, allowing for ease of management.\n\n[Kasm Technologies](https://www.kasmweb.com/) developed Kasm Workspaces, the Containerized Streaming Platform. Kasm has open-sourced the Workspace docker images, which include containerized [full desktops and apps](https://github.com/kasmtech/workspaces-images) and [base images](https://github.com/kasmtech/workspaces-core-images) intended for developers to create customized streaming containers. These containers can be used standalone or within the [Kasm Workspaces Platform](https://www.kasmweb.com/) which provides a full Enterprise feature set.\n\nDocumentation\n-------------\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#documentation)\n\n**Do not use the README from the master branch**, unless you are compiling KasmVNC yourself from the tip of master. Use the documentation for your specific release.\n\n*   [KasmVNC 1.0.0 Documentation](https://www.kasmweb.com/kasmvnc/docs/1.0.0/index.html)\n\nFor beta releases prior to version 1.0.0, use the README in this github project on the tagged commit for that release.\n\nInstallation\n------------\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#installation)\n\n**You must disconnect and reconnect to the server after installation, for the group membership to apply.**\n\n### Debian/Ubuntu/Kali\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#debianubuntukali)\n\n# Please choose the package for your distro here (under Assets):\n# https://github.com/kasmtech/KasmVNC/releases\nwget <package\\_url\\>\n\nsudo apt-get install ./kasmvncserver\\_\\*.deb\n\n# Add your user to the ssl-cert group\nsudo adduser $USER ssl-cert\n\n### Oracle 8\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#oracle-8)\n\n# Please choose the package for your distro here (under Assets):\n# https://github.com/kasmtech/KasmVNC/releases\nwget <package\\_url\\>\n\n# Ensure KasmVNC dependencies are available\nsudo dnf config-manager --set-enabled ol8\\_codeready\\_builder\nsudo dnf install oracle-epel-release-el8\n\nsudo dnf localinstall ./kasmvncserver\\_\\*.rpm\n\n# Add your user to the kasmvnc-cert group\nsudo usermod -a -G kasmvnc-cert $USER\n\n### CentOS 7\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#centos-7)\n\n# Please choose the package for your distro here (under Assets):\n# https://github.com/kasmtech/KasmVNC/releases\nwget <package\\_url\\>\n\n# Ensure KasmVNC dependencies are available\nsudo yum install epel-release\n\nsudo yum install ./kasmvncserver\\_\\*.rpm\n\n# Add your user to the kasmvnc-cert group\nsudo usermod -a -G kasmvnc-cert $USER\n\nGetting Started\n---------------\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#getting-started)\n\nThe following examples provide basic usage of KasmVNC with the tools provided. For full documentation on all the utilities and the runtime environment, see our [KasmVNC Documentation](https://www.kasmweb.com/kasmvnc/docs/latest/index.html)\n\n# Start a session and be guided to setup a user and select a default desktop environment\nvncserver\n\n# Start a session with the mate desktop environment\nvncserver -select-de mate\n\n# Add a new user with read/write permissions\nvncpasswd -u my\\_username -w -r\n\n# Tail the logs\ntail -f ~/.vnc/\\*.log\n\n# Get a list of current sessions with display IDs\nvncserver -list\n\n# Kill the VNC session with display ID :2\nvncserver -kill :2\n\nConfiguration\n-------------\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#configuration)\n\nKasmVNC is configured via YAML based configurations. The server level configuration is at `/etc/kasmvnc/kasmvnc.yaml`. Edits to this file apply to all users. Individual users can override server global configurations by specifying them in their configuration file at `~/.vnc/kasmvnc.yaml`.\n\nThe following configuration shows all default settings. Many of the encoding settings can be overridden by the client, unless the `runtime_configuration.allow_client_to_override_kasm_server_settings` setting is set tot false. By default the client is allowed to modify encoding settings.\n\nFor a full description of each setting see the [configuration reference](https://www.kasmweb.com/kasmvnc/docs/latest/configuration.html).\n\ndesktop:\n  resolution:\n    width: 1024\n    height: 768\n  allow\\_resize: true\n  pixel\\_depth: 24\n  gpu:\n    hw3d: false\n    drinode: /dev/dri/renderD128\n\nnetwork:\n  protocol: http\n  interface: 0.0.0.0\n  websocket\\_port: auto\n  use\\_ipv4: true\n  use\\_ipv6: true\n  udp:\n    public\\_ip: auto\n    port: auto\n    stun\\_server: auto\n  ssl:\n    pem\\_certificate: /etc/ssl/certs/ssl-cert-snakeoil.pem\n    pem\\_key: /etc/ssl/private/ssl-cert-snakeoil.key\n    require\\_ssl: true\n\nuser\\_session:\n  new\\_session\\_disconnects\\_existing\\_exclusive\\_session: false\n  concurrent\\_connections\\_prompt: false\n  concurrent\\_connections\\_prompt\\_timeout: 10\n  idle\\_timeout: never\n\nkeyboard:\n  remap\\_keys:\n  ignore\\_numlock: false\n  raw\\_keyboard: false\n\npointer:\n  enabled: true\n\nruntime\\_configuration:\n  allow\\_client\\_to\\_override\\_kasm\\_server\\_settings: true\n  allow\\_override\\_standard\\_vnc\\_server\\_settings: true\n  allow\\_override\\_list:\n    - pointer.enabled\n    - data\\_loss\\_prevention.clipboard.server\\_to\\_client.enabled\n    - data\\_loss\\_prevention.clipboard.client\\_to\\_server.enabled\n    - data\\_loss\\_prevention.clipboard.server\\_to\\_client.primary\\_clipboard\\_enabled\n\nlogging:\n  log\\_writer\\_name: all\n  log\\_dest: logfile\n  level: 30\n\nsecurity:\n  brute\\_force\\_protection:\n    blacklist\\_threshold: 5\n    blacklist\\_timeout: 10\n\ndata\\_loss\\_prevention:\n  visible\\_region:\n    # top: 10\n    # left: 10\n    # right: 40\n    # bottom: 40\n    concealed\\_region:\n      allow\\_click\\_down: false\n      allow\\_click\\_release: false\n  clipboard:\n    delay\\_between\\_operations: none\n    allow\\_mimetypes:\n      - chromium/x-web-custom-data\n      - text/html\n      - image/png\n    server\\_to\\_client:\n      enabled: true\n      size: unlimited\n      primary\\_clipboard\\_enabled: false\n    client\\_to\\_server:\n      enabled: true\n      size: unlimited\n  keyboard:\n    enabled: true\n    rate\\_limit: unlimited\n  logging:\n    level: off\n\nencoding:\n  max\\_frame\\_rate: 60\n  full\\_frame\\_updates: none\n  rect\\_encoding\\_mode:\n    min\\_quality: 7\n    max\\_quality: 8\n    consider\\_lossless\\_quality: 10\n    rectangle\\_compress\\_threads: auto\n\n  video\\_encoding\\_mode:\n    jpeg\\_quality: \\-1\n    webp\\_quality: \\-1\n    max\\_resolution:\n      width: 1920\n      height: 1080\n    enter\\_video\\_encoding\\_mode:\n      time\\_threshold: 5\n      area\\_threshold: 45%\n    exit\\_video\\_encoding\\_mode:\n      time\\_threshold: 3\n    logging:\n      level: off\n    scaling\\_algorithm: progressive\\_bilinear\n\n  compare\\_framebuffer: auto\n  zrle\\_zlib\\_level: auto\n  hextile\\_improved\\_compression: true\n\nserver:\n  http:\n    headers:\n      - Cross-Origin-Embedder-Policy=require-corp\n      - Cross-Origin-Opener-Policy=same-origin\n    httpd\\_directory: /usr/share/kasmvnc/www\n  advanced:\n    x\\_font\\_path: auto\n    kasm\\_password\\_file: ${HOME}/.kasmpasswd\n    x\\_authority\\_file: auto\n  auto\\_shutdown:\n    no\\_user\\_session\\_timeout: never\n    active\\_user\\_session\\_timeout: never\n    inactive\\_user\\_session\\_timeout: never\n\ncommand\\_line:\n  prompt: true\n\nNew Features!\n-------------\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#new-features)\n\n*   Faster jpeg compression (via statically linked libjpeg-turbo)\n*   Webp image compression for better bandwidth usage\n*   Automatic mixing of webp and jpeg based on CPU availability on server\n*   Multi-threaded image encoding for smoother frame rate for servers with more cores\n*   WebRTC UDP Transit\n*   Lossless QOI Image format for Local LAN\n*   [Full screen video detection](https://github.com/kasmtech/KasmVNC/wiki/Video-Rendering-Options#video-mode), goes into configurable video mode for better full screen videoo playback performance.\n*   [Dynamic jpeg/webp image coompression](https://github.com/kasmtech/KasmVNC/wiki/Video-Rendering-Options#dynamic-image-quality) quality settings based on screen change rates\n*   Seemless clipboard support (on Chromium based browsers)\n*   Binary clipboard support for text, images, and formatted text (on Chromium based browsers)\n*   Allow client to set/change most configuration settings\n*   [Data Loss Prevention features](https://github.com/kasmtech/KasmVNC/wiki/Data-Loss-Prevention)\n    *   Key stroke logging\n    *   Clipboard logging\n    *   Max clipboard transfer size up and down\n    *   Min time between clipboard operations required\n    *   Keyboard input rate limit\n    *   Screen region selection\n*   Deb packages for Debian, Ubuntu, and Kali Linux included in release.\n*   RPM packages for CentOS, Oracle, OpenSUSE, Fedora. RPM packages are currently not updatable and not released, though you can build and install them. See build documentation.\n*   Web [API](https://github.com/kasmtech/KasmVNC/wiki/API) added for remotely controlling and getting information from KasmVNC\n*   Multi-User support with permissions that can be changed via the API\n*   Web UI uses a webpack for faster load times.\n*   Network and CPU bottleneck statistics\n*   Relative cursor support (game pointer mode)\n*   Cursor lock\n*   IME support for languages with extended characters\n*   Better mobile support\n*   DRI3 GPU acceleration with open source drivers (AMDGPU,Intel,ATI,ARM)\n\nFuture Goals:\n\n*   H264 encoding\n\n### Compiling From Source\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#compiling-from-source)\n\nSee the [builder/README.md](https://github.com/kasmtech/KasmVNC/blob/master/builder/README.md). We containerize our build systems to ensure highly repeatable builds.\n\n### License and Acknowledgements\n\n[](https://github.com/kasmtech/KasmVNC?screenshot=true#license-and-acknowledgements)\n\nSee the [LICENSE.TXT](https://github.com/kasmtech/KasmVNC/blob/master/LICENSE.TXT) and [ACKNOWLEDGEMENTS.md](https://github.com/kasmtech/KasmVNC/blob/master/ACKNOWLEDGEMENTS.md)",
  "usage": {
    "tokens": 2828
  }
}
```
