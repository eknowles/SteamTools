#!/usr/bin/python
import os, os.path
import sys
import subprocess as sp
import time

folder = "H:\steamtools\demos"

for root, dirs, files in os.walk(folder):
    for demo in files:
        if demo.endswith("dem"):
            os.chdir(folder)
            demoname = demo[:-4]
            rarup = "\"C:\\Program Files (x86)\\7-Zip\\7z.exe\" a -mmt -tzip " + demoname + ".zip \"" + demo + "\""
            sp.Popen(rarup)
            time.sleep(20)