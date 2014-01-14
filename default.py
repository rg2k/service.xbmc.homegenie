import xbmc,xbmcgui
import subprocess,os
import urllib2
import xbmcaddon
import base64

__settings__ = xbmcaddon.Addon("service.xbmc.homegenie")

password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
homegenie_url = "http://" + __settings__.getSetting("ipaddress") + "/api/HomeAutomation.HomeGenie/Automation/Programs.Run/"

base64string = base64.encodestring("%s:%s" % ("admin", __settings__.getSetting("password"))).replace("\n", "")

class MyPlayer(xbmc.Player):
	def __init__ (self):
		xbmc.Player.__init__(self)

	def onPlayBackStarted(self):
		if xbmc.Player().isPlayingVideo():
			if __settings__.getSetting("RunonmoviePlaySwitch") == "true":
				request = ""
				request = urllib2.Request(homegenie_url + __settings__.getSetting("RunonmoviePlayScriptID")+"/")
				#base64string = base64.encodestring("%s:%s" % ("admin", __settings__.getSetting("password"))).replace("\n", "")
				request.add_header("Authorization", "Basic %s" % base64string)   
				try:
					result = urllib2.urlopen(request)
				except HTTPError as e:
					xbmc.log("HomeGenie - Movie Play - " + e.code)
				except URLError as e:
					xbmc.log("HomeGenie - Movie Play - " + e.reason)
				else:
    					xbmc.log("HomeGenie - Movie Play - " + homegenie_url + __settings__.getSetting("RunonmoviePlayScriptID") + "/")
					xbmc.log("HomeGenie - Movie Play - " + "No Error")

				
	def onPlayBackPaused(self):
		if xbmc.Player().isPlayingVideo():
			if __settings__.getSetting("RunonmoviePauseSwitch") == "true":
				request = urllib2.Request(homegenie_url + __settings__.getSetting("RunonmoviePauseScriptID")+"/")
				#base64string = base64.encodestring("%s:%s" % ("admin", __settings__.getSetting("password"))).replace("\n", "")
				request.add_header("Authorization", "Basic %s" % base64string)
				try:
					result = urllib2.urlopen(request)
				except HTTPError as e:
					xbmc.log("HomeGenie - Movie Pause - " + e.code)
				except URLError as e:
					xbmc.log("HomeGenie - Movie Pause - " + e.reason)
				else:
					xbmc.log("HomeGenie - Movie Pause - " + homegenie_url + __settings__.getSetting("RunonmoviePauseScriptID")+"/")
					xbmc.log("HomeGenie - Movie Pause - " + "No Error")
				
	def onPlayBackStopped(self):
		if (VIDEO == 1):
			if __settings__.getSetting("RunonmovieStopSwitch") == "true":
				request = urllib2.Request(homegenie_url + __settings__.getSetting("RunonmovieStopScriptID")+"/")
				#base64string = base64.encodestring("%s:%s" % ("admin", __settings__.getSetting("password"))).replace("\n", "")
				request.add_header("Authorization", "Basic %s" % base64string)   
				result = urllib2.urlopen(request)
				xbmc.log("HomeGenie - Movie Stop - " + homegenie_url + __settings__.getSetting("RunonmovieStopScriptID")+"/")

	def onPlayBackEnded(self):
		if (VIDEO == 1):
			if __settings__.getSetting("RunonmovieStopSwitch") == "true":
				request = urllib2.Request(homegenie_url + __settings__.getSetting("RunonmovieStopScriptID")+"/")
				#base64string = base64.encodestring("%s:%s" % ("admin", __settings__.getSetting("password"))).replace("\n", "")
				request.add_header("Authorization", "Basic %s" % base64string)   
				result = urllib2.urlopen(request)
				xbmc.log("HomeGenie - Movie End - " + homegenie_url + __settings__.getSetting("RunonmovieStopScriptID")+"/")

	def onPlayBackResumed(self):
		if xbmc.Player().isPlayingVideo():
			if __settings__.getSetting("RunonmovieResumeSwitch") == "true":
				request = urllib2.Request(homegenie_url + __settings__.getSetting("RunonmovieResumeScriptID")+"/")
				#base64string = base64.encodestring("%s:%s" % ("admin", __settings__.getSetting("password"))).replace("\n", "")
				request.add_header("Authorization", "Basic %s" % base64string)
				try:
					result = urllib2.urlopen(request)
				except HTTPError as e:
					xbmc.log("HomeGenie - Movie Resume - " + e.code)
				except URLError as e:
					xbmc.log("HomeGenie - Movie Resume - " + e.reason)
				else:
					xbmc.log("HomeGenie - Movie Resume - " + homegenie_url + __settings__.getSetting("RunonmovieResumeScriptID")+"/")
					xbmc.log("HomeGenie - Movie Resume - " + "No Error")
					
player=MyPlayer()
 
VIDEO = 0

xbmc.log("HomeGenie - RunonmoviePlaySwitch " + __settings__.getSetting("RunonmoviePlaySwitch"))
xbmc.log("HomeGenie - RunonmoviePauseSwitch " + __settings__.getSetting("RunonmoviePauseSwitch"))
xbmc.log("HomeGenie - RunonmovieStopSwitch " + __settings__.getSetting("RunonmovieStopSwitch"))
xbmc.log("HomeGenie - RunonmovieResumeSwitch " + __settings__.getSetting("RunonmovieResumeSwitch"))

 
while(not xbmc.abortRequested):
    if xbmc.Player().isPlaying():
		if xbmc.Player().isPlayingVideo():
			VIDEO = 1
 
		else:
			VIDEO = 0
 
    xbmc.sleep(3000)
