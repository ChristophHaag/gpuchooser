#!/usr/bin/env python3
from PyQt5 import QtCore
import subprocess
from xml.dom import minidom

from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QLabel, QLineEdit, QComboBox, QCheckBox

from subprocess import PIPE
import sys
import ui_gpuchooser
from glob import glob
import locale
import xml.etree.ElementTree as ET
import os
from os.path import expanduser

# global variables: driconfroot, drircfile, xmlvalues, tagids
home = expanduser("~")
drircfile = home + "/.drirc"
xmlvalues = []
tagids = []


if not os.path.isfile(drircfile):
    print(drircfile + " does not exist, please run driconf once, it will create the file...")
    exit(1)
if not os.access(drircfile, os.W_OK):
    print("WARNING: " + drircfile + " is not writable. You can not save your changes!")


def removealldeviceel(root):
    to_remove = []
    for devicedriver in root:
        if devicedriver.get("driver") == "loader":
            to_remove.append(devicedriver)
    for i in to_remove:
        root.remove(i)

def getdeviceel(root):
    for devicedriver in root:
        if devicedriver.get("driver") == "loader":
            deviceel = devicedriver
            return deviceel
    #else none


def gpuname_from_tag(tag):
    for i in tagids:
        if i["tag"] == tag:
            return i


def gpuindex_from_tag(tag):
    for index, i in enumerate(tagids):
        if i["tag"] == tag:
            return index


class Entry(QHBoxLayout):
    entries = []
    def __init__(self, desc, path, gpuindex):
        super().__init__()
        Entry.entries.append(self)
        self.desc = desc
        self.path = path
        self.gpuindex = gpuindex
        self.box = None
        self.make_gui_entry_layout(desc,path,gpuindex)

    def updatevars(self): # TODO: mvc or so
        self.desc = self.descriptionle.text()
        lepath = self.pathtoexecutablele.text()
        path = lepath.split("/")[-1] # Can not be full path, must be executable name
        self.pathtoexecutablele.setText(path)
        self.path = path
        self.gpuindex = self.gpuindexbox.currentIndex()

    def make_gui_entry_layout(self, desc, path, gpuindex):
        #horiz = QHBoxLayout()
        box = QCheckBox()
        self.box = box
        self.addWidget(box)

        self.descriptionlabel = QLabel("Description:")
        self.addWidget(self.descriptionlabel)
        self.descriptionle = QLineEdit()
        self.descriptionle.setText(desc)
        self.addWidget(self.descriptionle)

        self.pathtoexecutablelabel = QLabel("Executable name:")
        self.addWidget(self.pathtoexecutablelabel)
        self.pathtoexecutablele = QLineEdit()
        self.pathtoexecutablele.setText(path)
        self.addWidget(self.pathtoexecutablele)

        self.gpuindexbox = QComboBox()
        for tid in tagids:
            self.gpuindexbox.addItem(tid["name"])

        self.gpuindexbox.setCurrentIndex(gpuindex)
        self.addWidget(self.gpuindexbox)

    #http://stackoverflow.com/a/9383780
    def remove(self):
        Entry.entries.remove(self)
        parent = self.parent()
        while self.count():
            item = self.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                parent.remove(item.layout())

#http://stackoverflow.com/a/17402424
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    halfpretty = reparsed.toprettyxml(indent="\t")
    pretty = '\n'.join([line for line in halfpretty.split('\n') if line.strip()])
    return pretty

class MainWindow(QMainWindow, ui_gpuchooser.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.statuslabel = QLabel()
        self.statusbar.addWidget(self.statuslabel)

        self.mainvertlayout.setAlignment(QtCore.Qt.AlignTop)

        for i in xmlvalues:
            gputag = i["tag"]
            desc = i["desc"]
            path = i["path"]
            gpuindex = gpuindex_from_tag(gputag)
            horiz = Entry(desc, path, gpuindex)
            self.mainvertlayout.addLayout(horiz)
        self.statuslabel.setText("Loaded " + str(len(xmlvalues)) + " items")

        self.addentrybtn.clicked.connect(self.addapp)
        self.cancelbtn.clicked.connect(QApplication.quit)
        self.savebtn.clicked.connect(self.save)
        self.removebtn.clicked.connect(self.remove_entry)

    def remove_entry(self):
        to_remove = []
        for index, entry in enumerate(Entry.entries):
            assert isinstance(entry.box, QCheckBox)
            if entry.box.isChecked():
                #print(index, "box", entry.box.isChecked())
                to_remove.append(entry)
        self.statuslabel.setText("Removed " + str(len(to_remove)) + " items")
        while len(to_remove) > 0:
            entry = to_remove.pop()
            entry.remove()


    def save(self):
        deviceel = getdeviceel(driconfroot)
        #assert isinstance(deviceel, ET.Element)

        if not deviceel == None: removealldeviceel(driconfroot) # just in case there are more

        newdeviceel = ET.Element("device")
        newdeviceel.set("driver", "loader")

        for entry in Entry.entries:
            entry.updatevars()
            if not entry.path:
                print("Error, no executable name set, not saving this entry!")
                continue
            appl = ET.Element("application")
            appl.set("name", entry.desc)
            appl.set("executable", entry.path)
            opt = ET.Element("option")
            opt.set("name", "device_id")
            opt.set("value", tagids[entry.gpuindex]["tag"])
            appl.append(opt)
            newdeviceel.append(appl)

        driconfroot.append(newdeviceel)
        xml = prettify(driconfroot)
        #print("write\n", xml)
        with open(drircfile, "w") as f:
            f.write(xml)
        self.statuslabel.setText("Saved " + str(len(Entry.entries)) + " items")

    def addapp(self):
        horiz = Entry("", "", 0)
        self.mainvertlayout.addLayout(horiz)
        horiz.descriptionle.setFocus()

def gpuname_from_glxinfo(tag):
    env = os.environ.copy()
    env["DRI_PRIME"] = tag
    glxinfo = subprocess.Popen(["glxinfo"], stdout=PIPE, env=env).communicate()
    #print(glxinfo)
    for line in glxinfo[0].split(b"\n"):
        if line:
            decoded = line.decode(locale.getdefaultlocale()[1])
            if decoded.find("OpenGL renderer string") != -1:
                renderer = decoded.replace("OpenGL renderer string: ", "")
                return renderer

def main():
    global driconfroot
    tree = ET.parse(drircfile)
    driconfroot = tree.getroot()


    deviceel = getdeviceel(driconfroot)
    #assert isinstance(deviceel, ET.Element) or none

    for i in deviceel:
        gputag = i.find("option").get("value")
        #print (gpu)
        gpuname = i.get("name")
        gpupath = i.get("executable")
        xmlvalues.append({
            "desc": gpuname,
            "path": gpupath,
            "tag": gputag
        })


    gpupaths = glob("/sys/class/drm/card?") # only 9 cards supported
    gpucards = [g.split("/")[-1] for g in gpupaths] #todo: find out names
    for index,i in enumerate(gpucards):
        #print("reading ", i)
        udev = subprocess.Popen(["udevadm", "info", "/dev/dri/" + i], stdout=PIPE).communicate()

        for line in udev[0].split(b"\n"):
            if line:
                decoded = line.decode(locale.getdefaultlocale()[1])
                id = "ID_PATH_TAG"
                #print("line: ",  decoded)
                if decoded.find(id) != -1:
                    tag = decoded.split("=")[1]
                    #print("tag id:", decoded)
                    gpuname = gpuname_from_glxinfo(tag)
                    tagids.append({
                        "tag": tag.strip(),
                        "carddev": i,
                        "name": gpuname # TODO: proper name
                    })
                    continue
    #print("tagids", tagids)

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())