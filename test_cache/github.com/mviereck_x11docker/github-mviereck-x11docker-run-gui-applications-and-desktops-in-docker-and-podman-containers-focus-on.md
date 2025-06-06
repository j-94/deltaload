---
title: GitHub - mviereck/x11docker: Run GUI applications and desktops in docker and podman containers. Focus on security.
description: Run GUI applications and desktops in docker and podman containers. Focus on security. - mviereck/x11docker
url: https://github.com/mviereck/x11docker
timestamp: 2025-01-20T15:30:15.261Z
domain: github.com
path: mviereck_x11docker
---

# GitHub - mviereck/x11docker: Run GUI applications and desktops in docker and podman containers. Focus on security.


Run GUI applications and desktops in docker and podman containers. Focus on security. - mviereck/x11docker


## Content

x11docker: [![Image 35: x11docker logo](https://github.com/mviereck/x11docker/raw/master/x11docker.png)](https://github.com/mviereck/x11docker/blob/master/x11docker.png) Run GUI applications in Docker or podman containers.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[](https://github.com/mviereck/x11docker?screenshot=true#x11docker--run-gui-applications-in-docker-or-podman-containers)

Avoid X security leaks and enhance container security
-----------------------------------------------------

[](https://github.com/mviereck/x11docker?screenshot=true#avoid-x-security-leaks-and-enhance-container-security)

[![Image 36: DOI](https://camo.githubusercontent.com/39bde7cc2bb7828d664e7fe5bb76cc15570df0b14afcdefb6fa702d10b7dfe29/687474703a2f2f6a6f73732e7468656f6a2e6f72672f7061706572732f31302e32313130352f6a6f73732e30313334392f7374617475732e737667)](https://doi.org/10.21105/joss.01349)

Table of contents
-----------------

[](https://github.com/mviereck/x11docker?screenshot=true#table-of-contents)

*   [Introduction](https://github.com/mviereck/x11docker?screenshot=true#introduction)
    *   [Docker Desktop or Docker Engine](https://github.com/mviereck/x11docker?screenshot=true#docker-desktop-or-docker-engine)
    *   [TL;DR](https://github.com/mviereck/x11docker?screenshot=true#tldr)
    *   [Features](https://github.com/mviereck/x11docker?screenshot=true#features)
    *   [Supported systems](https://github.com/mviereck/x11docker?screenshot=true#supported-systems)
*   [Terminal syntax](https://github.com/mviereck/x11docker?screenshot=true#terminal-syntax)
*   [Options](https://github.com/mviereck/x11docker?screenshot=true#options)
    *   [Choice of X servers and Wayland compositors](https://github.com/mviereck/x11docker?screenshot=true#choice-of-x-servers-and-wayland-compositors)
    *   [Desktop or seamless mode](https://github.com/mviereck/x11docker?screenshot=true#desktop-or-seamless-mode)
    *   [Internet access](https://github.com/mviereck/x11docker?screenshot=true#internet-access)
    *   [Shared folders and HOME in container](https://github.com/mviereck/x11docker?screenshot=true#shared-folders-volumes-and-home-in-container)
    *   [GPU hardware acceleration](https://github.com/mviereck/x11docker?screenshot=true#gpu-hardware-acceleration)
    *   [Clipboard](https://github.com/mviereck/x11docker?screenshot=true#clipboard)
    *   [Sound](https://github.com/mviereck/x11docker?screenshot=true#sound)
    *   [Webcam](https://github.com/mviereck/x11docker?screenshot=true#webcam)
    *   [Printer](https://github.com/mviereck/x11docker?screenshot=true#printer)
    *   [Language locales](https://github.com/mviereck/x11docker?screenshot=true#language-locales)
    *   [Wayland](https://github.com/mviereck/x11docker?screenshot=true#wayland)
    *   [Init system](https://github.com/mviereck/x11docker?screenshot=true#init-system)
    *   [DBus](https://github.com/mviereck/x11docker?screenshot=true#dbus)
    *   [Container runtime](https://github.com/mviereck/x11docker?screenshot=true#container-runtime)
    *   [Backends other than docker](https://github.com/mviereck/x11docker?screenshot=true#backends-other-than-docker)
    *   [Preconfiguration with --preset](https://github.com/mviereck/x11docker?screenshot=true#preconfiguration-with---preset)
        *   [Default preset for all x11docker sessions](https://github.com/mviereck/x11docker?screenshot=true#default-preset-for-all-x11docker-sessions)
*   [Security](https://github.com/mviereck/x11docker?screenshot=true#security)
    *   [Security weaknesses](https://github.com/mviereck/x11docker?screenshot=true#security-weaknesses)
    *   [Options degrading container isolation](https://github.com/mviereck/x11docker?screenshot=true#options-degrading-container-isolation)
    *   [Sandbox](https://github.com/mviereck/x11docker?screenshot=true#sandbox)
    *   [Security and feature check](https://github.com/mviereck/x11docker?screenshot=true#security-and-feature-check)
*   [Installation](https://github.com/mviereck/x11docker?screenshot=true#installation)
    *   [Installation from distribution repositories](https://github.com/mviereck/x11docker?screenshot=true#installation-from-distribution-repositories)
    *   [Manual installation](https://github.com/mviereck/x11docker?screenshot=true#manual-installation)
        *   [Installation options](https://github.com/mviereck/x11docker?screenshot=true#installation-options)
        *   [Installed files](https://github.com/mviereck/x11docker?screenshot=true#installed-files)
        *   [Shortest way for first installation](https://github.com/mviereck/x11docker?screenshot=true#shortest-way-for-first-installation)
        *   [Minimal installation](https://github.com/mviereck/x11docker?screenshot=true#minimal-installation)
        *   [Installation on MS Windows](https://github.com/mviereck/x11docker?screenshot=true#installation-on-ms-windows)
        *   [Deinstallation](https://github.com/mviereck/x11docker?screenshot=true#deinstallation)
*   [Dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies)
*   [Troubleshooting](https://github.com/mviereck/x11docker?screenshot=true#troubleshooting)
    *   [Core checks](https://github.com/mviereck/x11docker?screenshot=true#core-checks)
    *   [Privilege checks](https://github.com/mviereck/x11docker?screenshot=true#privilege-checks)
    *   [Other checks](https://github.com/mviereck/x11docker?screenshot=true#other-checks)
*   [Contact](https://github.com/mviereck/x11docker?screenshot=true#contact)
    *   [Issues](https://github.com/mviereck/x11docker?screenshot=true#issues)
    *   [Contributing](https://github.com/mviereck/x11docker?screenshot=true#contributing)
    *   [Support](https://github.com/mviereck/x11docker?screenshot=true#support)
*   [Donation](https://github.com/mviereck/x11docker?screenshot=true#donation)
*   [Examples](https://github.com/mviereck/x11docker?screenshot=true#examples)
    *   [Single applications](https://github.com/mviereck/x11docker?screenshot=true#single-applications)
    *   [Desktop environments](https://github.com/mviereck/x11docker?screenshot=true#desktop-environments)
    *   [Adjust images for your needs](https://github.com/mviereck/x11docker?screenshot=true#adjust-images-for-your-needs)
    *   [Screenshots](https://github.com/mviereck/x11docker?screenshot=true#screenshots)

Introduction
------------

[](https://github.com/mviereck/x11docker?screenshot=true#introduction)

x11docker allows to run graphical desktop applications (and entire desktops) in Linux containers.

*   [Container tools](https://github.com/mviereck/x11docker?screenshot=true#backend-docker-podman-or-nerdctl) like [Docker](https://en.wikipedia.org/wiki/Docker_(software)), [podman](http://docs.podman.io/en/latest/) and [nerdctl](https://github.com/containerd/nerdctl) allow to run applications in an isolated [container](https://en.wikipedia.org/wiki/Operating-system-level_virtualization) environment. Containers need much less resources than [virtual machines](https://en.wikipedia.org/wiki/Virtual_machine) for similar tasks.
*   Docker, podman and nerdctl do not provide a [display server](https://en.wikipedia.org/wiki/Display_server) that would allow to run applications with a [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface).
*   x11docker fills the gap. It runs an [X display server](https://en.wikipedia.org/wiki/X_Window_System) and provides it to containers. X servers can run from host or in a container of image [x11docker/xserver](https://github.com/mviereck/dockerfile-x11docker-xserver).
*   Additionally x11docker does some [security setup](https://github.com/mviereck/x11docker#security) to enhance container isolation and to avoid X security leaks. This allows a [sandbox](https://github.com/mviereck/x11docker?screenshot=true#sandbox) environment that fairly well protects the host system from possibly malicious or buggy software.

Software can be installed in a deployable image with a rudimentary Linux system inside. This can help to run or deploy software that is difficult to install on several systems due to dependency issues. It is possible to run outdated versions or latest development versions side by side. Files to work on can be shared between host and container.

[x11docker wiki](https://github.com/mviereck/x11docker/wiki) provides some how-to's for basic setups without x11docker.

### Docker Desktop or Docker Engine

[](https://github.com/mviereck/x11docker?screenshot=true#docker-desktop-or-docker-engine)

Since a while Docker distributes a version called "Docker Desktop" that runs Docker in a QEMU VM. x11docker is not designed to support this VM based version. Instead, use x11docker with the native ["Docker Engine Server version"](https://docs.docker.com/engine/install/#server) that uses your host kernel to run containers.

*   If you install Docker from your distribution's repository, you'll likely get this native version.
*   The supported native Docker Engine package name is mostly `docker.io` or `docker-ce`, in opposite to the non-supported VM based `docker-desktop` package.
*   If you prefer podman over Docker, you don't need to care about this difference.

### TL;DR

[](https://github.com/mviereck/x11docker?screenshot=true#tldr)

For a quick start:

*   [Install](https://github.com/mviereck/x11docker?screenshot=true#installation) x11docker with:
    
    curl -fsSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker | sudo bash -s -- --update
    
*   Install [dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies):
    *   Either pull image `x11docker/xserver` or install at least `nxagent` or `xpra` and `xephyr`.
*   [Run](https://github.com/mviereck/x11docker?screenshot=true#terminal-syntax) a GUI in container with:
    
    x11docker IMAGENAME \[COMMAND\]
    
*   Add [options](https://github.com/mviereck/x11docker?screenshot=true#options):
    *   `--desktop` for a desktop environment in image.
    *   `--gpu` for hardware acceleration.
*   [Examples](https://github.com/mviereck/x11docker?screenshot=true#examples):
    
    x11docker x11docker/xfce thunar
    x11docker --desktop x11docker/xfce
    x11docker --gpu x11docker/xfce glxgears
    

### Features

[](https://github.com/mviereck/x11docker?screenshot=true#features)

*   Focus on [security](https://github.com/mviereck/x11docker?screenshot=true#security):
    *   Avoids X security leaks by running [additional X servers](https://github.com/mviereck/x11docker?screenshot=true#choice-of-x-servers-and-wayland-compositors).
    *   Restricts container capabilities to bare minimum.
    *   Container user is same as host user to avoid root in container.
*   Low [dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies):
    *   No obliging dependencies on host beside X and one of `docker`, `podman` or `nerdctl`. Recommended: `nxagent` and `Xephyr`, alternatively image `x11docker/xserver`.
    *   No dependencies inside of images except for some optional features.
*   Several [optional features](https://github.com/mviereck/x11docker?screenshot=true#options) like [GPU](https://github.com/mviereck/x11docker?screenshot=true#gpu-hardware-acceleration), [sound](https://github.com/mviereck/x11docker?screenshot=true#sound), [webcam](https://github.com/mviereck/x11docker?screenshot=true#webcam) and [printer](https://github.com/mviereck/x11docker?screenshot=true#printer) support.
*   Remote access with [SSH](https://github.com/mviereck/x11docker/wiki/Remote-access-with-SSH), [VNC](https://github.com/mviereck/x11docker/wiki/VNC) or [HTML5](https://github.com/mviereck/x11docker/wiki/Container-applications-running-in-Browser-with-HTML5) possible.
*   Easy to use. [Examples](https://github.com/mviereck/x11docker?screenshot=true#examples):

### Supported systems

[](https://github.com/mviereck/x11docker?screenshot=true#supported-systems)

x11docker runs on Linux and (with some setup and limitations) on [MS Windows](https://github.com/mviereck/x11docker?screenshot=true#installation-on-ms-windows). x11docker does not run on macOS except in a Linux VM.

Terminal syntax
---------------

[](https://github.com/mviereck/x11docker?screenshot=true#terminal-syntax)

Just type `x11docker IMAGENAME [COMMAND]`.

*   Get an [overview of options](https://github.com/mviereck/x11docker/wiki/x11docker-options-overview) with `x11docker --help`.
    *   For desktop environments in image add option `-d, --desktop`.
    *   For internet access use option `-I, --network`.
    *   To run without X at all use option `-t, --tty`.
    *   Get an interactive TTY with option `-i, --interactive`.
    *   See generated container backend command (and further infos) with option `--debug`.
*   If startup fails, look at chapter [Troubleshooting](https://github.com/mviereck/x11docker?screenshot=true#troubleshooting).

General syntax:

```
Usage:
To run a container on a new X server:
  x11docker IMAGE
  x11docker [OPTIONS] IMAGE [COMMAND]
  x11docker [OPTIONS] -- IMAGE [COMMAND [ARG1 ARG2 ...]]
  x11docker [OPTIONS] -- CUSTOM_RUN_OPTIONS -- IMAGE [COMMAND [ARG1 ARG2 ...]]
To run a host application on a new X server:
  x11docker [OPTIONS] --backend=host COMMAND
  x11docker [OPTIONS] --backend=host -- COMMAND [ARG1 ARG2 ...]
  x11docker [OPTIONS] --backend=host -- -- COMMAND [ARG1 ARG2 ...] -- [ARG3]
To run only an empty new X server:
  x11docker [OPTIONS] --xonly
```

`CUSTOM_RUN_OPTIONS` are just added to the `docker|podman|nerdctl run` command without a serious check by x11docker.

Options
-------

[](https://github.com/mviereck/x11docker?screenshot=true#options)

Description of some commonly used feature [options](https://github.com/mviereck/x11docker/wiki/x11docker-options-overview).

*   Some of these options have dependencies on host and/or in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).
*   For often used option combinations you can make shortcuts with [option `--preset`](https://github.com/mviereck/x11docker?screenshot=true#option---preset).

### Choice of X servers and Wayland compositors

[](https://github.com/mviereck/x11docker?screenshot=true#choice-of-x-servers-and-wayland-compositors)

If no X server option is specified, x11docker automatically chooses one depending on installed [dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies) and on given or missing options `--desktop`, `--gpu` and `--wayland`. Most recommended are `nxagent` and `Xephyr`.

*   [Overview of all possible X server and Wayland options.](https://github.com/mviereck/x11docker/wiki/X-server-and-Wayland-Options)
    *   [Hints to use option `--xorg` within X.](https://github.com/mviereck/x11docker/wiki/Setup-for-option---xorg)
    *   Use option `-t, --tty` to run without X at all.

### Desktop or seamless mode

[](https://github.com/mviereck/x11docker?screenshot=true#desktop-or-seamless-mode)

x11docker assumes that you want to run a single application in seamless mode, i.e. a single window on your regular desktop. If you want to run a desktop environment in image, add option `--desktop`.

*   Seamless mode is supported with options `--nxagent` and `--xpra`. As a fallback insecure option `--hostdisplay` is possible.
*   Desktop mode with `--desktop` is supported with all X server options except `--hostdisplay`. If available, x11docker prefers `--xephyr` and `--nxagent`.
*   Special case: Single applications with a window manager (option `--wm`).
    *   If neither `nxagent` nor `xpra` are installed, but x11docker finds a desktop capable X server like `Xephyr`, it avoids insecure option `--hostdisplay` and runs Xephyr with a window manager.

### Internet access

[](https://github.com/mviereck/x11docker?screenshot=true#internet-access)

By default x11docker disables Network access for containers with `--network=none` because it targets best possible container isolation. To allow internet access set option `-I` or `--network`.

### Shared folders, volumes and HOME in container

[](https://github.com/mviereck/x11docker?screenshot=true#shared-folders-volumes-and-home-in-container)

Changes in a running container system will be lost, the created container will be discarded. For persistent data storage you can share host directories or volumes:

*   Option `-m, --home` creates a host directory in `~/.local/share/x11docker/IMAGENAME` that is shared with the container and mounted as its `HOME` directory. Files in container home and user configuration changes will persist. x11docker creates a softlink from `~/.local/share/x11docker` to `~/x11docker`.
    *   You can specify another host directory for container `HOME` with `--home=DIR`.
    *   You can specify a volume for container `HOME` with `--home=VOLUME`.
*   Option `--share PATH` mounts a host file or folder at the same location in container.
    *   You can also specify a volume with `--share VOLUME`.
    *   `--share PATH:ro` restricts to read-only access.
    *   Device files in `/dev` are supported, too.
*   Special cases for `$HOME`:
    *   `--home=$HOME` will use your host home as container home. Discouraged, use with care.
    *   `--share $HOME` will symlink your host home as a subfolder of container home.

Note that x11docker copies files from `/etc/skel` in container to `HOME` if `HOME` is empty. That allows to provide predefined user configurations in the image.

### GPU hardware acceleration

[](https://github.com/mviereck/x11docker?screenshot=true#gpu-hardware-acceleration)

Hardware acceleration for OpenGL is possible with option `-g, --gpu`.

*   This will work out of the box in most cases with open source drivers on host. Otherwise have a look at [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).
*   Closed source [NVIDIA drivers](https://github.com/mviereck/x11docker/wiki/NVIDIA-driver-support-for-docker-container) need some setup and support less [x11docker X server options](https://github.com/mviereck/x11docker/wiki/X-server-and-Wayland-Options#attributes-of-x-server-and-wayland-options) for driver version < v470.x and Xwayland < v22.1.2.

### Clipboard

[](https://github.com/mviereck/x11docker?screenshot=true#clipboard)

Clipboard sharing is possible with option `-c, --clipboard [=ARG]`.

*   Optional arguments `superv` and `altv` only provide host clipboard content to container if keys `[SUPER][v]` or `[ALT][v]` are pressed.
*   Optional argument `oneway` only transfers clipboard content from container to host.

### Sound

[](https://github.com/mviereck/x11docker?screenshot=true#sound)

Sound is possible with options `-p, --pulseaudio` and `--alsa`.

*   For pulseaudio sound with `--pulseaudio` you need `pulseaudio` on host and `pulseaudio` (at least the `pulseaudio` client libraries) in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).
*   For ALSA sound with `--alsa` you might need to specify a sound card with e.g. `--alsa=Generic`. Get a list of available sound cards with `aplay -l`.

### Webcam

[](https://github.com/mviereck/x11docker?screenshot=true#webcam)

Webcams on host can be shared with option `--webcam`.

*   If webcam application in image fails, install `--gpu` dependencies in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).
*   `guvcview` needs `--pulseaudio` or `--alsa`.
*   `cheese` and [`gnome-ring`](https://ring.cx/) need `--init=systemd`.

### Printer

[](https://github.com/mviereck/x11docker?screenshot=true#printer)

Printers on host can be provided to container with option `--printer`.

*   It needs `cups` on host, the default printer server for most linux distributions.
*   The container needs `cups` client libraries in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).

### Language locales

[](https://github.com/mviereck/x11docker?screenshot=true#language-locales)

x11docker provides option `--lang` for flexible language locale settings.

*   `--lang` without an argument sets `LANG` in container to same as on host. Same as `--lang=$LANG`
*   x11docker will check on container startup if the desired locale is already present in image and enable it.
*   If x11docker does not find the locale, it creates it on container startup. This needs some `locale` packages in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).
*   Examples: `--lang=de` for German, `--lang=zh_CN` for Chinese, `--lang=ru` for Russian, `--lang=$LANG` for your host locale.
*   For support of chinese, japanese and korean characters install a font like `fonts-arphic-uming` in image.
*   Keyboard input methods like `fcitx-pinyin` are possible with some container setup. Compare ticket [#269](https://github.com/mviereck/x11docker/issues/269#issuecomment-667124421).

### Wayland

[](https://github.com/mviereck/x11docker?screenshot=true#wayland)

To run [Wayland](https://wayland.freedesktop.org/) instead of an X server x11docker provides options `--wayland`, `--weston`, `--kwin` and `--hostwayland`. For further description loot at [wiki: Description of Wayland options](https://github.com/mviereck/x11docker/wiki/X-server-and-Wayland-Options#description-of-wayland-options).

*   Option `--wayland` automatically sets up a Wayland environment. It regards option `--desktop`.
*   Options `--weston` and `--kwin` run Wayland compositors `weston` or `kwin_wayland`.
*   Option `--hostwayland` can run applications seamless on host Wayland desktops like Gnome 3, KDE 5 and [Sway](https://github.com/swaywm/sway).
*   Example: `xfce4-terminal` on Wayland: `x11docker --wayland x11docker/xfce xfce4-terminal`

### Init system

[](https://github.com/mviereck/x11docker?screenshot=true#init-system)

x11docker supports several init systems as PID 1 in container with option `--init`. Init in container solves the [zombie reaping issue](https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/). As default x11docker uses `tini` in`/usr/bin/docker-init`. Also available are `systemd`, `SysVinit`, `runit`, `OpenRC` and `s6-overlay`. `elogind` is supported, too. Look at [wiki: Init systems in Docker](https://github.com/mviereck/x11docker/wiki/Init-systems).

### DBus

[](https://github.com/mviereck/x11docker?screenshot=true#dbus)

Some desktop environments and applications need a running DBus system daemon and/or DBus user session. DBus options need `dbus` in image.

*   use `--dbus` to run a DBus user session daemon.
*   A DBus system daemon will be started automatically with [init systems](https://github.com/mviereck/x11docker?screenshot=true#Init-system) `systemd`, `openrc`, `runit` and `sysvinit` (option `--init`).
    *   It is also possible to run a DBus system daemon with `--dbus=system` without advanced init systems. However, this causes trouble in some cases and is not recommended in general.
*   use `--hostdbus` to connect to host DBus user session.
*   use `--share /run/dbus/system_bus_socket` to share host DBus system socket.

### Container runtime

[](https://github.com/mviereck/x11docker?screenshot=true#container-runtime)

It is possible to run containers with different backends following the [OCI runtime specification](https://github.com/opencontainers/runtime-spec). Docker's default runtime is `runc`. You can specify another one with option `--runtime=RUNTIME`. Container runtimes known and supported by x11docker are:

*   `runc`: Docker default.
*   [`nvidia`](https://github.com/mviereck/x11docker/wiki/NVIDIA-driver-support-for-docker-container#nvidianvidia-docker-images): Specialized fork of `runc` to support `nvidia/nvidia-docker` images.
*   [`crun`](https://github.com/giuseppe/crun): Fast and lightweight alternative to `runc` with same functionality.
*   `oci`: Runtime reported in [#205](https://github.com/mviereck/x11docker/issues/205), no documentation found. Handled by x11docker like `runc`.
*   [`sysbox-runtime`](https://github.com/nestybox/sysbox): Based on runc, aims to enhance container isolation. Support is experimental yet. Needs Sybox\>\=0.5.0 and kernel version \>\=5.12.

Using different runtimes is well tested for rootful Docker, but not for other [backend setups](https://github.com/mviereck/x11docker?screenshot=true#backend-docker-podman-or-nerdctl).

Example: possible runtime configuration in `/etc/docker/daemon.json`:

{
  "default-runtime": "runc",
  "runtimes": {
    "crun": {
      "path": "/usr/local/bin/crun",
      "runtimeArgs": \[\]
    },
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": \[\]
    },
    "sysbox-runc": {
      "path": "/usr/bin/sysbox-runc"
    }
  }
}

### Backends other than docker

[](https://github.com/mviereck/x11docker?screenshot=true#backends-other-than-docker)

x11docker supports container tools [Docker](https://en.wikipedia.org/wiki/Docker_(software)), [podman](http://docs.podman.io/en/latest/) and [nerdctl](https://github.com/containerd/nerdctl) with option `--backend=BACKEND` in rootful and rootless mode. Supported `--backend` arguments: `docker` `podman` `nerdctl` `host`

Container backends:

*   By default x11docker tries to run `docker`.
    *   To change the default `--backend=docker` to another one like `--backend=podman`, create a [`default` file for `--preset`](https://github.com/mviereck/x11docker?screenshot=true#default-preset-for-all-x11docker-sessions).
*   Recommended for rootful container backend: `docker` or `podman`
*   Recommended for rootless container backend: `podman`
    *   Only `podman` allows option `--home` in rootless mode yet.
    *   Only `podman` provides useful file ownerships with option `--share` in rootless mode yet.
*   `--backend=nerdctl` is experimental yet. It supports rootful and rootless mode. `nerdctl` is in heavy development stage.

Other supported backends that are in fact no containers:

*   `--backend=host` runs a host application on a new X server. No containerization is involved.

### Preconfiguration with --preset

[](https://github.com/mviereck/x11docker?screenshot=true#preconfiguration-with---preset)

For often used option combinations you might want to use option `--preset FILENAME` to have a command shortcut. `FILENAME` is a file in `~/.config/x11docker/preset` or in `/etc/x11docker/preset` containing some x11docker options.

*   Example `multimedia`: Create a file `~/.config/x11docker/preset/multimedia`:
    
    ```
    --gpu
    --webcam
    --printer
    --pulseaudio
    --clipboard
    --share ~/Videos
    --share ~/Music
    ```
    
    Use it like: `x11docker --preset=multimedia jess/vlc`
*   Example deepin desktop: Instead of long command
    
    ```
    x11docker --desktop --init=systemd --gpu --pulseaudio --home -- --cap-add=IPC_LOCK -- x11docker/deepin
    ```
    
    you can create a file `~/.config/x11docker/preset/deepin` containing the desired options and even the image name:
    
    ```
    --desktop 
    --init=systemd
    --gpu
    --pulseaudio
    --home
    -- 
    --cap-add=IPC_LOCK
    -- 
    x11docker/deepin
    ```
    
    Run with: `x11docker --preset=deepin`

#### Default preset for all x11docker sessions

[](https://github.com/mviereck/x11docker?screenshot=true#default-preset-for-all-x11docker-sessions)

You can create a `default` preset file that is applied on all x11docker sessions. You can think of it as a configuration file for x11docker.

*   Example: To always use `podman` instead of docker, create a file with name `default` in `~/.config/x11docker/preset` or in `/etc/x11docker/preset` with content: This will cause x11docker to always use `podman` instead of `docker` unless specified otherwise in the x11docker command.

The same way you can specify other and more options as default, e.g. `--homebasedir=/my/containerhome/path`. Note that a local user `default` file will supersede a system wide `default` file.

Security
--------

[](https://github.com/mviereck/x11docker?screenshot=true#security)

Scope of x11docker is to run containerized GUI applications while preserving and improving container isolation. Core concept is:

*   Runs a second X server to avoid [X security leaks](http://tutorials.section6.net/tutorials/freebsd/security/basics-of-securing-x11.html).
    *   This in opposite to widespread solutions that share host X socket of display :0, thus breaking container isolation, allowing keylogging and remote host control. (However, x11docker provides this with fallback option `--hostdisplay`).
    *   Authentication is done with MIT-MAGIC-COOKIE, stored separate from file `~/.Xauthority`.
*   Creates container user similar to host user to [avoid root in container](http://blog.dscpl.com.au/2015/12/don-run-as-root-inside-of-docker.html).
    *   You can also specify another user with `--user=USERNAME` or a non-existing one with `--user=UID:GID`.
    *   Disables possible root password and deletes entries in `/etc/sudoers`.
        *   If you want root permissions in container, use option `--sudouser` that allows `su` and `sudo` with password `x11docker`.
    *   If you want to use `USER` specified in image instead, set option `--user=RETAIN`. x11docker won't change container's `/etc/passwd` or `/etc/sudoers` in that case. Option `--home` won't be available.
*   Reduces [container capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities) to bare minimum.
    *   Sets run option `--cap-drop=ALL` to drop all capabilities. Most applications don't need them.
    *   Sets run option [`--security-opt=no-new-privileges`](https://www.projectatomic.io/blog/2016/03/no-new-privs-docker/).
    *   These restrictions can be disabled with x11docker option `--cap-default` or reduced with `--sudouser`, `--newprivileges`.

That being said, the default docker capabilities and the seccomp/SELinux/apparmor profiles are set up well to protect the host system. Nonetheless, x11docker follows the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Containers should not have capabilities or privileges that they don't need for their job.

### Security weaknesses

[](https://github.com/mviereck/x11docker?screenshot=true#security-weaknesses)

*   Possible SELinux restrictions are degraded for x11docker containers with run option `--security-opt label=type:container_runtime_t` to allow access to new X unix socket. A more restrictive solution is desirable. Compare: [SELinux and Docker: allow access to X unix socket in /tmp/.X11-unix](https://unix.stackexchange.com/questions/386767/selinux-and-docker-allow-access-to-x-unix-socket-in-tmp-x11-unix)
*   A possible user namespace remapping setup is disabled to allow options `--home` and `--share` without file ownership issues.
    *   This is less an issue because x11docker already avoids root in container.
    *   Exception: User namespace remapping is not disabled for `--user=RETAIN`.
*   x11docker provides several different X server options. Each X server involved might have its individual vulnerabilities. x11docker only covers well-known X security leaks that result from X11 protocol design.
    *   An additional security layer for most supported X servers is set up if image [x11docker/xserver](https://github.com/mviereck/dockerfile-x11docker-xserver) is available. It will be used automatically in most cases if available. Enforce its usage with option `--xc=yes`.

### Options degrading container isolation

[](https://github.com/mviereck/x11docker?screenshot=true#options-degrading-container-isolation)

x11docker shows warning messages in terminal if chosen options degrade container isolation. Note that x11docker does not check custom `DOCKER_RUN_OPTIONS`.

_Most important:_

*   `--hostdisplay` shares host X socket of display :0 instead of running a second X server.
    *   Danger of abuse is reduced providing so-called untrusted cookies, but do not rely on this.
    *   If additionally using `--gpu` or `--clipboard`, option `--ipc=host` and trusted cookies are enabled and no protection against X security leaks is left.
    *   If you don't care about container isolation, `x11docker --hostdisplay --gpu` is an insecure but quite fast setup without any overhead.
*   `--gpu` allows access to GPU hardware. This can be abused to get window content from host ([palinopsia bug](https://hsmr.cc/palinopsia/)) and makes [GPU rootkits](https://github.com/LucaBongiorni/jellyfish) like [keyloggers](http://www.cs.columbia.edu/~mikepo/papers/gpukeylogger.eurosec13.pdf) possible.
*   `--pulseaudio` and `--alsa` allow catching audio output and microphone input from host.

_Rather special options reducing security, but not needed for regular use:_

*   `--sudouser` allows `su` and `sudo` with password `x11docker`for container user. If an application somehow breaks out of container, it can harm your host system. Allows many container capabilities that x11docker would drop otherwise.
*   `--cap-default` disables x11docker's container security hardening and falls back to default container capabilities as provided by the backends docker, podman or nerdctl. If an application somehow breaks out of container, it can harm your host system.
*   `--init=systemd|sysvinit|openrc|runit` allow some container capabilities that x11docker would drop otherwise. `--init=systemd` also shares access to `/sys/fs/cgroup`. Some processes will run as root in container. If a root process somehow breaks out of container, it can harm your host system. Allows many container capabilities that x11docker would drop otherwise.
*   `--hostdbus` allows communication over DBus with host applications.

### Sandbox

[](https://github.com/mviereck/x11docker?screenshot=true#sandbox)

Container isolation enhanced with x11docker allows to use containers as a [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) that fairly well protects the host system from possibly malicious or buggy software. Though, no sandbox solution in the wild can provide a perfect secure protection, and Docker even with enhanced security settings from x11docker is no exception.

Using x11docker as a sandbox is not intended to run obviously evil software. Rather use it as:

*   Compatibility environment to run software that is hard or impossible to install on host due to dependency issues.
*   Development environment to collect libraries, compiler and so on to keep the host clean.
*   Development environment to mitigate damage caused by unexpected/buggy behaviour.
*   Security layer for software that may be malicious in worst case. Examples: Internet browser with enabled `javascript`, or `wine` with MS Windows applications.

x11docker already restricts process capabilities. You can additionally restrict access to CPU and RAM with option `--limit`. As default `--limit` restricts to 50% of available CPUs and 50% of currently free RAM. Another amount can be specified with `--limit=FACTOR` with a `FACTOR` greater than zero and less than or equal one.

For more custom fine tuning have a look at [Docker documentation: Limit a container's resources](https://docs.docker.com/config/containers/resource_constraints).

**WARNING**: There is no restriction that can prevent the container from flooding the hard disk storing the container or in shared folders.

### Security and feature check

[](https://github.com/mviereck/x11docker?screenshot=true#security-and-feature-check)

To check container isolation and some feature options use image `x11docker/check` and try out with several options.

*   An insecure setup is `x11docker --hostdisplay --gpu x11docker/check`. It fairly well demonstrates common X security leaks.
*   Add options like `--pulseaudio --alsa --webcam --clipboard --printer` to check their functionality.

Installation
------------

[](https://github.com/mviereck/x11docker?screenshot=true#installation)

Note that x11docker is just a **bash script** without library dependencies. Basically it is just a wrapper for X servers and container backends docker, podman and nerdctl. To allow advanced usage of x11docker abilities have a look at chapter [Dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies).

### Installation from distribution repositories

[](https://github.com/mviereck/x11docker?screenshot=true#installation-from-distribution-repositories)

x11docker is available as a package in some distributions.

Stable releases:

[![Image 37: GitHub release (latest by date)](https://camo.githubusercontent.com/b4bb31de55970b4534d6fe20dc7014c6fe34fadd0a5d50e9fece78470b582c86/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6d7669657265636b2f783131646f636b65723f6c6162656c3d783131646f636b65722532306c617465737425323072656c65617365)](https://camo.githubusercontent.com/b4bb31de55970b4534d6fe20dc7014c6fe34fadd0a5d50e9fece78470b582c86/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6d7669657265636b2f783131646f636b65723f6c6162656c3d783131646f636b65722532306c617465737425323072656c65617365)

[![Image 38: Packaging status](https://camo.githubusercontent.com/ce117ecaf3f25119b45121ec616a05a059918053d22cd4373f2483c36a6e12f3/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f766572746963616c2d616c6c7265706f732f783131646f636b65722e737667)](https://repology.org/project/x11docker/versions)

Latest git master/beta version:

[![Image 39: AUR latest git](https://camo.githubusercontent.com/6582b96571ad9f74e73e3bd01e56ec3dbb6f241e33c1593acee84afe4bcf8e9d/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f76657273696f6e2d666f722d7265706f2f6175722f783131646f636b65722e7376673f616c6c6f775f69676e6f7265643d31)](https://repology.org/project/x11docker/versions)

Much thanks to the maintainers who decided to provide these packages! There are some hints for [packaging x11docker](https://github.com/mviereck/x11docker/wiki/Packaging-x11docker) in the wiki.

### Manual installation

[](https://github.com/mviereck/x11docker?screenshot=true#manual-installation)

#### Installation options

[](https://github.com/mviereck/x11docker?screenshot=true#installation-options)

As root you can install, update and remove x11docker in system directories to be available system-wide:

*   `x11docker --install` : install x11docker from current directory. (Useful to install from an extracted `zip` file or a cloned `git` repository.)
*   `x11docker --update` : download and install latest [release](https://github.com/mviereck/x11docker/releases) from github.
*   `x11docker --update-master` : download and install latest master version from github.
*   `x11docker --remove` : remove all files installed by x11docker.
    *   Note: This does not remove `~/.local/share/x11docker` where it stores persistent files of option `--home`.
*   `x11docker --remove-oldprefix` : Before version 7.6.0 x11docker installed itself into `/usr/bin`. Now it installs into `/usr/local/bin`. Use `--remove-oldprefix` to remove `/usr/bin` installations.

To see the difference between current and coming updated version, you can use optional argument `diff` for `--update` and `--update-master`. Example: `x11docker --update-master=diff` will show you the code changes from your current installation to latest master/beta version without installing it.

#### Installed files

[](https://github.com/mviereck/x11docker?screenshot=true#installed-files)

What the installation does (just for information):

*   Copies script `x11docker` to `/usr/local/bin`.
*   Installs icon `x11docker.png` below `/usr/share/icons` using `xdg-icon-resource`.
*   Copies documentation `README.md`, `CHANGELOG.md` and `LICENSE.txt` to `/usr/local/share/doc/x11docker`.
*   Stores `man` page for x11docker in `/usr/local/share/man/man1/x11docker.1.gz`.

#### Shortest way for first installation:

[](https://github.com/mviereck/x11docker?screenshot=true#shortest-way-for-first-installation)

*   For systems using `sudo`:
    
    curl -fsSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker | sudo bash -s -- --update
    
*   Directly as `root`:
    
    curl -fsSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker | bash -s -- --update
    

#### Minimal installation

[](https://github.com/mviereck/x11docker?screenshot=true#minimal-installation)

You can run x11docker from an arbitrary location with `bash x11docker` or `./x11docker`. For minimal system-wide installation make `x11docker` executable with `chmod +x x11docker` and move it to `/usr/local/bin` (or another location in `PATH`). Other files than script `x11docker` itself are not essential.

#### Installation on MS Windows

[](https://github.com/mviereck/x11docker?screenshot=true#installation-on-ms-windows)

x11docker can run natively on MS Windows electively in one of:

*   [WSL (Windows subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/about)
*   [Cygwin](https://www.cygwin.com/)
*   [MSYS2](https://www.msys2.org/)

Further information at [wiki: x11docker on MS Windows](https://github.com/mviereck/x11docker/wiki/x11docker-on-MS-Windows).

#### Deinstallation

[](https://github.com/mviereck/x11docker?screenshot=true#deinstallation)

You can remove x11docker with `x11docker --remove`. That will remove the [files listed above](https://github.com/mviereck/x11docker?screenshot=true#installation-options). It will also remove `~/.cache/x11docker` and stop all running x11docker containers. x11docker will **not** remove:

*   Files and folders for persistent data storage with option `--home`. These are:
    *   `~/.local/share/x11docker` where persistent data is stored.
    *   Softlink `~/x11docker` that points there.
*   Folders you might have created yourself for x11docker:
    *   `~/.local/share/x11docker`
    *   `~/.config/x11docker`

Dependencies
------------

[](https://github.com/mviereck/x11docker?screenshot=true#dependencies)

x11docker can run with standard system utilities without additional dependencies on host or in image.

*   As a core it only needs `bash` and one of [`docker`](https://www.docker.com/), [`podman`](http://docs.podman.io/en/latest/) or [`nerdctl`](https://github.com/containerd/nerdctl) to run containers on X.
*   x11docker also needs an X server. x11docker can automatically use image [`x11docker/xserver`](https://github.com/mviereck/dockerfile-x11docker-xserver) that provides most optional x11docker dependencies and several X servers and Wayland compositors so you won't need to install them on host.
    *   If you prefer to install dependencies on host:
        *   The recommended base commands are: `nxagent` `Xephyr` `weston` `Xwayland` `xdotool` `xauth` `xinit` `xclip` `xhost` `xrandr` `xdpyinfo`. Some of them are probably already installed.
        *   See [wiki: Dependencies - Recommended base](https://github.com/mviereck/x11docker/wiki/Dependencies#recommended-base) for a package list matching your distribution.

Dependencies in image:

*   Some feature options have additional dependencies on host and/or in image. This affects especially options `--gpu`, `--printer` and `--pulseaudio`.
*   Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).

Troubleshooting
---------------

[](https://github.com/mviereck/x11docker?screenshot=true#troubleshooting)

For troubleshooting run `x11docker` in a terminal. x11docker shows warnings if something is insecure, missing or going wrong. Also it shows notes if options don't work and fallbacks are used. It might give hints to fix some issues.

### Core checks

[](https://github.com/mviereck/x11docker?screenshot=true#core-checks)

**1.** Make sure your x11docker version is up to date with `x11docker --update` (latest release) or `x11docker --update-master` (latest beta).

**2.** Carefully read the regular x11docker messages. Often they already give a hint what to do.

*   Use option `-D, --debug` to see some internal messages.
*   Use option `-v, --verbose` to see full logfile output.
*   You can find the latest dispatched logfile at `~/.cache/x11docker/x11docker.log`.

**3.** Try another X server option.

*   Some applications fail with fallback option `--hostdisplay`. Add `--clipboard` to disable some security restrictions of `--hostdisplay`.
*   If that does not help, install [additional X servers](https://github.com/mviereck/x11docker/wiki/Dependencies#recommended-base). The most stable and reliable option is `--xephyr`.

### Privilege checks

[](https://github.com/mviereck/x11docker?screenshot=true#privilege-checks)

Some applications need more privileges or [capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities) than x11docker provides by default. One attempt is to allow several privileges until the setup works. Than reduce privileges to find out which are needed indeed. (Note the `--` in the following commands, do not miss them).

**1.** Adding privileges:

*   Try `x11docker --cap-default IMAGENAME`
*   Try `x11docker --cap-default --ipc=host --network=host IMAGENAME`
*   Try `x11docker --cap-default --ipc=host --network=host --share /run/udev/data:ro -- --cap-add ALL --security-opt seccomp=unconfined --security-opt apparmor=unconfined --privileged -- IMAGENAME`

**2.** Reducing privileges:

*   Drop options one by one in this order: `--privileged` `--security-opt apparmor=unconfined` `--security-opt seccomp=unconfined` `--cap-add ALL` `--share /run/udev/data:ro` `--network=host` `--ipc=host` `--cap-default`. Only leave options that are needed to keep the setup working.
*   Option `--cap-default` might already be enough. It allows default container capabilities as docker|podman|nerdctl would do on themself.
    *   You can just stop debugging and reducing here if you like to.
    *   You can try to reduce `--cap-default`. Partially remove additional options to find out which one(s) are needed:
        *   First try `x11docker --newprivileges -- IMAGENAME`
        *   Than try and reduce: `x11docker --newprivileges -- --cap-add=SETPCAP --cap-add=MKNOD --cap-add=AUDIT_WRITE --cap-add=CHOWN --cap-add=NET_RAW --cap-add=DAC_OVERRIDE --cap-add=FOWNER --cap-add=FSETID --cap-add=KILL --cap-add=SETGID --cap-add=SETUID --cap-add=NET_BIND_SERVICE --cap-add=SYS_CHROOT --cap-add=SETFCAP -- IMAGENAME`
*   `--cap-add ALL` should not be considered to be a solution.
    *   Drop capabilities from following command to find the one(s) you need: `x11docker --cap-default -- --cap-add=SYS_MODULE --cap-add=SYS_RAWIO --cap-add=SYS_PACCT --cap-add=SYS_ADMIN --cap-add=SYS_NICE --cap-add=SYS_RESOURCE --cap-add=SYS_TIME --cap-add=SYS_TTY_CONFIG --cap-add=AUDIT_CONTROL --cap-add=MAC_OVERRIDE --cap-add=MAC_ADMIN --cap-add=NET_ADMIN --cap-add=SYSLOG --cap-add=DAC_READ_SEARCH --cap-add=LINUX_IMMUTABLE --cap-add=NET_BROADCAST --cap-add=IPC_LOCK --cap-add=IPC_OWNER --cap-add=SYS_PTRACE --cap-add=SYS_BOOT --cap-add=LEASE --cap-add=WAKE_ALARM --cap-add=BLOCK_SUSPEND --cap-add=AUDIT_READ -- IMAGENAME`
    *   Many of these capabilities are rather dangerous and should not be allowed for a container. Especially to mention is `SYS_ADMIN`.
*   Option `--privileged` should not be considered to be a solution. Basically it allows arbitrary access to the host for container applications.
    *   Likely you need to share a device file in `/dev`, e.g. something like `--share /dev/vboxdrv`.
*   `--ipc=host` and `--network=host` severely reduce container isolation. Better solutions are desirable.

**3.** Open a ticket to ask for possibilities how to optimize the privilege setup.

### Other checks

[](https://github.com/mviereck/x11docker?screenshot=true#other-checks)

**1.** Container user: By default x11docker sets up an unprivileged container user similar to your host user.

*   The image may have a `USER` specification and be designed for this user.
    *   Check for a `USER` specification in image with `docker inspect --format '{{.Config.User}}' IMAGENAME`
    *   You can enable this predefined user with `--user=RETAIN`
*   The container might need a root user. Try with `--user=root`, maybe add `--cap-default`.

**2.** Init and DBus

*   A few applications need a [DBus](https://github.com/mviereck/x11docker?screenshot=true#dbus) user daemon. Install `dbus` in image and try option `--dbus`.
*   A few applications need systemd and/or a running [DBus](https://github.com/mviereck/x11docker?screenshot=true#dbus) system daemon. Install `systemd` in image and try option `--init=systemd`.

**3.** Architecture check of host OS and image

*   The image may not be built for the architecture of your host OS. (ie. Image is built for amd64 but your OS runs on arm, e.g. on a RaspBerry PI). With a mismatch the container will quit unexpectedly & x11docker may emit the error `dockerrc(): Did not receive PID of PID1 in container.`
    *   You can check the image architecture with `docker inspect --format {{.Architecture}} IMAGENAME`.
    *   You can check the host architecture with `uname -m`.
    *   For further information and multi-arch setups look at [wiki: Multi-arch setups with QEMU](https://github.com/mviereck/x11docker/wiki/Multiarch-setups-with-QEMU).

Contact
-------

[](https://github.com/mviereck/x11docker?screenshot=true#contact)

Feel free to open a [ticket](https://github.com/mviereck/x11docker/issues) if you have a question or encounter an issue.

### Issues

[](https://github.com/mviereck/x11docker?screenshot=true#issues)

If reporting an [issue](https://github.com/mviereck/x11docker/issues):

*   Have a look at chapter [Troubleshooting](https://github.com/mviereck/x11docker?screenshot=true#troubleshooting).
*   Most times it makes sense to store the `--verbose` output (or `~/.cache/x11docker/x11docker.log`) at [pastebin.com](https://pastebin.com/).
    *   Personal information in the logfile is mainly the user name (also in paths) and some hardware and system information.

### Contributing

[](https://github.com/mviereck/x11docker?screenshot=true#contributing)

If you want to contribute to x11docker, please open a [ticket](https://github.com/mviereck/x11docker/issues) before creating a pull request. Often it is possible to accomplish desired tasks with already available options. Note that x11docker is considered to be stable and changes other than bug fixes are less likely to be merged. In general new features are not intended.

### Support

[](https://github.com/mviereck/x11docker?screenshot=true#support)

Please open a [ticket](https://github.com/mviereck/x11docker/issues) if you need support. Please note that `x11docker` is a non-commercial project maintained in free time. I'll help where I can, but there is no organisation behind `x11docker` that can provide large scale support.

Donation
--------

[](https://github.com/mviereck/x11docker?screenshot=true#donation)

If you like to make a donation: Thank you! :) Please have a look at [my sponsor site](https://github.com/sponsors/mviereck).

Instead of sponsoring me, you can as well spend some money to [Galsan Tschinag](http://galsan-tschinag.de/portrait/) in Mongolia ([Wikipedia](https://en.wikipedia.org/wiki/Galsan_Tschinag)). One of his great projects is the afforestation of Mongolia. A donation account in Germany is provided by [Förderverein Mongolei e.V.](http://foerderverein-mongolei.de/spenden/).

```
Förderverein Mongolei e.V.
IBAN DE7261290120 0394 3660 00
BIC GENODES1NUE
Volksbank Kirchheim-Nürtingen
```

I personally know some of the people behind this. I assure that they are trustworthy and have a great heart and soul and do a good thing.

Examples
--------

[](https://github.com/mviereck/x11docker?screenshot=true#examples)

[Some x11docker image examples with desktop environments can be found on docker hub.](https://hub.docker.com/u/x11docker/) A special one to check features and container isolation is `x11docker/check`.

Docker does not provide automated builds for free anymore, so the images are becoming outdated. Instead of pulling them, rather build them locally with x11docker option `--build`.

Some x11docker Dockerfiles are provided at [https://github.com/mviereck?tab=repositories](https://github.com/mviereck?tab=repositories); look for repositories beginning with `dockerfile-x11docker`. You can build locally from these Dockerfiles with x11docker option `--build`. Example:

```
x11docker --build x11docker/fvwm
```

### Single applications

[](https://github.com/mviereck/x11docker?screenshot=true#single-applications)

| Application | x11docker command |
| --- | --- |
| Xfce4 Terminal | `x11docker x11docker/xfce xfce4-terminal` |
| GLXgears with hardware acceleration | `x11docker --gpu x11docker/xfce glxgears` |
| [Kodi media center](https://kodi.tv/) with hardware  
acceleration, Pulseaudio sound  
and shared `Videos` folder.  
For setup look at [ehough/docker-kodi](https://github.com/ehough/docker-kodi). | `x11docker --gpu --pulseaudio --share ~/Videos erichough/kodi`. |
| [XaoS](https://github.com/patrick-nw/xaos) fractal generator | `x11docker patricknw/xaos` |
| [Telegram messenger](https://telegram.org/) with persistent  
`HOME` for configuration storage | `x11docker --home xorilog/telegram` |
| Firefox with shared `Download` folder  
and internet access. | `x11docker -I --share $HOME/Downloads -- --tmpfs /dev/shm -- jess/firefox` |
| [Tor browser](https://www.torproject.org/projects/torbrowser.html) | `x11docker -I jess/tor-browser` |
| Chromium browser with restricted resource usage | `x11docker -I --limit -- jess/chromium --no-sandbox` |
| VLC media player with shared `Videos`  
folder and Pulseaudio sound | `x11docker --pulseaudio --share=$HOME/Videos jess/vlc` |
| [GNU Octave Scientific Programming Language](https://www.gnu.org/software/octave/) built for arm & arm64 | `x11docker aptman/dbhi:bionic-octave octave` |

### Desktop environments

[](https://github.com/mviereck/x11docker?screenshot=true#desktop-environments)

| Desktop environment  
(most based on Debian) | x11docker command |
| --- | --- |
| [Cinnamon](https://github.com/mviereck/dockerfile-x11docker-cinnamon) | `x11docker --desktop --gpu --init=systemd --cap-default x11docker/cinnamon` |
| [deepin](https://github.com/mviereck/dockerfile-x11docker-deepin) ([website](https://www.deepin.org/en/dde/)) (3D desktop from China) | `x11docker --desktop --gpu --init=systemd -- --cap-add=IPC_LOCK -- x11docker/deepin` |
| [Enlightenment](https://github.com/mviereck/dockerfile-x11docker-enlightenment) (based on [Void Linux](https://www.voidlinux.org/)) | `x11docker --desktop --gpu --runit x11docker/enlightenment` |
| [Fluxbox](https://github.com/mviereck/dockerfile-x11docker-fluxbox) (based on Debian, 87 MB) | `x11docker --desktop x11docker/fluxbox` |
| [FVWM](https://github.com/mviereck/dockerfile-x11docker-fvwm) (based on [Alpine](https://alpinelinux.org/), 22.5 MB) | `x11docker --desktop x11docker/fvwm` |
| [Gnome 3](https://github.com/mviereck/dockerfile-x11docker-gnome) | `x11docker --desktop --gpu --init=systemd x11docker/gnome` |
| [KDE Plasma](https://github.com/mviereck/dockerfile-x11docker-kde-plasma) on X | `x11docker --desktop --gpu --init=systemd x11docker/kde-plasma` |
| [KDE Plasma](https://github.com/mviereck/dockerfile-x11docker-kde-plasma) on Wayland | `x11docker --kwin --wayland x11docker/kde-plasma plasmashell` |
| [KDE Plasma](https://github.com/mviereck/dockerfile-x11docker-kde-plasma) as nested Wayland compositor | `x11docker --gpu --init=systemd -- --cap-add SYS_RESOURCE -- x11docker/kde-plasma startplasma-wayland` |
| [Lumina](https://github.com/mviereck/dockerfile-x11docker-lumina) ([website](https://lumina-desktop.org/)) (based on [Void Linux](https://www.voidlinux.org/)) | `x11docker --desktop x11docker/lumina` |
| [LiriOS](https://liri.io/) (based on Fedora) | `x11docker --desktop --gpu lirios/unstable` |
| [LXDE](https://github.com/mviereck/dockerfile-x11docker-lxde) | `x11docker --desktop x11docker/lxde` |
| [LXDE with wine and PlayOnLinux](https://github.com/mviereck/dockerfile-x11docker-lxde-wine) and  
a persistent `HOME` folder to preserve  
installed Windows applications,  
and with Pulseaudio sound. | `x11docker --desktop --home --pulseaudio x11docker/lxde-wine` |
| [LXQt](https://github.com/mviereck/dockerfile-x11docker-lxqt) | `x11docker --desktop x11docker/lxqt` |
| [Mate](https://github.com/mviereck/dockerfile-x11docker-mate) | `x11docker --desktop x11docker/mate` |
| [Trinity](https://github.com/mviereck/dockerfile-x11docker-trinity) ([website](https://www.trinitydesktop.org/)) (successor of KDE 3) | `x11docker --desktop x11docker/trinity` |
| [Xfce](https://github.com/mviereck/dockerfile-x11docker-xfce) | `x11docker --desktop x11docker/xfce` |

### Adjust images for your needs

[](https://github.com/mviereck/x11docker?screenshot=true#adjust-images-for-your-needs)

For persistent changes of image system adjust Dockerfile and rebuild. To add custom applications to x11docker example images you can create a new Dockerfile based on them. Example:

# xfce desktop with VLC media player
FROM x11docker/xfce
RUN apt-get update && apt-get install -y vlc

### Screenshots

[](https://github.com/mviereck/x11docker?screenshot=true#screenshots)

More screenshots are stored in [screenshot branch](https://github.com/mviereck/x11docker/tree/screenshots)

`x11docker --desktop x11docker/lxqt` [![Image 40: screenshot](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-lxqt.png)](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-lxqt.png)

`x11docker --desktop x11docker/lxde-wine` [![Image 41: screenshot](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-lxde-wine.png)](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-lxde-wine.png)

`x11docker --desktop --gpu --init=systemd -- --cap-add=IPC_LOCK --security-opt seccomp=unconfined -- x11docker/deepin` [![Image 42: screenshot](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-deepin.png)](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-deepin.png)

## Metadata

```json
{
  "title": "GitHub - mviereck/x11docker: Run GUI applications and desktops in docker and podman containers. Focus on security.",
  "description": "Run GUI applications and desktops in docker and podman containers. Focus on security. - mviereck/x11docker",
  "url": "https://github.com/mviereck/x11docker?screenshot=true",
  "content": "x11docker: [![Image 35: x11docker logo](https://github.com/mviereck/x11docker/raw/master/x11docker.png)](https://github.com/mviereck/x11docker/blob/master/x11docker.png) Run GUI applications in Docker or podman containers.\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#x11docker--run-gui-applications-in-docker-or-podman-containers)\n\nAvoid X security leaks and enhance container security\n-----------------------------------------------------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#avoid-x-security-leaks-and-enhance-container-security)\n\n[![Image 36: DOI](https://camo.githubusercontent.com/39bde7cc2bb7828d664e7fe5bb76cc15570df0b14afcdefb6fa702d10b7dfe29/687474703a2f2f6a6f73732e7468656f6a2e6f72672f7061706572732f31302e32313130352f6a6f73732e30313334392f7374617475732e737667)](https://doi.org/10.21105/joss.01349)\n\nTable of contents\n-----------------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#table-of-contents)\n\n*   [Introduction](https://github.com/mviereck/x11docker?screenshot=true#introduction)\n    *   [Docker Desktop or Docker Engine](https://github.com/mviereck/x11docker?screenshot=true#docker-desktop-or-docker-engine)\n    *   [TL;DR](https://github.com/mviereck/x11docker?screenshot=true#tldr)\n    *   [Features](https://github.com/mviereck/x11docker?screenshot=true#features)\n    *   [Supported systems](https://github.com/mviereck/x11docker?screenshot=true#supported-systems)\n*   [Terminal syntax](https://github.com/mviereck/x11docker?screenshot=true#terminal-syntax)\n*   [Options](https://github.com/mviereck/x11docker?screenshot=true#options)\n    *   [Choice of X servers and Wayland compositors](https://github.com/mviereck/x11docker?screenshot=true#choice-of-x-servers-and-wayland-compositors)\n    *   [Desktop or seamless mode](https://github.com/mviereck/x11docker?screenshot=true#desktop-or-seamless-mode)\n    *   [Internet access](https://github.com/mviereck/x11docker?screenshot=true#internet-access)\n    *   [Shared folders and HOME in container](https://github.com/mviereck/x11docker?screenshot=true#shared-folders-volumes-and-home-in-container)\n    *   [GPU hardware acceleration](https://github.com/mviereck/x11docker?screenshot=true#gpu-hardware-acceleration)\n    *   [Clipboard](https://github.com/mviereck/x11docker?screenshot=true#clipboard)\n    *   [Sound](https://github.com/mviereck/x11docker?screenshot=true#sound)\n    *   [Webcam](https://github.com/mviereck/x11docker?screenshot=true#webcam)\n    *   [Printer](https://github.com/mviereck/x11docker?screenshot=true#printer)\n    *   [Language locales](https://github.com/mviereck/x11docker?screenshot=true#language-locales)\n    *   [Wayland](https://github.com/mviereck/x11docker?screenshot=true#wayland)\n    *   [Init system](https://github.com/mviereck/x11docker?screenshot=true#init-system)\n    *   [DBus](https://github.com/mviereck/x11docker?screenshot=true#dbus)\n    *   [Container runtime](https://github.com/mviereck/x11docker?screenshot=true#container-runtime)\n    *   [Backends other than docker](https://github.com/mviereck/x11docker?screenshot=true#backends-other-than-docker)\n    *   [Preconfiguration with --preset](https://github.com/mviereck/x11docker?screenshot=true#preconfiguration-with---preset)\n        *   [Default preset for all x11docker sessions](https://github.com/mviereck/x11docker?screenshot=true#default-preset-for-all-x11docker-sessions)\n*   [Security](https://github.com/mviereck/x11docker?screenshot=true#security)\n    *   [Security weaknesses](https://github.com/mviereck/x11docker?screenshot=true#security-weaknesses)\n    *   [Options degrading container isolation](https://github.com/mviereck/x11docker?screenshot=true#options-degrading-container-isolation)\n    *   [Sandbox](https://github.com/mviereck/x11docker?screenshot=true#sandbox)\n    *   [Security and feature check](https://github.com/mviereck/x11docker?screenshot=true#security-and-feature-check)\n*   [Installation](https://github.com/mviereck/x11docker?screenshot=true#installation)\n    *   [Installation from distribution repositories](https://github.com/mviereck/x11docker?screenshot=true#installation-from-distribution-repositories)\n    *   [Manual installation](https://github.com/mviereck/x11docker?screenshot=true#manual-installation)\n        *   [Installation options](https://github.com/mviereck/x11docker?screenshot=true#installation-options)\n        *   [Installed files](https://github.com/mviereck/x11docker?screenshot=true#installed-files)\n        *   [Shortest way for first installation](https://github.com/mviereck/x11docker?screenshot=true#shortest-way-for-first-installation)\n        *   [Minimal installation](https://github.com/mviereck/x11docker?screenshot=true#minimal-installation)\n        *   [Installation on MS Windows](https://github.com/mviereck/x11docker?screenshot=true#installation-on-ms-windows)\n        *   [Deinstallation](https://github.com/mviereck/x11docker?screenshot=true#deinstallation)\n*   [Dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies)\n*   [Troubleshooting](https://github.com/mviereck/x11docker?screenshot=true#troubleshooting)\n    *   [Core checks](https://github.com/mviereck/x11docker?screenshot=true#core-checks)\n    *   [Privilege checks](https://github.com/mviereck/x11docker?screenshot=true#privilege-checks)\n    *   [Other checks](https://github.com/mviereck/x11docker?screenshot=true#other-checks)\n*   [Contact](https://github.com/mviereck/x11docker?screenshot=true#contact)\n    *   [Issues](https://github.com/mviereck/x11docker?screenshot=true#issues)\n    *   [Contributing](https://github.com/mviereck/x11docker?screenshot=true#contributing)\n    *   [Support](https://github.com/mviereck/x11docker?screenshot=true#support)\n*   [Donation](https://github.com/mviereck/x11docker?screenshot=true#donation)\n*   [Examples](https://github.com/mviereck/x11docker?screenshot=true#examples)\n    *   [Single applications](https://github.com/mviereck/x11docker?screenshot=true#single-applications)\n    *   [Desktop environments](https://github.com/mviereck/x11docker?screenshot=true#desktop-environments)\n    *   [Adjust images for your needs](https://github.com/mviereck/x11docker?screenshot=true#adjust-images-for-your-needs)\n    *   [Screenshots](https://github.com/mviereck/x11docker?screenshot=true#screenshots)\n\nIntroduction\n------------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#introduction)\n\nx11docker allows to run graphical desktop applications (and entire desktops) in Linux containers.\n\n*   [Container tools](https://github.com/mviereck/x11docker?screenshot=true#backend-docker-podman-or-nerdctl) like [Docker](https://en.wikipedia.org/wiki/Docker_(software)), [podman](http://docs.podman.io/en/latest/) and [nerdctl](https://github.com/containerd/nerdctl) allow to run applications in an isolated [container](https://en.wikipedia.org/wiki/Operating-system-level_virtualization) environment. Containers need much less resources than [virtual machines](https://en.wikipedia.org/wiki/Virtual_machine) for similar tasks.\n*   Docker, podman and nerdctl do not provide a [display server](https://en.wikipedia.org/wiki/Display_server) that would allow to run applications with a [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface).\n*   x11docker fills the gap. It runs an [X display server](https://en.wikipedia.org/wiki/X_Window_System) and provides it to containers. X servers can run from host or in a container of image [x11docker/xserver](https://github.com/mviereck/dockerfile-x11docker-xserver).\n*   Additionally x11docker does some [security setup](https://github.com/mviereck/x11docker#security) to enhance container isolation and to avoid X security leaks. This allows a [sandbox](https://github.com/mviereck/x11docker?screenshot=true#sandbox) environment that fairly well protects the host system from possibly malicious or buggy software.\n\nSoftware can be installed in a deployable image with a rudimentary Linux system inside. This can help to run or deploy software that is difficult to install on several systems due to dependency issues. It is possible to run outdated versions or latest development versions side by side. Files to work on can be shared between host and container.\n\n[x11docker wiki](https://github.com/mviereck/x11docker/wiki) provides some how-to's for basic setups without x11docker.\n\n### Docker Desktop or Docker Engine\n\n[](https://github.com/mviereck/x11docker?screenshot=true#docker-desktop-or-docker-engine)\n\nSince a while Docker distributes a version called \"Docker Desktop\" that runs Docker in a QEMU VM. x11docker is not designed to support this VM based version. Instead, use x11docker with the native [\"Docker Engine Server version\"](https://docs.docker.com/engine/install/#server) that uses your host kernel to run containers.\n\n*   If you install Docker from your distribution's repository, you'll likely get this native version.\n*   The supported native Docker Engine package name is mostly `docker.io` or `docker-ce`, in opposite to the non-supported VM based `docker-desktop` package.\n*   If you prefer podman over Docker, you don't need to care about this difference.\n\n### TL;DR\n\n[](https://github.com/mviereck/x11docker?screenshot=true#tldr)\n\nFor a quick start:\n\n*   [Install](https://github.com/mviereck/x11docker?screenshot=true#installation) x11docker with:\n    \n    curl -fsSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker | sudo bash -s -- --update\n    \n*   Install [dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies):\n    *   Either pull image `x11docker/xserver` or install at least `nxagent` or `xpra` and `xephyr`.\n*   [Run](https://github.com/mviereck/x11docker?screenshot=true#terminal-syntax) a GUI in container with:\n    \n    x11docker IMAGENAME \\[COMMAND\\]\n    \n*   Add [options](https://github.com/mviereck/x11docker?screenshot=true#options):\n    *   `--desktop` for a desktop environment in image.\n    *   `--gpu` for hardware acceleration.\n*   [Examples](https://github.com/mviereck/x11docker?screenshot=true#examples):\n    \n    x11docker x11docker/xfce thunar\n    x11docker --desktop x11docker/xfce\n    x11docker --gpu x11docker/xfce glxgears\n    \n\n### Features\n\n[](https://github.com/mviereck/x11docker?screenshot=true#features)\n\n*   Focus on [security](https://github.com/mviereck/x11docker?screenshot=true#security):\n    *   Avoids X security leaks by running [additional X servers](https://github.com/mviereck/x11docker?screenshot=true#choice-of-x-servers-and-wayland-compositors).\n    *   Restricts container capabilities to bare minimum.\n    *   Container user is same as host user to avoid root in container.\n*   Low [dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies):\n    *   No obliging dependencies on host beside X and one of `docker`, `podman` or `nerdctl`. Recommended: `nxagent` and `Xephyr`, alternatively image `x11docker/xserver`.\n    *   No dependencies inside of images except for some optional features.\n*   Several [optional features](https://github.com/mviereck/x11docker?screenshot=true#options) like [GPU](https://github.com/mviereck/x11docker?screenshot=true#gpu-hardware-acceleration), [sound](https://github.com/mviereck/x11docker?screenshot=true#sound), [webcam](https://github.com/mviereck/x11docker?screenshot=true#webcam) and [printer](https://github.com/mviereck/x11docker?screenshot=true#printer) support.\n*   Remote access with [SSH](https://github.com/mviereck/x11docker/wiki/Remote-access-with-SSH), [VNC](https://github.com/mviereck/x11docker/wiki/VNC) or [HTML5](https://github.com/mviereck/x11docker/wiki/Container-applications-running-in-Browser-with-HTML5) possible.\n*   Easy to use. [Examples](https://github.com/mviereck/x11docker?screenshot=true#examples):\n\n### Supported systems\n\n[](https://github.com/mviereck/x11docker?screenshot=true#supported-systems)\n\nx11docker runs on Linux and (with some setup and limitations) on [MS Windows](https://github.com/mviereck/x11docker?screenshot=true#installation-on-ms-windows). x11docker does not run on macOS except in a Linux VM.\n\nTerminal syntax\n---------------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#terminal-syntax)\n\nJust type `x11docker IMAGENAME [COMMAND]`.\n\n*   Get an [overview of options](https://github.com/mviereck/x11docker/wiki/x11docker-options-overview) with `x11docker --help`.\n    *   For desktop environments in image add option `-d, --desktop`.\n    *   For internet access use option `-I, --network`.\n    *   To run without X at all use option `-t, --tty`.\n    *   Get an interactive TTY with option `-i, --interactive`.\n    *   See generated container backend command (and further infos) with option `--debug`.\n*   If startup fails, look at chapter [Troubleshooting](https://github.com/mviereck/x11docker?screenshot=true#troubleshooting).\n\nGeneral syntax:\n\n```\nUsage:\nTo run a container on a new X server:\n  x11docker IMAGE\n  x11docker [OPTIONS] IMAGE [COMMAND]\n  x11docker [OPTIONS] -- IMAGE [COMMAND [ARG1 ARG2 ...]]\n  x11docker [OPTIONS] -- CUSTOM_RUN_OPTIONS -- IMAGE [COMMAND [ARG1 ARG2 ...]]\nTo run a host application on a new X server:\n  x11docker [OPTIONS] --backend=host COMMAND\n  x11docker [OPTIONS] --backend=host -- COMMAND [ARG1 ARG2 ...]\n  x11docker [OPTIONS] --backend=host -- -- COMMAND [ARG1 ARG2 ...] -- [ARG3]\nTo run only an empty new X server:\n  x11docker [OPTIONS] --xonly\n```\n\n`CUSTOM_RUN_OPTIONS` are just added to the `docker|podman|nerdctl run` command without a serious check by x11docker.\n\nOptions\n-------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#options)\n\nDescription of some commonly used feature [options](https://github.com/mviereck/x11docker/wiki/x11docker-options-overview).\n\n*   Some of these options have dependencies on host and/or in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).\n*   For often used option combinations you can make shortcuts with [option `--preset`](https://github.com/mviereck/x11docker?screenshot=true#option---preset).\n\n### Choice of X servers and Wayland compositors\n\n[](https://github.com/mviereck/x11docker?screenshot=true#choice-of-x-servers-and-wayland-compositors)\n\nIf no X server option is specified, x11docker automatically chooses one depending on installed [dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies) and on given or missing options `--desktop`, `--gpu` and `--wayland`. Most recommended are `nxagent` and `Xephyr`.\n\n*   [Overview of all possible X server and Wayland options.](https://github.com/mviereck/x11docker/wiki/X-server-and-Wayland-Options)\n    *   [Hints to use option `--xorg` within X.](https://github.com/mviereck/x11docker/wiki/Setup-for-option---xorg)\n    *   Use option `-t, --tty` to run without X at all.\n\n### Desktop or seamless mode\n\n[](https://github.com/mviereck/x11docker?screenshot=true#desktop-or-seamless-mode)\n\nx11docker assumes that you want to run a single application in seamless mode, i.e. a single window on your regular desktop. If you want to run a desktop environment in image, add option `--desktop`.\n\n*   Seamless mode is supported with options `--nxagent` and `--xpra`. As a fallback insecure option `--hostdisplay` is possible.\n*   Desktop mode with `--desktop` is supported with all X server options except `--hostdisplay`. If available, x11docker prefers `--xephyr` and `--nxagent`.\n*   Special case: Single applications with a window manager (option `--wm`).\n    *   If neither `nxagent` nor `xpra` are installed, but x11docker finds a desktop capable X server like `Xephyr`, it avoids insecure option `--hostdisplay` and runs Xephyr with a window manager.\n\n### Internet access\n\n[](https://github.com/mviereck/x11docker?screenshot=true#internet-access)\n\nBy default x11docker disables Network access for containers with `--network=none` because it targets best possible container isolation. To allow internet access set option `-I` or `--network`.\n\n### Shared folders, volumes and HOME in container\n\n[](https://github.com/mviereck/x11docker?screenshot=true#shared-folders-volumes-and-home-in-container)\n\nChanges in a running container system will be lost, the created container will be discarded. For persistent data storage you can share host directories or volumes:\n\n*   Option `-m, --home` creates a host directory in `~/.local/share/x11docker/IMAGENAME` that is shared with the container and mounted as its `HOME` directory. Files in container home and user configuration changes will persist. x11docker creates a softlink from `~/.local/share/x11docker` to `~/x11docker`.\n    *   You can specify another host directory for container `HOME` with `--home=DIR`.\n    *   You can specify a volume for container `HOME` with `--home=VOLUME`.\n*   Option `--share PATH` mounts a host file or folder at the same location in container.\n    *   You can also specify a volume with `--share VOLUME`.\n    *   `--share PATH:ro` restricts to read-only access.\n    *   Device files in `/dev` are supported, too.\n*   Special cases for `$HOME`:\n    *   `--home=$HOME` will use your host home as container home. Discouraged, use with care.\n    *   `--share $HOME` will symlink your host home as a subfolder of container home.\n\nNote that x11docker copies files from `/etc/skel` in container to `HOME` if `HOME` is empty. That allows to provide predefined user configurations in the image.\n\n### GPU hardware acceleration\n\n[](https://github.com/mviereck/x11docker?screenshot=true#gpu-hardware-acceleration)\n\nHardware acceleration for OpenGL is possible with option `-g, --gpu`.\n\n*   This will work out of the box in most cases with open source drivers on host. Otherwise have a look at [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).\n*   Closed source [NVIDIA drivers](https://github.com/mviereck/x11docker/wiki/NVIDIA-driver-support-for-docker-container) need some setup and support less [x11docker X server options](https://github.com/mviereck/x11docker/wiki/X-server-and-Wayland-Options#attributes-of-x-server-and-wayland-options) for driver version < v470.x and Xwayland < v22.1.2.\n\n### Clipboard\n\n[](https://github.com/mviereck/x11docker?screenshot=true#clipboard)\n\nClipboard sharing is possible with option `-c, --clipboard [=ARG]`.\n\n*   Optional arguments `superv` and `altv` only provide host clipboard content to container if keys `[SUPER][v]` or `[ALT][v]` are pressed.\n*   Optional argument `oneway` only transfers clipboard content from container to host.\n\n### Sound\n\n[](https://github.com/mviereck/x11docker?screenshot=true#sound)\n\nSound is possible with options `-p, --pulseaudio` and `--alsa`.\n\n*   For pulseaudio sound with `--pulseaudio` you need `pulseaudio` on host and `pulseaudio` (at least the `pulseaudio` client libraries) in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).\n*   For ALSA sound with `--alsa` you might need to specify a sound card with e.g. `--alsa=Generic`. Get a list of available sound cards with `aplay -l`.\n\n### Webcam\n\n[](https://github.com/mviereck/x11docker?screenshot=true#webcam)\n\nWebcams on host can be shared with option `--webcam`.\n\n*   If webcam application in image fails, install `--gpu` dependencies in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).\n*   `guvcview` needs `--pulseaudio` or `--alsa`.\n*   `cheese` and [`gnome-ring`](https://ring.cx/) need `--init=systemd`.\n\n### Printer\n\n[](https://github.com/mviereck/x11docker?screenshot=true#printer)\n\nPrinters on host can be provided to container with option `--printer`.\n\n*   It needs `cups` on host, the default printer server for most linux distributions.\n*   The container needs `cups` client libraries in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).\n\n### Language locales\n\n[](https://github.com/mviereck/x11docker?screenshot=true#language-locales)\n\nx11docker provides option `--lang` for flexible language locale settings.\n\n*   `--lang` without an argument sets `LANG` in container to same as on host. Same as `--lang=$LANG`\n*   x11docker will check on container startup if the desired locale is already present in image and enable it.\n*   If x11docker does not find the locale, it creates it on container startup. This needs some `locale` packages in image. Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).\n*   Examples: `--lang=de` for German, `--lang=zh_CN` for Chinese, `--lang=ru` for Russian, `--lang=$LANG` for your host locale.\n*   For support of chinese, japanese and korean characters install a font like `fonts-arphic-uming` in image.\n*   Keyboard input methods like `fcitx-pinyin` are possible with some container setup. Compare ticket [#269](https://github.com/mviereck/x11docker/issues/269#issuecomment-667124421).\n\n### Wayland\n\n[](https://github.com/mviereck/x11docker?screenshot=true#wayland)\n\nTo run [Wayland](https://wayland.freedesktop.org/) instead of an X server x11docker provides options `--wayland`, `--weston`, `--kwin` and `--hostwayland`. For further description loot at [wiki: Description of Wayland options](https://github.com/mviereck/x11docker/wiki/X-server-and-Wayland-Options#description-of-wayland-options).\n\n*   Option `--wayland` automatically sets up a Wayland environment. It regards option `--desktop`.\n*   Options `--weston` and `--kwin` run Wayland compositors `weston` or `kwin_wayland`.\n*   Option `--hostwayland` can run applications seamless on host Wayland desktops like Gnome 3, KDE 5 and [Sway](https://github.com/swaywm/sway).\n*   Example: `xfce4-terminal` on Wayland: `x11docker --wayland x11docker/xfce xfce4-terminal`\n\n### Init system\n\n[](https://github.com/mviereck/x11docker?screenshot=true#init-system)\n\nx11docker supports several init systems as PID 1 in container with option `--init`. Init in container solves the [zombie reaping issue](https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/). As default x11docker uses `tini` in`/usr/bin/docker-init`. Also available are `systemd`, `SysVinit`, `runit`, `OpenRC` and `s6-overlay`. `elogind` is supported, too. Look at [wiki: Init systems in Docker](https://github.com/mviereck/x11docker/wiki/Init-systems).\n\n### DBus\n\n[](https://github.com/mviereck/x11docker?screenshot=true#dbus)\n\nSome desktop environments and applications need a running DBus system daemon and/or DBus user session. DBus options need `dbus` in image.\n\n*   use `--dbus` to run a DBus user session daemon.\n*   A DBus system daemon will be started automatically with [init systems](https://github.com/mviereck/x11docker?screenshot=true#Init-system) `systemd`, `openrc`, `runit` and `sysvinit` (option `--init`).\n    *   It is also possible to run a DBus system daemon with `--dbus=system` without advanced init systems. However, this causes trouble in some cases and is not recommended in general.\n*   use `--hostdbus` to connect to host DBus user session.\n*   use `--share /run/dbus/system_bus_socket` to share host DBus system socket.\n\n### Container runtime\n\n[](https://github.com/mviereck/x11docker?screenshot=true#container-runtime)\n\nIt is possible to run containers with different backends following the [OCI runtime specification](https://github.com/opencontainers/runtime-spec). Docker's default runtime is `runc`. You can specify another one with option `--runtime=RUNTIME`. Container runtimes known and supported by x11docker are:\n\n*   `runc`: Docker default.\n*   [`nvidia`](https://github.com/mviereck/x11docker/wiki/NVIDIA-driver-support-for-docker-container#nvidianvidia-docker-images): Specialized fork of `runc` to support `nvidia/nvidia-docker` images.\n*   [`crun`](https://github.com/giuseppe/crun): Fast and lightweight alternative to `runc` with same functionality.\n*   `oci`: Runtime reported in [#205](https://github.com/mviereck/x11docker/issues/205), no documentation found. Handled by x11docker like `runc`.\n*   [`sysbox-runtime`](https://github.com/nestybox/sysbox): Based on runc, aims to enhance container isolation. Support is experimental yet. Needs Sybox\\>\\=0.5.0 and kernel version \\>\\=5.12.\n\nUsing different runtimes is well tested for rootful Docker, but not for other [backend setups](https://github.com/mviereck/x11docker?screenshot=true#backend-docker-podman-or-nerdctl).\n\nExample: possible runtime configuration in `/etc/docker/daemon.json`:\n\n{\n  \"default-runtime\": \"runc\",\n  \"runtimes\": {\n    \"crun\": {\n      \"path\": \"/usr/local/bin/crun\",\n      \"runtimeArgs\": \\[\\]\n    },\n    \"nvidia\": {\n      \"path\": \"nvidia-container-runtime\",\n      \"runtimeArgs\": \\[\\]\n    },\n    \"sysbox-runc\": {\n      \"path\": \"/usr/bin/sysbox-runc\"\n    }\n  }\n}\n\n### Backends other than docker\n\n[](https://github.com/mviereck/x11docker?screenshot=true#backends-other-than-docker)\n\nx11docker supports container tools [Docker](https://en.wikipedia.org/wiki/Docker_(software)), [podman](http://docs.podman.io/en/latest/) and [nerdctl](https://github.com/containerd/nerdctl) with option `--backend=BACKEND` in rootful and rootless mode. Supported `--backend` arguments: `docker` `podman` `nerdctl` `host`\n\nContainer backends:\n\n*   By default x11docker tries to run `docker`.\n    *   To change the default `--backend=docker` to another one like `--backend=podman`, create a [`default` file for `--preset`](https://github.com/mviereck/x11docker?screenshot=true#default-preset-for-all-x11docker-sessions).\n*   Recommended for rootful container backend: `docker` or `podman`\n*   Recommended for rootless container backend: `podman`\n    *   Only `podman` allows option `--home` in rootless mode yet.\n    *   Only `podman` provides useful file ownerships with option `--share` in rootless mode yet.\n*   `--backend=nerdctl` is experimental yet. It supports rootful and rootless mode. `nerdctl` is in heavy development stage.\n\nOther supported backends that are in fact no containers:\n\n*   `--backend=host` runs a host application on a new X server. No containerization is involved.\n\n### Preconfiguration with --preset\n\n[](https://github.com/mviereck/x11docker?screenshot=true#preconfiguration-with---preset)\n\nFor often used option combinations you might want to use option `--preset FILENAME` to have a command shortcut. `FILENAME` is a file in `~/.config/x11docker/preset` or in `/etc/x11docker/preset` containing some x11docker options.\n\n*   Example `multimedia`: Create a file `~/.config/x11docker/preset/multimedia`:\n    \n    ```\n    --gpu\n    --webcam\n    --printer\n    --pulseaudio\n    --clipboard\n    --share ~/Videos\n    --share ~/Music\n    ```\n    \n    Use it like: `x11docker --preset=multimedia jess/vlc`\n*   Example deepin desktop: Instead of long command\n    \n    ```\n    x11docker --desktop --init=systemd --gpu --pulseaudio --home -- --cap-add=IPC_LOCK -- x11docker/deepin\n    ```\n    \n    you can create a file `~/.config/x11docker/preset/deepin` containing the desired options and even the image name:\n    \n    ```\n    --desktop \n    --init=systemd\n    --gpu\n    --pulseaudio\n    --home\n    -- \n    --cap-add=IPC_LOCK\n    -- \n    x11docker/deepin\n    ```\n    \n    Run with: `x11docker --preset=deepin`\n\n#### Default preset for all x11docker sessions\n\n[](https://github.com/mviereck/x11docker?screenshot=true#default-preset-for-all-x11docker-sessions)\n\nYou can create a `default` preset file that is applied on all x11docker sessions. You can think of it as a configuration file for x11docker.\n\n*   Example: To always use `podman` instead of docker, create a file with name `default` in `~/.config/x11docker/preset` or in `/etc/x11docker/preset` with content: This will cause x11docker to always use `podman` instead of `docker` unless specified otherwise in the x11docker command.\n\nThe same way you can specify other and more options as default, e.g. `--homebasedir=/my/containerhome/path`. Note that a local user `default` file will supersede a system wide `default` file.\n\nSecurity\n--------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#security)\n\nScope of x11docker is to run containerized GUI applications while preserving and improving container isolation. Core concept is:\n\n*   Runs a second X server to avoid [X security leaks](http://tutorials.section6.net/tutorials/freebsd/security/basics-of-securing-x11.html).\n    *   This in opposite to widespread solutions that share host X socket of display :0, thus breaking container isolation, allowing keylogging and remote host control. (However, x11docker provides this with fallback option `--hostdisplay`).\n    *   Authentication is done with MIT-MAGIC-COOKIE, stored separate from file `~/.Xauthority`.\n*   Creates container user similar to host user to [avoid root in container](http://blog.dscpl.com.au/2015/12/don-run-as-root-inside-of-docker.html).\n    *   You can also specify another user with `--user=USERNAME` or a non-existing one with `--user=UID:GID`.\n    *   Disables possible root password and deletes entries in `/etc/sudoers`.\n        *   If you want root permissions in container, use option `--sudouser` that allows `su` and `sudo` with password `x11docker`.\n    *   If you want to use `USER` specified in image instead, set option `--user=RETAIN`. x11docker won't change container's `/etc/passwd` or `/etc/sudoers` in that case. Option `--home` won't be available.\n*   Reduces [container capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities) to bare minimum.\n    *   Sets run option `--cap-drop=ALL` to drop all capabilities. Most applications don't need them.\n    *   Sets run option [`--security-opt=no-new-privileges`](https://www.projectatomic.io/blog/2016/03/no-new-privs-docker/).\n    *   These restrictions can be disabled with x11docker option `--cap-default` or reduced with `--sudouser`, `--newprivileges`.\n\nThat being said, the default docker capabilities and the seccomp/SELinux/apparmor profiles are set up well to protect the host system. Nonetheless, x11docker follows the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Containers should not have capabilities or privileges that they don't need for their job.\n\n### Security weaknesses\n\n[](https://github.com/mviereck/x11docker?screenshot=true#security-weaknesses)\n\n*   Possible SELinux restrictions are degraded for x11docker containers with run option `--security-opt label=type:container_runtime_t` to allow access to new X unix socket. A more restrictive solution is desirable. Compare: [SELinux and Docker: allow access to X unix socket in /tmp/.X11-unix](https://unix.stackexchange.com/questions/386767/selinux-and-docker-allow-access-to-x-unix-socket-in-tmp-x11-unix)\n*   A possible user namespace remapping setup is disabled to allow options `--home` and `--share` without file ownership issues.\n    *   This is less an issue because x11docker already avoids root in container.\n    *   Exception: User namespace remapping is not disabled for `--user=RETAIN`.\n*   x11docker provides several different X server options. Each X server involved might have its individual vulnerabilities. x11docker only covers well-known X security leaks that result from X11 protocol design.\n    *   An additional security layer for most supported X servers is set up if image [x11docker/xserver](https://github.com/mviereck/dockerfile-x11docker-xserver) is available. It will be used automatically in most cases if available. Enforce its usage with option `--xc=yes`.\n\n### Options degrading container isolation\n\n[](https://github.com/mviereck/x11docker?screenshot=true#options-degrading-container-isolation)\n\nx11docker shows warning messages in terminal if chosen options degrade container isolation. Note that x11docker does not check custom `DOCKER_RUN_OPTIONS`.\n\n_Most important:_\n\n*   `--hostdisplay` shares host X socket of display :0 instead of running a second X server.\n    *   Danger of abuse is reduced providing so-called untrusted cookies, but do not rely on this.\n    *   If additionally using `--gpu` or `--clipboard`, option `--ipc=host` and trusted cookies are enabled and no protection against X security leaks is left.\n    *   If you don't care about container isolation, `x11docker --hostdisplay --gpu` is an insecure but quite fast setup without any overhead.\n*   `--gpu` allows access to GPU hardware. This can be abused to get window content from host ([palinopsia bug](https://hsmr.cc/palinopsia/)) and makes [GPU rootkits](https://github.com/LucaBongiorni/jellyfish) like [keyloggers](http://www.cs.columbia.edu/~mikepo/papers/gpukeylogger.eurosec13.pdf) possible.\n*   `--pulseaudio` and `--alsa` allow catching audio output and microphone input from host.\n\n_Rather special options reducing security, but not needed for regular use:_\n\n*   `--sudouser` allows `su` and `sudo` with password `x11docker`for container user. If an application somehow breaks out of container, it can harm your host system. Allows many container capabilities that x11docker would drop otherwise.\n*   `--cap-default` disables x11docker's container security hardening and falls back to default container capabilities as provided by the backends docker, podman or nerdctl. If an application somehow breaks out of container, it can harm your host system.\n*   `--init=systemd|sysvinit|openrc|runit` allow some container capabilities that x11docker would drop otherwise. `--init=systemd` also shares access to `/sys/fs/cgroup`. Some processes will run as root in container. If a root process somehow breaks out of container, it can harm your host system. Allows many container capabilities that x11docker would drop otherwise.\n*   `--hostdbus` allows communication over DBus with host applications.\n\n### Sandbox\n\n[](https://github.com/mviereck/x11docker?screenshot=true#sandbox)\n\nContainer isolation enhanced with x11docker allows to use containers as a [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) that fairly well protects the host system from possibly malicious or buggy software. Though, no sandbox solution in the wild can provide a perfect secure protection, and Docker even with enhanced security settings from x11docker is no exception.\n\nUsing x11docker as a sandbox is not intended to run obviously evil software. Rather use it as:\n\n*   Compatibility environment to run software that is hard or impossible to install on host due to dependency issues.\n*   Development environment to collect libraries, compiler and so on to keep the host clean.\n*   Development environment to mitigate damage caused by unexpected/buggy behaviour.\n*   Security layer for software that may be malicious in worst case. Examples: Internet browser with enabled `javascript`, or `wine` with MS Windows applications.\n\nx11docker already restricts process capabilities. You can additionally restrict access to CPU and RAM with option `--limit`. As default `--limit` restricts to 50% of available CPUs and 50% of currently free RAM. Another amount can be specified with `--limit=FACTOR` with a `FACTOR` greater than zero and less than or equal one.\n\nFor more custom fine tuning have a look at [Docker documentation: Limit a container's resources](https://docs.docker.com/config/containers/resource_constraints).\n\n**WARNING**: There is no restriction that can prevent the container from flooding the hard disk storing the container or in shared folders.\n\n### Security and feature check\n\n[](https://github.com/mviereck/x11docker?screenshot=true#security-and-feature-check)\n\nTo check container isolation and some feature options use image `x11docker/check` and try out with several options.\n\n*   An insecure setup is `x11docker --hostdisplay --gpu x11docker/check`. It fairly well demonstrates common X security leaks.\n*   Add options like `--pulseaudio --alsa --webcam --clipboard --printer` to check their functionality.\n\nInstallation\n------------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#installation)\n\nNote that x11docker is just a **bash script** without library dependencies. Basically it is just a wrapper for X servers and container backends docker, podman and nerdctl. To allow advanced usage of x11docker abilities have a look at chapter [Dependencies](https://github.com/mviereck/x11docker?screenshot=true#dependencies).\n\n### Installation from distribution repositories\n\n[](https://github.com/mviereck/x11docker?screenshot=true#installation-from-distribution-repositories)\n\nx11docker is available as a package in some distributions.\n\nStable releases:\n\n[![Image 37: GitHub release (latest by date)](https://camo.githubusercontent.com/b4bb31de55970b4534d6fe20dc7014c6fe34fadd0a5d50e9fece78470b582c86/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6d7669657265636b2f783131646f636b65723f6c6162656c3d783131646f636b65722532306c617465737425323072656c65617365)](https://camo.githubusercontent.com/b4bb31de55970b4534d6fe20dc7014c6fe34fadd0a5d50e9fece78470b582c86/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f762f72656c656173652f6d7669657265636b2f783131646f636b65723f6c6162656c3d783131646f636b65722532306c617465737425323072656c65617365)\n\n[![Image 38: Packaging status](https://camo.githubusercontent.com/ce117ecaf3f25119b45121ec616a05a059918053d22cd4373f2483c36a6e12f3/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f766572746963616c2d616c6c7265706f732f783131646f636b65722e737667)](https://repology.org/project/x11docker/versions)\n\nLatest git master/beta version:\n\n[![Image 39: AUR latest git](https://camo.githubusercontent.com/6582b96571ad9f74e73e3bd01e56ec3dbb6f241e33c1593acee84afe4bcf8e9d/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f76657273696f6e2d666f722d7265706f2f6175722f783131646f636b65722e7376673f616c6c6f775f69676e6f7265643d31)](https://repology.org/project/x11docker/versions)\n\nMuch thanks to the maintainers who decided to provide these packages! There are some hints for [packaging x11docker](https://github.com/mviereck/x11docker/wiki/Packaging-x11docker) in the wiki.\n\n### Manual installation\n\n[](https://github.com/mviereck/x11docker?screenshot=true#manual-installation)\n\n#### Installation options\n\n[](https://github.com/mviereck/x11docker?screenshot=true#installation-options)\n\nAs root you can install, update and remove x11docker in system directories to be available system-wide:\n\n*   `x11docker --install` : install x11docker from current directory. (Useful to install from an extracted `zip` file or a cloned `git` repository.)\n*   `x11docker --update` : download and install latest [release](https://github.com/mviereck/x11docker/releases) from github.\n*   `x11docker --update-master` : download and install latest master version from github.\n*   `x11docker --remove` : remove all files installed by x11docker.\n    *   Note: This does not remove `~/.local/share/x11docker` where it stores persistent files of option `--home`.\n*   `x11docker --remove-oldprefix` : Before version 7.6.0 x11docker installed itself into `/usr/bin`. Now it installs into `/usr/local/bin`. Use `--remove-oldprefix` to remove `/usr/bin` installations.\n\nTo see the difference between current and coming updated version, you can use optional argument `diff` for `--update` and `--update-master`. Example: `x11docker --update-master=diff` will show you the code changes from your current installation to latest master/beta version without installing it.\n\n#### Installed files\n\n[](https://github.com/mviereck/x11docker?screenshot=true#installed-files)\n\nWhat the installation does (just for information):\n\n*   Copies script `x11docker` to `/usr/local/bin`.\n*   Installs icon `x11docker.png` below `/usr/share/icons` using `xdg-icon-resource`.\n*   Copies documentation `README.md`, `CHANGELOG.md` and `LICENSE.txt` to `/usr/local/share/doc/x11docker`.\n*   Stores `man` page for x11docker in `/usr/local/share/man/man1/x11docker.1.gz`.\n\n#### Shortest way for first installation:\n\n[](https://github.com/mviereck/x11docker?screenshot=true#shortest-way-for-first-installation)\n\n*   For systems using `sudo`:\n    \n    curl -fsSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker | sudo bash -s -- --update\n    \n*   Directly as `root`:\n    \n    curl -fsSL https://raw.githubusercontent.com/mviereck/x11docker/master/x11docker | bash -s -- --update\n    \n\n#### Minimal installation\n\n[](https://github.com/mviereck/x11docker?screenshot=true#minimal-installation)\n\nYou can run x11docker from an arbitrary location with `bash x11docker` or `./x11docker`. For minimal system-wide installation make `x11docker` executable with `chmod +x x11docker` and move it to `/usr/local/bin` (or another location in `PATH`). Other files than script `x11docker` itself are not essential.\n\n#### Installation on MS Windows\n\n[](https://github.com/mviereck/x11docker?screenshot=true#installation-on-ms-windows)\n\nx11docker can run natively on MS Windows electively in one of:\n\n*   [WSL (Windows subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/about)\n*   [Cygwin](https://www.cygwin.com/)\n*   [MSYS2](https://www.msys2.org/)\n\nFurther information at [wiki: x11docker on MS Windows](https://github.com/mviereck/x11docker/wiki/x11docker-on-MS-Windows).\n\n#### Deinstallation\n\n[](https://github.com/mviereck/x11docker?screenshot=true#deinstallation)\n\nYou can remove x11docker with `x11docker --remove`. That will remove the [files listed above](https://github.com/mviereck/x11docker?screenshot=true#installation-options). It will also remove `~/.cache/x11docker` and stop all running x11docker containers. x11docker will **not** remove:\n\n*   Files and folders for persistent data storage with option `--home`. These are:\n    *   `~/.local/share/x11docker` where persistent data is stored.\n    *   Softlink `~/x11docker` that points there.\n*   Folders you might have created yourself for x11docker:\n    *   `~/.local/share/x11docker`\n    *   `~/.config/x11docker`\n\nDependencies\n------------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#dependencies)\n\nx11docker can run with standard system utilities without additional dependencies on host or in image.\n\n*   As a core it only needs `bash` and one of [`docker`](https://www.docker.com/), [`podman`](http://docs.podman.io/en/latest/) or [`nerdctl`](https://github.com/containerd/nerdctl) to run containers on X.\n*   x11docker also needs an X server. x11docker can automatically use image [`x11docker/xserver`](https://github.com/mviereck/dockerfile-x11docker-xserver) that provides most optional x11docker dependencies and several X servers and Wayland compositors so you won't need to install them on host.\n    *   If you prefer to install dependencies on host:\n        *   The recommended base commands are: `nxagent` `Xephyr` `weston` `Xwayland` `xdotool` `xauth` `xinit` `xclip` `xhost` `xrandr` `xdpyinfo`. Some of them are probably already installed.\n        *   See [wiki: Dependencies - Recommended base](https://github.com/mviereck/x11docker/wiki/Dependencies#recommended-base) for a package list matching your distribution.\n\nDependencies in image:\n\n*   Some feature options have additional dependencies on host and/or in image. This affects especially options `--gpu`, `--printer` and `--pulseaudio`.\n*   Compare [wiki: feature dependencies](https://github.com/mviereck/x11docker/wiki/Dependencies#dependencies-of-feature-options).\n\nTroubleshooting\n---------------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#troubleshooting)\n\nFor troubleshooting run `x11docker` in a terminal. x11docker shows warnings if something is insecure, missing or going wrong. Also it shows notes if options don't work and fallbacks are used. It might give hints to fix some issues.\n\n### Core checks\n\n[](https://github.com/mviereck/x11docker?screenshot=true#core-checks)\n\n**1.** Make sure your x11docker version is up to date with `x11docker --update` (latest release) or `x11docker --update-master` (latest beta).\n\n**2.** Carefully read the regular x11docker messages. Often they already give a hint what to do.\n\n*   Use option `-D, --debug` to see some internal messages.\n*   Use option `-v, --verbose` to see full logfile output.\n*   You can find the latest dispatched logfile at `~/.cache/x11docker/x11docker.log`.\n\n**3.** Try another X server option.\n\n*   Some applications fail with fallback option `--hostdisplay`. Add `--clipboard` to disable some security restrictions of `--hostdisplay`.\n*   If that does not help, install [additional X servers](https://github.com/mviereck/x11docker/wiki/Dependencies#recommended-base). The most stable and reliable option is `--xephyr`.\n\n### Privilege checks\n\n[](https://github.com/mviereck/x11docker?screenshot=true#privilege-checks)\n\nSome applications need more privileges or [capabilities](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities) than x11docker provides by default. One attempt is to allow several privileges until the setup works. Than reduce privileges to find out which are needed indeed. (Note the `--` in the following commands, do not miss them).\n\n**1.** Adding privileges:\n\n*   Try `x11docker --cap-default IMAGENAME`\n*   Try `x11docker --cap-default --ipc=host --network=host IMAGENAME`\n*   Try `x11docker --cap-default --ipc=host --network=host --share /run/udev/data:ro -- --cap-add ALL --security-opt seccomp=unconfined --security-opt apparmor=unconfined --privileged -- IMAGENAME`\n\n**2.** Reducing privileges:\n\n*   Drop options one by one in this order: `--privileged` `--security-opt apparmor=unconfined` `--security-opt seccomp=unconfined` `--cap-add ALL` `--share /run/udev/data:ro` `--network=host` `--ipc=host` `--cap-default`. Only leave options that are needed to keep the setup working.\n*   Option `--cap-default` might already be enough. It allows default container capabilities as docker|podman|nerdctl would do on themself.\n    *   You can just stop debugging and reducing here if you like to.\n    *   You can try to reduce `--cap-default`. Partially remove additional options to find out which one(s) are needed:\n        *   First try `x11docker --newprivileges -- IMAGENAME`\n        *   Than try and reduce: `x11docker --newprivileges -- --cap-add=SETPCAP --cap-add=MKNOD --cap-add=AUDIT_WRITE --cap-add=CHOWN --cap-add=NET_RAW --cap-add=DAC_OVERRIDE --cap-add=FOWNER --cap-add=FSETID --cap-add=KILL --cap-add=SETGID --cap-add=SETUID --cap-add=NET_BIND_SERVICE --cap-add=SYS_CHROOT --cap-add=SETFCAP -- IMAGENAME`\n*   `--cap-add ALL` should not be considered to be a solution.\n    *   Drop capabilities from following command to find the one(s) you need: `x11docker --cap-default -- --cap-add=SYS_MODULE --cap-add=SYS_RAWIO --cap-add=SYS_PACCT --cap-add=SYS_ADMIN --cap-add=SYS_NICE --cap-add=SYS_RESOURCE --cap-add=SYS_TIME --cap-add=SYS_TTY_CONFIG --cap-add=AUDIT_CONTROL --cap-add=MAC_OVERRIDE --cap-add=MAC_ADMIN --cap-add=NET_ADMIN --cap-add=SYSLOG --cap-add=DAC_READ_SEARCH --cap-add=LINUX_IMMUTABLE --cap-add=NET_BROADCAST --cap-add=IPC_LOCK --cap-add=IPC_OWNER --cap-add=SYS_PTRACE --cap-add=SYS_BOOT --cap-add=LEASE --cap-add=WAKE_ALARM --cap-add=BLOCK_SUSPEND --cap-add=AUDIT_READ -- IMAGENAME`\n    *   Many of these capabilities are rather dangerous and should not be allowed for a container. Especially to mention is `SYS_ADMIN`.\n*   Option `--privileged` should not be considered to be a solution. Basically it allows arbitrary access to the host for container applications.\n    *   Likely you need to share a device file in `/dev`, e.g. something like `--share /dev/vboxdrv`.\n*   `--ipc=host` and `--network=host` severely reduce container isolation. Better solutions are desirable.\n\n**3.** Open a ticket to ask for possibilities how to optimize the privilege setup.\n\n### Other checks\n\n[](https://github.com/mviereck/x11docker?screenshot=true#other-checks)\n\n**1.** Container user: By default x11docker sets up an unprivileged container user similar to your host user.\n\n*   The image may have a `USER` specification and be designed for this user.\n    *   Check for a `USER` specification in image with `docker inspect --format '{{.Config.User}}' IMAGENAME`\n    *   You can enable this predefined user with `--user=RETAIN`\n*   The container might need a root user. Try with `--user=root`, maybe add `--cap-default`.\n\n**2.** Init and DBus\n\n*   A few applications need a [DBus](https://github.com/mviereck/x11docker?screenshot=true#dbus) user daemon. Install `dbus` in image and try option `--dbus`.\n*   A few applications need systemd and/or a running [DBus](https://github.com/mviereck/x11docker?screenshot=true#dbus) system daemon. Install `systemd` in image and try option `--init=systemd`.\n\n**3.** Architecture check of host OS and image\n\n*   The image may not be built for the architecture of your host OS. (ie. Image is built for amd64 but your OS runs on arm, e.g. on a RaspBerry PI). With a mismatch the container will quit unexpectedly & x11docker may emit the error `dockerrc(): Did not receive PID of PID1 in container.`\n    *   You can check the image architecture with `docker inspect --format {{.Architecture}} IMAGENAME`.\n    *   You can check the host architecture with `uname -m`.\n    *   For further information and multi-arch setups look at [wiki: Multi-arch setups with QEMU](https://github.com/mviereck/x11docker/wiki/Multiarch-setups-with-QEMU).\n\nContact\n-------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#contact)\n\nFeel free to open a [ticket](https://github.com/mviereck/x11docker/issues) if you have a question or encounter an issue.\n\n### Issues\n\n[](https://github.com/mviereck/x11docker?screenshot=true#issues)\n\nIf reporting an [issue](https://github.com/mviereck/x11docker/issues):\n\n*   Have a look at chapter [Troubleshooting](https://github.com/mviereck/x11docker?screenshot=true#troubleshooting).\n*   Most times it makes sense to store the `--verbose` output (or `~/.cache/x11docker/x11docker.log`) at [pastebin.com](https://pastebin.com/).\n    *   Personal information in the logfile is mainly the user name (also in paths) and some hardware and system information.\n\n### Contributing\n\n[](https://github.com/mviereck/x11docker?screenshot=true#contributing)\n\nIf you want to contribute to x11docker, please open a [ticket](https://github.com/mviereck/x11docker/issues) before creating a pull request. Often it is possible to accomplish desired tasks with already available options. Note that x11docker is considered to be stable and changes other than bug fixes are less likely to be merged. In general new features are not intended.\n\n### Support\n\n[](https://github.com/mviereck/x11docker?screenshot=true#support)\n\nPlease open a [ticket](https://github.com/mviereck/x11docker/issues) if you need support. Please note that `x11docker` is a non-commercial project maintained in free time. I'll help where I can, but there is no organisation behind `x11docker` that can provide large scale support.\n\nDonation\n--------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#donation)\n\nIf you like to make a donation: Thank you! :) Please have a look at [my sponsor site](https://github.com/sponsors/mviereck).\n\nInstead of sponsoring me, you can as well spend some money to [Galsan Tschinag](http://galsan-tschinag.de/portrait/) in Mongolia ([Wikipedia](https://en.wikipedia.org/wiki/Galsan_Tschinag)). One of his great projects is the afforestation of Mongolia. A donation account in Germany is provided by [Förderverein Mongolei e.V.](http://foerderverein-mongolei.de/spenden/).\n\n```\nFörderverein Mongolei e.V.\nIBAN DE7261290120 0394 3660 00\nBIC GENODES1NUE\nVolksbank Kirchheim-Nürtingen\n```\n\nI personally know some of the people behind this. I assure that they are trustworthy and have a great heart and soul and do a good thing.\n\nExamples\n--------\n\n[](https://github.com/mviereck/x11docker?screenshot=true#examples)\n\n[Some x11docker image examples with desktop environments can be found on docker hub.](https://hub.docker.com/u/x11docker/) A special one to check features and container isolation is `x11docker/check`.\n\nDocker does not provide automated builds for free anymore, so the images are becoming outdated. Instead of pulling them, rather build them locally with x11docker option `--build`.\n\nSome x11docker Dockerfiles are provided at [https://github.com/mviereck?tab=repositories](https://github.com/mviereck?tab=repositories); look for repositories beginning with `dockerfile-x11docker`. You can build locally from these Dockerfiles with x11docker option `--build`. Example:\n\n```\nx11docker --build x11docker/fvwm\n```\n\n### Single applications\n\n[](https://github.com/mviereck/x11docker?screenshot=true#single-applications)\n\n| Application | x11docker command |\n| --- | --- |\n| Xfce4 Terminal | `x11docker x11docker/xfce xfce4-terminal` |\n| GLXgears with hardware acceleration | `x11docker --gpu x11docker/xfce glxgears` |\n| [Kodi media center](https://kodi.tv/) with hardware  \nacceleration, Pulseaudio sound  \nand shared `Videos` folder.  \nFor setup look at [ehough/docker-kodi](https://github.com/ehough/docker-kodi). | `x11docker --gpu --pulseaudio --share ~/Videos erichough/kodi`. |\n| [XaoS](https://github.com/patrick-nw/xaos) fractal generator | `x11docker patricknw/xaos` |\n| [Telegram messenger](https://telegram.org/) with persistent  \n`HOME` for configuration storage | `x11docker --home xorilog/telegram` |\n| Firefox with shared `Download` folder  \nand internet access. | `x11docker -I --share $HOME/Downloads -- --tmpfs /dev/shm -- jess/firefox` |\n| [Tor browser](https://www.torproject.org/projects/torbrowser.html) | `x11docker -I jess/tor-browser` |\n| Chromium browser with restricted resource usage | `x11docker -I --limit -- jess/chromium --no-sandbox` |\n| VLC media player with shared `Videos`  \nfolder and Pulseaudio sound | `x11docker --pulseaudio --share=$HOME/Videos jess/vlc` |\n| [GNU Octave Scientific Programming Language](https://www.gnu.org/software/octave/) built for arm & arm64 | `x11docker aptman/dbhi:bionic-octave octave` |\n\n### Desktop environments\n\n[](https://github.com/mviereck/x11docker?screenshot=true#desktop-environments)\n\n| Desktop environment  \n(most based on Debian) | x11docker command |\n| --- | --- |\n| [Cinnamon](https://github.com/mviereck/dockerfile-x11docker-cinnamon) | `x11docker --desktop --gpu --init=systemd --cap-default x11docker/cinnamon` |\n| [deepin](https://github.com/mviereck/dockerfile-x11docker-deepin) ([website](https://www.deepin.org/en/dde/)) (3D desktop from China) | `x11docker --desktop --gpu --init=systemd -- --cap-add=IPC_LOCK -- x11docker/deepin` |\n| [Enlightenment](https://github.com/mviereck/dockerfile-x11docker-enlightenment) (based on [Void Linux](https://www.voidlinux.org/)) | `x11docker --desktop --gpu --runit x11docker/enlightenment` |\n| [Fluxbox](https://github.com/mviereck/dockerfile-x11docker-fluxbox) (based on Debian, 87 MB) | `x11docker --desktop x11docker/fluxbox` |\n| [FVWM](https://github.com/mviereck/dockerfile-x11docker-fvwm) (based on [Alpine](https://alpinelinux.org/), 22.5 MB) | `x11docker --desktop x11docker/fvwm` |\n| [Gnome 3](https://github.com/mviereck/dockerfile-x11docker-gnome) | `x11docker --desktop --gpu --init=systemd x11docker/gnome` |\n| [KDE Plasma](https://github.com/mviereck/dockerfile-x11docker-kde-plasma) on X | `x11docker --desktop --gpu --init=systemd x11docker/kde-plasma` |\n| [KDE Plasma](https://github.com/mviereck/dockerfile-x11docker-kde-plasma) on Wayland | `x11docker --kwin --wayland x11docker/kde-plasma plasmashell` |\n| [KDE Plasma](https://github.com/mviereck/dockerfile-x11docker-kde-plasma) as nested Wayland compositor | `x11docker --gpu --init=systemd -- --cap-add SYS_RESOURCE -- x11docker/kde-plasma startplasma-wayland` |\n| [Lumina](https://github.com/mviereck/dockerfile-x11docker-lumina) ([website](https://lumina-desktop.org/)) (based on [Void Linux](https://www.voidlinux.org/)) | `x11docker --desktop x11docker/lumina` |\n| [LiriOS](https://liri.io/) (based on Fedora) | `x11docker --desktop --gpu lirios/unstable` |\n| [LXDE](https://github.com/mviereck/dockerfile-x11docker-lxde) | `x11docker --desktop x11docker/lxde` |\n| [LXDE with wine and PlayOnLinux](https://github.com/mviereck/dockerfile-x11docker-lxde-wine) and  \na persistent `HOME` folder to preserve  \ninstalled Windows applications,  \nand with Pulseaudio sound. | `x11docker --desktop --home --pulseaudio x11docker/lxde-wine` |\n| [LXQt](https://github.com/mviereck/dockerfile-x11docker-lxqt) | `x11docker --desktop x11docker/lxqt` |\n| [Mate](https://github.com/mviereck/dockerfile-x11docker-mate) | `x11docker --desktop x11docker/mate` |\n| [Trinity](https://github.com/mviereck/dockerfile-x11docker-trinity) ([website](https://www.trinitydesktop.org/)) (successor of KDE 3) | `x11docker --desktop x11docker/trinity` |\n| [Xfce](https://github.com/mviereck/dockerfile-x11docker-xfce) | `x11docker --desktop x11docker/xfce` |\n\n### Adjust images for your needs\n\n[](https://github.com/mviereck/x11docker?screenshot=true#adjust-images-for-your-needs)\n\nFor persistent changes of image system adjust Dockerfile and rebuild. To add custom applications to x11docker example images you can create a new Dockerfile based on them. Example:\n\n# xfce desktop with VLC media player\nFROM x11docker/xfce\nRUN apt-get update && apt-get install -y vlc\n\n### Screenshots\n\n[](https://github.com/mviereck/x11docker?screenshot=true#screenshots)\n\nMore screenshots are stored in [screenshot branch](https://github.com/mviereck/x11docker/tree/screenshots)\n\n`x11docker --desktop x11docker/lxqt` [![Image 40: screenshot](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-lxqt.png)](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-lxqt.png)\n\n`x11docker --desktop x11docker/lxde-wine` [![Image 41: screenshot](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-lxde-wine.png)](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-lxde-wine.png)\n\n`x11docker --desktop --gpu --init=systemd -- --cap-add=IPC_LOCK --security-opt seccomp=unconfined -- x11docker/deepin` [![Image 42: screenshot](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-deepin.png)](https://raw.githubusercontent.com/mviereck/x11docker/screenshots/screenshot-deepin.png)",
  "usage": {
    "tokens": 15167
  }
}
```
