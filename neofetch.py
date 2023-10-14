from colorama import Back, Fore, init
from getpass import getuser
from socket import gethostname
import platform
from os import environ
import wmi
from pyautogui import size
from psutil import virtual_memory
from datetime import timedelta
from uptime import uptime
import winreg
import sys
init()
def fg(text, _color):
    tx = text + Fore.RESET
    if _color == 'red':
        return Fore.RED + tx
    elif _color == 'blue':
        return Fore.BLUE + tx
    elif _color == 'green':
        return Fore.GREEN + tx
    elif _color == 'reset':
        return Fore.RESET + tx
    elif _color == 'yellow':
        return Fore.YELLOW + tx
    elif _color == 'cyan':
        return Fore.CYAN + tx
    elif _color == 'magneta':
        return Fore.MAGENTA + tx
def bg(text, _color):
    tx = text + Back.RESET
    if _color == 'red':
        return Back.RED + tx
    elif _color == 'blue':
        return Back.BLUE + tx
    elif _color == 'green':
        return Back.GREEN + tx
    elif _color == 'reset':
        return Back.RESET + tx
    elif _color == 'yellow':
        return Back.YELLOW + tx
    elif _color == 'cyan':
        return Back.CYAN + tx
    elif _color == 'magneta':
        return Back.MAGENTA + tx


if '-?' in sys.argv or '-h' in sys.argv or '-help' in sys.argv:
    print('''
neofetch-win help topics
args
    -color <color>
        this will change foreground text color
        red; green; blue; yellow; cyan; magneta
    --no-ascii-image
        this will hide the ASCII image
''')
    sys.exit()


ascii_images = {'ubuntu':'''            .-/+oossssoo+/-.            
        `:+ssssssssssssssssss+:`        
      -+ssssssssssssssssssyyssss+-      
    .ossssssssssssssssssdMMMNysssso.    
   /ssssssssssshdmmNNmmyNMMMMhssssss/   
  +ssssssssshmydMMMMMMMNddddyssssssss+  
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/ 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
ossyNMMMNyMMhsssssssssssssshmmmhssssssso
ossyNMMMNyMMhsssssssssssssshmmmhssssssso
+sssshhhyNMMNyssssssssssssyNMMMysssssss+
.ssssssssdMMMNhsssssssssshNMMMdssssssss.
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/ 
  +sssssssssdmydMMMMMMMMddddyssssssss+  
   /ssssssssssshdmNNNNmyNMMMMhssssss/   
    .ossssssssssssssssssdMMMNysssso.    
      -+sssssssssssssssssyyyssss+-      
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-. 
''', 
'windows':'''                              ##     
               # ###############     
    ############ ###############     
    ############ ###############     
    ############ ###############     
    ############ ###############     
    ############ ###############     
    ============ ===============     
    ############ ###############     
    ############ ###############     
    ############ ###############     
    ############ ###############     
            #### ###############     
                          ######                                           
'''}


def get_theme_name():
    if platform.system() == 'Windows':
        try:
            reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize'
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
            theme_name, _ = winreg.QueryValueEx(reg_key, 'AppsUseLightTheme')
            winreg.CloseKey(reg_key)
            return 'Light' if theme_name == 0 else 'Dark'
        except:
            return 'Unknown'
    else:
        return 'Unknown'



user = getuser()
hostname = gethostname()
osname = platform.platform(1,1).replace('-', ' ')
kernel = platform.version() + '-' + environ['PROCESSOR_ARCHITECTURE'].lower()
_uptime = str(timedelta(seconds=uptime()))
#_uptime = str(timedelta(seconds=100000))
#if 100000 < 86400:
if uptime() < 86400:
    _uptime=_uptime.split(':')
    __uptime = _uptime[0] + ' hours, ' + _uptime[1] + ' mins'
else:
    hms = _uptime.split(' day, ')[1].split(':')
    __uptime = _uptime.split(' day, ')[0] + hms[0] + ' hours, ' + hms[1] + ' mins'

try:
    shell = environ['SHELL']
except:
    shell = 'Unknown'
res = str(size()[0]) + 'x' + str(size()[1])
themename = get_theme_name()
cpuname = wmi.WMI().Win32_Processor()[0].Name
mem = virtual_memory()
memtotal = str(round(mem.total / 1024 / 1024))
memused = str(round(mem.used / 1024 / 1024))
memf = memused + 'MiB / ' + memtotal + 'MiB'

# Customs
fgcolor = 'red'
for i in range(len(sys.argv)):
    if sys.argv[i] == '-color':
        fgcolor = sys.argv[i+1]
imgcolor = 'red'
for i in range(len(sys.argv)):
    if sys.argv[i] == '--img-color':
        imgcolor = sys.argv[i+1]

def neoprint(NoAsciiImg=False):
    ascii_image = ascii_images['windows'].split('\n')
    j=0
    if NoAsciiImg:
        ascii_image = []
    lengtha = len(ascii_image)
    lengthb = len(text)
    if lengtha > lengthb:
        long = lengtha-lengthb
        short = lengthb
    else:
        long = lengthb-lengtha
        short = lengtha
    for i in range(short):
        print(fg(ascii_image[i], 'red') + '    ' + text[i])
        j = i+1
    if lengtha > lengthb:
        for k in range(long):
            print(fg(ascii_image[j+k], 'red'))
    else:
        for k in range(long):
            if NoAsciiImg:
                print(text[j+k])
            else:
                print(45*' ' + text[j+k])


text = []
text.append(fg(user, fgcolor)+'@'+hostname)
text.append('-----------------')
text.append(fg('OS: ', fgcolor) + osname)
text.append(fg('Kernel: ', fgcolor) + kernel)
text.append(fg('Uptime: ', fgcolor) + __uptime)
text.append(fg('Shell: ', fgcolor) + shell)
text.append(fg('Resolution: ', fgcolor) + res)
text.append(fg('Theme: ', fgcolor) + themename)
text.append(fg('CPU: ', fgcolor) + cpuname)
text.append(fg('Memory: ', fgcolor) + memf)
neoprint('--no-ascii-image' in sys.argv)