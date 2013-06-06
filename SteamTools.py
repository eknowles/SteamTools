#!/usr/bin/python

#===============================================================================
# Steam Tools
# -- by Edward KLUTCH Knowles --
# --- @NedKnowles on twitter ---
# 
# To compile from source you will need:
# python 2.7 32bit
# pyqt4 for 32bit (py2.7)
# pywin32-217.win32-py2.7.exe (http://sourceforge.net/projects/pywin32)
# elementtree-1.2.6-20050316.win32.exe (http://effbot.org/downloads/#elementtree)
#===============================================================================

import os, os.path
import sys
import webbrowser
import scgui
import codecs
import syntax
import urllib
import urllib2
import math
import random
import win32api, win32con, win32clipboard
import subprocess
import re
import distutils.dir_util
import time, datetime
from zipfile import ZipFile as zip
from pastebin import submit
from PyQt4 import QtCore, QtGui, QtNetwork
from demo_options import Ui_DemoOptions
from windowUi import Ui_MainWindow
from splashUi import Ui_Splash
from demofile import demoFile
import elementtree.ElementTree as ET
import xml.etree.ElementTree as xml
from _winreg import *

class Splash(QtGui.QDialog):
        
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.splashui=Ui_Splash()
        self.splashui.setupUi(self)
        
        self.version = "3.0"
        self.programname = "Steam Tools"
        
        self.splashui.msg.stackUnder(self.splashui.title)
        self.splashui.bg.stackUnder(self.splashui.msg)
        
    def UpdateCheck(self):
        self.splashui.msg.setText("Getting URLs...")
        url = "http://steam-tools.googlecode.com/svn/version/current.xml"
        self.splashui.msg.setText("Reading Updates...")
        updatexml = xml.parse(urllib.urlopen(url))
        currentversion = updatexml.findall("update")

        for item in currentversion:
            latestversion = item.findtext('version')
            latestlink = item.findtext('link')
        
        if latestversion > self.version:
            self.splashui.msg.setText("This version is out of date.")
            response = QtGui.QMessageBox.question(self
                , "New Update Available"
                , self.programname + " v" + latestversion + " has been released!\nDo you wish to visit the download page now?"
                , QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if response == QtGui.QMessageBox.Yes:
                print str(self.TimeStamp()) + "Open Download Page"
                webbrowser.open_new_tab(str(latestlink))
            else:
                print str(self.TimeStamp()) + "Open Download Page"
                
        else:
            self.splashui.msg.setText("You have the latest update installed.")
            
#        self.splashui.msg.setText("Loading application...")
            
class Main(QtGui.QMainWindow):
    
    def mousePressEvent(self, event):
        self.offset = event.pos()
        QtGui.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)
        QtGui.QWidget.mousePressEvent(self, event)
        
    def __init__(self):
        #=======================================================================
        # Game Defs
        #=======================================================================
        self.CSS = "240"
        self.CSGO = "730"
        self.TF2 = "440"
        self.HL2DM = "320"
        self.CS = "10"
        self.DOTA2 = "570"
        self.L4D2 = "550"
        
        self.HeaderFileDownload = 0
        
        self.beta = 1
        QtGui.QMainWindow.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        #=======================================================================
        # makes an instance of scgui as kgui so use kgui to get the functions from scgui
        #=======================================================================
        self.kgui=scgui.klutchguitool()
        
        self.Splash=Splash()
        
        
        #=======================================================================
        # On launch find out if a skin is installed and refresh the array with info
        #=======================================================================
        self.kgui.getinstalledskin(self.kgui.steamacc)
        
        if self.kgui.settings.get('skin', 'installedskin') == "":
            print str(self.TimeStamp()) + "No Skin is installed on main __init__"
        else:
            print str(self.TimeStamp()) + "Found '" + self.kgui.settings.get('skin', 'installedskin') + "' installed on main __init__"
            
        print self.kgui.settings.get('main', 'gamepath')
        
        self.ui.BTN_skinFolder.clicked.connect(self.kgui.openskinsfolder)
        self.ui.btn_OpenGameFolder.clicked.connect(self.OpenGameFolder)
        self.ui.BTN_steampath.clicked.connect(self.GrabSteamRegs)
        self.ui.BTN_refreshteams.clicked.connect(self.resetteamtab)
        self.ui.BTN_updateTeams.clicked.connect(self.applyteamupdate)
        self.ui.BTN_swapSides.clicked.connect(self.clickedswapteams)  
        self.ui.cfglist.itemClicked.connect(self.printcfgItem)
        self.ui.dltypelist.itemClicked.connect(self.DownloadCatClicked)
        self.ui.BTN_updateCfg.clicked.connect(self.cfgfile_save)
        self.ui.BTN_uninstallSkin.clicked.connect(self.clickedremoveskin)
        self.ui.BTN_installSkin.clicked.connect(self.clickedinstallskin)
        self.ui.BTN_uninstallSkin.setEnabled(False)
        self.ui.BTN_installSkin.setEnabled(False)
        self.connect(self.ui.game, QtCore.SIGNAL('activated(QString)'), self.SetGame)
        self.ui.BTN_cfgadd.clicked.connect(self.CFGNew)
        self.ui.BTN_cfgdel.clicked.connect(self.CFGDelete)
        
        self.ui.cfglist.clear()
        self.RefreshCFGFiles()
        self.RefreshDemos()
        
        syntax.PythonHighlighter(self.ui.cfgEdit.document())
        self.ui.BGIMG.stackUnder(self.ui.tabWidget)
        self.ui.launchgame.clicked.connect(self.launchgame)
        self.ui.btn_close.clicked.connect(self.MakeQuit)
        self.ui.BTN_viewdemo.clicked.connect(self.launchdemo)
        self.ui.btn_feedback.clicked.connect(self.SubmitFeedback)
        
        self.kgui.settings.set('main', 'version', self.Splash.version)
        self.ui.btn_minimize.clicked.connect(self.mini)
        self.connect(self.ui.treedemos,QtCore.SIGNAL("itemClicked(QTreeWidgetItem * ,int)"),self.democlicked)
        self.connect(self.ui.treeDownloads,QtCore.SIGNAL("itemClicked(QTreeWidgetItem * ,int)"),self.downloadclicked)
        self.ui.btn_dldownload.clicked.connect(self.DownloadFileClicked)
        self.ui.BTN_cfgshare.clicked.connect(self.ShareCFG)
        self.ui.BTN_UpdateSettings.clicked.connect(self.UpdateSettings)
        self.GrabSteamRegs()
        self.RefreshSettings()
        
        if self.kgui.settings.get("main", "steamacc") == "":
            print str(self.TimeStamp()) + "no account set yet"
            self.ui.tabWidget.setCurrentIndex(5)
            self.ui.game.setCurrentIndex(-1)
#            QtGui.QMessageBox.information(self
#                , "First time launch"
#                , "Welcome to "+ self.Splash.programname +".\n\nIf this is the first time you using it you need to set up your Steam account path in the settings tab. If you have any problems or bugs please submit them to the google code page."
#                , QtGui.QMessageBox.Ok)
#            self.SteamAccountFolderDialog()
        else:
            self.GameToIndex()
        

        
        #=======================================================================
        # Connecting Tools tab functions to UI
        #=======================================================================
        self.ui.NewslistWidget.itemClicked.connect(self.AnnoucementClicked)
        self.ui.ToolButton_ChangeName.clicked.connect(self.ChangeSteamPicture)
        self.ui.ToolButton_EditProfile.clicked.connect(self.EditSteamProfile)
        self.ui.ToolButton_BackupGame.clicked.connect(self.BackupGame)
        self.ui.ToolButton_Defrag.clicked.connect(self.DefragGame)
        self.ui.ToolButton_Validate.clicked.connect(self.ValidateGame)
        self.ui.ToolButton_FriendsOnline.clicked.connect(self.SetFriendsOnline)
        self.ui.ToolButton_FriendsAway.clicked.connect(self.SetFriendsAway)
        self.ui.ToolButton_FriendsBusy.clicked.connect(self.SetFriendsBusy)
        self.ui.ToolButton_FriendsOffline.clicked.connect(self.SetFriendsOffline)
        self.ui.ToolButton_DeleteClientReg.clicked.connect(self.DeleteClientRegBlob)
        self.ui.ToolButton_SIDtoURL.clicked.connect(self.SIDtoURL)
        self.ui.CopySteamIDToClipbaord.clicked.connect(self.CopyIDToClip)
        self.ui.ToolButton_AddFriend.clicked.connect(self.AddToSteamFriends)
        self.ui.ToolButton_SendMessage.clicked.connect(self.MessageSteamUser)
        
        #=======================================================================
        # Set up XML API with webserver
        #=======================================================================
        self.DL_Cat_Configs = "http://myesports.co.uk/data/Configsxml.php"
        self.DL_Cat_Maps = "http://myesports.co.uk/data/Mapsxml.php"
        self.DL_Cat_Demos = "http://myesports.co.uk/data/Demosxml.php"
        self.DL_Cat_Skins = "http://myesports.co.uk/data/Skinsxml.php"
        self.AnnoucementsXML = "http://myesports.co.uk/data/Announcementsxml.php"
        self.xmlnews = xml.parse(urllib.urlopen(self.AnnoucementsXML))
        self.xmlnewsitems = self.xmlnews.findall("announcement")
        self.dldir = ""
        
        #=======================================================================
        # Banner Advert Control
        #=======================================================================
        #self.ui.BannerAdWebView.setUrl(QtCore.QUrl("http://myesports.co.uk/ads.html"))
        #self.ui.BannerAdWebView.connect(self.ui.BannerAdWebView, QtCore.SIGNAL('linkClicked(const QUrl&)'), self.linkClicked)
        self.CheckAnnouncements()
        
    def linkClicked(self, url):
        webbrowser.open_new_tab(url)
       
    def AnnoucementClicked(self):
        for item in self.xmlnewsitems:
            if item.findtext('Title') == str(self.ui.NewslistWidget.currentItem().text()):
                self.GenerateNewsItem(item.findtext('Title'), item.findtext('Author'), item.findtext('Published'), item.findtext('Message'))
                if item.attrib['TYPE'].startswith("UPDATE"):
                    updateversion = item.attrib['TYPE'].split("-")
                    if updateversion[1] > self.Splash.version:
                        versioncount = updateversion[1]

    def CheckAnnouncements(self):
        print str(self.TimeStamp()) + "Checking Announcements" 
        #print "Found " + str(len(lst))
        for item in self.xmlnewsitems:
            if item.findtext('Banner') == self.CSS: #CSS
                icon = ":/icons/icons/games/css.jpg"
            elif item.findtext('Banner') == self.CSGO: #CSGO
                icon =  ":/icons/icons/games/csgo.jpg"
            elif item.findtext('Banner') == self.TF2: #TF2
                icon =  ":/icons/icons/games/tf2.jpg"
            elif item.findtext('Banner') == self.HL2DM: #HL2SM
                icon =  ":/icons/icons/games/hl2dm.jpg"
            elif item.findtext('Banner') == self.CS: #CS 1.6
                icon =  ":/icons/icons/games/cs.jpg"
            elif item.findtext('Banner') == self.DOTA2: #DOTA2
                icon =  ":/icons/icons/games/dota2.jpg"
            elif item.findtext('Banner') == self.L4D2: #L4D2
                icon =  ":/icons/icons/games/l4d2.jpg"
            else:
                icon =  ":/16/icons/16/file_extension_txt.png"
            self.ui.NewslistWidget.addItem(QtGui.QListWidgetItem(QtGui.QIcon(icon),str(item.findtext('Title'))))
    
    def GenerateNewsItem(self, title, author, date, message):
        html = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\"><html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\"><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">"+title+"</span></p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">"+date+" - </span><span style=\" font-size:10pt; font-style:italic;\">"+author+"</span></p><p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600;\"><br /></p><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">"+message+"</span></p><p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p><p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"       
        self.ui.NewstextEdit.clear()
        self.ui.NewstextEdit.insertHtml(html)
        return html
        
    def OpenGameFolder(self):
        subprocess.Popen('explorer ' + os.path.normpath(self.kgui.settings.get('main', 'gamepath')))
    
    def ChangeToScriptDir(self):
        if hasattr(sys,'frozen'): # only when running in py2exe this exists
            base = sys.prefix
        else: # otherwise this is a regular python script
            base = os.path.dirname(os.path.realpath(__file__))
        print base
        return base
       
    def DownloadFileClicked(self):
        self.downloadChunks(self.DLFile, self.DLFileID)
        
    def DownloadCatClicked(self):
        self.ui.BTN_uninstallSkin.setEnabled(False)
        self.ui.BTN_installSkin.setEnabled(False)
        
        tv = self.ui.treeDownloads
        tv.clear()
        tv.setColumnCount(0)
        cat = str(self.ui.dltypelist.currentItem().text())
        
        scriptpath = self.ChangeToScriptDir()
        self.dldir = os.path.join(scriptpath, 'Downloads', cat, self.kgui.settings.get('main', 'game'))
        
        self.ui.DownloadProgressBar.setFormat("Retrieving data from " + cat + ". Please wait...")
        
        if cat == "Configs":            
            tv.headerItem().setText(0, "")
            tv.headerItem().setText(1, "Player")
            tv.headerItem().setText(2, "Config")
            tv.headerItem().setText(3, "Uploaded")
            tv.headerItem().setText(4, "File")
            self.HeaderFileDownload = 4
            tv.setColumnWidth(0,22)      # Small Icon
            tv.setColumnWidth(1,150)
            tv.setColumnWidth(2,150)
            
            tree = xml.parse(urllib.urlopen(self.DL_Cat_Configs))
            lst = tree.findall("config")
            #print "Found " + str(len(lst))
            for item in lst:
                if item.attrib['Game'] == self.kgui.settings.get('main', 'game'):
                    tvitem = QtGui.QTreeWidgetItem(0)
                    tvitem.setData(0,0,item.findtext('ID'))
                    tvitem.setIcon(0, QtGui.QIcon(self.GetGameIcon()))
                    tvitem.setIcon(1, QtGui.QIcon(":/flags/icons/flags/"+item.findtext('Country')+".gif"))
                    tvitem.setData(1,0,item.findtext('Username'))
                    tvitem.setData(2,0,item.findtext('Filename'))
                    tvitem.setData(3,0,item.findtext('Uploaded'))
                    tvitem.setData(4,0,item.findtext('File'))
                    tv.addTopLevelItem(tvitem)
            tv.sortByColumn(1)
            
        elif cat == "Replays":
            tv.headerItem().setText(0, "")
            tv.headerItem().setText(1, "Date")
            tv.headerItem().setText(2, "Home")
            tv.headerItem().setText(3, "Away")
            tv.headerItem().setText(4, "Map")
            tv.headerItem().setText(5, "Event")
            tv.headerItem().setText(6, "File")
            self.HeaderFileDownload = 6
            tv.setColumnWidth(0,22)      # Small Icon
            tv.setColumnWidth(1,70)
            tv.setColumnWidth(2,100)
            tv.setColumnWidth(3,100)
            tv.setColumnWidth(4,70)
            tv.setColumnWidth(5,150)
            
            tree = xml.parse(urllib.urlopen(self.DL_Cat_Demos))
            lst = tree.findall("demo")
            #print "Found " + str(len(lst))
            for item in lst:
                if item.attrib['Game'] == self.kgui.settings.get('main', 'game'):
                    tvitem = QtGui.QTreeWidgetItem(0)
                    tvitem.setData(0,0,item.findtext('ID'))
                    tvitem.setIcon(0, QtGui.QIcon(self.GetGameIcon()))
                    tvitem.setData(1,0,item.findtext('Date'))
                    tvitem.setData(2,0,item.findtext('Home'))
                    tvitem.setIcon(2, QtGui.QIcon(":/flags/icons/flags/"+item.findtext('HomeCountry')+".gif"))
                    tvitem.setData(3,0,item.findtext('Away'))
                    tvitem.setIcon(3, QtGui.QIcon(":/flags/icons/flags/"+item.findtext('AwayCountry')+".gif"))
                    tvitem.setData(4,0,item.findtext('Map'))
                    tvitem.setData(5,0,item.findtext('Event'))
                    #tvitem.setData(6,0,item.findtext('File'))
                    tv.addTopLevelItem(tvitem)
            tv.sortByColumn(1)
            
        elif cat == "Maps":
            tv.headerItem().setText(0, "")
            tv.headerItem().setText(1, "Type")
            tv.headerItem().setText(2, "Name")
            tv.headerItem().setText(3, "File")
            self.HeaderFileDownload = 3
            tv.setColumnWidth(0,22)      # Small Icon
            tv.setColumnWidth(1,50)
            tv.setColumnWidth(2,150)
            
            tree = xml.parse(urllib.urlopen(self.DL_Cat_Maps))
            lst = tree.findall("map")
            #print "Found " + str(len(lst))
            for item in lst:
                if item.attrib['Game'] == self.kgui.settings.get('main', 'game'):
                    itemindlpath = os.path.join(self.kgui.settings.get('main', 'gamepath'),"maps",item.findtext('Name')+".bsp")
                    tvitem = QtGui.QTreeWidgetItem(0)
                    tvitem.setData(0,0,item.findtext('ID'))
                    if os.path.exists(itemindlpath):
                        tvitem.setIcon(0, QtGui.QIcon(self.GetGameIcon()))
                    else:
                        tvitem.setIcon(0, QtGui.QIcon(":/icons/icons/new/download.png"))
                    tvitem.setData(1,0,item.findtext('Type'))
                    tvitem.setData(2,0,item.findtext('Name'))
                    tvitem.setData(3,0,item.findtext('File'))
                    tv.addTopLevelItem(tvitem)
                    
        elif cat == "GUI":
            tv.headerItem().setText(0, "Name")
            tv.headerItem().setText(1, "Author")
            tv.headerItem().setText(2, "Uploaded")
            tv.headerItem().setText(3, "File")
            self.HeaderFileDownload = 3
            tv.setColumnWidth(0,250)      # Small Icon
            tv.setColumnWidth(1,90)
            tv.setColumnWidth(2,70)
            
            tree = xml.parse(urllib.urlopen(self.DL_Cat_Skins))
            lst = tree.findall("skin")
            #print "Found " + str(len(lst))
            for item in lst:
                if item.attrib['Game'] == self.kgui.settings.get('main', 'game'):
                    itemindlpath = os.path.join(self.dldir, item.findtext('Name'))

                    tvitem = QtGui.QTreeWidgetItem(0)
                    tvitem.setData(0,0,item.findtext('ID'))
                    tvitem.setIcon(0, QtGui.QIcon(self.GetGameIcon()))
                    tvitem.setData(0,0,item.findtext('Name'))
                    tvitem.setIcon(1, QtGui.QIcon(":/flags/icons/flags/"+item.findtext('AuthorCountry')+".gif"))
                    tvitem.setData(1,0,item.findtext('Author'))
                    tvitem.setData(2,0,item.findtext('Uploaded'))
                    if os.path.exists(itemindlpath):
                        if item.findtext('Name') == self.kgui.settings.get('skin', 'installedskin'):
                            tvitem.setData(3,0,"Installed")
                            tvitem.setIcon(0, QtGui.QIcon(self.GetGameIcon()))
                        else:
                            tvitem.setData(3,0,"Downloaded")
                            tvitem.setIcon(0, QtGui.QIcon(":/icons/icons/new/wrench--arrow.png"))
                    else:
                        tvitem.setIcon(0, QtGui.QIcon(":/icons/icons/new/download.png"))
                        tvitem.setData(3,0,item.findtext('File'))
                    tv.addTopLevelItem(tvitem)
            tv.sortByColumn(4)
        self.ui.DownloadProgressBar.setFormat("")
            
    def TimeStamp(self):
        stampedtime = str(time.strftime("[%H:%M:%S] "))
        return stampedtime
        
    def CopyIDToClip(self):
        steamid = str(self.ui.steamid.text())
        self.CopyToClipboard(steamid)
        self.ui.CopySteamIDToClipbaord.setText("Copied")
        
        
    def SIDtoURL(self):
        steamid = str(self.ui.steamidtool.text())
        m = re.match(r'STEAM_[0-1]:[0-1]:[0-9]+$', steamid)
        if m:
            steamid = steamid[8:].split(':')
            steamid = str(int(steamid[0]) + int(steamid[1]) * 2 + 76561197960265728)
            self.steamid64 = steamid
            print str(self.TimeStamp()) + "Converted 64ID: " + steamid
            self.ui.steamidtool.setText(str(steamid))
            url = "http://steamcommunity.com/profiles/" + str(steamid)
            webbrowser.open_new_tab(url)
            self.CopyToClipboard(url)
        else:
            self.ui.steamidtool.setText("Bad ID")
        
    def SubmitFeedback(self):
        webbrowser.open_new_tab("http://twitter.com/NedKnowles")
    def ChangeSteamPicture(self):
        webbrowser.open_new_tab("steam://open/settings/friends/")
    def EditSteamProfile(self):
        webbrowser.open_new_tab("steam://url/SteamIDEditPage/")
    def ReadUpdateNews(self):
        webbrowser.open_new_tab("steam://appnews/"+ str(self.kgui.settings.get('main', 'game'))+"/")
    def BackupGame(self):
        webbrowser.open_new_tab("steam://backup/"+ str(self.kgui.settings.get('main', 'game'))+"/")
    def DefragGame(self):
        webbrowser.open_new_tab("steam://defrag/"+ str(self.kgui.settings.get('main', 'game'))+"/")
    def ValidateGame(self):
        webbrowser.open_new_tab("steam://validate/"+ str(self.kgui.settings.get('main', 'game'))+"/")
        
        ##Steam Friends
    def SetFriendsOnline(self):
        webbrowser.open_new_tab("steam://friends/status/online/")
    def SetFriendsAway(self):
        webbrowser.open_new_tab("steam://friends/status/away/")
    def SetFriendsBusy(self):
        webbrowser.open_new_tab("steam://friends/status/busy/")
    def SetFriendsOffline(self):
        webbrowser.open_new_tab("steam://friends/status/offline/")
    def AddToSteamFriends(self):
        steamid = str(self.ui.steamidtool.text())
        m = re.match(r'STEAM_[0-1]:[0-1]:[0-9]+$', steamid)
        if m:
            steamid = steamid[8:].split(':')
            steamid = str(int(steamid[0]) + int(steamid[1]) * 2 + 76561197960265728)
            self.steamid64 = steamid
            print str(self.TimeStamp()) + "Added User " + steamid + " to Steam Friends"
        webbrowser.open_new_tab("steam://friends/add/"+steamid+"/")
        
    def MessageSteamUser(self):
        steamid = str(self.ui.steamidtool.text())
        m = re.match(r'STEAM_[0-1]:[0-1]:[0-9]+$', steamid)
        if m:
            steamid = steamid[8:].split(':')
            steamid = str(int(steamid[0]) + int(steamid[1]) * 2 + 76561197960265728)
            self.steamid64 = steamid
            print str(self.TimeStamp()) + "Messaged User " + steamid + " on Steam"
        webbrowser.open_new_tab("steam://friends/message/"+steamid+"/")
        
    def TDeleteBlob(self):
        print str(self.TimeStamp()) + "TDeleteBlob"
    
    def GameToIndex(self):
        print str(self.TimeStamp()) + "GAMETOINDEX"
        gameid = self.kgui.settings.get('main', 'game')
        if gameid == self.CSS:
            self.ui.game.setCurrentIndex(0)
            print str(self.TimeStamp()) + "CSS"
        elif gameid == self.CSGO:
            self.ui.game.setCurrentIndex(1)
            print str(self.TimeStamp()) + "CSGO"
        elif gameid == self.TF2:
            self.ui.game.setCurrentIndex(2)
            print str(self.TimeStamp()) + "TF2"
        elif gameid == self.HL2DM:
            self.ui.game.setCurrentIndex(3)
            print str(self.TimeStamp()) + "HL2DM"
        elif gameid == self.CS:
            self.ui.game.setCurrentIndex(4)
            print str(self.TimeStamp()) + "CS"
        elif gameid == self.DOTA2:
            self.ui.game.setCurrentIndex(5)
            print str(self.TimeStamp()) + "DOTA2"
        elif gameid == self.L4D2:
            self.ui.game.setCurrentIndex(6)
            print str(self.TimeStamp()) + "L4D2"
        else:
            self.ui.game.setCurrentIndex(-1)
            print str(self.TimeStamp()) + "None"
            
    def RefreshSettings(self):
        print str(self.TimeStamp()) + "RefreshSettings"
        
        self.GrabSteamRegs()
        
        gameoptions = self.kgui.settings.get('launchoptions', 'game')
        demooptions = self.kgui.settings.get('launchoptions', 'demo')
        msid = self.kgui.settings.get('user', 'steamid')
        self.ui.gameoptions.setText(str(gameoptions))
        self.ui.demooptions.setText(str(demooptions))
        
        if not msid == "":
            self.GetPlayerName(str(msid))
        
        self.ui.steamid.setText(str(msid))
    
    def UpdateSettings(self):
        print str(self.TimeStamp()) + " >>>>>>>>>>>>>> UpdateSettings"
        sid = self.ui.steamid.text()
        goptions = self.ui.gameoptions.text()
        doptions = self.ui.demooptions.text()
        
        cfgfile = open("settings.ini", "w")
        if not sid == "":
            self.kgui.settings.set('user', 'steamid', str(sid))
        self.kgui.settings.set('launchoptions', 'game', str(goptions))
        self.kgui.settings.set('launchoptions', 'demo', str(doptions))
        
        self.kgui.settings.write(cfgfile)
        cfgfile.close()
        
        print str(self.TimeStamp()) + "Setting Launch Options: " + str(goptions)
        print str(self.TimeStamp()) + "Setting Demo Options: " + str(doptions)
        
        self.GetPlayerName(str(sid))
        
        print str(self.TimeStamp()) + " <<<<<<<<<<<<<< UpdateSettings"
        
    def GetPlayerName(self, steamid):
        print str(self.TimeStamp()) + "GetPlayerName"
        print str(self.TimeStamp()) + "Steam ID: " + steamid
        m = re.match(r'STEAM_[0-1]:[0-1]:[0-9]+$', steamid)
        if m:
            steamid = steamid[8:].split(':')
            steamid = str(int(steamid[0]) + int(steamid[1]) * 2 + 76561197960265728)
            self.steamid64 = steamid
            print str(self.TimeStamp()) + "Converted 64ID: " + steamid
        else:
            self.customurl = steamid
        
#        STEAM_0:0:26262312
#        76561198012790352
# http://steamcommunity.com/profiles/76561198012790352/?xml=1&l=english
        
             
#        try:
#            tree = ET.parse(urllib.urlopen("http://steamcommunity.com/profiles/"+steamid+"/?xml=1&l=english"))
#            steamplayer = tree.findtext("steamID")
#            if not steamplayer == "None":
#                self.kgui.settings.set('user', 'name', str(steamplayer))
#                print str(self.TimeStamp()) + "Player set to " + str(steamplayer)
#                if self.beta == 1:
#                    self.setWindowTitle(self.Splash.programname + " " + self.Splash.version + " BETA - " + self.kgui.settings.get('user', 'name'))
#                else:
#                    self.setWindowTitle(self.Splash.programname + " " + self.Splash.version + " - " + self.kgui.settings.get('user', 'name'))
#                
#                """QtGui.QMessageBox.information(self
#                    , "Steam ID Saved"
#                    , "Player name set to " +str(steamplayer)+ ". This will be used when uploading replays and configs."
#                    , QtGui.QMessageBox.Ok)"""
#            else:
#                print str(self.TimeStamp()) + "Error"
#        except:
#            print str(self.TimeStamp()) + "Error: Cannot get feed"
#            

    def ShareCFG(self):
        print str(self.TimeStamp()) + "ShareCFG"
        cfg = str((self.ui.cfglist.currentItem().text()))
        if not str(self.ui.steamid.text()) == "":
            url = submit(unicode(self.ui.cfgEdit.toPlainText()),
                 paste_format="javascript",
                 paste_name=self.kgui.settings.get('user', 'name') + " - " + cfg,
                 paste_expire_date="N")
            ident = re.search("http://pastebin.com/(.*)", url)
            fullurl = "http://pastebin.com/raw.php?i=" + str(ident.group(1))
            print fullurl
            webbrowser.open_new_tab(fullurl)
            QtGui.QMessageBox.information(self
                , "Config Uploaded"
                , cfg + " was uploaded!\nA link has been copied to your clipboard.\nTo confirm enter the captcha in your browser."
                , QtGui.QMessageBox.Ok)
            self.CopyToClipboard(fullurl)
        else:
            QtGui.QMessageBox.warning(self
                , "Sorry"
                , "We cannot upload " + cfg + " yet!\nPlease enter your Steam ID into the settings tab and try again."
                , QtGui.QMessageBox.Ok)
            print str(self.TimeStamp()) + "Steam ID Not Found"
        
    def CopyToClipboard(self, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_TEXT, data)
        print str(self.TimeStamp()) + "Data was copied to clipboard"
        win32clipboard.CloseClipboard()
    
    def CheckClipboard(self):
        print str(self.TimeStamp()) + "CheckClipboard"
        win32clipboard.OpenClipboard() 
        contents=win32clipboard.GetClipboardData(win32con.CF_TEXT) 
        win32clipboard.CloseClipboard() 
        m = re.search('connect\s([0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]):([0-9]?[0-9]?[0-9]?[0-9]?[0-9]);password\s(.*)', contents)
        print str(self.TimeStamp()) + "IP:" + str(m.group(1))
        print str(self.TimeStamp()) + "PORT:" + str(m.group(2))
        print str(self.TimeStamp()) + "PASSWORD:" + str(m.group(3))
        print contents 
        
    def OpenDemoOptions(self):
        print str(self.TimeStamp()) + "OpenDemoOptions"
        demogui=QtGui.QDialog()
        demoui=Ui_DemoOptions()
        demoui.setupUi(demogui)
        demogui.open()

    def mini(self):
        self.showMinimized()
        
    def setWindowTitle(self, text):
        print str(self.TimeStamp()) + "setWindowTitle to " + str(text)
        self.ui.apptitle.setText(text)

    """def steamadd(self):
        webbrowser.open_new_tab("steam://friends/add/76561198012790352")
    def steamview(self):
        webbrowser.open_new_tab("steam://url/SteamIDPage/76561198012790352")
    def openchangelog(self):
        webbrowser.open_new_tab("http://www.scgui.com/about")
    def openyoutube(self):
        webbrowser.open_new_tab("http://www.youtube.com/user/j5eddie")
    def opentwitter(self):
        webbrowser.open_new_tab("http://twitter.com/NedKnowles")
    def opentumblr(self):
        webbrowser.open_new_tab("http://www.scgui.com")
    
    def gototab0(self):
        self.ui.tabWidget.setCurrentIndex(0)
    def gototab1(self):
        self.ui.tabWidget.setCurrentIndex(1)
    def gototab2(self):
        self.ui.tabWidget.setCurrentIndex(2)
    def gototab3(self):
        self.ui.tabWidget.setCurrentIndex(3)
    def gototab4(self):
        self.ui.tabWidget.setCurrentIndex(4)"""

    def MakeQuit(self):
        sys.exit()
        
    def DelSettings(self):
        print str(self.TimeStamp()) + "DelSettings"
        if os.path.exists(self.kgui.settingsfile):
            response = QtGui.QMessageBox.question(self
                , "Reset"
                , "Are you sure you want to reset your settings?"
                , QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if response == QtGui.QMessageBox.Yes:
                os.remove(self.kgui.settingsfile)
                self.RefreshCFGFiles()
                self.ui.cfglist.clear()
                self.RefreshCFGFiles()
                self.RefreshDemos()       
                self.ui.steampath.setText("")
#                if self.beta == 1:
#                    self.setWindowTitle(self.Splash.programname + " " + self.Splash.version + " (Private Beta)")
#                else:
#                    self.setWindowTitle(self.Splash.programname + " " + self.Splash.version + "")
                self.ui.tabWidget.setCurrentIndex(4)
        else:
            print str(self.TimeStamp()) + "No settings exist yet"
            QtGui.QMessageBox.question(self
                , "File doesn't exist"
                , "The settings file doesn't exist yet."
                , QtGui.QMessageBox.Ok)
            
 
        
    def CFGNew(self):
        text, ok = QtGui.QInputDialog.getText(self, 'New Config', 
            'Enter a filename with an extention')
        newcfgpath = os.path.join(self.kgui.settings.get('main', 'cfgpath') + "/" + str(text))
        if ok:
            if os.path.exists(newcfgpath):
                QtGui.QMessageBox.warning(self
                    , "Warning"
                    , "The config " + str(text) + " already exists. Choose a different name."
                    , QtGui.QMessageBox.Ok)
            else:
                f = open(newcfgpath,'w')
                f.write("// " + str(text) + " created by " + self.Splash.programname + " " + self.Splash.version + "\n\n")
                f.close()
                self.ui.cfglist.clear()
                self.RefreshCFGFiles()
        
    def CFGDelete(self):
        response = QtGui.QMessageBox.warning(self
            , "Delete config file"
            , "Are you sure you want to permanently delete this file?"
            , QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if response == QtGui.QMessageBox.Yes:
            cfgpathrel = self.kgui.settings.get('main', 'cfgpath')
            filepath = os.path.join(cfgpathrel, str(self.ui.cfglist.currentItem().text()))
            os.remove(filepath)
            print str(self.TimeStamp()) + "Deleted: " + filepath
            self.ui.cfgEdit.clear()
            self.ui.cfglist.clear()
            self.RefreshCFGFiles()            
        
    def RefreshGameCombo(self):
        print str(self.TimeStamp()) + "RefreshGameCombo (Need to fix!)"
        #self.ui.game.setCurrentIndex(int(self.kgui.settings.get('main', 'game')))
    
    def RefreshDemos(self):
        print str(self.TimeStamp()) + "RefreshDemos"
        #Set Demo column sizes
        self.ui.treedemos.sortByColumn(2)           # Sorts by filename
        self.ui.treedemos.setHeaderLabel("")
        self.ui.treedemos.setColumnWidth(0,22)      # Small Icon
        self.ui.treedemos.setColumnWidth(1,120)     # Date
        self.ui.treedemos.setColumnWidth(2,180)     # File
        if not self.kgui.settings.get('main', 'gamepath') == "":
            tree = self.ui.treedemos
            demopath = os.path.join(self.kgui.settings.get("main", "gamepath"))
            if not demopath == "":
                demos = []
                dirList=os.listdir(demopath)
                for fname in dirList:
                    #print fname
                    if fname.endswith(".dem"):
                        demos.append(fname)
            tree.clear()
            for halflifedem in demos:
                target = os.path.join(self.kgui.settings.get('main', 'gamepath'), halflifedem)
                #print target
                if self.kgui.settings.get('main', 'game') == "10":
                    Demo = demoFile(target, "HL1")
                else:
                    Demo = demoFile(target, "HL2")
                item = QtGui.QTreeWidgetItem(0)
                demosize = os.path.getsize(target)
                nicesize = self.prettySize(demosize)
                datetime = Demo.gettime(target)
                item.setIcon(0, QtGui.QIcon(self.GetGameIcon()))
                if Demo.client == "SourceTV Demo":
                    item.setIcon(2, QtGui.QIcon(":/icons/icons/games/iconVideo.png"))
                    item.setData(5,0,"Source TV")
                else:
                    item.setIcon(2, QtGui.QIcon(":/icons/icons/games/iconFriends.png"))
                    item.setData(5,0,Demo.client)
                item.setData(1,0,datetime)
                item.setData(2,0,halflifedem)        # Filename
                item.setData(3,0,Demo.map)      # Map
                item.setData(4,0,Demo.getlength()) # Time
                item.setData(6,0,Demo.server)
                item.setData(7,0,nicesize)
                
                print ">>>>>>>> Demo"
                print "header: " + str(Demo.header)
                print "demoProtocol: " + str(Demo.demoProtocol)
                print "networkProtocol: " + str(Demo.networkProtocol)
                print "map: " + str(Demo.map)
                print "game: " + str(Demo.game)
                print "mapcrc: " + str(Demo.mapcrc)
                print "server: " + str(Demo.server)
                print "client: " + str(Demo.client)
                print "length: " + str(Demo.length)
                print "playback: " + str(Demo.playback)
                print "ticks: " + str(Demo.ticks)
                print "frames: " + str(Demo.frames)
                print "<<<<<<<< Demo\n"
                
                tree.addTopLevelItem(item)
    
    def GetGameIcon(self):
        #print str(self.TimeStamp()) + "GetGameIcon"
        game = self.kgui.settings.get('main', 'game')
        if game == self.CSS: #CSS
            return ":/icons/icons/games/css.jpg"
        elif game == self.CSGO: #CSGO
            return ":/icons/icons/games/csgo.jpg"
        elif game == self.TF2: #TF2
            return ":/icons/icons/games/tf2.jpg"
        elif game == self.HL2DM: #HL2SM
            return ":/icons/icons/games/hl2dm.jpg"
        elif game == self.CS: #CS 1.6
            return ":/icons/icons/games/cs.jpg"
        elif game == self.DOTA2: #DOTA2
            return ":/icons/icons/games/dota2.jpg"
        elif game == self.L4D2: #L4D2
            return ":/icons/icons/games/l4d2.jpg"
 
    def prettySize(self, size):
        suffixes = [("B",2**10), ("K",2**20), ("MB",2**30), ("GB",2**40), ("T",2**50)]
        for suf, lim in suffixes:
            if size > lim:
                continue
            else:
                rounded = round(size/float(lim/2**10),0).__str__()
                rounded = rounded[:-2]
                return rounded + " " + suf
            
    def SetGame(self, text):
        self.cspath=self.kgui.settings.get('main', 'gamepath')
        cfgfile = open("settings.ini",'w')
        
        if text == "Counter-Strike: Source": # Index 0
            gamepathsel = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\Counter-Strike Source\cstrike\cfg")
            print str(self.TimeStamp()) + "Game Path = " + gamepathsel
            if os.path.exists(gamepathsel): 
                self.kgui.settings.set('main', 'game', '240')
                pathjoined = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\Counter-Strike Source\cstrike")
                self.kgui.settings.set('main', 'gamepath', pathjoined)
                self.kgui.settings.set('main', 'cfgpath', os.path.join(pathjoined, "cfg"))
                print str(self.TimeStamp()) + "Game set to css"
                self.RefreshCFGFiles()
                self.ui.cfglist.clear()
                self.RefreshCFGFiles()
                self.RefreshDemos()
            else:
                QtGui.QMessageBox.information(self
                    , "Information"
                    , "Counter-Strike: Source is not installed!"
                    , QtGui.QMessageBox.Ok)
                self.RefreshGameCombo()
            
        if text == "Counter-Strike: Global Offensive": # Index 1
            gamepathsel = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\Counter-Strike Global Offensive\csgo\cfg")
            print str(self.TimeStamp()) + "Game Path = " + gamepathsel
            if os.path.exists(gamepathsel): 
                self.kgui.settings.set('main', 'game', '730')
                pathjoined = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\Counter-Strike Global Offensive\csgo")
                self.kgui.settings.set('main', 'gamepath', pathjoined)
                self.kgui.settings.set('main', 'cfgpath', os.path.join(pathjoined, "cfg"))
                
                print str(self.TimeStamp()) + "Game set to csgo"
                self.RefreshCFGFiles()
                self.ui.cfglist.clear()
                self.RefreshCFGFiles()
                self.RefreshDemos()
            else:
                QtGui.QMessageBox.information(self
                    , "Information"
                    , "Counter-Strike: Global Offensive is not installed!"
                    , QtGui.QMessageBox.Ok)
                self.RefreshGameCombo()
            
        if text == "Team Fortress 2": # Index 2
            gamepathsel = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\Team Fortress 2\tf\cfg")
            print str(self.TimeStamp()) + "Game Path = " + gamepathsel
            if os.path.exists(gamepathsel): 
                self.kgui.settings.set('main', 'game', '440')
                pathjoined = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\Team Fortress 2\tf")
                self.kgui.settings.set('main', 'gamepath', pathjoined)
                self.kgui.settings.set('main', 'cfgpath', os.path.join(pathjoined, "cfg"))
                print str(self.TimeStamp()) + "Game set to tf2"
                self.RefreshCFGFiles()
                self.ui.cfglist.clear()
                self.RefreshCFGFiles()
                self.RefreshDemos()
            else:
                QtGui.QMessageBox.information(self
                    , "Information"
                    , "Team Fortress 2 is not installed!"
                    , QtGui.QMessageBox.Ok)
                self.RefreshGameCombo()
            
        if text == "Half-Life 2: Deathmatch": # Index 3
            gamepathsel = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\half-life 2 deathmatch\hl2mp\cfg")
            print str(self.TimeStamp()) + "Game Path = " + gamepathsel
            if os.path.exists(gamepathsel): 
                self.kgui.settings.set('main', 'game', '320')
                pathjoined = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\half-life 2 deathmatch\hl2mp")
                self.kgui.settings.set('main', 'gamepath', pathjoined)
                self.kgui.settings.set('main', 'cfgpath', os.path.join(pathjoined, "cfg"))
                print str(self.TimeStamp()) + "Game set to hl2dm"
                self.RefreshCFGFiles()
                self.ui.cfglist.clear()
                self.RefreshCFGFiles()
                self.RefreshDemos()
            else:
                QtGui.QMessageBox.information(self
                    , "Information"
                    , "Half-Life 2: Deathmatch is not installed!"
                    , QtGui.QMessageBox.Ok)
                self.RefreshGameCombo()
            
        if text == "Counter-Strike": # Index 4
            gamepathsel = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\Half-Life\cstrike")
            print str(self.TimeStamp()) + "Game Path = " + gamepathsel
            if os.path.exists(gamepathsel): 
                self.kgui.settings.set('main', 'game', '10')
                pathjoined = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\Half-Life\cstrike")
                self.kgui.settings.set('main', 'gamepath', pathjoined)
                self.kgui.settings.set('main', 'cfgpath', pathjoined)
                print str(self.TimeStamp()) + "Game set to cs"
                self.RefreshCFGFiles()
                self.RefreshDemos()
            else:
                QtGui.QMessageBox.information(self
                    , "Information"
                    , "Counter-Strike 1.6 is not installed!"
                    , QtGui.QMessageBox.Ok)
                self.RefreshGameCombo()
            
        if text == "Dota 2": # Index 5
            gamepathsel = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\dota 2\dota\cfg")
            print str(self.TimeStamp()) + "Game Path = " + gamepathsel
            if os.path.exists(gamepathsel): 
                self.kgui.settings.set('main', 'game', '570')
                pathjoineddota = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\dota 2\dota")
                self.kgui.settings.set('main', 'gamepath', pathjoineddota)
                self.kgui.settings.set('main', 'cfgpath', os.path.join(pathjoineddota, "cfg"))
                print str(self.TimeStamp()) + "Game set to dota2beta"
                self.RefreshCFGFiles()
                self.ui.cfglist.clear()
                self.RefreshCFGFiles()
                self.RefreshDemos()
            else:
                QtGui.QMessageBox.information(self
                    , "Information"
                    , "Dota 2 Beta is not installed!"
                    , QtGui.QMessageBox.Ok)
                self.RefreshGameCombo()
            
        if text == "Left 4 Dead 2": # Index 6
            gamepathsel = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\left 4 dead 2\left4dead2\cfg")
            print str(self.TimeStamp()) + "Game Path = " + gamepathsel
            if os.path.exists(gamepathsel): 
                self.kgui.settings.set('main', 'game', '550')
                pathjoineddota = os.path.join(self.kgui.settings.get('main', 'steamacc'), "steamapps\common\left 4 dead 2\left4dead2")
                self.kgui.settings.set('main', 'gamepath', pathjoineddota)
                self.kgui.settings.set('main', 'cfgpath', os.path.join(pathjoineddota, "cfg"))
                print str(self.TimeStamp()) + "Game set to l4d2"
                self.RefreshCFGFiles()
                self.ui.cfglist.clear()
                self.RefreshCFGFiles()
                self.RefreshDemos()
            else:
                QtGui.QMessageBox.information(self
                    , "Information"
                    , "Left 4 Dead 2 is not installed!"
                    , QtGui.QMessageBox.Ok)
                self.RefreshGameCombo()
            
        self.kgui.settings.write(cfgfile)
        cfgfile.close() 
        
    def listdemos(self):
        #print str(self.TimeStamp()) + "demoooo"
        row = 1
        actualrow = 1
        self.ui.demotree.setColumnWidth(0, 30)
    
    
    def printcfgItem(self, item):
        """These two are equivalent"""
        #print(item.text())
        #print(self.ui.cfglist.currentItem().text())
        self.cfgrefresh(str((self.ui.cfglist.currentItem().text())))
                       
    def RefreshCFGFiles(self): 
        self.ui.cfgEdit.clear()
        self.ui.cfglist.clear()
        cfgpath = os.path.normpath(os.path.join(self.kgui.settings.get("main", "cfgpath")))
        print cfgpath
        if cfgpath == "":
            print str(self.TimeStamp()) + "No config path found"
        else:
            if os.path.exists(cfgpath):
                dirList=os.listdir(cfgpath)
                for fname in dirList:
                    if fname.endswith("cfg"):
                        self.ui.cfglist.addItem(QtGui.QListWidgetItem(QtGui.QIcon(":/icons/icons/games/iconWishlist.png"),fname))
                    elif fname.endswith("rc"):
                        self.ui.cfglist.addItem(QtGui.QListWidgetItem(QtGui.QIcon(":/icons/icons/games/iconInventory.png"),fname))
                    elif fname.endswith("vdf"):
                        self.ui.cfglist.addItem(QtGui.QListWidgetItem(QtGui.QIcon(":/icons/icons/games/iconInventory.png"),fname))
            
    def GrabSteamRegs(self):
        print str(self.TimeStamp()) + "Getting Steam Keys from Registry"
        steamhkey = OpenKey(HKEY_CURRENT_USER, r'Software\\Valve\\Steam', 0, KEY_ALL_ACCESS)
        self.SteamPath = os.path.abspath(QueryValueEx(steamhkey, "SteamPath")[0])
        self.LastGameNameUsed = QueryValueEx(steamhkey, "LastGameNameUsed")[0]
        self.ui.steampath.setText(self.SteamPath)
        cfgfile = open("settings.ini", "w")
        self.kgui.settings.set('main', 'steamacc', str(self.SteamPath))
        self.kgui.settings.set('user', 'name', str(self.LastGameNameUsed))
        self.kgui.settings.write(cfgfile)
        cfgfile.close()
        print str(self.TimeStamp()) + "Player set to " + str(self.LastGameNameUsed)
        if self.beta == 1:
            self.setWindowTitle(self.Splash.programname + " " + self.Splash.version + " BETA - " + self.kgui.settings.get('user', 'name'))
        else:
            self.setWindowTitle(self.Splash.programname + " " + self.Splash.version + " - " + self.kgui.settings.get('user', 'name'))  
        
    def SteamAccountFolderDialog(self):
        fname = QtGui.QFileDialog.getExistingDirectory(self, "Choose your steam account folder", 
                "/Program Files (x86)/Steam/steamapps",
                QtGui.QFileDialog.ShowDirsOnly
                | QtGui.QFileDialog.DontResolveSymlinks)
        # This will then open and write the users steam acc dir to the settings
        cfgfile = open("settings.ini", "w")
        self.kgui.settings.set('main', 'steamacc', str(fname))
        self.kgui.settings.write(cfgfile)
        cfgfile.close()
        self.ui.steampath.setText(fname)
        self.kgui.getinstalledskin(fname)
        pathsplit = os.path.split(str(fname))
        
    def cfgfile_save(self):
        currentfile = str(self.ui.cfglist.currentItem().text())
        relcfgfile = os.path.join(self.kgui.settings.get("main", "cfgpath"), currentfile)
        from os.path import isfile
        if isfile(relcfgfile):
            s = codecs.open(relcfgfile,'w','utf-8')
            s.write(unicode(self.ui.cfgEdit.toPlainText()))
            s.close()
            print str(self.TimeStamp()) + "Config File Saved"
            QtGui.QMessageBox.information(self
                , "Information"
                , "Config " + currentfile + " has been saved."
                , QtGui.QMessageBox.Ok)
            self.RefreshGameCombo()
        
    def cfgrefresh(self, configfile):
        #
        # Advanced Tab
        #
        targetfilelocation=os.path.join(self.kgui.settings.get("main", "cfgpath"), configfile)
        from os.path import isfile
        if isfile(targetfilelocation):
            #print targetfilelocation
            #s = codecs.open(targetfilelocation,'r','utf-8').read()
            s = codecs.open(targetfilelocation,'r').read()
            self.ui.cfgEdit.setPlainText(s)
        #
        # Simple Tab
        #
        # This opens up the cfg and finds "cl_cvar" "1" and puts the in to a tuple
#        self.kgui.cfgfileinterp(configfile)
#        
#        row = 1
#        actualrow = 1
#        self.ui.cfgTable.showGrid()
#        self.ui.cfgTable.setRowCount(row)
#        self.ui.cfgTable.setColumnCount(2)
#        headers=["Console Variable","Value"]
#        self.ui.cfgTable.setHorizontalHeaderLabels(headers)
#        self.ui.cfgTable.setColumnWidth(0, 300)  # Sets CVAR column width so it will fit cvars
#        for key, value in self.kgui.cfgsettings.items():
#            row += 1
#            
#            cvar = QtGui.QTableWidgetItem(key)
#            self.ui.cfgTable.setItem(actualrow-1, 0, cvar)
#            
#            cvarvalue = QtGui.QTableWidgetItem(value)
#            self.ui.cfgTable.setItem(actualrow-1, 1, cvarvalue)
#            
#            actualrow += 1
#            self.ui.cfgTable.setRowCount(row)
#        print self.ui.cfglist.currentItem()

    def resetteamtab(self):
        self.kgui.readfiles()
        self.ui.Box_t1name.setText(self.kgui.specsettings["t1name"])
        self.ui.Box_t1url.setText(self.kgui.specsettings["t1url"])
        self.ui.Box_t2name.setText(self.kgui.specsettings["t2name"])
        self.ui.Box_t2url.setText(self.kgui.specsettings["t2url"])
        self.flagspath = os.path.join(self.kgui.settings.get('main','gamepath'),'materials','vgui','klutch','flags')
        if os.path.exists(self.flagspath):
            os.chdir(str(self.flagspath))
            for files in os.listdir("."):
                if files.endswith(".vtf"): # So we dont have vtf and vmt in our list
                    files=files[:-4]
                    self.ui.comboBox_t1flag.addItem(files)
                    self.ui.comboBox_t2flag.addItem(files)
        else:
            print str(self.TimeStamp()) + "Can not find flags folder"
                
    def clickedswapteams(self):
        team1name = str(self.ui.Box_t1name.displayText())
        team1url = str(self.ui.Box_t1url.displayText())
        team2name = str(self.ui.Box_t2name.displayText())
        team2url = str(self.ui.Box_t2url.displayText())
        team1flag = self.kgui.specsettings["t1flag"]
        team2flag = self.kgui.specsettings["t2flag"]
        
        self.kgui.specsettings["t1name"]=team2name
        self.kgui.specsettings["t1url"]=team2url
        self.kgui.specsettings["t2name"]=team1name
        self.kgui.specsettings["t2url"]=team1url
        self.kgui.specsettings["t1flag"]=team2flag
        self.kgui.specsettings["t2flag"]=team1flag
        
        self.kgui.editres(self.kgui.resfiles[0])
        
        self.ui.Box_t1name.setText(self.kgui.specsettings["t1name"])
        self.ui.Box_t1url.setText(self.kgui.specsettings["t1url"])
        self.ui.Box_t2name.setText(self.kgui.specsettings["t2name"])
        self.ui.Box_t2url.setText(self.kgui.specsettings["t2url"])

    def applyteamupdate(self):
        team1name = str(self.ui.Box_t1name.displayText())
        team1url = str(self.ui.Box_t1url.displayText())
        team2name = str(self.ui.Box_t2name.displayText())
        team2url = str(self.ui.Box_t2url.displayText())
        team1flag = str(self.ui.comboBox_t1flag.currentText())
        team2flag = str(self.ui.comboBox_t2flag.currentText())
        print self.ui.comboBox_t1flag.currentText()
        print self.ui.comboBox_t2flag.currentText()
        
        #format flag output
        outputflag1 = "../vgui/klutch/flags/" + team1flag
        outputflag2 = "../vgui/klutch/flags/" + team2flag
        
        self.kgui.specsettings["t1name"]=team1name
        self.kgui.specsettings["t1url"]=team1url
        self.kgui.specsettings["t1flag"]=outputflag1
        self.kgui.specsettings["t2name"]=team2name
        self.kgui.specsettings["t2url"]=team2url
        self.kgui.specsettings["t2flag"]=outputflag2
        self.kgui.editres(self.kgui.resfiles[0])
        
    """
    def setsteamname(self):
        getsteamacc = str(self.ui.steaminput.displayText())
        accpath = os.path.join(os.environ["ProgramFiles(x86)"],"Steam\steamapps",getsteamacc,"counter-strike source\cstrike")
        if os.path.exists(accpath): 
            self.ui.steamstatus.setText("Success! Account is valid")
            self.ui.steamstatus.setStyleSheet("color: rgb(170, 170, 0)")
            self.kgui.steamacc = getsteamacc
            self.kgui.getinstalledskin(self.kgui.steamacc)
            print str(self.TimeStamp()) + "Steam account set to " + self.kgui.steamname
            
            # This will then open and write our new steamname to the settings
            cfgfile = open("settings.ini", "w")            
            self.kgui.settings.set('main', 'steamname', self.kgui.steamname)
            self.kgui.settings.write(cfgfile)
            cfgfile.close()
            
            print str(self.TimeStamp()) + "Steam account set to " + self.kgui.steamname
            print self.kgui.settings.get('main', 'gamepath')
            if not self.kgui.steamname == "":
                self.setWindowTitle(self.Splash.programname + " " + self.kgui.settings.get('main', 'version') + " - " + self.kgui.steamname)
            else:
                self.setWindowTitle(self.Splash.programname + " " + self.kgui.settings.get('main', 'version') + " - Unregistered")
        else:
            self.ui.steamstatus.setText("Error: Account Not Found!")
            self.ui.steamstatus.setStyleSheet("color: rgb(255, 0, 0)")
            self.setWindowTitle(self.Splash.programname + " " + self.kgui.settings.get('main', 'version') + " - Unregistered")
            self.kgui.settings.set('main', 'steamname', '')
            QtGui.QMessageBox.warning(self
                , "Error"
                , "The Steam account name you have entered can not be found in your Steam directory. Enter the name or email address you use to sign into steam."
                , QtGui.QMessageBox.Ok)
    """    
    
    def clickedremoveskin(self):
        self.SkinUninstall(self)
        QtGui.QMessageBox.information(self
            , "Skin Removed"
            , "Skin was removed successfully. You now have a clean game folder."
            , QtGui.QMessageBox.Ok)
        
        if self.kgui.skindetails["Skin"] == self.kgui.settings.get('skin', 'installedskin'):           
            #print str(self.TimeStamp()) + "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is installed"
            self.ui.BTN_installSkin.setEnabled(False)
            self.ui.BTN_uninstallSkin.setEnabled(True)
            #self.ui.skinName.setText(self.kgui.skindetails["Skin"] + " (Installed)")
        else:
            self.ui.BTN_uninstallSkin.setEnabled(False)
            self.ui.BTN_installSkin.setEnabled(True)
            #self.ui.skinName.setText(self.kgui.skindetails["Skin"])
            #print str(self.TimeStamp()) + "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is NOT installed"

    def clickedinstallskin(self):
        if not self.kgui.settings.get('main', 'steamacc') == "":
            if self.kgui.settings.get('skin', 'installedskin') == "":
                self.SkinInstall(self.SkinClicked)
                QtGui.QMessageBox.information(self
                    , "Skin installed"
                    , "Skin was installed successfully."
                    , QtGui.QMessageBox.Ok)
                
            else:
                QtGui.QMessageBox.warning(self
                    , "Warning"
                    , "Please uninstall '" + self.kgui.settings.get('main', 'installedskin') + "' before trying to install another skin"
                    , QtGui.QMessageBox.Ok)
                print str(self.TimeStamp()) + "Warning: Please set your steam account name before trying to install a skin"
        else:
            QtGui.QMessageBox.warning(self
                , "Warning"
                , "Please set your steam account name before trying to install a skin"
                , QtGui.QMessageBox.Ok)
            print str(self.TimeStamp()) + "Warning: Please set your steam account name before trying to install a skin"
            
        if self.kgui.skindetails["Skin"] == self.kgui.settings.get('skin', 'installedskin'):           
            #print str(self.TimeStamp()) + "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is installed"
            self.ui.BTN_installSkin.setEnabled(False)
            self.ui.BTN_uninstallSkin.setEnabled(True)
        else:
            self.ui.BTN_uninstallSkin.setEnabled(False)
            self.ui.BTN_installSkin.setEnabled(True)
            #print str(self.TimeStamp()) + "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is NOT installed"
        self.RefreshCFGFiles()
    
    def SkinChosen(self, text):
        # On launch find out if a skin is installed and refresh the array with info
        self.kgui.getinstalledskin(self.kgui.settings.get('main', 'steamacc'))
        #kgui.installskin("Base")
        self.ui.skinName.setText(self.kgui.installedskin["Skin"])
        self.ui.skinAuthor.setText(self.kgui.installedskin["Author"])
        self.ui.skinVersion.setText(self.kgui.installedskin["Version"])
        self.ui.skinType.setText(self.kgui.installedskin["Type"])
        self.ui.skinDescription.setPlainText(self.kgui.installedskin["Info"])
        
        self.kgui.getskindetails(str(text))
        self.ui.SkinPreviewImage.setPixmap(QtGui.QPixmap(os.path.join(self.kgui.skinspath, self.kgui.skindetails["Skin"], "preview.jpg")))
        self.ui.skinName.setText(self.kgui.skindetails["Skin"])
        self.ui.skinAuthor.setText(self.kgui.skindetails["Author"])
        self.ui.skinVersion.setText(self.kgui.skindetails["Version"])
        self.ui.skinType.setText(self.kgui.skindetails["Type"])
        self.ui.skinDescription.setPlainText(self.kgui.skindetails["Info"])
        
        # Set the teams tab enables
        if not self.kgui.skindetails["TeamBar"] == "yes":
            #Disable team groups
            self.ui.teamgrouphome.setEnabled(False)
            self.ui.teamgroupaway.setEnabled(False)
            self.ui.BTN_refreshteams.setEnabled(False)
            self.ui.BTN_updateTeams.setEnabled(False)
            self.ui.BTN_refreshteams.setEnabled(False)
            self.ui.BTN_swapSides.setEnabled(False)
            print str(self.TimeStamp()) + "disabled team groups"
        else:
            #Enable team groups
            self.ui.teamgrouphome.setEnabled(True)
            self.ui.teamgroupaway.setEnabled(True)
            self.ui.BTN_updateTeams.setEnabled(True)
            self.ui.BTN_refreshteams.setEnabled(True)
            self.ui.BTN_swapSides.setEnabled(True)
            print str(self.TimeStamp()) + "enabled team groups"
        if not self.kgui.skindetails["PlayerBar"] == "yes":
            #Disable PlayerBar
            #self.ui.playergroup.setEnabled(False)
            print str(self.TimeStamp()) + "disabled player group"
        else:
            #Enable PlayerBar
            #self.ui.playergroup.setEnabled(True)
            print str(self.TimeStamp()) + "enabled player group"
        
        if self.kgui.skindetails["Skin"] == self.kgui.settings.get('skin', 'installedskin'):
            #print str(self.TimeStamp()) + "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is installed"
            self.ui.BTN_installSkin.setEnabled(False)
            self.ui.BTN_uninstallSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"] + " (Installed)")
        else:
            self.ui.BTN_uninstallSkin.setEnabled(False)
            self.ui.BTN_installSkin.setEnabled(True)
            self.ui.skinName.setText(self.kgui.skindetails["Skin"])
            #print str(self.TimeStamp()) + "Skin: " + self.kgui.settings.get('main', 'installedskin') + " is NOT installed"
    
    def DeleteClientRegBlob(self):
        steamdir = os.path.join(self.kgui.settings.get('main', 'steamacc'))
        normsteampath = os.path.normpath(steamdir)
        bloblocation = os.path.join(normsteampath, "ClientRegistry.blob")
        print normsteampath
        print bloblocation
        subprocess.Popen("taskkill /IM steam.exe /F")
        time.sleep(5)
        os.remove(str(bloblocation))
        time.sleep(3)
        subprocess.Popen(normsteampath + "\steam.exe")

    def launchgame(self):
        gameid = self.kgui.settings.get('main', 'game')
        gamelaunchoptions = self.kgui.settings.get('launchoptions', 'game')
        steamexe = os.path.join(self.kgui.settings.get('main', 'steamacc'))
        datpath = steamexe + "/Steam.exe -applaunch "+ str(gameid) + " " + gamelaunchoptions
        print datpath
        subprocess.Popen(datpath)    
    
    def launchdemo(self):
        gameid = self.kgui.settings.get('main', 'game')
        demo = self.selecteddemo
        demolaunchoptions = self.kgui.settings.get('launchoptions', 'demo')
        if not self.ui.tick.text() == "":
            demolaunchoptions = demolaunchoptions + " +demo_gototick " + str(self.ui.tick.text())
        steamexe = os.path.join(self.kgui.settings.get('main', 'steamacc'))
        datpath = steamexe + "/Steam.exe -applaunch "+ str(gameid) + " " + demolaunchoptions + " +playdemo " + demo
        print datpath
        subprocess.Popen(datpath)    
    
    def democlicked(self, item):
        self.selecteddemo = unicode(item.text(2))
        print self.selecteddemo 
        
    def downloadclicked(self, item):
        if self.HeaderFileDownload == 0:
            print "Fail."
        else:
            self.DLFile = str(item.text(self.HeaderFileDownload))
            
            #Check to see if file is downloaded
            if str.startswith(self.DLFile, "http") == False:
                self.ui.btn_dldownload.setDisabled(1)
                #Check if file is installed
                if self.kgui.settings.get('skin', 'installedskin') == str(item.text(0)):
                    print "Installed"
                    self.ui.BTN_installSkin.setDisabled(1)
                    self.ui.BTN_uninstallSkin.setDisabled(0)
                else:
                    print "Not installed"
                    self.ui.BTN_installSkin.setDisabled(0)
                    self.ui.BTN_uninstallSkin.setDisabled(1)
                    self.SkinClicked = str(item.text(0))
                    print self.SkinClicked
            else:
                self.ui.btn_dldownload.setEnabled(True)
                
            cat = str(self.ui.dltypelist.currentItem().text())
            if cat == "Configs":
                self.DLFileID = str(item.text(0) + "-" + item.text(1)) 
            elif cat == "Maps":
                self.DLFileID = str(item.text(0) + "-" + item.text(2)) 
            elif cat == "Replays":
                self.DLFileID = str( item.text(0) + "-" + item.text(4) +"-"+ item.text(2) + "_vs_" + item.text(3)  ) 
            elif cat == "Mods":
                self.DLFileID = str(item.text(0)) 
                
        print self.DLFileID
        
    def downloadChunks(self, url, newfilename):    
        print "downloadChunks"
        
        self.ui.DownloadProgressBar.setFormat("%p%")
        baseFile = os.path.basename(url)
        
        cat = str(self.ui.dltypelist.currentItem().text())
        if cat == "Configs":
            movepath = self.kgui.settings.get('main', 'cfgpath')
        elif cat == "Maps":
            movepath = os.path.join(self.kgui.settings.get('main', 'gamepath'), "maps")
        else:
            movepath = self.kgui.settings.get('main', 'gamepath')
        
        scriptpath = self.ChangeToScriptDir()
        print scriptpath
        
            
        # Temp Path
        #str(random.randint(1000, 9999))
        tmpdir = os.path.join(scriptpath, 'tmp')
        if not os.path.exists(tmpdir):
            os.makedirs(tmpdir)
            
        # Download Final Path
        dlpath = os.path.join(scriptpath, 'Downloads', cat, self.kgui.settings.get('main', 'game'))
        if not os.path.exists(dlpath):
            os.makedirs(dlpath)
            
        
        os.umask(0002)
        try:
            OriginalBaseFile = baseFile
            baseFile = newfilename + "-" + baseFile
            if cat == "Skins":
                os.chdir(dlpath)
                myfile = os.path.join(dlpath,baseFile)
            elif cat == "Configs": 
                os.chdir(movepath)
                myfile = os.path.join(movepath,baseFile)
            elif cat == "Maps": 
                os.chdir(movepath)
                myfile = os.path.join(movepath,OriginalBaseFile)
            else: 
                os.chdir(movepath)
                myfile = os.path.join(movepath,baseFile)
                
            req = urllib2.urlopen(url)
            total_size = int(req.info().getheader('Content-Length').strip())
            print total_size
            downloaded = 0
            #CHUNK = 256 * 10240
            CHUNK = 32 * 10240
            with open(myfile, 'wb') as fp:
                while True:
                    chunk = req.read(CHUNK)
                    downloaded = downloaded + len(chunk)
                    progress = (1.0 * downloaded / total_size ) * 100
                    print progress
                    self.ui.DownloadProgressBar.setValue(progress)
                    if not chunk: break
                    fp.write(chunk)
        except urllib2.HTTPError, e:
            print "HTTP Error:",e.code , url
            return False
        except urllib2.URLError, e:
            print "URL Error:",e.reason , url
            return False
        
        self.ui.DownloadProgressBar.setValue(0)
        self.ui.DownloadProgressBar.setFormat("Download Complete")
        #Move file
        if myfile.endswith("zip") or myfile.endswith("bz2") or myfile.endswith("rar"):
            bzipextract = "\"" + str(scriptpath) + "\\7z.exe\" x -y -p76561198012790352 \"" + str(myfile) + "\""
            subprocess.Popen(bzipextract)
            time.sleep(5)
            os.remove(myfile)
        elif myfile.endswith("cfg"):
            self.RefreshCFGFiles()
            self.ui.tabWidget.setCurrentIndex(1)
        os.chdir(scriptpath)
        return myfile
    
    def extractAll(self, zipName):
        z = zip(zipName)
        for f in z.namelist():
            if f.endswith('/'):
                os.makedirs(f)
            else:
                z.extract(f)
     
    
    def SkinUninstall(self, status):
        currentskindir = os.path.join(self.dldir,self.kgui.settings.get('skin','installedskin'))
        print "___UNINSTALLING_SKIN________________________________________________"
        for subdir, dirs, files in os.walk(currentskindir):
            for name in files:
                filepath = os.path.join(subdir,name)
                filepathrel = os.path.relpath(filepath, currentskindir)
                filepathmain = os.path.normpath(os.path.join(self.kgui.settings.get('main','gamepath'), filepathrel))
                if os.path.exists(filepathmain):
                    fileAtt = win32api.GetFileAttributes(filepathmain)
                    if (fileAtt & win32con.FILE_ATTRIBUTE_READONLY):
                        # File is read-only, so make it writeable
                        win32api.SetFileAttributes(filepathmain, ~win32con.FILE_ATTRIBUTE_READONLY)
                    os.remove(filepathmain)
                    print "Removing file "+name+"..."
                    
                    self.ui.DownloadProgressBar.setFormat("Removing file "+name+"...")
                filebasemain = os.path.dirname(filepathmain)    
                if os.path.exists(filebasemain) and os.listdir(filebasemain) == []:
                    os.rmdir(filebasemain)
                    print "Removing folder "+filebasemain+"..."
                    self.ui.DownloadProgressBar.setFormat("Removing folder "+filebasemain+"...")
        # This will then open and write the installedskin to the settings
        self.kgui.settings.set('skin', 'installedskin', '')
        print "____________________________________________________________________"
        print "Files have been removed."
    
    # This will copy the desired skin files into the game folder and create any folders it may need
    def SkinInstall(self, desiredskin):  
        dirtydesiredskindir = os.path.join(self.dldir, desiredskin)
        desiredskindir = os.path.normpath(dirtydesiredskindir)
        if not os.path.exists(desiredskindir):
            os.makedirs(desiredskindir)
        distutils.dir_util.copy_tree(desiredskindir, self.kgui.settings.get('main', 'gamepath'))
        # This will then open and write our new desiredskin to the settings
        self.kgui.settings.set('skin', 'installedskin', desiredskin)
        
        print "____________________________________________________________________"
        print desiredskin + " installed successfully."   
                

            
def main():
    app = QtGui.QApplication(sys.argv)
#    Create and display the splash screen
#    splash_pix = QtGui.QPixmap('splash_loading.png')
#    splash = QtGui.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
#    splash.setMask(splash_pix.mask())
#    splash.show()
    
    loading=Splash()
    loading.show()
    loading.UpdateCheck()
    app.processEvents()
    
    
    window=Main()
    window.show()
    #splash.hide()
    loading.hide()
    
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())

if __name__ == "__main__":

    main()