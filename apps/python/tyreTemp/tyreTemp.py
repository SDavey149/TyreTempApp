__author__ = 'Scott Davey'

"""Simple tyre temperature plugin for Assetto Corsa"""

import sys
import ac
import acsys

APP_NAME = "Tyre Temps"
tyre1Label = tyre2Label = tyre3Label = tyre4Label = 0

def acMain(ac_version):
    appWindow = ac.newApp(APP_NAME)
    ac.setSize(appWindow, 200, 200)
    ac.log("==TYRE TEMPS BEGIN==")
    setupUI(appWindow)
    return APP_NAME

def setupUI(appWindow):
    global tyre1Label, tyre2Label, tyre3Label, tyre4Label
    tyre1Label = ac.addLabel(appWindow, "Tyre 1: 0");
    tyre2Label = ac.addLabel(appWindow, "Tyre 2: 0");
    tyre3Label = ac.addLabel(appWindow, "Tyre 3: 0");
    tyre4Label = ac.addLabel(appWindow, "Tyre 4: 0");
    ac.setPosition(tyre1Label, 3, 30)
    ac.setPosition(tyre2Label, 3, 40)
    ac.setPosition(tyre3Label, 3, 50)
    ac.setPosition(tyre4Label, 3, 60)

def acUpdate(deltaT):
    temps = ac.getCarState(0, acsys.CS.ThermalState)
    ac.setText(tyre1Label, "Tyre 1: {}".format(temps[0]))
    ac.setText(tyre2Label, "Tyre 2: {}".format(temps[1]))
    ac.setText(tyre3Label, "Tyre 3: {}".format(temps[2]))
    ac.setText(tyre4Label, "Tyre 4: {}".format(temps[3]))
