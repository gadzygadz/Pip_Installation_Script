from subprocess import call
import os

"""
Installs user defined packages from pip during compile time
packages - a list of the names of the required packages
pythons - the python or pythons command you wish to install them to - Default is python and python3
pips - the usable pip commands, Defaulted to pip and pip3
"""
def install(packages, pythons=['python3 ', 'py3 '], pips=['pip ', 'pip3 ']):
    if os.system() != 'Windows':
        #ask for sudo permissions becuase of the large amount of unformated pythons out there  
        call('sudo thisIsNotARealCommandButItWillGrantTheTerminalSudoAccess', shell=True)

    #cleaning imports
    for i in range(len(pythons)):
        pythons[i] = pythons[i].strip()
        pythons[i] += ' '
        if '-m' not in pythons[i]:
            pythons[i] += ' -m '

    for i in range(len(pips)):
        pips[i] = pips[i].strip()
        if 'install' not in pips[i]:
            pips[i] += ' install '
        else:
            pips[i] += ' '

    # handles
    for i in range(len(packages)):
        packages[i] = packages[i].strip()

    print('Now installing ' + str(packages))

    # actual installing
    for pip in pips:
        for package in packages:
            try:
                call(pip + package, shell=True)
            except:
                for python in pythons:
                    try:
                        call(python + pip + package, shell=True)
                    except:
                        None

    # clears the terminal
    try:
        call('cls', shell=True)
    except:
        call('clear', shell=True)

    
    if os.system() != 'Windows':
        #kills the sudo
        call('sudo -k')