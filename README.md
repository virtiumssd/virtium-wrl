With this tool you can integrate virtium recipes (vtTestCmd, vtSecureCmd, vtView) into your Wind River Linux platform project.

Prerequisites
-------------

A Linux host that meets the requirements for using Wind River Linux. This includes Git version 1.9 or greater and Python 3.

Download
-------------
The setup program is expected to be clone inside the project directory.

$ cd my-project
$ git clone https://github.com/virtiumssd/virtium-wrl.git

Intergate
-------------
x86-64 platform

$./virtium-wrl/setup.sh -m x86-64

arm platform

$./virtium-wrl/setup.sh -m arm
