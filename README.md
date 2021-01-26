With this tool you can integrate Virtium recipes (vtTestCmd, vtSecureCmd, vtView) into your Wind River Linux platform project.

Prerequisites
-------------

+ A Linux host that meets the requirements for using [Wind River Linux LTS 19](https://docs.windriver.com/category/os_linux_lts_19 "OS Wind River Linux 19")
+ [Git](https://git-scm.com/ "Git project page") (>= 1.9)
+ [Python](https://www.python.org/ "Python project page") (>= 2.7)

Download
-------------
The setup program is expected to be cloned inside the project directory.

    $ cd my-project
    $ git clone https://github.com/virtiumssd/virtium-wrl.git

Integration
-------------
x86-64 platform

    $ ./virtium-wrl/setup.sh -m x86-64

ARM platform

    $ ./virtium-wrl/setup.sh -m arm
