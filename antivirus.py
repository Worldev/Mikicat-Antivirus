#!/usr/bin/python3

#################################### BY MIKICAT ###############################################
###############################A CATBOTS AFFILIATE#############################################
###IF YOU DETECT BUGS, PLEASE OPEN AN ISSUE OR REPORT THEM TO http://mikicatantivirus.weebly.com/contact.html ##

import os
import platform
import time
from tkinter import *

# Auto dir setup.
if platform.system() == "Windows":
    linux = False
    windows = True
elif platform.system() == "Linux":
    linux = True
    windows = False
else:
    print("Mikicat Antivirus is not compatible with your operative system.")
    os._exit(1)
home = os.path.expanduser('~')

extfiles = []
files = []

directory = ("{0}\AppData\Local".format(home) if windows else "{0}/.config".format(home))
directory2 = ("C:\Windows\system32" if windows else "/sbin")
directory3 = ("{0}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(home) if windows else "/etc/init.d")
directory4 = ("{0}\Downloads".format(home) if windows else "{0}/Downloads".format(home))

# Extensions
ext = '.bat'
ext2 = '.Gen'
ext3 = '.gen'
ext4 = '.vbs' # Do not scan it in system32
ext5 = '.inf' # Do not scan it in system32
ext6 = '.vbe' # Do not scan it in system32
ext7 = '.vb'  # Do not scan it in system32
ext8 = '.gzquar'
ext9 = '.vexe'
ext10 = '.sys' # Important: Only detect this if found in Downloads. If it is in any other detection of any other part of the code, please delete the "or file.endswith(ext10)". If it is put in the system32, it will delete essential system files.
ext11 = '.aru'
ext12 = '.smtmp'
ext13 = '.ctbl'
ext14 = '.dxz'
ext15 = '.cih'
ext16 = '.kcd'
ext17 = '.sop'
ext18 = '.tsa'
ext19 = '.xir'
ext20 = '.fnr'
ext21 = '.dom'
ext22 = '.hlw'
ext23 = '.lik'
ext24 = '.s7p'
ext25 = '.rhk'
ext26 = '.dlb'
ext27 = '.bll'
ext28 = '.dyz'
ext29 = '.fag'
ext30 = '.xtbl'
ext31 = '.fjl'
ext32 = '.cryptolocker'
ext33 = '.mjz'
ext34 = '.osa'
ext35 = '.bxz'
ext36 = '.mfu'
ext37 = '.ezt'
ext38 = '.dyv'
ext39 = '.iws'
ext40 = '.xdu'
ext41 = '.dllx'
ext42 = '.uzy'
ext43 = '.ska'
ext44 = '.mjg'
ext45 = '.txs'
ext46 = '.upa'
ext47 = '.bls'
ext48 = '.cc'
ext49 = '.lkh'
ext50 = '.tko'
ext51 = '.tti'
ext52 = '.dli'
ext53 = '.ceo'
ext54 = '.rna'
ext55 = '.delf'
ext56 = '.spam'
ext57 = '.cxq'
ext58 = '.vzr'
ext59 = '.bmw'
ext60 = '.atm'
ext61 = '.fuj'
ext62 = '.ce0'
ext63 = '.lok'
ext64 = '.ssy'
ext65 = '.hts'
ext66 = '.hsq'
ext67 = '.qit'
ext68 = '.pid'
ext69 = '.aepl'
ext70 = '.xnt'
ext71 = '.aut'
ext72 = '.dx'
ext73 = '.zvz'
ext74 = '.bqf'
ext75 = '.iva'
ext76 = '.pr'
ext77 = '.let'
ext78 = '.cyw'
ext79 = '.bup'
ext80 = '.bps'
ext81 = '.epub.exe'
# Extensions

master = Tk()
ideatxt = open("assets/idea.txt").read()
def idea():
    print('opening')
    tk = Tk()
    tk.title("Idea --> Content from idea.txt")
    tk.resizable(0, 0)
    Label(tk, text=ideatxt).grid(row=1, sticky=W)
    Button(tk, text="Quit", command=tk.destroy).grid(row=2, column=2, sticky=W)

def done4():
    root = Tk()
    root.title("Mikicat's Antivirus™: Finished")
    root.resizable(0, 0)
    Label(root, text="DONE: No virus found in %s." % directory4).grid(row=1, sticky=W)
    Label(root, text="\n").grid(row=2, sticky=W)
    Label(root, text="Thanks for using Miquel's Antivirus!").grid(row=3, sticky=W)
    Button(root, text="Quit", command=root.destroy).grid(row=4, column=2, sticky=W)
    Button(root, text="Idea", command=idea).grid(row=4, sticky=W)
    print("4")

def finish():
    root = Tk()
    Label(root, text="Thanks for using Miquel's Antivirus!").grid(row=3, sticky=W)
    Button(root, text="Quit", command=root.destroy).grid(row=4, column=2, sticky=W)
    Button(root, text="Idea", command=idea).grid(row=4, sticky=W)
    
def yes4():
    for item in extfiles:
        os.remove(directory4 + ("/" if linux else "\\") + item)
    del files[:]
    del extfiles[:]
    root = Tk()
    root.title("Done")
    root.resizable(0, 0)
    Label(root, text="Done").grid(row=1, sticky=W)
    Button(root, text="Finish", command=finish).grid(row=2, sticky=W)
    print("Done")
        
def detection4():
    del files[:]
    del extfiles[:]
    for file in os.listdir(directory4): 
        if file.endswith(ext) or file.endswith(ext2) or file.endswith(ext3) or file.endswith(ext4) or file.endswith(ext5)\
           or file.endswith(ext6) or file.endswith(ext7) or file.endswith(ext8) or file.endswith(ext9) or file.endswith(ext10)\
           or file.endswith(ext11) or file.endswith(ext12) or file.endswith(ext13) or file.endswith(ext14) or file.endswith(ext15)\
           or file.endswith(ext16) or file.endswith(ext17) or file.endswith(ext18) or file.endswith(ext19) or file.endswith(ext20)\
           or file.endswith(ext21) or file.endswith(ext22) or file.endswith(ext23) or file.endswith(ext24) or file.endswith(ext25)\
           or file.endswith(ext26) or file.endswith(ext27) or file.endswith(ext28) or file.endswith(ext29) or file.endswith(ext30)\
           or file.endswith(ext31) or file.endswith(ext32) or file.endswith(ext33) or file.endswith(ext34) or file.endswith(ext35)\
           or file.endswith(ext36) or file.endswith(ext37) or file.endswith(ext38) or file.endswith(ext39) or file.endswith(ext40)\
           or file.endswith(ext41) or file.endswith(ext42) or file.endswith(ext43) or file.endswith(ext44) or file.endswith(ext45)\
           or file.endswith(ext46) or file.endswith(ext47) or file.endswith(ext48) or file.endswith(ext49) or file.endswith(ext50)\
           or file.endswith(ext51) or file.endswith(ext52) or file.endswith(ext53) or file.endswith(ext54) or file.endswith(ext55)\
           or file.endswith(ext56) or file.endswith(ext57) or file.endswith(ext58) or file.endswith(ext59) or file.endswith(ext60)\
           or file.endswith(ext61) or file.endswith(ext62) or file.endswith(ext63) or file.endswith(ext64) or file.endswith(ext65)\
           or file.endswith(ext66) or file.endswith(ext67) or file.endswith(ext68) or file.endswith(ext69) or file.endswith(ext70)\
           or file.endswith(ext71) or file.endswith(ext72) or file.endswith(ext73) or file.endswith(ext74) or file.endswith(ext75)\
           or file.endswith(ext76) or file.endswith(ext77) or file.endswith(ext78) or file.endswith(ext79) or file.endswith(ext80)\
           or file.endswith(ext81):
            extfiles.append(file)
    for file in os.listdir(directory4):
        files.append(file)
    if extfiles != []:
        tk = Tk()
        tk.title("WARNING")
        tk.resizable(0, 0)
        Label(tk, text="WARNING: POSSIBLE VIRUS DETECTED").grid(row=1, sticky=W)
        Label(tk, text="Possible virus: %s" % extfiles).grid(row=2, sticky=W)
        Button(tk, text="Delete", command=yes4).grid(row=8, column=2, sticky=W)
        Button(tk, text="Cancel", command=tk.destroy).grid(row=8, sticky=W)
    if extfiles == []:  
        done4()

def done3():
    root = Tk()
    root.title("Mikicat's Antivirus™: Done")
    root.resizable(0, 0)
    Label(root, text="DONE: No virus found in %s" % directory3).grid(row=1, sticky=W)
    Button(root, text="Continue", command=detection4).grid(row=3, column=2, sticky=W)
    Button(root, text="Quit", command=root.destroy).grid(row=3, sticky=W)
    print("3")

def yes3():
    for item in extfiles:
        os.remove(directory3 + ("/" if linux else "\\") + item)
    del files[:]
    del extfiles[:]
    root = Tk()
    root.title("Done")
    root.resizable(0, 0)
    Label(root, text="Done").grid(row=1, sticky=W)
    Button(root, text="Continue", command=detection4).grid(row=2, column=2, sticky=W)
    Button(root, text="Quit", command=root.destroy).grid(row=2, sticky=W)
    print("Done")

def detection3():
    del files[:]
    del extfiles[:]
    for file in os.listdir(directory3): 
        if file.endswith(ext) or file.endswith(ext2) or file.endswith(ext3) or file.endswith(ext8) or file.endswith(ext9)\
           or file.endswith(ext11) or file.endswith(ext12) or file.endswith(ext13) or file.endswith(ext14) or file.endswith(ext15)\
           or file.endswith(ext16) or file.endswith(ext17) or file.endswith(ext18) or file.endswith(ext19) or file.endswith(ext20)\
           or file.endswith(ext21) or file.endswith(ext22) or file.endswith(ext23) or file.endswith(ext24) or file.endswith(ext25)\
           or file.endswith(ext26) or file.endswith(ext27) or file.endswith(ext28) or file.endswith(ext29) or file.endswith(ext30)\
           or file.endswith(ext31) or file.endswith(ext32) or file.endswith(ext33) or file.endswith(ext34) or file.endswith(ext35)\
           or file.endswith(ext36) or file.endswith(ext37) or file.endswith(ext38) or file.endswith(ext39) or file.endswith(ext40)\
           or file.endswith(ext41) or file.endswith(ext42) or file.endswith(ext43) or file.endswith(ext44) or file.endswith(ext45)\
           or file.endswith(ext46) or file.endswith(ext47) or file.endswith(ext48) or file.endswith(ext49) or file.endswith(ext50)\
           or file.endswith(ext51) or file.endswith(ext52) or file.endswith(ext53) or file.endswith(ext54) or file.endswith(ext55)\
           or file.endswith(ext56) or file.endswith(ext57) or file.endswith(ext58) or file.endswith(ext59) or file.endswith(ext60)\
           or file.endswith(ext61) or file.endswith(ext62) or file.endswith(ext63) or file.endswith(ext64) or file.endswith(ext65)\
           or file.endswith(ext66) or file.endswith(ext67) or file.endswith(ext68) or file.endswith(ext69) or file.endswith(ext70)\
           or file.endswith(ext71) or file.endswith(ext72) or file.endswith(ext73) or file.endswith(ext74) or file.endswith(ext75)\
           or file.endswith(ext76) or file.endswith(ext77) or file.endswith(ext78) or file.endswith(ext79) or file.endswith(ext80)\
           or file.endswith(ext81):
            extfiles.append(file)
    for file in os.listdir(directory3):
        files.append(file)
    if extfiles != []:
        tk = Tk()
        tk.title("WARNING")
        tk.resizable(0, 0)
        Label(tk, text="WARNING: POSSIBLE VIRUS DETECTED").grid(row=1, sticky=W)
        Label(tk, text="Possible virus: %s" % extfiles).grid(row=2, sticky=W)
        Button(tk, text="Delete", command=yes3).grid(row=8, column=2, sticky=W)
        Button(tk, text="Cancel", command=tk.destroy).grid(row=8, sticky=W)
    if extfiles == []:  
        done3()

def done2():
    root = Tk()
    root.title("Mikicat's Antivirus™: Done")
    root.resizable(0, 0)
    Label(root, text="DONE: No virus found in %s" % directory2).grid(row=1, sticky=W)
    Button(root, text="Continue", command=detection3).grid(row=3, column=2, sticky=W)
    Button(root, text="Quit", command=root.destroy).grid(row=3, sticky=W)
    print("2")

def yes2():
    for item in extfiles:
        os.remove(directory2 + ("/" if linux else "\\") + item)
    del files[:]
    del extfiles[:]
    root = Tk()
    root.title("Done")
    root.resizable(0, 0)
    Label(root, text="Done").grid(row=1, sticky=W)
    Button(root, text="Continue", command=detection3).grid(row=2, column=2, sticky=W)
    Button(root, text="Quit", command=root.destroy).grid(row=2, sticky=W)
    print("Done")

def detection2():
    del files[:]
    del extfiles[:]
    for file in os.listdir(directory2): 
        if file.endswith(ext) or file.endswith(ext2) or file.endswith(ext3) or file.endswith(ext8) or file.endswith(ext9)\
           or file.endswith(ext11) or file.endswith(ext12) or file.endswith(ext13) or file.endswith(ext14) or file.endswith(ext15)\
           or file.endswith(ext16) or file.endswith(ext17) or file.endswith(ext18) or file.endswith(ext19) or file.endswith(ext20)\
           or file.endswith(ext21) or file.endswith(ext22) or file.endswith(ext23) or file.endswith(ext24) or file.endswith(ext25)\
           or file.endswith(ext26) or file.endswith(ext27) or file.endswith(ext28) or file.endswith(ext29) or file.endswith(ext30)\
           or file.endswith(ext31) or file.endswith(ext32) or file.endswith(ext33) or file.endswith(ext34) or file.endswith(ext35)\
           or file.endswith(ext36) or file.endswith(ext37) or file.endswith(ext38) or file.endswith(ext39) or file.endswith(ext40)\
           or file.endswith(ext41) or file.endswith(ext42) or file.endswith(ext43) or file.endswith(ext44) or file.endswith(ext45)\
           or file.endswith(ext46) or file.endswith(ext47) or file.endswith(ext48) or file.endswith(ext49) or file.endswith(ext50)\
           or file.endswith(ext51) or file.endswith(ext52) or file.endswith(ext53) or file.endswith(ext54) or file.endswith(ext55)\
           or file.endswith(ext56) or file.endswith(ext57) or file.endswith(ext58) or file.endswith(ext59) or file.endswith(ext60)\
           or file.endswith(ext61) or file.endswith(ext62) or file.endswith(ext63) or file.endswith(ext64) or file.endswith(ext65)\
           or file.endswith(ext66) or file.endswith(ext67) or file.endswith(ext68) or file.endswith(ext69) or file.endswith(ext70)\
           or file.endswith(ext71) or file.endswith(ext72) or file.endswith(ext73) or file.endswith(ext74) or file.endswith(ext75)\
           or file.endswith(ext76) or file.endswith(ext77) or file.endswith(ext78) or file.endswith(ext79) or file.endswith(ext80)\
           or file.endswith(ext81):
            extfiles.append(file)
    for file in os.listdir(directory2):
        files.append(file)
    if extfiles != []:
        tk = Tk()
        tk.title("WARNING")
        tk.resizable(0, 0)
        Label(tk, text="WARNING: POSSIBLE VIRUS DETECTED").grid(row=1, sticky=W)
        Label(tk, text="Possible virus: %s" % extfiles).grid(row=2, sticky=W)
        Button(tk, text="Delete", command=yes2).grid(row=8, column=2, sticky=W)
        Button(tk, text="Cancel", command=tk.destroy).grid(row=8, sticky=W)
    if extfiles == []:  
        done2()

def done1():
    root = Tk()
    root.resizable(0, 0)
    root.title("Mikicat's Antivirus™: Done")
    Label(root, text="DONE: No virus found in %s" % directory).grid(row=1, sticky=W)
    Button(root, text="Continue", command=detection2).grid(row=3, column=2, sticky=W)
    Button(root, text="Quit", command=root.destroy).grid(row=3, sticky=W)
    print("1")

def yes1():
    for item in extfiles:
        os.remove(directory + ("/" if linux else "\\") + item)
    del files[:]
    del extfiles[:]
    root = Tk()
    root.resizable(0, 0)
    root.title("Done")
    Label(root, text="Done").grid(row=1, sticky=W)
    Button(root, text="Continue", command=detection2).grid(row=2, column=2, sticky=W)
    Button(root, text="Quit", command=root.destroy).grid(row=2, sticky=W)
    print("Done")
    
def detection1():
    del files[:]
    del extfiles[:]
    for file in os.listdir(directory): 
        if file.endswith(ext) or file.endswith(ext2) or file.endswith(ext3) or file.endswith(ext4) or file.endswith(ext5)\
           or file.endswith(ext6) or file.endswith(ext7) or file.endswith(ext8) or file.endswith(ext9) or file.endswith(ext11)\
           or file.endswith(ext12) or file.endswith(ext13) or file.endswith(ext14) or file.endswith(ext15)\
           or file.endswith(ext16) or file.endswith(ext17) or file.endswith(ext18) or file.endswith(ext19) or file.endswith(ext20)\
           or file.endswith(ext21) or file.endswith(ext22) or file.endswith(ext23) or file.endswith(ext24) or file.endswith(ext25)\
           or file.endswith(ext26) or file.endswith(ext27) or file.endswith(ext28) or file.endswith(ext29) or file.endswith(ext30)\
           or file.endswith(ext31) or file.endswith(ext32) or file.endswith(ext33) or file.endswith(ext34) or file.endswith(ext35)\
           or file.endswith(ext36) or file.endswith(ext37) or file.endswith(ext38) or file.endswith(ext39) or file.endswith(ext40)\
           or file.endswith(ext41) or file.endswith(ext42) or file.endswith(ext43) or file.endswith(ext44) or file.endswith(ext45)\
           or file.endswith(ext46) or file.endswith(ext47) or file.endswith(ext48) or file.endswith(ext49) or file.endswith(ext50)\
           or file.endswith(ext51) or file.endswith(ext52) or file.endswith(ext53) or file.endswith(ext54) or file.endswith(ext55)\
           or file.endswith(ext56) or file.endswith(ext57) or file.endswith(ext58) or file.endswith(ext59) or file.endswith(ext60)\
           or file.endswith(ext61) or file.endswith(ext62) or file.endswith(ext63) or file.endswith(ext64) or file.endswith(ext65)\
           or file.endswith(ext66) or file.endswith(ext67) or file.endswith(ext68) or file.endswith(ext69) or file.endswith(ext70)\
           or file.endswith(ext71) or file.endswith(ext72) or file.endswith(ext73) or file.endswith(ext74) or file.endswith(ext75)\
           or file.endswith(ext76) or file.endswith(ext77) or file.endswith(ext78) or file.endswith(ext79) or file.endswith(ext80)\
           or file.endswith(ext81):
            extfiles.append(file)
    for file in os.listdir(directory):
        files.append(file)
    if extfiles != []:
        tk = Tk()
        tk.title("WARNING")
        tk.resizable(0, 0)
        Label(tk, text="WARNING: POSSIBLE VIRUS DETECTED").grid(row=1, sticky=W)
        Label(tk, text="Possible virus: %s" % extfiles).grid(row=2, sticky=W)
        Button(tk, text="Delete", command=yes1).grid(row=8, column=2, sticky=W)
        Button(tk, text="Cancel", command=tk.destroy).grid(row=8, sticky=W)
    if extfiles == []:  
        done1()

lic = "This program is free software: You can redistribute it and/or modify it under the terms of the General Public License version 3"
imp = open("assets/IMPORTANT.txt").read()
helptxt = open("assets/help.txt").read()
def licinfo():
    print('opening')
    tk = Tk()
    tk.resizable(0, 0)
    tk.title("License")
    Label(tk, text=lic).grid(row=1, sticky=W)
    Button(tk, text="Quit", command=tk.destroy).grid(row=2, column=2, sticky=W)
def important():
    print('opening')
    tk = Tk()
    tk.resizable(0, 0)
    tk.title("IMPORTANT --> Content from IMPORTANT.txt")
    Label(tk, text=imp).grid(row=1, sticky=W)
    Button(tk, text="Quit", command=tk.destroy).grid(row=2, column=2, sticky=W)
def destroy():
    master.destroy()
    print("Exited cleanly")
    time.sleep(0.5)
def infohelp():
    tk = Tk()
    tk.resizable(0, 0)
    tk.title("Help --> Content from help.txt")
    Label(tk, text=helptxt).grid(row=1, sticky=W)
    Button(tk, text="Return", command=tk.destroy).grid(row=2, sticky=W)
    
master.title("Mikicat's Antivirus™")
master.resizable(0, 0)
Button(master, text="Help", command=infohelp).grid(row=0, column=5, sticky=W)
photo = PhotoImage(file="antivirus2.gif")
label = Label(image=photo)
label.image = photo 
label.grid(row=1)
Label(master, text="Today is %s !" % time.asctime()).grid(row=2, sticky=W)
Label(master, text="\n").grid(row=3, sticky=W)
Label(master, text="\n").grid(row=5, sticky=W)
Label(master, text="By Mikicat").grid(row=6, sticky=W)
Label(master, text="\n").grid(row=7, sticky=W)
Button(master, text="Start", underline=0, command=detection1).grid(row=8, column=2, sticky=W)
Button(master, text="Quit", underline=0, command=destroy).grid(row=8, sticky=W)
Button(master, text="License", underline=0, command=licinfo).grid(row=8, column=3, sticky=W)
Button(master, text="Important", underline=0, command=important).grid(row=8, column=4, sticky=W)
Button(master, text="Idea", underline=0, command=idea).grid(row=8, column=5, sticky=W)

print("Starting tkinter cleanly")

mainloop()

