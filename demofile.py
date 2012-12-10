#!/usr/bin/python

"""
Coded by my flatmate and good friend Nic West :)


------------
Example
from demofile import demoFile
target = "C:\\Program Files (x86)\\Steam\\steamapps\\3fk\\counter-strike source\\cphwolves.dem"
demo = demoFile(target)
print "Head:\t"+demo.header
print "Game:\t"+demo.game
print "Server:\t"+demo.server
print "Client:\t"+demo.client
print "Map:\t"+demo.map
print "Length:\t"+demo.getlength()

"""

import os.path
import array
import struct
import time, datetime


class BadDemoFile(Exception):
    pass

class demoFile():
    def __init__ (self, filename, engine):
        t = self.read_binary_file(filename)
        fsize = t[0]
        
        ### SETTING DEFAULTS FOR DEBUG
        self.header = ""
        self.demoProtocol = 0
        self.networkProtocol = 0
        self.map = ""
        self.game = ""
        self.server = ""
        self.client = ""
        self.length = 0
        self.mapcrc = 0
        self.playback = 0
        self.ticks = 0
        self.frames = 0
        
        
        #if we are good to go...
        if (fsize > 0):
            data = t[1]
            #try:
            if engine == "HL2":
                unpacked=struct.unpack('8sii260s260s260s260sfiii', data[0:1072])
            elif engine == "HL1":
                unpacked=struct.unpack('8sii260s260si', data[0:540])
            #except:
                #raise BadDemoFile, "Unable to unpack demofile: %s" % filename
            output = []
            
            
            #strip excess whiteness from strings
            for item in unpacked:
                if type(item) == str:
                    item = item.replace('\x00', '')
                output.append(item)
            
            if engine == "HL2":
                self.header, self.demoProtocol, self.networkProtocol, self.server, self.client, self.map, self.game, self.length, self.playback, self.ticks, self.frames = output
            elif engine == "HL1":
                self.header, self.demoProtocol, self.networkProtocol, self.map, self.game, self.mapcrc = output   
            
            #break down time
            self.seconds = int(self.length)
            self.hours = self.seconds / 3600
            self.seconds -= 3600*self.hours
            self.minutes = self.seconds / 60
            self.seconds -= 60*self.minutes
            
        else:
            raise BadDemoFile, "Unable to read demo file: %s" % filename
        
    def getlength (self):
        output = ""
        if not int(self.hours) == 0:
            output = str(int(self.hours)) + "h "
        if not int(self.minutes) == 0:
            output = output + str(int(self.minutes)) + "m "
        if not int(self.seconds) == 0:
            output = output + str(int(self.seconds)) + "s "
            
        return output
    
    def gettime(self, target):
        newtime = os.path.getmtime(target) - int(self.length)
        return time.strftime("%d %b '%y  %H:%M",time.localtime(newtime))  
     
    def read_binary_file(self, filename):
        try:
            f = open(filename, 'rb')
            n = os.path.getsize(filename)
            data = array.array('B')
            data.read(f, n)
            f.close()
            fsize = data.__len__()
            return (fsize, data)
        
        except IOError:
            return (-1, [])