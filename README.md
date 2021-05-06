# Python File to Windows/macOS Applications

A program which converts Python scripts into standalone applications using cx_Freeze and py2app

## Information

This program is written in 100% Python, you can find the prebuilt Windows version [here](https://github.com/ShadowStonks/Python-To-Executable)

Remember to put your .py files you wish to convert in the same directory as the tool.

### Running on macOS

Due to how py2app works on macOS, I can't make a pre-compiled stand-alone app for the project, in order to use the tool on macOS exctract [the macOS zip](https://github.com/ShadowStonks/Python-To-Executable) file to $HOME/Documents, the folder exctracted should be called 'PyToApp' and contain 'GUI.py' and 'setups.py', the 'GUI.py' is the file you want to run to convert your files.

Enjoy!

### Prerequisites

These are the things you need to run this script:

```
Python 3, tkinter and cx_Freeze or py2app.
```

### Installing Prerequisites

How to install these prerequisites, make sure to preinstall python 3 from [here](https://www.python.org/downloads/)

Open a terminal and enter these commands:

```
pip3 install tkinter
```

```
pip3 cx_Freeze   (for Windows version)
```

```
pip3 py2app   (for macOS version)
```
### Running

Simply download the python file from the [Releases](https://github.com/ShadowStonks/Discord-Bot/releases/) and run it using Python Launcher and you're done!

P.S: Make sure to create an empty Python file called: 'setups.py'. 

Enjoy!
