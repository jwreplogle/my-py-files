import subprocess
import os
import sys


def uupdt():
#Installs updates and software
    os.system('clear')
    subprocess.call("sudo apt-get install x11-xserver-utils libnss3 unclutter", shell=True)
    subprocess.call("sudo apt-get update", shell=True)
    subprocess.call("sudo apt-get dist-upgrade -y", shell=True)
    os.system('clear')
    print('\x1b[6;30;42m' + 'Updates & Software Installed!' + '\x1b[0m')
    
def uusr():
#Creates a user and add them to sudo and adm       
    uname = raw_input("Type Username: ")
    subprocess.call(["useradd", uname])
    subprocess.call(["passwd", uname])
    subprocess.call(["usermod", "-aG","sudo", uname])
    subprocess.call(["usermod", "-aG","adm", uname])
    print('\x1b[6;30;42m' + 'Sudo user creation is a Success!' + '\x1b[0m')        

def startmod():
#modifies the autostart file
    os.system('sudo cp /etc/xdg/lxsession/LXDE-pi/autostart /etc/xdg/lxsession/LXDE-pi/autostartorg')
    os.system('sudo rm /etc/xdg/lxsession/LXDE-pi/autostart') 
    f = open('/etc/xdg/lxsession/LXDE-pi/autostart','w+')
    f.write('\n' + '@lxpanel --profile LXDE-pi')
    f.write('\n' + '@pcmanfm --desktop --profile LXDE-pi')
    f.write('\n' + '@point-rpi')    
    f.write('\n' + '@xset s noblank')
    f.write('\n' + '@xset s off')
    f.write('\n' + '@xset -dpms')
    f.write('\n' + '@unclutter -idle 0.1 -root')
    uurl = raw_input("Enter URL=")
    bob = '@chromium-browser --incognito --kiosk ' + uurl
    f.write('\n' + bob)
    f.close()

def limod():
#modifies the lightdm.conf file
    f = open('/etc/lightdm/lightdm.conf','a')
    f.write('\n' + 'xserver-command= X -s 0 -dpms')
    f.close()
    print('\x1b[6;30;42m' + 'File modification was a Success!' + '\x1b[0m')

def umod():
#remove login pi from sudo and adm
    os.system('sudo deluser pi sudo')
    os.system('sudo deluser pi adm')
    print('\x1b[6;30;42m' + 'User Pi demotion was a Success!' + '\x1b[0m')

def flpscr():
    f = open('/boot/config.txt','w+')
    f.write('\n' + 'lcd_rotate=2')
    f.close()

def uprint():
#the ending is near
    print('\x1b[6;30;42m' + 'You may now reboot your system to go into KIOSK' + '\x1b[0m')


#start of programming
print('\033[94m' + "This script will:" + '\x1b[0m')
print('\033[94m' + "1: Update the system" + '\x1b[0m')
print('\033[94m' + "2: Install necessary software" + '\x1b[0m')
print('\033[94m' + "3: Ask you to create Admin user" + '\x1b[0m')
print('\033[94m' + "4: Modify autostart & lightdm files" + '\x1b[0m')
print('\033[94m' + "5: Demote user Pi" + '\x1b[0m')
print('\033[94m' + "Press CTRL C to Stop this process" + '\x1b[0m')
print('\033[94m' + "Or" + '\x1b[0m')
syop = int(input('\033[94m' + "Process Script? 1 -Continue 2 -Exit Script:" + '\x1b[0m'))

if syop == 1:
    uupdt()
    uusr()
    startmod()
    limod()
    umod()
    flpscr()
    uprint()

else:
    sys.exit()
