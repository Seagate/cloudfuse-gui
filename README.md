# Cloudfuse-GUI - Frontend for Cloudfuse, an S3 and Azure Storage FUSE driver

[![License][license-badge]][license-url]
[![Release][release-badge]][release-url]
[![OpenSSF Scorecard][openssf-badge]][openssf-url]

[license-badge]: https://img.shields.io/github/license/Seagate/cloudfuse-gui
[license-url]: https://github.com/Seagate/cloudfuse-gui/blob/main/LICENSE
[release-badge]: https://img.shields.io/github/release/Seagate/cloudfuse-gui.svg
[release-url]: https://github.com/Seagate/cloudfuse-gui/releases/latest
[openssf-badge]: https://img.shields.io/ossf-scorecard/github.com/Seagate/cloudfuse-gui?label=openssf%20scorecard
[openssf-url]: https://scorecard.dev/viewer/?uri=github.com/Seagate/cloudfuse-gui

Cloudfuse-GUI provides the ability to mount a cloud bucket in your local filesystem on Linux and Windows with a GUI for easy configuration.
With Cloudfuse you can easily read and write to the cloud, and connect programs on your computer to the cloud even if they're not cloud-aware.
Cloudfuse uses file caching to provide the performance of local storage, or you can use streaming mode to efficiently access small parts of large files (e.g. video playback).
Cloudfuse-GUI adds a functional GUI to cloudfuse for both Windows and Linux.

## Table of Contents

- [Installation](#installation)
  - [Windows](#windows)
  - [Linux](#linux)
  - [From Archive](#from-archive)
  - [From Source](#from-source)
- [Basic Use](#basic-use)
- [License](#license)
- [Support](#support)
- [Contributing](#contributing)

## Installation

### Windows

Download and run the cloudfuse .exe installer from our latest release [here](https://github.com/Seagate/cloudfuse/releases).

Download and run the cloudfuse-gui .exe installer from our latest release [here](https://github.com/Seagate/cloudfuse-gui/releases).

### Linux

#### Debian /Ubuntu

##### Using Release on GitHub

Download the cloudfuse .deb file from our latest release [here](https://github.com/Seagate/cloudfuse/releases) and run the following command in your terminal:

`sudo apt-get install ./cloudfuse*.deb`

Download the cloudfuse-gui .deb file from our latest release [here](https://github.com/Seagate/cloudfuse-gui/releases) and run the following command in your terminal:

`sudo apt-get install ./cloudfuse-gui*.deb`

##### Using APT Repository

1. **Add the GPG key for the repository:**

    ```bash
    sudo apt-get update
    sudo apt-get install -y curl gpg
    curl -fsSL https://seagate.github.io/cloudfuse/public.key | sudo gpg --dearmor -o /usr/share/keyrings/cloudfuse-archive-keyring.gpg
    ```

2. **Add the repository to your APT sources:**

    ```bash
    echo "deb [signed-by=/usr/share/keyrings/cloudfuse-archive-keyring.gpg] https://seagate.github.io/cloudfuse stable main" | sudo tee /etc/apt/sources.list.d/cloudfuse.list > /dev/null
    echo "deb [signed-by=/usr/share/keyrings/cloudfuse-archive-keyring.gpg] https://seagate.github.io/cloudfuse-gui stable main" | sudo tee /etc/apt/sources.list.d/cloudfuse.list > /dev/null
    ```

3. **Install `cloudfuse-gui`:**

    ```bash
    sudo apt-get update
    sudo apt-get install cloudfuse-gui
    ```

#### Fedora / RHEL

##### Using Release on GitHub

Download the cloudfuse .rpm file from our latest release [here](https://github.com/Seagate/cloudfuse/releases) and run the following command in your terminal:

`sudo rpm -i ./cloudfuse*.rpm`

Download the cloudfuse-gui .rpm file from our latest release [here](https://github.com/Seagate/cloudfuse-gui/releases) and run the following command in your terminal:

`sudo rpm -i ./cloudfuse-gui*.rpm`

##### Using YUM/DNF Repository

1. **Add the `cloudfuse` repository:**

    ```bash
    sudo tee /etc/yum.repos.d/cloudfuse.repo <<EOF
    [cloudfuse]
    name=cloudfuse Repository
    baseurl=https://seagate.github.io/cloudfuse/rpm-repo/
    enabled=1
    gpgcheck=1
    gpgkey=https://seagate.github.io/cloudfuse/public.key
    [cloudfuse-gui]
    name=cloudfuse-gui Repository
    baseurl=https://seagate.github.io/cloudfuse-gui/rpm-repo/
    enabled=1
    gpgcheck=1
    gpgkey=https://seagate.github.io/cloudfuse-gui/public.key
    EOF
    ```

2. **Install `cloudfuse`:**

    ```bash
    # For Fedora, RHEL 8+
    sudo dnf install cloudfuse-gui

    # For RHEL 7
    sudo yum install cloudfuse-gui
    ```

### From Archive

Download the archive for your platform and architecture from the latest release [here](https://github.com/Seagate/cloudfuse-gui/releases).
On Windows, you will need to install WinFsp to use Cloudfuse. See [this](https://winfsp.dev/rel/) to install WinFSP.

### From Source

Please refer to the [Installation from source](https://github.com/Seagate/cloudfuse-gui/wiki/Installation-From-Source) to
manually install Cloudfuse.

## Basic Use

 Open Cloudfuse from the desktop shortcut to launch it.
If you installed Cloudfuse from an archive, run `cloudfuseGUI` from the extracted archive.
To run the GUI from source, see [instructions](https://github.com/Seagate/cloudfuse/wiki/Running-the-GUI-from-source).

- Choose mount settings:
  - Select the desired type of cloud (Azure or S3).
  - Click `config` to open the settings window.
  - Enter the credentials for your cloud storage container.
  (see [here for S3](https://github.com/Seagate/cloudfuse/wiki/S3-Storage-Configuration), or [here for Azure](https://github.com/Seagate/cloudfuse/wiki/Azure-Storage-Configuration) credential requirements).
  - Select file caching or streaming mode (see [File-Cache](https://github.com/Seagate/cloudfuse/wiki/File-Cache) and [Streaming](https://github.com/Seagate/cloudfuse/wiki/Streaming) for details).
  - Close the settings window and save your changes.

  The config file is written to this location on Windows: `C:\Users\{username}\AppData\Roaming`, and on Linux: `/opt/cloudfuse/`.
  You can view and edit the config file directly (see [guide](https://github.com/Seagate/cloudfuse/wiki/Config-File)).
- Mount your container:
  - Click `Browse` in the main window and browse to the EMPTY folder you want to mount your container in. You may need to create this folder.
  - Click `Mount`.
  - Watch for status messages below. On success, your files will appear in the mount directory.
    Note: if mount fails with an error mentioning WinFSP, you may need to install WinFSP (see [installation instructions](#installation)).

  On Windows, mounted containers can persist across system restarts.

- Unmount:
  - Make sure the mount directory you want to unmount is listed. If it isn't, click `browse` and select it.
  - Click the `unmount` mutton.
  - Watch for a status message below. On success, the mount directory will become empty.
    Note: If you enabled the `Persist File Cache` option, the local file cache for the container will be kept and reused when the container is mounted again.

## License

The Cloudfuse project is licensed under MIT.

### Third-Party Notices

See [notices](./NOTICE) for third party license notices.

Qt is licensed under the GNU Lesser General Public License version 3, which is available [here](https://doc.qt.io/qt-6/lgpl.html).

WinFSP is licensed under the GPLv3 license with a special exception for Free/Libre and Open Source Software,
which is available [here](https://github.com/winfsp/winfsp/blob/master/License.txt).

### Attribution

WinFsp - Windows File System Proxy, Copyright (C) Bill Zissimopoulos - [link](https://github.com/winfsp/winfsp)

## Support

### Contact Us

We welcome your questions and feedback!
Email us: [cloudfuse@seagate.com](mailto:cloudfuse@seagate.com).

### Report Issues and Request Features

Please submit [issues and requests here](https://github.com/Seagate/cloudfuse-gui/issues).

## Contributing

This project welcomes contributions and suggestions.

This project is governed by the [code of conduct](CODE_OF_CONDUCT.md).
You are expected to follow this as you contribute to the project.
Please report all unacceptable behavior to [opensource@seagate.com](mailto:opensource@seagate.com)
