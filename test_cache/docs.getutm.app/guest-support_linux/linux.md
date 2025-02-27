---
title: Linux
description: Documentation for UTM virtual machines
url: https://docs.getutm.app/guest-support/linux/
timestamp: 2025-01-20T15:50:53.138Z
domain: docs.getutm.app
path: guest-support_linux
---

# Linux


Documentation for UTM virtual machines


## Content

Sections

*   [Drivers](https://docs.getutm.app/guest-support/linux/#drivers)
*   [SPICE Agent](https://docs.getutm.app/guest-support/linux/#spice-agent)
    *   [Ubuntu, Debian, apt based](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based)
    *   [Fedora, CentOS, RPM based](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based)
    *   [ArchLinux](https://docs.getutm.app/guest-support/linux/#archlinux)
*   [QEMU Agent](https://docs.getutm.app/guest-support/linux/#qemu-agent)
    *   [Ubuntu, Debian, apt based](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based-1)
    *   [Fedora, CentOS, RPM based](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based-1)
    *   [ArchLinux](https://docs.getutm.app/guest-support/linux/#archlinux-1)
*   [SPICE WebDAV](https://docs.getutm.app/guest-support/linux/#spice-webdav)
    *   [Ubuntu, Debian, apt based](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based-2)
    *   [Fedora, CentOS, RPM based](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based-2)
    *   [ArchLinux](https://docs.getutm.app/guest-support/linux/#archlinux-2)
*   [VirtFS](https://docs.getutm.app/guest-support/linux/#virtfs)
    *   [Fixing permission errors](https://docs.getutm.app/guest-support/linux/#fixing-permission-errors)
*   [**macOS** VirtioFS](https://docs.getutm.app/guest-support/linux/#macos-virtiofs)

[](https://docs.getutm.app/guest-support/linux/#drivers)Drivers
---------------------------------------------------------------

Most popular Linux distributions will have the correct drivers already built in. If you are building your own kernel, make sure to include the following options:

*   `CONFIG_VIRTIO`
*   `CONFIG_VIRTIO_RING`
*   `CONFIG_VIRTIO_PCI`
*   `CONFIG_VIRTIO_BALLOON`
*   `CONFIG_VIRTIO_BLK` for storage devices
*   `CONFIG_VIRTIO_CONSOLE` for console devices
*   `CONFIG_VIRTIO_NET` for networking
*   `CONFIG_DRM_VIRTIO_GPU` for graphical output
*   `CONFIG_NET_9P`, `CONFIG_NET_9P_VIRTIO`, `CONFIG_9P_FS`, `CONFIG_9P_FS_POSIX_ACL` for VirtFS directory sharing
*   `CONFIG_VIRTIO_FS` for VirtioFS directory sharing

To use the experimental OpenGL hardware acceleration features in the QEMU backend, make sure a [compatible display card is selected](https://docs.getutm.app/settings-qemu/devices/display/#emulated-display-card) and the VirGL driver is enabled in Mesa.

[](https://docs.getutm.app/guest-support/linux/#spice-agent)SPICE Agent
-----------------------------------------------------------------------

SPICE agent is required for clipboard sharing (both [QEMU](https://docs.getutm.app/settings-qemu/sharing/#clipboard-sharing) and [Apple](https://docs.getutm.app/settings-apple/virtualization/#macos-13-clipboard-sharing) backend) as well as dynamic display resolution in [QEMU](https://docs.getutm.app/settings-qemu/devices/display/#auto-resolution) backend.

Most distributions will have a package named `spice-vdagent` but you can also build it [from the source](https://gitlab.freedesktop.org/spice/linux/vd_agent). Some common distributions and install instructions are listed below.

### [](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based)Ubuntu, Debian, apt based

```
$ sudo apt install spice-vdagent
```

### [](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based)Fedora, CentOS, RPM based

```
$ sudo yum install spice-vdagent
```

These systems will typically already have SPICE agent installed.

### [](https://docs.getutm.app/guest-support/linux/#archlinux)ArchLinux

```
$ sudo pacman -S spice-vdagent
```

[](https://docs.getutm.app/guest-support/linux/#qemu-agent)QEMU Agent
---------------------------------------------------------------------

Additional features such as time syncing and [scripting](https://docs.getutm.app/scripting/scripting/) are supported by the QEMU agent.

### [](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based-1)Ubuntu, Debian, apt based

```
$ sudo apt install qemu-guest-agent
```

### [](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based-1)Fedora, CentOS, RPM based

```
$ sudo yum install qemu-guest-agent
```

### [](https://docs.getutm.app/guest-support/linux/#archlinux-1)ArchLinux

```
$ sudo pacman -S qemu-guest-agent
```

[](https://docs.getutm.app/guest-support/linux/#spice-webdav)SPICE WebDAV
-------------------------------------------------------------------------

SPICE WebDAV is required for [QEMU directory sharing](https://docs.getutm.app/settings-qemu/sharing/#spice-webdav) as an alternative to VirtFS.

Once SPICE WebDAV is installed and running, you should be able to access `http://127.0.0.1:9843` from inside the guest. This is a WebDAV share that you can mount using something like `davfs2`.

Most distributions will have a package named `spice-webdavd` or `phodav` but you can also build it [from the source](https://gitlab.gnome.org/GNOME/phodav). Some common distributions and install instructions are listed below.

### [](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based-2)Ubuntu, Debian, apt based

```
$ sudo apt install spice-webdavd
```

### [](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based-2)Fedora, CentOS, RPM based

```
$ sudo yum install spice-webdavd
```

### [](https://docs.getutm.app/guest-support/linux/#archlinux-2)ArchLinux

[](https://docs.getutm.app/guest-support/linux/#virtfs)VirtFS
-------------------------------------------------------------

VirtFS enables [QEMU directory sharing](https://docs.getutm.app/settings-qemu/sharing/#virtfs) as an alternative to SPICE WebDAV. Note that VirtFS sharing must be enabled in the settings and you cannot use it at the same time as WebDAV directory sharing.

After making sure your Linux installation [supports 9pfs](https://docs.getutm.app/guest-support/linux/#drivers), you can automatically mount the share by adding the following entry to your `/etc/fstab`:

```
# UTM Shared Folder
share /mnt/utm 9p trans=virtio,version=9p2000.L,rw,_netdev,nofail,auto 0 0
```

_Note_: `share` is the name UTM uses for the VirtIO device and you should not change it. You can replace `/mnt/utm` with a different folder if you like.

After updating `/etc/fstab` you need to create an empty folder for the mount:

You can apply the changes to `/etc/fstab` with the following commands (this will automatically happen on reboot as well):

```
systemctl daemon-reload
systemctl restart network-fs.target
systemctl list-units --type=mount
```

A systemd `.mount` unit for `/mnt/utm` should now be displayed in the list, and you can access the contents of your shared folder.

### [](https://docs.getutm.app/guest-support/linux/#fixing-permission-errors)Fixing permission errors

You may notice that accessing the mount point fails with “access denied” unless you’re the root user. This is because by default the directory inherits the UID/GID from macOS/iOS which has a different numbering scheme.

To fix this we are going to use [`bindfs`](https://bindfs.org/) to create a mount in the user’s home directory that we can access normally. You have to first install `bindfs` with your system’s package manager.

The first step is to get the UID and GID used by the host:

```
$ ls -na /mnt/utm
total 8
drwxr-xr-x 4 502 20  128 Feb 22 15:52 .
drwxr-xr-x 3   0  0 4096 Feb 22 14:50 ..
-rw-r--r-- 1 502 20   13 Feb 22 15:52 shared-file.txt
```

In this case the UID for the host is `502` and the GID is `20`. You have to do the same for the guest user (usually UID `1000` and GID `1000`). Additionally, create an empty folder for the `bindfs` mount in the home directory:

_Note_: In this example the username is `user`, you might have to adjust this to match your configuration.

Now add another entry to `/etc/fstab`:

```
# bindfs mount to remap UID/GID
/mnt/utm /home/user/utm fuse.bindfs map=502/1000:@20/@1000,x-systemd.requires=/mnt/utm,_netdev,nofail,auto 0 0
```

An alternative solution is to recursively change the permissions of the files in your shared folder:

```
$ sudo chown -R $USER /mnt/utm
```

_Note_: This will not change the permissions on your host system, but it will add a custom `user.virtfs` file attributes to every file to store the guest ownership. It is not recommended to do this if you want to share your host’s home folder for instance.

[](https://docs.getutm.app/guest-support/linux/#macos-virtiofs)**macOS** VirtioFS
---------------------------------------------------------------------------------

When using Apple Virtualization backend, [directory sharing](https://docs.getutm.app/settings-apple/sharing/) is enabled through VirtioFS.

VirtioFS is NOT the same as [VirtFS](https://docs.getutm.app/guest-support/linux/#virtfs) which is used by the QEMU backend for directory sharing.

After making sure your Linux installation [supports VirtioFS](https://docs.getutm.app/guest-support/linux/#drivers), you can mount the share with the following command:

```
$ sudo mkdir [mount point]
$ sudo mount -t virtiofs share [mount point]
```

Where `[mount point]` is the desired destination path. For example: `/media/share`.

You can also modify `/etc/fstab` and add the following line to automatically mount the share on startup:

```
share	[mount point]	virtiofs	rw,nofail	0	0
```

## Metadata

```json
{
  "title": "Linux",
  "description": "Documentation for UTM virtual machines",
  "url": "https://docs.getutm.app/guest-support/linux/",
  "content": "Sections\n\n*   [Drivers](https://docs.getutm.app/guest-support/linux/#drivers)\n*   [SPICE Agent](https://docs.getutm.app/guest-support/linux/#spice-agent)\n    *   [Ubuntu, Debian, apt based](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based)\n    *   [Fedora, CentOS, RPM based](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based)\n    *   [ArchLinux](https://docs.getutm.app/guest-support/linux/#archlinux)\n*   [QEMU Agent](https://docs.getutm.app/guest-support/linux/#qemu-agent)\n    *   [Ubuntu, Debian, apt based](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based-1)\n    *   [Fedora, CentOS, RPM based](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based-1)\n    *   [ArchLinux](https://docs.getutm.app/guest-support/linux/#archlinux-1)\n*   [SPICE WebDAV](https://docs.getutm.app/guest-support/linux/#spice-webdav)\n    *   [Ubuntu, Debian, apt based](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based-2)\n    *   [Fedora, CentOS, RPM based](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based-2)\n    *   [ArchLinux](https://docs.getutm.app/guest-support/linux/#archlinux-2)\n*   [VirtFS](https://docs.getutm.app/guest-support/linux/#virtfs)\n    *   [Fixing permission errors](https://docs.getutm.app/guest-support/linux/#fixing-permission-errors)\n*   [**macOS** VirtioFS](https://docs.getutm.app/guest-support/linux/#macos-virtiofs)\n\n[](https://docs.getutm.app/guest-support/linux/#drivers)Drivers\n---------------------------------------------------------------\n\nMost popular Linux distributions will have the correct drivers already built in. If you are building your own kernel, make sure to include the following options:\n\n*   `CONFIG_VIRTIO`\n*   `CONFIG_VIRTIO_RING`\n*   `CONFIG_VIRTIO_PCI`\n*   `CONFIG_VIRTIO_BALLOON`\n*   `CONFIG_VIRTIO_BLK` for storage devices\n*   `CONFIG_VIRTIO_CONSOLE` for console devices\n*   `CONFIG_VIRTIO_NET` for networking\n*   `CONFIG_DRM_VIRTIO_GPU` for graphical output\n*   `CONFIG_NET_9P`, `CONFIG_NET_9P_VIRTIO`, `CONFIG_9P_FS`, `CONFIG_9P_FS_POSIX_ACL` for VirtFS directory sharing\n*   `CONFIG_VIRTIO_FS` for VirtioFS directory sharing\n\nTo use the experimental OpenGL hardware acceleration features in the QEMU backend, make sure a [compatible display card is selected](https://docs.getutm.app/settings-qemu/devices/display/#emulated-display-card) and the VirGL driver is enabled in Mesa.\n\n[](https://docs.getutm.app/guest-support/linux/#spice-agent)SPICE Agent\n-----------------------------------------------------------------------\n\nSPICE agent is required for clipboard sharing (both [QEMU](https://docs.getutm.app/settings-qemu/sharing/#clipboard-sharing) and [Apple](https://docs.getutm.app/settings-apple/virtualization/#macos-13-clipboard-sharing) backend) as well as dynamic display resolution in [QEMU](https://docs.getutm.app/settings-qemu/devices/display/#auto-resolution) backend.\n\nMost distributions will have a package named `spice-vdagent` but you can also build it [from the source](https://gitlab.freedesktop.org/spice/linux/vd_agent). Some common distributions and install instructions are listed below.\n\n### [](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based)Ubuntu, Debian, apt based\n\n```\n$ sudo apt install spice-vdagent\n```\n\n### [](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based)Fedora, CentOS, RPM based\n\n```\n$ sudo yum install spice-vdagent\n```\n\nThese systems will typically already have SPICE agent installed.\n\n### [](https://docs.getutm.app/guest-support/linux/#archlinux)ArchLinux\n\n```\n$ sudo pacman -S spice-vdagent\n```\n\n[](https://docs.getutm.app/guest-support/linux/#qemu-agent)QEMU Agent\n---------------------------------------------------------------------\n\nAdditional features such as time syncing and [scripting](https://docs.getutm.app/scripting/scripting/) are supported by the QEMU agent.\n\n### [](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based-1)Ubuntu, Debian, apt based\n\n```\n$ sudo apt install qemu-guest-agent\n```\n\n### [](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based-1)Fedora, CentOS, RPM based\n\n```\n$ sudo yum install qemu-guest-agent\n```\n\n### [](https://docs.getutm.app/guest-support/linux/#archlinux-1)ArchLinux\n\n```\n$ sudo pacman -S qemu-guest-agent\n```\n\n[](https://docs.getutm.app/guest-support/linux/#spice-webdav)SPICE WebDAV\n-------------------------------------------------------------------------\n\nSPICE WebDAV is required for [QEMU directory sharing](https://docs.getutm.app/settings-qemu/sharing/#spice-webdav) as an alternative to VirtFS.\n\nOnce SPICE WebDAV is installed and running, you should be able to access `http://127.0.0.1:9843` from inside the guest. This is a WebDAV share that you can mount using something like `davfs2`.\n\nMost distributions will have a package named `spice-webdavd` or `phodav` but you can also build it [from the source](https://gitlab.gnome.org/GNOME/phodav). Some common distributions and install instructions are listed below.\n\n### [](https://docs.getutm.app/guest-support/linux/#ubuntu-debian-apt-based-2)Ubuntu, Debian, apt based\n\n```\n$ sudo apt install spice-webdavd\n```\n\n### [](https://docs.getutm.app/guest-support/linux/#fedora-centos-rpm-based-2)Fedora, CentOS, RPM based\n\n```\n$ sudo yum install spice-webdavd\n```\n\n### [](https://docs.getutm.app/guest-support/linux/#archlinux-2)ArchLinux\n\n[](https://docs.getutm.app/guest-support/linux/#virtfs)VirtFS\n-------------------------------------------------------------\n\nVirtFS enables [QEMU directory sharing](https://docs.getutm.app/settings-qemu/sharing/#virtfs) as an alternative to SPICE WebDAV. Note that VirtFS sharing must be enabled in the settings and you cannot use it at the same time as WebDAV directory sharing.\n\nAfter making sure your Linux installation [supports 9pfs](https://docs.getutm.app/guest-support/linux/#drivers), you can automatically mount the share by adding the following entry to your `/etc/fstab`:\n\n```\n# UTM Shared Folder\nshare /mnt/utm 9p trans=virtio,version=9p2000.L,rw,_netdev,nofail,auto 0 0\n```\n\n_Note_: `share` is the name UTM uses for the VirtIO device and you should not change it. You can replace `/mnt/utm` with a different folder if you like.\n\nAfter updating `/etc/fstab` you need to create an empty folder for the mount:\n\nYou can apply the changes to `/etc/fstab` with the following commands (this will automatically happen on reboot as well):\n\n```\nsystemctl daemon-reload\nsystemctl restart network-fs.target\nsystemctl list-units --type=mount\n```\n\nA systemd `.mount` unit for `/mnt/utm` should now be displayed in the list, and you can access the contents of your shared folder.\n\n### [](https://docs.getutm.app/guest-support/linux/#fixing-permission-errors)Fixing permission errors\n\nYou may notice that accessing the mount point fails with “access denied” unless you’re the root user. This is because by default the directory inherits the UID/GID from macOS/iOS which has a different numbering scheme.\n\nTo fix this we are going to use [`bindfs`](https://bindfs.org/) to create a mount in the user’s home directory that we can access normally. You have to first install `bindfs` with your system’s package manager.\n\nThe first step is to get the UID and GID used by the host:\n\n```\n$ ls -na /mnt/utm\ntotal 8\ndrwxr-xr-x 4 502 20  128 Feb 22 15:52 .\ndrwxr-xr-x 3   0  0 4096 Feb 22 14:50 ..\n-rw-r--r-- 1 502 20   13 Feb 22 15:52 shared-file.txt\n```\n\nIn this case the UID for the host is `502` and the GID is `20`. You have to do the same for the guest user (usually UID `1000` and GID `1000`). Additionally, create an empty folder for the `bindfs` mount in the home directory:\n\n_Note_: In this example the username is `user`, you might have to adjust this to match your configuration.\n\nNow add another entry to `/etc/fstab`:\n\n```\n# bindfs mount to remap UID/GID\n/mnt/utm /home/user/utm fuse.bindfs map=502/1000:@20/@1000,x-systemd.requires=/mnt/utm,_netdev,nofail,auto 0 0\n```\n\nAn alternative solution is to recursively change the permissions of the files in your shared folder:\n\n```\n$ sudo chown -R $USER /mnt/utm\n```\n\n_Note_: This will not change the permissions on your host system, but it will add a custom `user.virtfs` file attributes to every file to store the guest ownership. It is not recommended to do this if you want to share your host’s home folder for instance.\n\n[](https://docs.getutm.app/guest-support/linux/#macos-virtiofs)**macOS** VirtioFS\n---------------------------------------------------------------------------------\n\nWhen using Apple Virtualization backend, [directory sharing](https://docs.getutm.app/settings-apple/sharing/) is enabled through VirtioFS.\n\nVirtioFS is NOT the same as [VirtFS](https://docs.getutm.app/guest-support/linux/#virtfs) which is used by the QEMU backend for directory sharing.\n\nAfter making sure your Linux installation [supports VirtioFS](https://docs.getutm.app/guest-support/linux/#drivers), you can mount the share with the following command:\n\n```\n$ sudo mkdir [mount point]\n$ sudo mount -t virtiofs share [mount point]\n```\n\nWhere `[mount point]` is the desired destination path. For example: `/media/share`.\n\nYou can also modify `/etc/fstab` and add the following line to automatically mount the share on startup:\n\n```\nshare\t[mount point]\tvirtiofs\trw,nofail\t0\t0\n```",
  "usage": {
    "tokens": 2416
  }
}
```
