from tkinter import *
from ahk import *
from ahk.window import Window
from ahk import ActionChain
import ahk
from global_hotkeys import *
import time


global actionchain
actionchain = []

class TimerSettings:
    def __init__(self, master):
        self.master = master
        master.title("meera's reset-inator 3000")
        #self.ActionChain = ActionChain()
        #CREATE
        self.label = Label(master, text="Choose Settings:")
        
        self.seedtypelabel = Label(master, text="Random or Set Seed:")
        self.seedtype = Button(master, text="RSG", command=self.ChangeSeedType, bg="#ffddf7")

        self.difficultylabel = Label(master, text="Difficulty:")
        self.difficulty = Button(master, text="EASY", command=self.ChangeDifficulty, bg="#ffddf7")
        
        self.seedlabel = Label(master, text="Enter the seed for SSG:")
        self.seedentry = Entry(master, borderwidth=2, bg="#ffedf7")

        self.delaylabel = Label(master, text="Macro Delay (ms):")
        self.delayentry = Entry(master, borderwidth=2, bg="#ffedf7")
        self.delayentry.insert(END, '70')

        #self.macrolabel = Label(master, text="Enter Keypress for Macro:")
        #self.macroentry = Button(master, text="CLICK", command=self.SetMacroKey)

        self.createac = Button(master, text="Solidify Settings", bg="#ffddf7", command=self.CreateActionChain)

        self.explainrun = Label(master, text="Once you solidify, click Run Macro")
        self.runahk = Button(master, text="Run Macro", bg="#ffddf7", command=self.SetAHK)
        
        #PLACE
        self.label.grid(row=0, column=0, padx=5, sticky=W+E)
        
        self.seedtypelabel.grid(row=2, column=0, padx=5, sticky=W)
        self.seedtype.grid(row=2, column=1, padx=5, pady=2, sticky=W)

        self.difficultylabel.grid(row=3, column=0, padx=5, sticky=W)
        self.difficulty.grid(row=3, column=1, padx=5, pady=2, sticky=W)
        
        self.seedlabel.grid(row=4, column=0, padx=5, sticky=W)
        self.seedentry.grid(row=4, column=1, padx=5, pady=2)
        
        self.delaylabel.grid(row=5, column=0, padx=5, sticky=W)
        self.delayentry.grid(row=5, column=1, padx=5, pady=2)

        #self.macrolabel.grid(row=6, column=0, sticky=W)
        #self.macroentry.grid(row=6, column=1)

        self.createac.grid(row=7, column=0)

        self.explainrun.grid(row=8, column=0)
        self.runahk.grid(row=9, column=0)


    def ChangeSeedType(self):
        if self.seedtype['text'] == 'RSG':
            self.seedtype['text'] = 'SSG'
        else:
            self.seedtype['text'] = 'RSG'

    def ChangeDifficulty(self):
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


    def CreateActionChain(self):
        delay = int(self.delayentry.get())/1000

        for i in range(1000):
            ac = ActionChain(executable_path="AutoHotkey\AutoHotkey.exe")

            ac.key_press('TAB')
            ac.key_press('Space') #enter singleplayer
            ac.sleep(delay)
            ac.key_press('TAB')
            ac.key_press('TAB')
            ac.key_press('TAB') #hover create new world
            ac.sleep(delay)
            ac.key_press('Space') #enter world creation
            
            ac.key_press('TAB') #hover gamemode
            ac.sleep(delay)
            
            if self.difficulty['text'] == 'HARDCORE':
                ac.key_press('Space')
                ac.sleep(delay)
            else:
                ac.key_press('TAB') #hover difficulty, only for non hardcore
                
            #default normal, so if normal do nothing here
            if self.difficulty['text'] == 'HARD':
                ac.key_press('Space')
                ac.sleep(delay)
                
            elif self.difficulty['text'] == 'PEACEFUL':
                ac.key_press('Space')
                ac.key_press('Space')
                ac.sleep(delay)
                
            elif self.difficulty['text'] == 'EASY':
                ac.key_press('Space')
                ac.key_press('Space')
                ac.key_press('Space')

            if self.difficulty['text'] != 'HARDCORE':
                ac.key_press('TAB')
                ac.key_press('TAB') 
                ac.key_press('TAB')
                ac.key_press('TAB') #hover more world options
            else:
                ac.key_press('TAB') 
                ac.key_press('TAB')
                ac.key_press('TAB') #hover more world options

            #if SSG, enter seed
            if self.seedtype['text'] == 'SSG':
                seed = self.seedentry.get()
            
                ac.sleep(delay)
                ac.key_press('Space') #enter more world options
                
                ac.key_press('TAB')
                ac.key_press('TAB') 
                ac.sleep(delay)
                ac.key_press('TAB') #hover seed
                ac.type(seed) #enter seed
                ac.sleep(delay)

                ac.key_press('TAB')
                ac.key_press('TAB')
                ac.key_press('TAB')
                ac.key_press('TAB')
                ac.key_press('TAB') #hover done
                ac.sleep(delay)
                ac.key_press('space') #back to main create world screen
                ac.sleep(delay)

            ac.key_press('TAB') #hover create new world
            ac.sleep(delay)
            ac.key_press('space') #create new world

            self.ActionChain = ac
            actionchain.append(ac)
        

    def SetAHK(self, event=None):
        #global actionchain
        #actionchain = self.ActionChain
        self.master.destroy()


def bring_window():
    root = Tk()
    gui = TimerSettings(root)
    root.mainloop()

while True:   
    bring_window()

    global inte
    inte=0
    is_alive = True

    def add_to_bindings():
        global actionchain
        global currentac
        global inte
        currentac = actionchain[inte]
        inte+=1
        bindings.append([["control", "m"], None, perform_ac])
        perform_ac()

    def perform_ac():
        global currentac
        global inte
        ac = currentac
        ac.perform()
    
    def exit_resetting():
        global is_alive
        global inte
        global actionchain
        inte=0
        actionchain = []
        stop_checking_hotkeys()
        is_alive = False
    

    bindings=[]

    bindings.append([["control", "m"], None, add_to_bindings])
    bindings.append([["control", "l"], None, exit_resetting])

    register_hotkeys(bindings)
    start_checking_hotkeys()

    while is_alive:        
        time.sleep(5)

