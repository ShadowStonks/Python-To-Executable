from tkinter import *
import time
import subprocess


def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1


def write():
    scriptName = EntryBox1.get()
    packagesInclude = list(EntryBox2.get())
    packagesExclude = list(EntryBox3.get())
    nameInput = EntryBox4.get()
    versInput = EntryBox5.get()
    descInput = EntryBox6.get()
    packagesIncludeStr = listToString(packagesInclude)
    packagesExcludeStr = listToString(packagesExclude)

    executableStr = ('    executables = [Executable("' + scriptName + '", base=base)]')
    buildList = ('build_exe_options = {"packages": [' + packagesIncludeStr + '], "excludes": [' + packagesExcludeStr + ']}')
    name = ('    name="'+nameInput+'",')
    version = ('    version="'+versInput+'",')
    description = ('    description="'+descInput+'",')

    open_file = open('setups.py', 'w')

    open_file.write('import sys')
    open_file.write('\nfrom cx_Freeze import setup, Executable')
    open_file.write('\n')
    open_file.write(buildList)
    open_file.write('\n')
    open_file.write('\nbase = None')
    open_file.write('\nif sys.platform == "win32":')
    open_file.write('\n    base = "Win32GUI"')
    open_file.write('\n')
    open_file.write('\nsetup(')
    open_file.write('\n')
    open_file.write(name)
    open_file.write('\n')
    open_file.write(version)
    open_file.write('\n')
    open_file.write(description)
    open_file.write('\n    options={"build_exe": build_exe_options},')
    open_file.write('\n')
    open_file.write(executableStr)
    open_file.write('\n)')

    open_file.close()


def create():
    subprocess.call('start /wait pip3 install cx_Freeze', shell=True)
    time.sleep(3)
    subprocess.call('start /wait python3 setups.py build', shell=True)


root = Tk()
root.title('.py to .exe')

EnterLabelOne = Label(text="Enter name of script here (.py): ")
EnterLabelOne.pack()

EntryBox1 = Entry()
EntryBox1.config(justify=CENTER)
EntryBox1.pack()

EnterLabelTwo = Label(text="Enter package names to include in the program (leave blank if none): ")
EnterLabelTwo.pack()

EntryBox2 = Entry()
EntryBox2.config(justify=CENTER)
EntryBox2.pack()

EnterLabelThree = Label(text="Enter package names to exclude in the program (leave blank if none): ")
EnterLabelThree.pack()

EntryBox3 = Entry()
EntryBox3.config(justify=CENTER)
EntryBox3.pack()

EnterLabelFour = Label(text="Enter name of application: ")
EnterLabelFour.pack()

EntryBox4 = Entry()
EntryBox4.config(justify=CENTER)
EntryBox4.pack()

EnterLabelFive = Label(text="Enter application version: ")
EnterLabelFive.pack()

EntryBox5 = Entry()
EntryBox5.config(justify=CENTER)
EntryBox5.pack()

EnterLabelSix = Label(text="Enter application description: ")
EnterLabelSix.pack()

EntryBox6 = Entry()
EntryBox6.config(justify=CENTER)
EntryBox6.pack()

GenerateButton = Button(text='Make Setup', command=write)
GenerateButton.pack()

GenerateButton = Button(text='Create application', command=create)
GenerateButton.pack()

root.mainloop()
