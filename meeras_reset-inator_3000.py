from tkinter import *
from tkinter import Tk
import keyboard as kb
from global_hotkeys import *
import time
import subprocess as sp
from sys import exit


global GlobDificulty
GlobDifficulty = ""
global GlobSeedType
GlobSeedType = ""
global GlobDelay
GlobDelay = 70
global GlobSeed
GlobSeed = ""
global GlobVersion
GlobVersion="1.16"


class TimerSettings:
    def __init__(self, master):
        self.master = master
        master.title("meera's reset-inator 3000")

        master.protocol("WM_DELETE_WINDOW", self.on_closing)

        #CREATE
        self.label = Label(master, text="Choose Settings:")

        self.versionlabel = Label(master, text="Choose Version")
        self.version = Button(master, text="1.16", command=self.ChangeVersion, bg="#ffedf7")
        
        self.seedtypelabel = Label(master, text="Random or Set Seed:")
        self.seedtype = Button(master, text="RSG", command=self.ChangeSeedType, bg="#ffedf7")

        self.difficultylabel = Label(master, text="Difficulty:")
        self.difficulty = Button(master, text="EASY", command=self.ChangeDifficulty, bg="#ffedf7")
        
        self.seedlabel = Label(master, text="Enter the seed for SSG:")
        self.seedentry = Entry(master, borderwidth=2, bg="#ffedf7")

        self.delaylabel = Label(master, text="Macro Delay (ms):")
        self.delayentry = Entry(master, borderwidth=2, bg="#ffedf7")
        self.delayentry.insert(END, '70')

        self.macrobutton = Button(master, text="Open Macro Settings", command = self.openmacros, borderwidth=2, bg="#ffedf7")


        self.createac = Button(master, text="Solidify Settings", bg="#ffddf7", command=self.SetVars)

        self.explainrun = Label(master, text="Once you solidify, click Run Macro")
        self.runahk = Button(master, text="Run Macro", bg="#ffddf7", command=self.SetAHK)
        
        #PLACE
        self.label.grid(row=0, column=0, padx=5, sticky=W+E)

        self.versionlabel.grid(row=1, column=0, padx=5, sticky=W)
        self.version.grid(row=1, column=1, padx=5, pady=2, sticky=W)
        
        self.seedtypelabel.grid(row=2, column=0, padx=5, sticky=W)
        self.seedtype.grid(row=2, column=1, padx=5, pady=2, sticky=W)

        self.difficultylabel.grid(row=3, column=0, padx=5, sticky=W)
        self.difficulty.grid(row=3, column=1, padx=5, pady=2, sticky=W)
        
        self.seedlabel.grid(row=4, column=0, padx=5, sticky=W)
        self.seedentry.grid(row=4, column=1, padx=5, pady=2)
        
        self.delaylabel.grid(row=5, column=0, padx=5, sticky=W)
        self.delayentry.grid(row=5, column=1, padx=5, pady=2)

        self.macrobutton.grid(row=6, column=1)

        self.createac.grid(row=8, column=0)

        self.explainrun.grid(row=9, column=0)
        self.runahk.grid(row=10, column=0)

        
    def on_closing(self):
        self.master.destroy()
        exit()

    def openmacros(self):
        programName = "notepad.exe"
        filename = "macrosettings.txt"
        sp.Popen([programName, filename])

    def ChangeVersion(self):
        if self.version['text'] == '1.16':
            self.version['text'] = '1.14/1.15'
            self.difficulty['text'] = 'NORMAL'
        else:
            self.version['text'] = "1.16"

    def ChangeSeedType(self):
        if self.seedtype['text'] == 'RSG':
            self.seedtype['text'] = 'SSG'
        elif self.seedtype['text'] == 'SSG':
            self.seedtype['text'] = 'FSG'
        else:
            self.seedtype['text'] = 'RSG'

    def ChangeDifficulty(self):
        if self.version['text'] == '1.16':
            if self.difficulty['text'] == 'EASY':
                self.difficulty['text'] = 'NORMAL'
                
            elif self.difficulty['text'] == 'NORMAL':
                self.difficulty['text'] = 'HARD'

            elif self.difficulty['text'] == 'HARD':
                self.difficulty['text'] = 'HARDCORE'

            elif self.difficulty['text'] == 'HARDCORE':
                self.difficulty['text'] = 'PEACEFUL'

            elif self.difficulty['text'] == 'PEACEFUL':
                self.difficulty['text'] = 'EASY'
                
        else:
            if self.difficulty['text'] == 'NORMAL':
                self.difficulty['text'] = 'HARDCORE'
            else:
                self.difficulty['text'] = 'NORMAL'
                    

    def SetVars(self):
        global GlobDifficulty
        global GlobSeedType
        global GlobDelay
        global GlobSeed
        global GlobVersion
        GlobDifficulty = self.difficulty["text"]
        GlobSeedType = self.seedtype["text"]
        GlobDelay = float(self.delayentry.get())/1000 #convert to seconds
        GlobSeed = self.seedentry.get()
        GlobVersion = self.version["text"]

    def SetAHK(self, event=None):
        self.master.destroy()


        
def RunActionChain():
        global GlobDifficulty
        global GlobSeedType
        global GlobDelay
        global GlobSeed
        global GlobVersion

        delay = GlobDelay

        if GlobVersion=="1.16":
            kb.press_and_release('\t')
            time.sleep(delay)
            kb.press_and_release(' ') #enter singleplayer
            time.sleep(2*delay)
            kb.press_and_release('\t')
            kb.press_and_release('\t')
            kb.press_and_release('\t') #hover create new world
            time.sleep(delay)
            kb.press_and_release(' ') #enter world creation
                
            kb.press_and_release('\t') #hover gamemode
            time.sleep(delay)
                
            if GlobDifficulty == 'HARDCORE':
                kb.press_and_release(' ')
                time.sleep(delay)
            else:
                kb.press_and_release('\t') #hover difficulty, only for non hardcore

            time.sleep(delay)

            #default normal, so if normal do nothing here
            if GlobDifficulty == 'HARD':
                kb.press_and_release(' ')
                    
            elif GlobDifficulty == 'PEACEFUL':
                kb.press_and_release(' ')
                kb.press_and_release(' ')
                    
            elif GlobDifficulty == 'EASY':
                kb.press_and_release(' ')
                kb.press_and_release(' ')
                kb.press_and_release(' ')
                
            time.sleep(delay)

            if GlobDifficulty != 'HARDCORE':
                kb.press_and_release('\t')
                kb.press_and_release('\t') 
                kb.press_and_release('\t')
                kb.press_and_release('\t') #hover more world options
            else:
                kb.press_and_release('\t') 
                kb.press_and_release('\t')
                kb.press_and_release('\t') #hover more world options
                
            
            #if SSG or FSG, enter seed
            if GlobSeedType != 'RSG':
                seed = GlobSeed
                
                time.sleep(delay)
                kb.press_and_release(' ') #enter more world options
                    
                kb.press_and_release('\t')
                kb.press_and_release('\t')
                
                time.sleep(delay)
                kb.press_and_release('\t') #hover seed
                
                time.sleep(delay)
                if GlobSeedType == "FSG":
                    seed = Tk().clipboard_get()
                    
                kb.write(seed) #enter seed
                time.sleep(delay)

                kb.press_and_release('\t')
                kb.press_and_release('\t')
                kb.press_and_release('\t')
                kb.press_and_release('\t')
                kb.press_and_release('\t') #hover done
                time.sleep(delay)
                kb.press_and_release(' ') #back to main create world screen
                time.sleep(delay)

            kb.press_and_release('\t') #hover create new world
            time.sleep(delay)
            kb.press_and_release(' ') #create new world

        #for 1.14/1.15
        else:
            kb.press_and_release('\t')
            time.sleep(delay)
            kb.press_and_release(' ') #enter singleplayer

            time.sleep(2*delay)
            kb.press_and_release('\t')
            kb.press_and_release('\t')
            kb.press_and_release('\t')
            kb.press_and_release('\t') #hover create new world
            time.sleep(delay)
            kb.press_and_release(' ') #enter world creation
            
            kb.press_and_release('\t')
            kb.press_and_release('\t') #hover gamemode
            time.sleep(delay)

            if GlobDifficulty == 'HARDCORE':
                kb.press_and_release(' ')
                time.sleep(delay)
                  
            
            if GlobSeedType != 'RSG':
                seed = GlobSeed
                kb.press_and_release('\t') #hover more world options
                time.sleep(delay)
            
                kb.press_and_release(' ') #enter more world options
                kb.press_and_release('\t') 
                kb.press_and_release('\t') 
                kb.press_and_release('\t') #hover seed

                time.sleep(delay)
                if GlobSeedType == "FSG":
                    seed = Tk().clipboard_get()
                    
                kb.write(seed) #enter seed
                time.sleep(delay)

                if GlobDifficulty != 'HARDCORE':
                    kb.press_and_release('\t')
                    kb.press_and_release('\t')
                kb.press_and_release('\t')
                kb.press_and_release('\t')
                kb.press_and_release('\t')
                kb.press_and_release('\t') #hover create new world
                time.sleep(delay)
                kb.press_and_release(' ') #press create new world
                
            else:

                kb.press_and_release('\t')
                kb.press_and_release('\t') #hover create new world
                time.sleep(delay)
                kb.press_and_release(' ') #press create new world

def DragonPerch():
    '''From onvo, SLTRR, DesktopFolder, Peej, and others AHK script for dragon perch'''

    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release(' ') #open to LAN settings
    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release('\t')
    kb.press_and_release(' ') #cheats on
    kb.press_and_release('\t')
    kb.press_and_release(' ') #open to LAN
    kb.press_and_release('/') #open text in mc  
    time.sleep(.05)
    kb.write('execute as @e[type=ender_dragon] run data modify entity @s DragonPhase set value 3\n')
                

def bring_window():
    root = Tk()
    gui = TimerSettings(root)
    root.mainloop()

while True:   
    bring_window()

    #global inte
    #inte=0
    is_alive = True
    
    def exit_resetting():
        global is_alive
        global inte
        global actionchain
        #inte=0
        #actionchain = []
        stop_checking_hotkeys()
        is_alive = False

    with open("macrosettings.txt") as f:
        macros = f.readlines()
        HKStart = macros[0].split()
        HKStart = HKStart[1:]
        HKEnd = macros[1].split()
        HKEnd = HKEnd[1:]
        HKPerch = macros[2].split()
        HKPerch = HKPerch[1:]
        
    bindings=[]
    
    bindings.append([HKStart, None, RunActionChain])
    bindings.append([HKEnd, None, exit_resetting])
    bindings.append([HKPerch, None, DragonPerch])

    register_hotkeys(bindings)
    start_checking_hotkeys()

    while is_alive:        
        time.sleep(5)
