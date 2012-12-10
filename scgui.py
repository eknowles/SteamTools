#!/usr/bin/python
import os, os.path
import re
import shutil
import commands
import distutils.dir_util
import subprocess
import sys
from PyQt4 import QtCore, QtGui, QtNetwork


# Import bits to read edit configs like settings.ini
from ConfigParser import SafeConfigParser

class klutchguitool():
    def __init__(self): 
        
        self.settingsfile = "settings.ini"
        
        self.settings = SafeConfigParser(allow_no_value=True)
        if (os.path.exists(self.settingsfile)) and (os.stat(self.settingsfile)[6]==0):
            os.remove(self.settingsfile)
            print "empty settings > del"
        if not os.path.exists(self.settingsfile):
            print "settings.ini doesn't exist so making a fresh one"
            # lets create that config file for next time...
            cfgfile = open("settings.ini",'w')
            # add the settings to the structure of the file, and lets write it out...
            self.settings.add_section('main')
            self.settings.set('main','version', '2.0')
            self.settings.set('main','steamacc', '')
            self.settings.set('main','game', '')
            self.settings.set('main','gamepath', '')
            self.settings.set('main','cfgpath', '')
            self.settings.add_section('user')
            self.settings.set('user','steamid', '')
            self.settings.set('user','name', '')
            self.settings.add_section('server')
            self.settings.set('server','ip', '')
            self.settings.set('server','pass', '')
            self.settings.set('server','rcon', '')
            self.settings.add_section('launchoptions')
            self.settings.set('launchoptions','game', '-novid -fullscreen -dxlevel 81 +fps_max 999')
            self.settings.set('launchoptions','demo', '-novid -sw -w 720 -h 480 +fps_max 999 +demoui')
            self.settings.add_section('skin')
            self.settings.set('skin','installedskin', '')
            self.settings.set('skin','teambar', '')
            self.settings.set('skin','playerbar', '')
            self.settings.write(cfgfile)
            cfgfile.close()
        self.settings.read('settings.ini')        
        
        self.steamacc = self.settings.get('main', 'steamacc')
        
        #self.skinspath = os.path.join(os.environ["ProgramFiles(x86)"],"KLUTCH\SCGUI\Skins")
        self.skinspath = os.path.join(os.path.dirname(sys.argv[0]), "Downloads", "Skins")
        self.cspath=self.settings.get('main', 'gamepath')
        
        self.installedskin = {"Skin":"No skin installed","Version":"No skin installed","Author":"No skin installed","Type":"No skin installed","Info":"How to install a GUI\n\n1. Pick a skin on the left\n2. If you wish to use it, click either the Download or Install button on the right."}
        self.skindetails = {"Skin":"","Version":"","Author":"","Type":"","Info":"","TeamBar":"","PlayerBar":""}
        self.specsettings ={"t1name":"","t1url":"","t1flag":"","t2name":"","t2url":"","t2flag":"","playername":"", "playerflag":""}
        self.cfgsettings = {}
        self.cfgheaders =["Console Variable","Value"]
        self.resfiles=["Spectator.res"] #, "ScoreBoard.res"]
        self.cfgfiles=["KLUTCH.cfg"] #, "autoexec.cfg"]
        self.noskininstalled = "SCGUI cannot find any skins installed in your game folder. Try installing one by choosing one from the dropdown list. If this problem persists try reinstalling the program."
        
    # This function opens up the KLUTCH.cfg and gets the installed skins name (this should match a dir in the skins folder)
    
    def getskindetails(self, skin):
        
        targetfilelocation=os.path.join(self.skinspath,skin,"cfg/KLUTCH.cfg")
        if os.path.exists(targetfilelocation):
            maincfg = open(targetfilelocation,"r")
            for line in maincfg.readlines():
                if re.search(r"// \[[^\]]*?=[^\]]*?\]", line):
                    matches = re.search(r"// \[([^\s]*?)=(.*?)\]", line)
                    if matches is not None:
                        self.skindetails[matches.group(1)] = matches.group(2)
                        
    
    def getinstalledskin(self, accountname):
        targetfilelocation=os.path.normpath(os.path.join(self.cspath,"cfg/KLUTCH.cfg"))
        if os.path.isfile(targetfilelocation):
            maincfg = open(targetfilelocation,"r")
            for line in maincfg.readlines():
                if re.search(r"// \[[^\]]*?=[^\]]*?\]", line):
                    matches = re.search(r"// \[([^\s]*?)=(.*?)\]", line)
                    if matches is not None:
                        self.installedskin[matches.group(1)] = matches.group(2)
                
                if re.search(r"// \[Skin=[^\]]*?\]", line):
                    matches = re.search(r"// \[Skin=(.*?)\]", line)
                    #print matches.group(1)
                    # This will then open and write the installedskin to the settings
                    cfgfile = open("settings.ini", "w")            
                    self.settings.set('skin', 'installedskin', matches.group(1))
                    self.settings.write(cfgfile)
                    cfgfile.close()
        else:
            print "Warning: No skin installed or incorrect steam username."
            # This will then open and write the installedskin to the settings
            cfgfile = open("settings.ini", "w")            
            self.settings.set('skin', 'installedskin', '')
            self.settings.write(cfgfile)
            cfgfile.close()
    
    # This will remove all skins from the cstrike dir
    def count_files(self,in_directory):
        joiner= (in_directory + os.path.sep).__add__
        return sum(
            os.path.isfile(filename)
            for filename
            in map(joiner, os.listdir(in_directory))
        )
    
        
    
    # Gets a list of folders in the skins folder
    def listskins(self):
        print "lol"#os.listdir(self.skinspath)
        
        
    # This reads resorce files and puts key settings into variables
    def resfileinterp(self, targetfile):
        targetfilelocation=os.path.join(self.settings.get('main', 'gamepath'),"resource/UI",targetfile)
        if os.path.exists(targetfilelocation):
            resfile = open(targetfilelocation,"r")
            for line in resfile.readlines():
                if re.search(r"\"[^\"]*\"[\s]*?\"[^\"]*\"[\s]*?//%[^%]*%", line):
                    matches = re.search(r"\"([^\"]*)\"[\s]*?\"([^\"]*)\"[\s]*?//%([^%]*)%", line)
                    self.specsettings[matches.group(3)] = matches.group(2)
        else:
            print "Resource File "+targetfile+" could not be found"
                
    def cfgfileinterp(self,targetfile):
        self.cfgsettings = {}
        targetfilelocation=os.path.join(self.settings.get("main", "cfgpath"), targetfile)
        #print "targetfilelocation: " + targetfilelocation
        if os.path.exists(targetfilelocation):
            cfgfile = open(targetfilelocation,"r")
            for line in cfgfile.readlines():
                if not line.startswith("bind"):
                    if not line.startswith("alias"):
                        if not line.startswith("//"):
                            if re.search(r"[^\"]*[\s]*?\"[^\"]*\"", line):
                                matches = re.search(r"([^\"]*)[\s]*?\"([^\"]*)\"", line)
                                self.cfgsettings[matches.group(1)] = matches.group(2)
        else:
            print "Can not find "+targetfile+" to interp"
                    
        #print self.cfgsettings
    
    
    def editres(self,targetfile):
        tgfile = os.path.join(self.cspath,"resource/UI",targetfile)
        if os.path.exists(tgfile):
            targetfilelocation= os.path.normpath(tgfile)
            resfile = open(targetfilelocation,"r")
            resfile_output = resfile.read();
            resfile.close()
            for key, setting  in self.specsettings.iteritems():
                resfile_output=re.sub(r"\"([^\"]*)\"[\s]*?\"([^\"]*)\"[\s]*?//%"+key+ "%","\""+r"\1"+"\" \""+setting+ "\" //%"+key+ "%", resfile_output)
            resfile = open(targetfilelocation,"w")
            resfile.write(resfile_output)
            resfile.close()
            #print resfile_output    
        else:
            print "Resource File "+targetfile+" could not be found"
            
    def editcfg(self,targetfile):
        targetfilelocation=os.path.join(self.cspath,"cfg/KLUTCH.cfg")
        cfgfile = open(targetfilelocation,"r")
        cfgfile_output = cfgfile.read();
        cfgfile.close()
        for key, setting  in self.cfgsettings.iteritems():
            #print key,setting
            cfgfile_output=re.sub(r"\""+key+ r"\"[\s]*?\"([^\"]*)\"", "\""+key+"\" \""+setting+ "\"",cfgfile_output)
        cfgfile = open(targetfilelocation,"w")
        cfgfile.write(cfgfile_output)
        cfgfile.close()
        #print cfgfile_output
        
    def readfiles(self):
        for guifile in self.resfiles:
            self.resfileinterp(guifile)
        for guifile in self.cfgfiles: 
            self.cfgfileinterp(guifile)
            
    def launchcs(self):
        os.execvp("C:\Program Files (x86)\Steam\Steam.exe", ['-applaunch 240','-novid','-sw','-w 1280','-h 720','-x 0','-y 0','-noborder','+fps_max 240'])

    def openskinsfolder(self):
        subprocess.Popen('explorer ' + self.skinspath)
        
    def opencstrikefolder(self):
        subprocess.Popen('explorer ' + os.path.normpath(self.cspath))
        print os.path.normpath(self.cspath)
