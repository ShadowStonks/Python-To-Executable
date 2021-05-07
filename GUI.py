from tkinter import *
import subprocess
from applescript import tell

def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1


def write():
    scriptName = EntryBox1.get()
    dataList = EntryBox2.get()
    optionsList = EntryBox3.get()

    scriptNameStr = ('APP = ["'+scriptName+'"]')
    dataListStr = ('DATA_FILES = ['+dataList+']')
    optionsListStr = ("'packages': ["+optionsList+"],")

    open_file = open('setups.py', 'w')

    open_file.write('from setuptools import setup')
    open_file.write('\n')
    open_file.write(scriptNameStr)
    open_file.write('\n')
    open_file.write(dataListStr)
    open_file.write('\nOPTIONS = {')
    open_file.write('\n')
    open_file.write(optionsListStr)
    open_file.write('\n}')
    open_file.write('\n')
    open_file.write('\nsetup(')
    open_file.write('\n    app=APP,')
    open_file.write('\n    data_files=DATA_FILES,')
    open_file.write("\n    options={'py2app': OPTIONS},")
    open_file.write("\n    setup_requires=['py2app'],")
    open_file.write('\n)')

    open_file.close()


def create():
    tell.app('Terminal', 'do script "' + 'cd $HOME/Documents/PyToApp ' + '&& python3 setups.py py2app''"')


root = Tk()
root.title('.py to .exe')

EnterLabelOne = Label(text="Enter name of script here (.py): ")
EnterLabelOne.pack()

EntryBox1 = Entry()
EntryBox1.config(justify=CENTER)
EntryBox1.pack()

EnterLabelTwo = Label(text="Enter extra files needed for Application: (eg text files or pictures)")
EnterLabelTwo.pack()

EntryBox2 = Entry()
EntryBox2.config(justify=CENTER)
EntryBox2.pack()

EnterLabelThree = Label(text="Enter package names to include in the program (leave blank if none): ")
EnterLabelThree.pack()

EntryBox3 = Entry()
EntryBox3.config(justify=CENTER)
EntryBox3.pack()

GenerateButton = Button(text='Make Setup', command=write)
GenerateButton.pack()

GenerateButton = Button(text='Create application', command=create)
GenerateButton.pack()

root.mainloop()
