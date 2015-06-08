__author__ = 'Scott Davey'

"""Simple tyre temperature plugin for Assetto Corsa"""

import sys
import ac
import acsys

APP_NAME = "tyreTemp"
tyre1Label = tyre2Label = tyre3Label = tyre4Label = 0

def acMain(ac_version):
    appWindow = ac.newApp(APP_NAME)
    ac.setSize(appWindow, 200, 200)
    ac.log("==TYRE TEMPS BEGIN==")
    setupUI(appWindow)
    ac.addRenderCallback(appWindow, onFormRender)
    return APP_NAME

def setupUI(appWindow):
    global tyre1Label, tyre2Label, tyre3Label, tyre4Label
    tyre1Label = ac.addLabel(appWindow, "FL: 0");
    tyre2Label = ac.addLabel(appWindow, "FR: 0");
    tyre3Label = ac.addLabel(appWindow, "RL: 0");
    tyre4Label = ac.addLabel(appWindow, "RR: 0");
    ac.setPosition(tyre1Label, 3, 30)
    ac.setPosition(tyre2Label, 3, 50)
    ac.setPosition(tyre3Label, 3, 70)
    ac.setPosition(tyre4Label, 3, 90)

def onFormRender(deltaT):
    global tyre1Label, tyre2Label, tyre3Label, tyre4Label
    try:        
        x,y,z,w = ac.getCarState(0, acsys.CS.CurrentTyresCoreTemp)
        ac.setText(tyre1Label, "FL: {}".format(round(x,1)))
        ac.setText(tyre2Label, "FR: {}".format(round(y,1)))
        ac.setText(tyre3Label, "RL: {}".format(round(z,1)))
        ac.setText(tyre4Label, "RR: {}".format(round(w,1)))
    except Exception as e:
        ac.log("TyreTemp: Error in function onFormRender: {}".format(e))
