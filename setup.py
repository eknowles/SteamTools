#!/usr/bin/python

import py2exe, sys, os
from glob import glob
from distutils.core import setup

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Windows\winsxs\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.30729.6161_none_50934f2ebcb7eb57\*.*'))]
setup(
    data_files=data_files,
    windows = [
        {
            "script": "SteamTools.py",
            "icon_resources": [(1, "icons/Steam.ico")]
        }
    ],
    options={"py2exe": {"optimize": 2, "includes": ["sip", "PyQt4.QtGui", "PyQt4.QtNetwork"]}},
    zipfile = "shared.lib",
)
