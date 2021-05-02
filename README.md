# meera's reset-inator 3000

Windows Only!

## 📝 changelog


### VERSION 2.1

- added installer for easy access
	- default settings should be fine, itll place the exe in your programfiles (if not, itll
	tell you where its going to install. There is also an uninstaller there)
- made background pink as well! she looks so pretty!!!!


### VERSION 2.0
- got rid of solidify settings delay
	- When you press "Solidify Settings", no need to wait a long time to let it apply, which was an
	issue in 1.0
- added support for 1.14/1.15
	- Since there is no difficulty setting from the main menu in these versions, the difficulty will
	only oscillate between NORMAL and HARDCORE
- added support for FSG
	- Set it to FSG, and before running the macro make sure the FSG seed is in your clipboard. Run the
	macro as normal
- added support to customize macro keys (you're welcome antoine :p)
	- In the GUI, click on "Open Macro Settings" to open a text file containing each macro for you
	change as you see fit, below it is a list of supported keys
-added command to open to LAN and make dragon perch
	-From the pause menu, hit the Perch macro to open to LAN and send a command for dragon perch


## 💻 Versions Supported
Minecraft versions currently supported: **1.16, 1.14, 1.15**.


## 📥 Installation
Download the .exe installer from github under releases: [DOWNLOAD](https://github.com/pistacium/meeras_reset-inator_3000/releases/tag/v2.1)


## 🧱 Building

### Compiling

This is written in python, which not everyone has, so we use pyinstaller to make it into an exe file.

#### Requirements:
Listed in requirements.txt. To install them all, run `pip install -r requirements.txt` in a terminal.


If you want to make it yourself, run `pyinstaller meeras_reset-inator_3000.py --icon=kitty.ico --onefile` in a terminal.

### Setup File

The first setup was created with [NSIS](https://nsis.sourceforge.io/), but the newer one is created with [Inno Setup](https://jrsoftware.org/isinfo.php).

## ⌨ Usage

The Macro Delay is measured in milliseconds, and a number must be in it for the program to work.
The default is set to 70, as this should in most cases show a frame of each world generation screen,
which is recommended for ease of verification. (delete old worlds if it's getting laggy, this can 
mess up the whole "70 should be fine" thing).

Once you've chosen settings, click "Solidify Settings" to save your settings.
If you want to change settings before running the macro, do so and hit "Solidify Settings" again.


After you are done, click "Run Macro" and the GUI will close, but the application will still be functioning.

RunMacro (default ctrl+m) starts the macro (be sure you're on your title screen of Minecraft when you do this, and that
the Minecraft window is in focus).

RestartGUI (default ctrl+l) restarts the program. You can do this at the end of runs and leave the program, or if you'd 
like to change settings at any time.

Perch (default ctrl+j) opens to LAN and sends a command to make the dragon perch. Run this macro
from the pause menu (not sure why but when I tried to make it run esc from within minecraft to make it pause
for you, it would hit the windows key. It makes no sense, maybe its just my computer idk lmao)


This program is designed to work with world files already existent, at the very least one. 
I recommend [Emma's End Practice Map](https://sites.google.com/view/emma-practice-map/home) [if you don't have it already, go get it. right now. im serious
go right now. not sponsored btw].

If any issues arise, message me on discord meera#6969, or on twitter @pistaacium.

\- Meera Pistacium & notfire

P.S.
amogus

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
