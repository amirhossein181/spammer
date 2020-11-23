from api import *
from docopt import docopt
import os
from colorama import AnsiToWin32,Back,init,Fore
import sys

init(wrap=False)
color = AnsiToWin32(sys.stderr).stream

usage = '''
Usage:
Spammer_Nasl.py --append <txt>
Spammer_Nasl.py --spam
Spammer_Nasl.py --settime <time>
Spammer_Nasl.py --reset'''

args = docopt(usage)
try:
    if args['--append']:
        append(args['<txt>'])
        print(Fore.GREEN,'[+] Text appended',file=color)

    elif args['--spam']:
        print(Fore.GREEN,'[+] Spam started...',file=color)
        spam()

    elif args['--settime']:
        time1 = args[('<time>')]
        set_time(time1)
        print(Fore.GREEN,'[+] Successfuly setting time')

    elif args['--reset']:
        con.close()
        os.remove('data.txt')
        os.remove('data.db')
        print(Fore.GREEN,'[+] Data successfuly deleted')
except:
    print(Fore.RED,'[-] Error: Please write like this:',usage,file=color)
# by AzraeL | @iam_azrael
