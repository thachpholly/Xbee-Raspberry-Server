# define main program

import imp
config = imp.load_source('module.name', "config.py")
data_manager = imp.load_source('data_manager', "\\Storage\\Storage.py")

Xbee_device