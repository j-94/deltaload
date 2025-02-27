---
title: DDEV Installation - DDEV Docs
description: Do local website development on your computer or in the cloud with DDEV.
url: https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/
timestamp: 2025-01-20T16:04:25.143Z
domain: ddev.readthedocs.io
path: en_stable_users_install_ddev-installation
---

# DDEV Installation - DDEV Docs


Do local website development on your computer or in the cloud with DDEV.


## Content

[](https://github.com/ddev/ddev/blob/master/docs/content/users/install/ddev-installation.md "Edit this page")Once you’ve [installed a Docker provider](https://ddev.readthedocs.io/en/stable/users/install/docker-installation/), you’re ready to install DDEV!

macOSLinuxWindowsGitpodCodespacesManual

macOS[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#macos "Permanent link")
-------------------------------------------------------------------------------------------------------

### Homebrew[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#homebrew "Permanent link")

[Homebrew](https://brew.sh/) is the easiest and most reliable way to install and [upgrade](https://ddev.readthedocs.io/en/stable/users/install/ddev-upgrade/) DDEV:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-1)# Install DDEV
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-2)brewinstallddev/ddev/ddev
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-3)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-4)# One-time initialization of mkcert
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-5)mkcert-install
```

### Install Script[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#install-script "Permanent link")

The [install script](https://github.com/ddev/ddev/blob/master/scripts/install_ddev.sh) is another option. It downloads, verifies, and sets up the `ddev` executable:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-1-1)# Download and run the install script
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-1-2)curl-fsSLhttps://ddev.com/install.sh|bash
```

Do you still have an old version after installing or upgrading?If `ddev --version` still shows an older version than you installed or upgraded to, use `which -a ddev` to find out where another version of the `ddev` executable must be installed. See the [“Why Do I Have An Old DDEV” FAQ](https://ddev.readthedocs.io/en/stable/users/usage/faq/#why-do-i-have-an-old-ddev).

Need a specific version?Use the `-s` argument to specify a specific stable or prerelease version:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-2-1)# Download and run the script to install DDEV v1.23.5
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-2-2)curl-fsSLhttps://ddev.com/install.sh|bash-sv1.23.5
```

Linux[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#linux "Permanent link")
-------------------------------------------------------------------------------------------------------

### Debian/Ubuntu[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#debianubuntu "Permanent link")

DDEV’s Debian and RPM packages work with `apt` and `yum` repositories and most variants that use them, including Windows WSL2:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-1)# Add DDEV’s GPG key to your keyring
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-2)sudosh-c'echo ""'
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-3)sudoapt-getupdate&&sudoapt-getinstall-ycurl
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-4)sudoinstall-m0755-d/etc/apt/keyrings
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-5)curl-fsSLhttps://pkg.ddev.com/apt/gpg.key|gpg--dearmor|sudotee/etc/apt/keyrings/ddev.gpg>/dev/null
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-6)sudochmoda+r/etc/apt/keyrings/ddev.gpg
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-7)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-8)# Add DDEV releases to your package repository
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-9)sudosh-c'echo ""'
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-10)echo"deb [signed-by=/etc/apt/keyrings/ddev.gpg] https://pkg.ddev.com/apt/ * *"|sudotee/etc/apt/sources.list.d/ddev.list>/dev/null
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-11)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-12)# Update package information and install DDEV
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-13)sudosh-c'echo ""'
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-14)sudoapt-getupdate&&sudoapt-getinstall-yddev
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-15)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-16)# One-time initialization of mkcert
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-17)mkcert-install
```

(Some versions of Firefox (Developer Edition, Flatpak) may need some [extra work](https://github.com/FiloSottile/mkcert/issues/370#issuecomment-1280377305) with `mkcert`, see also [this issue](https://github.com/ddev/ddev/issues/5415).)

Do you still have an old version after installing or upgrading?If `ddev --version` still shows an older version than you installed or upgraded to, use `which -a ddev` to find out where another version of the `ddev` executable must be installed. See the [“Why Do I Have An Old DDEV” FAQ](https://ddev.readthedocs.io/en/stable/users/usage/faq/#why-do-i-have-an-old-ddev).

Need to remove a previously-installed variant?If you previously used DDEV’s [install script](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#install-script), you can remove that version:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-4-1)sudo rm -f /usr/local/bin/ddev /usr/local/bin/mkcert /usr/local/bin/*ddev_nfs_setup.sh
```

If you previously [installed DDEV with Homebrew](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#homebrew), you can run `brew unlink ddev` to get rid of the Homebrew version.

### Fedora, Red Hat, etc.[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#fedora-red-hat-etc "Permanent link")

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-1)# Add DDEV releases to your package repository
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-2)sudosh-c'echo ""'
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-3)echo'[ddev]
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-4)name=ddev
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-5)baseurl=https://pkg.ddev.com/yum/
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-6)gpgcheck=0
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-7)enabled=1'|perl-p-e's/^ +//'|sudotee/etc/yum.repos.d/ddev.repo>/dev/null
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-8)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-9)# Install DDEV
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-10)sudosh-c'echo ""'
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-11)sudodnfinstall--refreshddev
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-12)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-13)# One-time initialization of mkcert
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-14)mkcert-install
```

Signed yum repository support will be added in the future.

### Arch Linux[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#arch-linux "Permanent link")

We maintain the [ddev-bin](https://aur.archlinux.org/packages/ddev-bin/) package in AUR for Arch-based systems including Arch Linux, EndeavourOS and Manjaro. Install with `yay` or your AUR tool of choice.

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-1)# Install DDEV
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-2)yay-Sddev-bin
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-3)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-4)# One-time initialization of mkcert
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-5)mkcert-install
```

### Homebrew (AMD64 only)[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#homebrew-amd64-only "Permanent link")

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-1)# Install DDEV using Homebrew
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-2)brewinstallddev/ddev/ddev
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-3)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-4)# One-time initialization of mkcert
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-5)mkcert-install
```

### Install Script[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#install-script-linux "Permanent link")

The [install script](https://github.com/ddev/ddev/blob/master/scripts/install_ddev.sh) is another option. It downloads, verifies, and sets up the `ddev` executable:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-8-1)# Download and run the install script
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-8-2)curl-fsSLhttps://ddev.com/install.sh|bash
```

Need a specific version?Use the `-s` argument to specify a specific stable or prerelease version:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-9-1)# Download and run the script to install DDEV v1.23.5
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-9-2)curl-fsSLhttps://ddev.com/install.sh|bash-sv1.23.5
```
Do you still have an old version after installing or upgrading?If `ddev --version` still shows an older version than you installed or upgraded to, use `which -a ddev` to find out where another version of the `ddev` executable must be installed. See the [“Why Do I Have An Old DDEV” FAQ](https://ddev.readthedocs.io/en/stable/users/usage/faq/#why-do-i-have-an-old-ddev).

Windows[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#windows "Permanent link")
-----------------------------------------------------------------------------------------------------------

You can install DDEV on Windows three ways:

1.  [Using WSL2 with Docker inside](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2-docker-ce-inside-install-script) **Recommended, best performance, most reliable**
2.  [Using WSL2 with Docker Desktop](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2-docker-desktop-install-script) **May require license, less reliable**
3.  [Installing directly on traditional Windows](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#traditional-windows) with an installer **Legacy, slower performance**

**We strongly recommend using WSL2 for your Windows DDEV development environment.** While its Linux experience may be new for some Windows users, it’s worth the performance benefit and common experience of working with Ubuntu and Bash.

### Important Considerations for WSL2 and DDEV[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#important-considerations-for-wsl2-and-ddev "Permanent link")

*   You **must** use WSL2, not WSL version 1. Use `wsl.exe -l -v` to see the versions of the distros you are using they should be v2.
*   WSL2 is supported on Windows 10 and 11. All Windows 10/11 editions, including Windows 10 Home support WSL2.
*   WSL2 offers a faster, smoother experience.  
    It’s vastly more performant, and you’re less likely to have obscure Windows problems.
    
*   Execute DDEV commands inside WSL2.  
    You’ll want to run DDEV commands inside Ubuntu, for example, and never on the Windows side in PowerShell or Git Bash.
    
*   Projects should live under the home directory of the Linux filesystem.  
    WSL2’s Linux filesystem (e.g. `/home/<your_username>`) is much faster and has proper permissions, so keep your projects there and **not** in the slower Windows filesystem (`/mnt/c`).
*   Custom hostnames are managed via the Windows hosts file, not within WSL2.  
    DDEV attempts to manage custom hostnames via the Windows-side hosts file—usually at `C:\Windows\system32\drivers\etc\hosts`—and it can only do this if it’s installed on the Windows side. (DDEV inside WSL2 uses `ddev.exe` on the Windows side as a proxy to update the Windows hosts file.) If `ddev.exe --version` shows the same version as `ddev --version` you’re all set up. Otherwise, install DDEV on Windows using `choco upgrade -y ddev` or by downloading and running the Windows installer. (The WSL2 scripts below install DDEV on the Windows side, taking care of that for you.) If you frequently run into Windows UAC Escalation, you can calm it down by running `gsudo.exe cache on` and `gsudo.exe config CacheMode auto`, see [gsudo docs](https://github.com/gerardog/gsudo#credentials-cache).
*   WSL2 is not the same as Docker Desktop’s WSL2 engine.  
    Using WSL2 to install and run DDEV is not the same as using Docker Desktop’s WSL2 engine, which itself runs in WSL2, but can serve applications running in both traditional Windows and inside WSL2.

The WSL2 install process involves:

*   Installing Chocolatey package manager (optional).
*   One time initialization of mkcert.
*   Installing WSL2 and installing a distro like Ubuntu.
*   Optionally installing Docker Desktop for Windows and enabling WSL2 integration with the distro (if you’re using the Docker Desktop approach).
*   Installing DDEV inside your distro; this is normally done by running one of the two scripts below, but can be done manually step-by-step as well.
*   Verify that your distro uses WSL version 2 with `wsl.exe -l -v`.

### WSL2 + Docker CE Inside Install Script[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2-docker-ce-inside-install-script "Permanent link")

This technique is our favorite, as it uses the most reliable WSL2 Docker provider (`docker-ce`), which is also free and open-source.

This script prepares your default WSL2 Ubuntu distro and doesn’t require Docker Desktop, and you can run the script multiple times without breaking anything.

In all cases:

1.  Install WSL2 with an Ubuntu distro.
    
    *   Install WSL:
        
    *   Reboot if required. (Usually required.)
        
    *   Verify that you have an Ubuntu distro set as default by running `wsl.exe -l -v`.  
        If you have WSL2 but not an Ubuntu distro, install one by running `wsl.exe --install Ubuntu`. If this doesn’t work, see [manual installation](https://docs.microsoft.com/en-us/windows/wsl/install-manual) and [troubleshooting](https://docs.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues).
        
    *   Verify that your Ubuntu default distro is WSL v2 using `wsl -l -v`.
        
2.  In an administrative PowerShell run [this PowerShell script](https://raw.githubusercontent.com/ddev/ddev/master/scripts/install_ddev_wsl2_docker_inside.ps1) by executing:
    
    ```
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-11-1)Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-11-2)iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/ddev/ddev/master/scripts/install_ddev_wsl2_docker_inside.ps1'))
    ```
    
3.  In _Windows Update Settings_ → _Advanced Options_ enable _Receive updates for other Microsoft products_. You may want to occasionally run `wsl.exe --update` as well.
    

Now you can use the “Ubuntu” terminal app or Windows Terminal to access your Ubuntu distro, which has DDEV and Docker working inside it.

### WSL2 + Docker Desktop Install Script[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2-docker-desktop-install-script "Permanent link")

WSL2 with Docker Desktop is a less-favored choice because Docker Desktop may be lightly supported, and has many features not required for use with DDEV that do not add particular value. It is also not free software (although smaller organizations can use it free of charge) and it is not open-source.

The script here prepares your default WSL2 Ubuntu distro for use with Docker Desktop, and you can run the script multiple times without breaking anything.

In all cases:

1.  Install WSL2 with an Ubuntu distro. On a system without WSL2, run:
    
    *   Verify that you have an Ubuntu distro set as the default default with `wsl -l -v`.
        
    *   If you have WSL2 but not an Ubuntu distro, install one with `wsl --install Ubuntu`.  
        If that doesn’t work for you, see [manual installation](https://docs.microsoft.com/en-us/windows/wsl/install-manual) and [troubleshooting](https://docs.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues).
        
    
    If you prefer to use another Ubuntu distro, install it and set it as default. For example, `wsl --set-default Ubuntu-24.04`.
    
2.  In _Windows Update Settings_ → _Advanced Options_ enable _Receive updates for other Microsoft products_. You may want to occasionally run `wsl.exe --update` as well.
    
3.  Install Docker Desktop. If you already have Chocolatey, run `choco install -y docker-desktop`. Otherwise [download Docker Desktop from Docker](https://www.docker.com/products/docker-desktop/).
    
4.  Start Docker Desktop. You should now be able to run `docker ps` in PowerShell or Git Bash.
5.  In _Docker Desktop_ → _Settings_ → _Resources_ → _WSL2 Integration_, verify that Docker Desktop is integrated with your distro.
6.  In an administrative PowerShell run [this PowerShell script](https://raw.githubusercontent.com/ddev/ddev/master/scripts/install_ddev_wsl2_docker_desktop.ps1) by executing:
    
    ```
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-13-1)Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-13-2)iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/ddev/ddev/master/scripts/install_ddev_wsl2_docker_desktop.ps1'))
    ```
    

Now you can use the “Ubuntu” terminal app or Windows Terminal to access your Ubuntu distro, which has DDEV and Docker Desktop integrated with it.

### WSL2/Docker Desktop Manual Installation[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2docker-desktop-manual-installation "Permanent link")

You can manually step through the process the install script attempts to automate:

1.  Install [Chocolatey](https://chocolatey.org/install):
    
    ```
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-14-1)Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-14-2)iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`
    ```
    
2.  In an administrative PowerShell, run `choco install -y ddev mkcert`.
3.  In an administrative PowerShell, run `mkcert -install` and follow the prompt to install the Certificate Authority.
4.  In an administrative PowerShell, run `$env:CAROOT="$(mkcert -CAROOT)"; setx CAROOT $env:CAROOT; If ($Env:WSLENV -notlike "*CAROOT/up:*") { $env:WSLENV="CAROOT/up:$env:WSLENV"; setx WSLENV $Env:WSLENV }`. This will set WSL2 to use the Certificate Authority installed on the Windows side. In some cases it takes a reboot to work correctly.
5.  In administrative PowerShell, run `wsl --install`. This will install WSL2 and Ubuntu for you. Reboot when this is done.
6.  **Docker Desktop for Windows:** If you already have the latest Docker Desktop, configure it in the General Settings to use the WSL2-based engine. Otherwise install the latest Docker Desktop for Windows and select the WSL2-based engine (not legacy Hyper-V) when installing. Install with Chocolatey by running `choco install docker-desktop`, or download the installer from [desktop.docker.com](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe). Start Docker. It may prompt you to log out and log in again, or reboot.
7.  Go to Docker Desktop’s _Settings_ → _Resources_ → _WSL integration_ → _enable integration for your distro_. Now `docker` commands will be available from within your WSL2 distro.
8.  Double-check in PowerShell: `wsl -l -v` should show three distros, and your Ubuntu should be the default. All three should be WSL version 2.
9.  Double-check in Ubuntu (or your distro): `echo $CAROOT` should show something like `/mnt/c/Users/<you>/AppData/Local/mkcert`
10.  Check that Docker is working inside Ubuntu (or your distro) by running `docker ps`.
11.  Open the WSL2 terminal, for example `Ubuntu` from the Windows start menu.
12.  Install DDEV:
    
    ```
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-1)sudoapt-getupdate&&sudoapt-getinstall-ycurl
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-2)sudoinstall-m0755-d/etc/apt/keyrings
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-3)curl-fsSLhttps://pkg.ddev.com/apt/gpg.key|gpg--dearmor|sudotee/etc/apt/keyrings/ddev.gpg>/dev/null
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-4)echo"deb [signed-by=/etc/apt/keyrings/ddev.gpg] https://pkg.ddev.com/apt/ * *"|sudotee/etc/apt/sources.list.d/ddev.list>/dev/null
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-5)sudoapt-getupdate&&sudoapt-getinstall-yddev
    ```
    
13.  In WSL2, run `mkcert -install`.
    

You have now installed DDEV on WSL2. If you’re using WSL2 for DDEV, remember to run all `ddev` commands inside the WSL2 distro.

Path to certificates

If you get the prompt `Installing to the system store is not yet supported on this Linux`, you may need to add `/usr/sbin` to the `$PATH` so that `/usr/sbin/update-ca-certificates` can be found.

### Traditional Windows[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#traditional-windows "Permanent link")

If you must use traditional Windows, then Docker Desktop is your only choice of a Docker provider. DDEV is supported in this configuration but it’s not as performant as the WSL2 options.

*   We recommend using [Chocolatey](https://chocolatey.org/). Once installed, you can run `choco install ddev docker-desktop git` from an administrative shell. You can upgrade by running `ddev poweroff && choco upgrade ddev`.
*   Each [DDEV release](https://github.com/ddev/ddev/releases) includes Windows installers for AMD64 and ARM64 Windows (`ddev_windows_<architecture>_installer.<version>.exe`). After running that, you can open a new Git Bash, PowerShell, or cmd.exe window and start using DDEV.

Most people interact with DDEV on traditional Windows using Git Bash, part of the [Windows Git suite](https://git-scm.com/download/win). Although DDEV does work with cmd.exe and PowerShell, it’s more at home in Bash. You can install Git Bash with Chocolatey by running `choco install -y git`.

Windows Firefox Trusted CA

The `mkcert -install` step on Windows isn’t enough for Firefox. You need to add the created root certificate authority to the security configuration yourself:

*   Run `mkcert -install` (you can use the shortcut from the Start Menu for that)
*   Run `mkcert -CAROOT` to see the local folder used for the newly-created root certificate authority
*   Open Firefox Preferences (`about:preferences#privacy`)
*   Enter “certificates” into the search box on the top
*   Click _View Certificates…_
*   Select _Authorities_ tab
*   Click to _Import…_
*   Navigate to the folder where your root certificate authority was stored
*   Select the `rootCA.pem` file
*   Click to _Open_

You should now see your CA under `mkcert development CA`.

Gitpod[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#gitpod "Permanent link")
---------------------------------------------------------------------------------------------------------

Choose any of the following methods to launch your project with [Gitpod](https://www.gitpod.io/):

1.  Add a [.gitpod.yml](https://www.gitpod.io/docs/references/gitpod-yml) to your project that installs DDEV and starts your project. The easy way to do this is with the excellent [ddev-gitpod-setup](https://github.com/tyler36/ddev-gitpod-setup) add-on. `ddev get tyler36/ddev-gitpod-setup` and add it to your git repository, push it, and then open it. You can even do all of this right on gitpod by opening your repository, doing the `ddev get` there and then pushing it back and restarting.
2.  [Open any repository](https://www.gitpod.io/docs/getting-started) using Gitpod and run the following:
    
    ```
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-1)# Add DDEV’s GPG key to your keyring
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-2)curl-fsSLhttps://pkg.ddev.com/apt/gpg.key|gpg--dearmor|sudotee/etc/apt/keyrings/ddev.gpg>/dev/null
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-3)
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-4)# Add DDEV releases to your package repository
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-5)echo"deb [signed-by=/etc/apt/keyrings/ddev.gpg] https://pkg.ddev.com/apt/ * *"|sudotee/etc/apt/sources.list.d/ddev.list>/dev/null
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-6)
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-7)
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-8)# Update package information and install DDEV
    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-9)sudoapt-getupdate&&sudoapt-getinstall-yddev
    ```
    
    *   You can install your web app there, or import a database.
    *   You may want to implement one of the `ddev pull` provider integrations to pull from a hosting provider or an upstream source.
3.  Use the [ddev-gitpod-launcher](https://ddev.github.io/ddev-gitpod-launcher/) form to launch a repository. You’ll provide a source repository and click a button to open a newly-established environment. You can specify a companion artifacts repository and automatically load `db.sql.gz` and `files.tgz` from it. (More details in the [repository’s README](https://github.com/ddev/ddev-gitpod-launcher/blob/main/README.md).)
    
4.  Save the following link to your bookmark bar: Open in ddev-gitpod. It’s easiest to drag the link into your bookmarks. When you’re on a Git repository, click the bookmark to open it with DDEV in Gitpod. It does the same thing as the second option, but it works on non-Chrome browsers and you can use native browser keyboard shortcuts.

It can be complicated to get private databases and files into Gitpod, so in addition to the launchers, the [`git` provider example](https://github.com/ddev/ddev/blob/master/pkg/ddevapp/dotddev_assets/providers/git.yaml.example) demonstrates pulling a database and files without complex setup or permissions. This was created explicitly for Gitpod integration, because in Gitpod you typically already have access to private Git repositories, which are a fine place to put a starter database and files. Although [ddev-gitpod-launcher](https://ddev.github.io/ddev-gitpod-launcher/) and the web extension provide the capability, you may want to integrate a Git provider—or one of the [other providers](https://github.com/ddev/ddev/tree/master/pkg/ddevapp/dotddev_assets/providers)—for each project.

GitHub Codespaces[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#github-codespaces "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------

You can use DDEV in remote [GitHub Codespaces](https://github.com/features/codespaces) without having to run Docker locally; you only need a browser and an internet connection.

Start by creating a `.devcontainer/devcontainer.json` file in your GitHub repository:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-1){
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-2)"image":"mcr.microsoft.com/devcontainers/universal:2",
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-3)"features":{
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-4)"ghcr.io/ddev/ddev/install-ddev:latest":{}
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-5)},
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-6)"postCreateCommand":"echo 'it should all be set up'"
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-7)}
```

Launch your repository in Codespaces:

![Image 9: Screenshot of codespace create dialog in a repository on GitHub](https://ddev.readthedocs.io/en/stable/images/codespaces-launch.png)

![Image 10: Screenshot of codespace create dialog in a repository on GitHub](https://ddev.readthedocs.io/en/stable/images/codespaces-setting-up.png)

DDEV is now available within your new codespace instance:

![Image 11](https://ddev.readthedocs.io/en/stable/images/codespaces-hello-screen.png)

Run `ddev config` to [start a new blank project](https://ddev.readthedocs.io/en/stable/users/project/) - or [install a CMS](https://ddev.readthedocs.io/en/stable/users/quickstart/).

Run `ddev start` if there is already a configured DDEV project in your repository.

**Troubleshooting**:

If there are errors after restarting a codespace, use `ddev restart` or `ddev poweroff`.

You can also use the commands

*   “Codespaces: Rebuild container”
*   “Codespaces: Full rebuild container” (Beware: database will be deleted)

via the [Visual Studio Code Command Palette](https://docs.github.com/en/enterprise-cloud@latest/codespaces/codespaces-reference/using-the-vs-code-command-palette-in-codespaces):

*   ⌘ + SHIFT + P on a Mac
*   CTRL + SHIFT + P on Windows/Linux
*   from the Application Menu, click View \> Command Palette (Firefox)

If you need DDEV-specific assistance or have further questions, see [support](https://ddev.readthedocs.io/en/stable/users/support/).

Your updated `devcontainer.json` file may differ depending on your project, but you should have `install-ddev` in the `features` section.

Normal Linux installation also works

You can also install DDEV as if it were on any normal [Linux installation](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#linux).

### Docker integration[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#docker-integration "Permanent link")

DDEV in Codespaces relies on [`docker-in-docker`](https://github.com/devcontainers/features), which is installed by default when you use the image `"mcr.microsoft.com/devcontainers/universal:2"`. Please be aware: GitHub Codespaces and its Docker-integration (docker-in-docker) are relatively new. See [devcontainers/features](https://github.com/devcontainers/features) for general support and issues regarding Docker-support.

### DDEV’s router is not used[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#ddevs-router-is-not-used "Permanent link")

Since Codespaces handles all the routing, the internal DDEV router will not be used on Codespaces. Therefore config settings like [`web_extra_exposed_ports`](https://ddev.readthedocs.io/en/stable/users/configuration/config/#web_extra_exposed_ports) will have no effect.

You can expose ports via the `ports` setting, which is usually not recommended if you work locally due to port conflicts. But you can load these additional Docker compose files only when Codespaces is detected. See [Defining Additional Services](https://ddev.readthedocs.io/en/stable/users/extend/custom-compose-files/#docker-composeyaml-examples) for more information.

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-18-1)services:
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-18-2)web:
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-18-3)ports:
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-18-4)-"5174:5174"
```

### Default environment variables[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#default-environment-variables "Permanent link")

Codespace instances already provide some [default environment values](https://docs.github.com/en/codespaces/developing-in-codespaces/default-environment-variables-for-your-codespace). You can inherit and inject them in your `.ddev/config.yaml`:

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-19-1)web_environment:
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-19-2)-CODESPACES
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-19-3)-CODESPACE_NAME
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-19-4)-GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN
```

### Advanced usage via devcontainer.json[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#advanced-usage-via-devcontainerjson "Permanent link")

A lot more customization is possible via the [`devcontainer.json`\-configuration](https://containers.dev/implementors/json_reference/). You can install Visual Studio Code extensions by default or run commands automatically.

#### postCreateCommand[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#postcreatecommand "Permanent link")

The [`postCreateCommand`](https://containers.dev/implementors/json_reference/) lets you run commands automatically when a new codespace is launched. DDEV commands are available here.

The event is triggered on: fresh creation, rebuilds and full rebuilds. `ddev poweroff` is used in this example to avoid errors on rebuilds since some Docker containers are kept.

You usually want to use a separate bash script to do this, as docker [might not yet be available when the command starts to run](https://github.com/devcontainers/features/issues/780).

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-1){
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-2)"image":"mcr.microsoft.com/devcontainers/universal:2",
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-3)"features":{
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-4)"ghcr.io/ddev/ddev/install-ddev:latest":{}
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-5)},
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-6)"portsAttributes":{
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-7)"3306":{
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-8)"label":"database"
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-9)},
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-10)"8027":{
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-11)"label":"mailpit"
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-12)},
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-13)"8080":{
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-14)"label":"web http"
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-15)},
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-16)"8443":{
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-17)"label":"web https"
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-18)}
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-19)},
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-20)"postCreateCommand":"bash .devcontainer/setup_project.sh"
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-21)}
```

```
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-1)#!/usr/bin/env bash
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-2)set-ex
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-3)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-4)wait_for_docker(){
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-5)whiletrue;do
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-6)dockerps>/dev/null2>&1&&break
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-7)sleep1
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-8)done
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-9)echo"Docker is ready."
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-10)}
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-11)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-12)wait_for_docker
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-13)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-14)# download images beforehand, optional
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-15)ddevdebugdownload-images
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-16)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-17)# avoid errors on rebuilds
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-18)ddevpoweroff
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-19)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-20)# start ddev project automatically
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-21)ddevstart-y
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-22)
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-23)# further automated install / setup steps, e.g. 
[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-24)ddevcomposerinstall
```

To check for errors during the `postCreateCommand` action, use the command

*   “Codespaces: View creation log”

via the [Visual Studio Code Command Palette](https://docs.github.com/en/enterprise-cloud@latest/codespaces/codespaces-reference/using-the-vs-code-command-palette-in-codespaces):

*   ⌘ + SHIFT + P on a Mac
*   CTRL + SHIFT + P on Windows/Linux
*   from the Application Menu, click View \> Command Palette (Firefox)

![Image 12](https://ddev.readthedocs.io/en/stable/images/codespaces-creation-log.png)

Manual[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#manual "Permanent link")
---------------------------------------------------------------------------------------------------------

DDEV is a single executable, so installation on any OS is a matter of copying the `ddev` executable for your architecture into the appropriate system path on your machine.

*   Download and extract the latest [DDEV release](https://github.com/ddev/ddev/releases) for your architecture.
*   Move `ddev` to `/usr/local/bin` with `mv ddev /usr/local/bin/` (may require `sudo`), or another directory in your `$PATH` as preferred.
*   Run `ddev` to test your installation. You should see DDEV’s command usage output.
*   As a one-time initialization, run `mkcert -install`, which may require your `sudo` password.
    
    If you don’t have `mkcert` installed, download the [latest release](https://github.com/FiloSottile/mkcert/releases) for your architecture and `sudo mv <downloaded_file> /usr/local/bin/mkcert && sudo chmod +x /usr/local/bin/mkcert`.

## Metadata

```json
{
  "title": "DDEV Installation - DDEV Docs",
  "description": "Do local website development on your computer or in the cloud with DDEV.",
  "url": "https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/",
  "content": "[](https://github.com/ddev/ddev/blob/master/docs/content/users/install/ddev-installation.md \"Edit this page\")Once you’ve [installed a Docker provider](https://ddev.readthedocs.io/en/stable/users/install/docker-installation/), you’re ready to install DDEV!\n\nmacOSLinuxWindowsGitpodCodespacesManual\n\nmacOS[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#macos \"Permanent link\")\n-------------------------------------------------------------------------------------------------------\n\n### Homebrew[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#homebrew \"Permanent link\")\n\n[Homebrew](https://brew.sh/) is the easiest and most reliable way to install and [upgrade](https://ddev.readthedocs.io/en/stable/users/install/ddev-upgrade/) DDEV:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-1)# Install DDEV\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-2)brewinstallddev/ddev/ddev\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-3)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-4)# One-time initialization of mkcert\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-0-5)mkcert-install\n```\n\n### Install Script[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#install-script \"Permanent link\")\n\nThe [install script](https://github.com/ddev/ddev/blob/master/scripts/install_ddev.sh) is another option. It downloads, verifies, and sets up the `ddev` executable:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-1-1)# Download and run the install script\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-1-2)curl-fsSLhttps://ddev.com/install.sh|bash\n```\n\nDo you still have an old version after installing or upgrading?If `ddev --version` still shows an older version than you installed or upgraded to, use `which -a ddev` to find out where another version of the `ddev` executable must be installed. See the [“Why Do I Have An Old DDEV” FAQ](https://ddev.readthedocs.io/en/stable/users/usage/faq/#why-do-i-have-an-old-ddev).\n\nNeed a specific version?Use the `-s` argument to specify a specific stable or prerelease version:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-2-1)# Download and run the script to install DDEV v1.23.5\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-2-2)curl-fsSLhttps://ddev.com/install.sh|bash-sv1.23.5\n```\n\nLinux[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#linux \"Permanent link\")\n-------------------------------------------------------------------------------------------------------\n\n### Debian/Ubuntu[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#debianubuntu \"Permanent link\")\n\nDDEV’s Debian and RPM packages work with `apt` and `yum` repositories and most variants that use them, including Windows WSL2:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-1)# Add DDEV’s GPG key to your keyring\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-2)sudosh-c'echo \"\"'\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-3)sudoapt-getupdate&&sudoapt-getinstall-ycurl\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-4)sudoinstall-m0755-d/etc/apt/keyrings\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-5)curl-fsSLhttps://pkg.ddev.com/apt/gpg.key|gpg--dearmor|sudotee/etc/apt/keyrings/ddev.gpg>/dev/null\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-6)sudochmoda+r/etc/apt/keyrings/ddev.gpg\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-7)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-8)# Add DDEV releases to your package repository\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-9)sudosh-c'echo \"\"'\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-10)echo\"deb [signed-by=/etc/apt/keyrings/ddev.gpg] https://pkg.ddev.com/apt/ * *\"|sudotee/etc/apt/sources.list.d/ddev.list>/dev/null\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-11)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-12)# Update package information and install DDEV\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-13)sudosh-c'echo \"\"'\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-14)sudoapt-getupdate&&sudoapt-getinstall-yddev\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-15)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-16)# One-time initialization of mkcert\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-3-17)mkcert-install\n```\n\n(Some versions of Firefox (Developer Edition, Flatpak) may need some [extra work](https://github.com/FiloSottile/mkcert/issues/370#issuecomment-1280377305) with `mkcert`, see also [this issue](https://github.com/ddev/ddev/issues/5415).)\n\nDo you still have an old version after installing or upgrading?If `ddev --version` still shows an older version than you installed or upgraded to, use `which -a ddev` to find out where another version of the `ddev` executable must be installed. See the [“Why Do I Have An Old DDEV” FAQ](https://ddev.readthedocs.io/en/stable/users/usage/faq/#why-do-i-have-an-old-ddev).\n\nNeed to remove a previously-installed variant?If you previously used DDEV’s [install script](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#install-script), you can remove that version:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-4-1)sudo rm -f /usr/local/bin/ddev /usr/local/bin/mkcert /usr/local/bin/*ddev_nfs_setup.sh\n```\n\nIf you previously [installed DDEV with Homebrew](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#homebrew), you can run `brew unlink ddev` to get rid of the Homebrew version.\n\n### Fedora, Red Hat, etc.[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#fedora-red-hat-etc \"Permanent link\")\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-1)# Add DDEV releases to your package repository\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-2)sudosh-c'echo \"\"'\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-3)echo'[ddev]\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-4)name=ddev\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-5)baseurl=https://pkg.ddev.com/yum/\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-6)gpgcheck=0\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-7)enabled=1'|perl-p-e's/^ +//'|sudotee/etc/yum.repos.d/ddev.repo>/dev/null\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-8)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-9)# Install DDEV\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-10)sudosh-c'echo \"\"'\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-11)sudodnfinstall--refreshddev\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-12)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-13)# One-time initialization of mkcert\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-5-14)mkcert-install\n```\n\nSigned yum repository support will be added in the future.\n\n### Arch Linux[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#arch-linux \"Permanent link\")\n\nWe maintain the [ddev-bin](https://aur.archlinux.org/packages/ddev-bin/) package in AUR for Arch-based systems including Arch Linux, EndeavourOS and Manjaro. Install with `yay` or your AUR tool of choice.\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-1)# Install DDEV\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-2)yay-Sddev-bin\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-3)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-4)# One-time initialization of mkcert\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-6-5)mkcert-install\n```\n\n### Homebrew (AMD64 only)[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#homebrew-amd64-only \"Permanent link\")\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-1)# Install DDEV using Homebrew\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-2)brewinstallddev/ddev/ddev\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-3)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-4)# One-time initialization of mkcert\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-7-5)mkcert-install\n```\n\n### Install Script[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#install-script-linux \"Permanent link\")\n\nThe [install script](https://github.com/ddev/ddev/blob/master/scripts/install_ddev.sh) is another option. It downloads, verifies, and sets up the `ddev` executable:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-8-1)# Download and run the install script\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-8-2)curl-fsSLhttps://ddev.com/install.sh|bash\n```\n\nNeed a specific version?Use the `-s` argument to specify a specific stable or prerelease version:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-9-1)# Download and run the script to install DDEV v1.23.5\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-9-2)curl-fsSLhttps://ddev.com/install.sh|bash-sv1.23.5\n```\nDo you still have an old version after installing or upgrading?If `ddev --version` still shows an older version than you installed or upgraded to, use `which -a ddev` to find out where another version of the `ddev` executable must be installed. See the [“Why Do I Have An Old DDEV” FAQ](https://ddev.readthedocs.io/en/stable/users/usage/faq/#why-do-i-have-an-old-ddev).\n\nWindows[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#windows \"Permanent link\")\n-----------------------------------------------------------------------------------------------------------\n\nYou can install DDEV on Windows three ways:\n\n1.  [Using WSL2 with Docker inside](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2-docker-ce-inside-install-script) **Recommended, best performance, most reliable**\n2.  [Using WSL2 with Docker Desktop](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2-docker-desktop-install-script) **May require license, less reliable**\n3.  [Installing directly on traditional Windows](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#traditional-windows) with an installer **Legacy, slower performance**\n\n**We strongly recommend using WSL2 for your Windows DDEV development environment.** While its Linux experience may be new for some Windows users, it’s worth the performance benefit and common experience of working with Ubuntu and Bash.\n\n### Important Considerations for WSL2 and DDEV[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#important-considerations-for-wsl2-and-ddev \"Permanent link\")\n\n*   You **must** use WSL2, not WSL version 1. Use `wsl.exe -l -v` to see the versions of the distros you are using they should be v2.\n*   WSL2 is supported on Windows 10 and 11. All Windows 10/11 editions, including Windows 10 Home support WSL2.\n*   WSL2 offers a faster, smoother experience.  \n    It’s vastly more performant, and you’re less likely to have obscure Windows problems.\n    \n*   Execute DDEV commands inside WSL2.  \n    You’ll want to run DDEV commands inside Ubuntu, for example, and never on the Windows side in PowerShell or Git Bash.\n    \n*   Projects should live under the home directory of the Linux filesystem.  \n    WSL2’s Linux filesystem (e.g. `/home/<your_username>`) is much faster and has proper permissions, so keep your projects there and **not** in the slower Windows filesystem (`/mnt/c`).\n*   Custom hostnames are managed via the Windows hosts file, not within WSL2.  \n    DDEV attempts to manage custom hostnames via the Windows-side hosts file—usually at `C:\\Windows\\system32\\drivers\\etc\\hosts`—and it can only do this if it’s installed on the Windows side. (DDEV inside WSL2 uses `ddev.exe` on the Windows side as a proxy to update the Windows hosts file.) If `ddev.exe --version` shows the same version as `ddev --version` you’re all set up. Otherwise, install DDEV on Windows using `choco upgrade -y ddev` or by downloading and running the Windows installer. (The WSL2 scripts below install DDEV on the Windows side, taking care of that for you.) If you frequently run into Windows UAC Escalation, you can calm it down by running `gsudo.exe cache on` and `gsudo.exe config CacheMode auto`, see [gsudo docs](https://github.com/gerardog/gsudo#credentials-cache).\n*   WSL2 is not the same as Docker Desktop’s WSL2 engine.  \n    Using WSL2 to install and run DDEV is not the same as using Docker Desktop’s WSL2 engine, which itself runs in WSL2, but can serve applications running in both traditional Windows and inside WSL2.\n\nThe WSL2 install process involves:\n\n*   Installing Chocolatey package manager (optional).\n*   One time initialization of mkcert.\n*   Installing WSL2 and installing a distro like Ubuntu.\n*   Optionally installing Docker Desktop for Windows and enabling WSL2 integration with the distro (if you’re using the Docker Desktop approach).\n*   Installing DDEV inside your distro; this is normally done by running one of the two scripts below, but can be done manually step-by-step as well.\n*   Verify that your distro uses WSL version 2 with `wsl.exe -l -v`.\n\n### WSL2 + Docker CE Inside Install Script[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2-docker-ce-inside-install-script \"Permanent link\")\n\nThis technique is our favorite, as it uses the most reliable WSL2 Docker provider (`docker-ce`), which is also free and open-source.\n\nThis script prepares your default WSL2 Ubuntu distro and doesn’t require Docker Desktop, and you can run the script multiple times without breaking anything.\n\nIn all cases:\n\n1.  Install WSL2 with an Ubuntu distro.\n    \n    *   Install WSL:\n        \n    *   Reboot if required. (Usually required.)\n        \n    *   Verify that you have an Ubuntu distro set as default by running `wsl.exe -l -v`.  \n        If you have WSL2 but not an Ubuntu distro, install one by running `wsl.exe --install Ubuntu`. If this doesn’t work, see [manual installation](https://docs.microsoft.com/en-us/windows/wsl/install-manual) and [troubleshooting](https://docs.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues).\n        \n    *   Verify that your Ubuntu default distro is WSL v2 using `wsl -l -v`.\n        \n2.  In an administrative PowerShell run [this PowerShell script](https://raw.githubusercontent.com/ddev/ddev/master/scripts/install_ddev_wsl2_docker_inside.ps1) by executing:\n    \n    ```\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-11-1)Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-11-2)iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/ddev/ddev/master/scripts/install_ddev_wsl2_docker_inside.ps1'))\n    ```\n    \n3.  In _Windows Update Settings_ → _Advanced Options_ enable _Receive updates for other Microsoft products_. You may want to occasionally run `wsl.exe --update` as well.\n    \n\nNow you can use the “Ubuntu” terminal app or Windows Terminal to access your Ubuntu distro, which has DDEV and Docker working inside it.\n\n### WSL2 + Docker Desktop Install Script[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2-docker-desktop-install-script \"Permanent link\")\n\nWSL2 with Docker Desktop is a less-favored choice because Docker Desktop may be lightly supported, and has many features not required for use with DDEV that do not add particular value. It is also not free software (although smaller organizations can use it free of charge) and it is not open-source.\n\nThe script here prepares your default WSL2 Ubuntu distro for use with Docker Desktop, and you can run the script multiple times without breaking anything.\n\nIn all cases:\n\n1.  Install WSL2 with an Ubuntu distro. On a system without WSL2, run:\n    \n    *   Verify that you have an Ubuntu distro set as the default default with `wsl -l -v`.\n        \n    *   If you have WSL2 but not an Ubuntu distro, install one with `wsl --install Ubuntu`.  \n        If that doesn’t work for you, see [manual installation](https://docs.microsoft.com/en-us/windows/wsl/install-manual) and [troubleshooting](https://docs.microsoft.com/en-us/windows/wsl/troubleshooting#installation-issues).\n        \n    \n    If you prefer to use another Ubuntu distro, install it and set it as default. For example, `wsl --set-default Ubuntu-24.04`.\n    \n2.  In _Windows Update Settings_ → _Advanced Options_ enable _Receive updates for other Microsoft products_. You may want to occasionally run `wsl.exe --update` as well.\n    \n3.  Install Docker Desktop. If you already have Chocolatey, run `choco install -y docker-desktop`. Otherwise [download Docker Desktop from Docker](https://www.docker.com/products/docker-desktop/).\n    \n4.  Start Docker Desktop. You should now be able to run `docker ps` in PowerShell or Git Bash.\n5.  In _Docker Desktop_ → _Settings_ → _Resources_ → _WSL2 Integration_, verify that Docker Desktop is integrated with your distro.\n6.  In an administrative PowerShell run [this PowerShell script](https://raw.githubusercontent.com/ddev/ddev/master/scripts/install_ddev_wsl2_docker_desktop.ps1) by executing:\n    \n    ```\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-13-1)Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-13-2)iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/ddev/ddev/master/scripts/install_ddev_wsl2_docker_desktop.ps1'))\n    ```\n    \n\nNow you can use the “Ubuntu” terminal app or Windows Terminal to access your Ubuntu distro, which has DDEV and Docker Desktop integrated with it.\n\n### WSL2/Docker Desktop Manual Installation[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#wsl2docker-desktop-manual-installation \"Permanent link\")\n\nYou can manually step through the process the install script attempts to automate:\n\n1.  Install [Chocolatey](https://chocolatey.org/install):\n    \n    ```\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-14-1)Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-14-2)iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`\n    ```\n    \n2.  In an administrative PowerShell, run `choco install -y ddev mkcert`.\n3.  In an administrative PowerShell, run `mkcert -install` and follow the prompt to install the Certificate Authority.\n4.  In an administrative PowerShell, run `$env:CAROOT=\"$(mkcert -CAROOT)\"; setx CAROOT $env:CAROOT; If ($Env:WSLENV -notlike \"*CAROOT/up:*\") { $env:WSLENV=\"CAROOT/up:$env:WSLENV\"; setx WSLENV $Env:WSLENV }`. This will set WSL2 to use the Certificate Authority installed on the Windows side. In some cases it takes a reboot to work correctly.\n5.  In administrative PowerShell, run `wsl --install`. This will install WSL2 and Ubuntu for you. Reboot when this is done.\n6.  **Docker Desktop for Windows:** If you already have the latest Docker Desktop, configure it in the General Settings to use the WSL2-based engine. Otherwise install the latest Docker Desktop for Windows and select the WSL2-based engine (not legacy Hyper-V) when installing. Install with Chocolatey by running `choco install docker-desktop`, or download the installer from [desktop.docker.com](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe). Start Docker. It may prompt you to log out and log in again, or reboot.\n7.  Go to Docker Desktop’s _Settings_ → _Resources_ → _WSL integration_ → _enable integration for your distro_. Now `docker` commands will be available from within your WSL2 distro.\n8.  Double-check in PowerShell: `wsl -l -v` should show three distros, and your Ubuntu should be the default. All three should be WSL version 2.\n9.  Double-check in Ubuntu (or your distro): `echo $CAROOT` should show something like `/mnt/c/Users/<you>/AppData/Local/mkcert`\n10.  Check that Docker is working inside Ubuntu (or your distro) by running `docker ps`.\n11.  Open the WSL2 terminal, for example `Ubuntu` from the Windows start menu.\n12.  Install DDEV:\n    \n    ```\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-1)sudoapt-getupdate&&sudoapt-getinstall-ycurl\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-2)sudoinstall-m0755-d/etc/apt/keyrings\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-3)curl-fsSLhttps://pkg.ddev.com/apt/gpg.key|gpg--dearmor|sudotee/etc/apt/keyrings/ddev.gpg>/dev/null\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-4)echo\"deb [signed-by=/etc/apt/keyrings/ddev.gpg] https://pkg.ddev.com/apt/ * *\"|sudotee/etc/apt/sources.list.d/ddev.list>/dev/null\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-15-5)sudoapt-getupdate&&sudoapt-getinstall-yddev\n    ```\n    \n13.  In WSL2, run `mkcert -install`.\n    \n\nYou have now installed DDEV on WSL2. If you’re using WSL2 for DDEV, remember to run all `ddev` commands inside the WSL2 distro.\n\nPath to certificates\n\nIf you get the prompt `Installing to the system store is not yet supported on this Linux`, you may need to add `/usr/sbin` to the `$PATH` so that `/usr/sbin/update-ca-certificates` can be found.\n\n### Traditional Windows[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#traditional-windows \"Permanent link\")\n\nIf you must use traditional Windows, then Docker Desktop is your only choice of a Docker provider. DDEV is supported in this configuration but it’s not as performant as the WSL2 options.\n\n*   We recommend using [Chocolatey](https://chocolatey.org/). Once installed, you can run `choco install ddev docker-desktop git` from an administrative shell. You can upgrade by running `ddev poweroff && choco upgrade ddev`.\n*   Each [DDEV release](https://github.com/ddev/ddev/releases) includes Windows installers for AMD64 and ARM64 Windows (`ddev_windows_<architecture>_installer.<version>.exe`). After running that, you can open a new Git Bash, PowerShell, or cmd.exe window and start using DDEV.\n\nMost people interact with DDEV on traditional Windows using Git Bash, part of the [Windows Git suite](https://git-scm.com/download/win). Although DDEV does work with cmd.exe and PowerShell, it’s more at home in Bash. You can install Git Bash with Chocolatey by running `choco install -y git`.\n\nWindows Firefox Trusted CA\n\nThe `mkcert -install` step on Windows isn’t enough for Firefox. You need to add the created root certificate authority to the security configuration yourself:\n\n*   Run `mkcert -install` (you can use the shortcut from the Start Menu for that)\n*   Run `mkcert -CAROOT` to see the local folder used for the newly-created root certificate authority\n*   Open Firefox Preferences (`about:preferences#privacy`)\n*   Enter “certificates” into the search box on the top\n*   Click _View Certificates…_\n*   Select _Authorities_ tab\n*   Click to _Import…_\n*   Navigate to the folder where your root certificate authority was stored\n*   Select the `rootCA.pem` file\n*   Click to _Open_\n\nYou should now see your CA under `mkcert development CA`.\n\nGitpod[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#gitpod \"Permanent link\")\n---------------------------------------------------------------------------------------------------------\n\nChoose any of the following methods to launch your project with [Gitpod](https://www.gitpod.io/):\n\n1.  Add a [.gitpod.yml](https://www.gitpod.io/docs/references/gitpod-yml) to your project that installs DDEV and starts your project. The easy way to do this is with the excellent [ddev-gitpod-setup](https://github.com/tyler36/ddev-gitpod-setup) add-on. `ddev get tyler36/ddev-gitpod-setup` and add it to your git repository, push it, and then open it. You can even do all of this right on gitpod by opening your repository, doing the `ddev get` there and then pushing it back and restarting.\n2.  [Open any repository](https://www.gitpod.io/docs/getting-started) using Gitpod and run the following:\n    \n    ```\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-1)# Add DDEV’s GPG key to your keyring\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-2)curl-fsSLhttps://pkg.ddev.com/apt/gpg.key|gpg--dearmor|sudotee/etc/apt/keyrings/ddev.gpg>/dev/null\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-3)\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-4)# Add DDEV releases to your package repository\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-5)echo\"deb [signed-by=/etc/apt/keyrings/ddev.gpg] https://pkg.ddev.com/apt/ * *\"|sudotee/etc/apt/sources.list.d/ddev.list>/dev/null\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-6)\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-7)\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-8)# Update package information and install DDEV\n    [](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-16-9)sudoapt-getupdate&&sudoapt-getinstall-yddev\n    ```\n    \n    *   You can install your web app there, or import a database.\n    *   You may want to implement one of the `ddev pull` provider integrations to pull from a hosting provider or an upstream source.\n3.  Use the [ddev-gitpod-launcher](https://ddev.github.io/ddev-gitpod-launcher/) form to launch a repository. You’ll provide a source repository and click a button to open a newly-established environment. You can specify a companion artifacts repository and automatically load `db.sql.gz` and `files.tgz` from it. (More details in the [repository’s README](https://github.com/ddev/ddev-gitpod-launcher/blob/main/README.md).)\n    \n4.  Save the following link to your bookmark bar: Open in ddev-gitpod. It’s easiest to drag the link into your bookmarks. When you’re on a Git repository, click the bookmark to open it with DDEV in Gitpod. It does the same thing as the second option, but it works on non-Chrome browsers and you can use native browser keyboard shortcuts.\n\nIt can be complicated to get private databases and files into Gitpod, so in addition to the launchers, the [`git` provider example](https://github.com/ddev/ddev/blob/master/pkg/ddevapp/dotddev_assets/providers/git.yaml.example) demonstrates pulling a database and files without complex setup or permissions. This was created explicitly for Gitpod integration, because in Gitpod you typically already have access to private Git repositories, which are a fine place to put a starter database and files. Although [ddev-gitpod-launcher](https://ddev.github.io/ddev-gitpod-launcher/) and the web extension provide the capability, you may want to integrate a Git provider—or one of the [other providers](https://github.com/ddev/ddev/tree/master/pkg/ddevapp/dotddev_assets/providers)—for each project.\n\nGitHub Codespaces[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#github-codespaces \"Permanent link\")\n-------------------------------------------------------------------------------------------------------------------------------\n\nYou can use DDEV in remote [GitHub Codespaces](https://github.com/features/codespaces) without having to run Docker locally; you only need a browser and an internet connection.\n\nStart by creating a `.devcontainer/devcontainer.json` file in your GitHub repository:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-1){\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-2)\"image\":\"mcr.microsoft.com/devcontainers/universal:2\",\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-3)\"features\":{\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-4)\"ghcr.io/ddev/ddev/install-ddev:latest\":{}\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-5)},\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-6)\"postCreateCommand\":\"echo 'it should all be set up'\"\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-17-7)}\n```\n\nLaunch your repository in Codespaces:\n\n![Image 9: Screenshot of codespace create dialog in a repository on GitHub](https://ddev.readthedocs.io/en/stable/images/codespaces-launch.png)\n\n![Image 10: Screenshot of codespace create dialog in a repository on GitHub](https://ddev.readthedocs.io/en/stable/images/codespaces-setting-up.png)\n\nDDEV is now available within your new codespace instance:\n\n![Image 11](https://ddev.readthedocs.io/en/stable/images/codespaces-hello-screen.png)\n\nRun `ddev config` to [start a new blank project](https://ddev.readthedocs.io/en/stable/users/project/) - or [install a CMS](https://ddev.readthedocs.io/en/stable/users/quickstart/).\n\nRun `ddev start` if there is already a configured DDEV project in your repository.\n\n**Troubleshooting**:\n\nIf there are errors after restarting a codespace, use `ddev restart` or `ddev poweroff`.\n\nYou can also use the commands\n\n*   “Codespaces: Rebuild container”\n*   “Codespaces: Full rebuild container” (Beware: database will be deleted)\n\nvia the [Visual Studio Code Command Palette](https://docs.github.com/en/enterprise-cloud@latest/codespaces/codespaces-reference/using-the-vs-code-command-palette-in-codespaces):\n\n*   ⌘ + SHIFT + P on a Mac\n*   CTRL + SHIFT + P on Windows/Linux\n*   from the Application Menu, click View \\> Command Palette (Firefox)\n\nIf you need DDEV-specific assistance or have further questions, see [support](https://ddev.readthedocs.io/en/stable/users/support/).\n\nYour updated `devcontainer.json` file may differ depending on your project, but you should have `install-ddev` in the `features` section.\n\nNormal Linux installation also works\n\nYou can also install DDEV as if it were on any normal [Linux installation](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#linux).\n\n### Docker integration[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#docker-integration \"Permanent link\")\n\nDDEV in Codespaces relies on [`docker-in-docker`](https://github.com/devcontainers/features), which is installed by default when you use the image `\"mcr.microsoft.com/devcontainers/universal:2\"`. Please be aware: GitHub Codespaces and its Docker-integration (docker-in-docker) are relatively new. See [devcontainers/features](https://github.com/devcontainers/features) for general support and issues regarding Docker-support.\n\n### DDEV’s router is not used[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#ddevs-router-is-not-used \"Permanent link\")\n\nSince Codespaces handles all the routing, the internal DDEV router will not be used on Codespaces. Therefore config settings like [`web_extra_exposed_ports`](https://ddev.readthedocs.io/en/stable/users/configuration/config/#web_extra_exposed_ports) will have no effect.\n\nYou can expose ports via the `ports` setting, which is usually not recommended if you work locally due to port conflicts. But you can load these additional Docker compose files only when Codespaces is detected. See [Defining Additional Services](https://ddev.readthedocs.io/en/stable/users/extend/custom-compose-files/#docker-composeyaml-examples) for more information.\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-18-1)services:\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-18-2)web:\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-18-3)ports:\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-18-4)-\"5174:5174\"\n```\n\n### Default environment variables[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#default-environment-variables \"Permanent link\")\n\nCodespace instances already provide some [default environment values](https://docs.github.com/en/codespaces/developing-in-codespaces/default-environment-variables-for-your-codespace). You can inherit and inject them in your `.ddev/config.yaml`:\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-19-1)web_environment:\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-19-2)-CODESPACES\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-19-3)-CODESPACE_NAME\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-19-4)-GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN\n```\n\n### Advanced usage via devcontainer.json[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#advanced-usage-via-devcontainerjson \"Permanent link\")\n\nA lot more customization is possible via the [`devcontainer.json`\\-configuration](https://containers.dev/implementors/json_reference/). You can install Visual Studio Code extensions by default or run commands automatically.\n\n#### postCreateCommand[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#postcreatecommand \"Permanent link\")\n\nThe [`postCreateCommand`](https://containers.dev/implementors/json_reference/) lets you run commands automatically when a new codespace is launched. DDEV commands are available here.\n\nThe event is triggered on: fresh creation, rebuilds and full rebuilds. `ddev poweroff` is used in this example to avoid errors on rebuilds since some Docker containers are kept.\n\nYou usually want to use a separate bash script to do this, as docker [might not yet be available when the command starts to run](https://github.com/devcontainers/features/issues/780).\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-1){\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-2)\"image\":\"mcr.microsoft.com/devcontainers/universal:2\",\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-3)\"features\":{\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-4)\"ghcr.io/ddev/ddev/install-ddev:latest\":{}\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-5)},\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-6)\"portsAttributes\":{\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-7)\"3306\":{\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-8)\"label\":\"database\"\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-9)},\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-10)\"8027\":{\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-11)\"label\":\"mailpit\"\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-12)},\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-13)\"8080\":{\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-14)\"label\":\"web http\"\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-15)},\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-16)\"8443\":{\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-17)\"label\":\"web https\"\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-18)}\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-19)},\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-20)\"postCreateCommand\":\"bash .devcontainer/setup_project.sh\"\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-20-21)}\n```\n\n```\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-1)#!/usr/bin/env bash\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-2)set-ex\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-3)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-4)wait_for_docker(){\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-5)whiletrue;do\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-6)dockerps>/dev/null2>&1&&break\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-7)sleep1\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-8)done\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-9)echo\"Docker is ready.\"\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-10)}\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-11)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-12)wait_for_docker\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-13)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-14)# download images beforehand, optional\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-15)ddevdebugdownload-images\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-16)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-17)# avoid errors on rebuilds\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-18)ddevpoweroff\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-19)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-20)# start ddev project automatically\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-21)ddevstart-y\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-22)\n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-23)# further automated install / setup steps, e.g. \n[](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#__codelineno-21-24)ddevcomposerinstall\n```\n\nTo check for errors during the `postCreateCommand` action, use the command\n\n*   “Codespaces: View creation log”\n\nvia the [Visual Studio Code Command Palette](https://docs.github.com/en/enterprise-cloud@latest/codespaces/codespaces-reference/using-the-vs-code-command-palette-in-codespaces):\n\n*   ⌘ + SHIFT + P on a Mac\n*   CTRL + SHIFT + P on Windows/Linux\n*   from the Application Menu, click View \\> Command Palette (Firefox)\n\n![Image 12](https://ddev.readthedocs.io/en/stable/images/codespaces-creation-log.png)\n\nManual[¶](https://ddev.readthedocs.io/en/stable/users/install/ddev-installation/#manual \"Permanent link\")\n---------------------------------------------------------------------------------------------------------\n\nDDEV is a single executable, so installation on any OS is a matter of copying the `ddev` executable for your architecture into the appropriate system path on your machine.\n\n*   Download and extract the latest [DDEV release](https://github.com/ddev/ddev/releases) for your architecture.\n*   Move `ddev` to `/usr/local/bin` with `mv ddev /usr/local/bin/` (may require `sudo`), or another directory in your `$PATH` as preferred.\n*   Run `ddev` to test your installation. You should see DDEV’s command usage output.\n*   As a one-time initialization, run `mkcert -install`, which may require your `sudo` password.\n    \n    If you don’t have `mkcert` installed, download the [latest release](https://github.com/FiloSottile/mkcert/releases) for your architecture and `sudo mv <downloaded_file> /usr/local/bin/mkcert && sudo chmod +x /usr/local/bin/mkcert`.",
  "usage": {
    "tokens": 11333
  }
}
```
