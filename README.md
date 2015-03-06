Explanation of manual setup in drirc:
http://lists.freedesktop.org/archives/mesa-dev/2014-May/060131.html
(run udevadm on /dev/dri/cardX instead of /dev/cardX)

Requirements:
* python3
* pyqt5

Build & Run:

```
pyuic5 gpuchooser.ui -o ui_gpuchooser.py
./gpuchooser.py
```

![Screenshot](http://haagch.frickel.club/files/gpuchooser.png "Screenshot")

