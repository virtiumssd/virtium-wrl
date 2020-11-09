#!/bin/bash
#Run vtsetup -m machine
#x86_64, arm. Currently support only for these machine
#Working step
#Checkout virtium meta
#Integrate vitium meta and virtium recipe

# Check Bash installed
if [ -z "${BASH_VERSION}" ]; then
	echo "This script must be run with bash."
	exit 1
fi

# Check Python installed
which python3 > /dev/null
if [ $? -ne 0 ]; then
	echo "WRLinux setup requires 'python2'."
	echo "Please install python2."
	exit 1
fi

LAYERSDIR="layers"
if [ ! -d $LAYERSDIR ]; then
	echo $LAYERSDIR "directory must exists."
	exit 1
fi

BBLAYERSFILE="build/conf/bblayers.conf"
if [ ! -f $BBLAYERSFILE ]; then
	echo $BBLAYERSFILE "file must exists."
	exit 1
fi

LOCALFILE="build/conf/local.conf"
if [ ! -f $LOCALFILE ]; then
	echo $LOCALFILE "file must exists."
	exit 1
fi

# Requires python
CMD="python virtium/bin/setup.py"

${CMD} $@

exit 0
