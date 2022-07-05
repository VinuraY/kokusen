# Creator --> AnonyMSAV (Vinura)
# Contact --> https://t.me/AnonyMSAV
import sys
import time
import port_scanner
import whois
import dos
import termcolor
import os
import platform


# Check system os type.
def check_system():

    system = platform.platform()

    if 'Linux' in system:

        os.system('clear')

    elif 'Windows' in system:

        os.system('cls')


# ASCII banners.
def banner(number):

    banner1 = termcolor.colored('''

                 ██ ▄█▀ ▒█████   ██ ▄█▀ █    ██   ██████ ▓█████  ███▄    █    
                 ██▄█▒ ▒██▒  ██▒ ██▄█▒  ██  ▓██▒▒██    ▒ ▓█   ▀  ██ ▀█   █    
                ▓███▄░ ▒██░  ██▒▓███▄░ ▓██  ▒██░░ ▓██▄   ▒███   ▓██  ▀█ ██▒   
                ▓██ █▄ ▒██   ██░▓██ █▄ ▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒   
                ▒██▒ █▄░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██████▒▒░▒████▒▒██░   ▓██░   
                ▒ ▒▒ ▓▒░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒    
                ░ ░▒ ▒░  ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░   
                ░ ░░ ░ ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░  ░  ░     ░      ░   ░ ░    
                ░  ░       ░ ░  ░  ░      ░           ░     ░  ░         ░    

                    A network scanner with some built in options!! 
                         Try and discover the world you need.''', 'blue', attrs=['blink'])

    banner2 = termcolor.colored('''
    
    ██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
    ██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
    ██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
    ██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝''', 'green')

    banner3 = termcolor.colored('''

    ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
    ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
    ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝''', 'yellow')

    banner4 = termcolor.colored('''

    ██████╗  ██████╗ ███████╗     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██║  ██║██║   ██║███████╗    ███████║   ██║      ██║   ███████║██║     █████╔╝ █████╗  ██████╔╝
    ██║  ██║██║   ██║╚════██║    ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝███████║    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝''', 'red')

    if number == 1:
        print(banner1)

    elif number == 2:
        print(banner2)

    elif number == 3:
        print(banner3)

    elif number == 4:
        print(banner4)


def info():

    text = termcolor.colored(f'''

            Creator : AnonyMSAV (Vinura)
            Version : 1.0v''', 'blue')

    for i in text:

        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.1)


check_system()

banner(1)
info()

time.sleep(0.2)
print(termcolor.colored('''

+-------------------+
| Available options |
+-------------------+

{1} Port Scanner
{2} Domain Lookup
{3} DoS attacker
{0} Exit''', 'yellow'))

options = int(input(termcolor.colored('\nEnter', 'red') +
              termcolor.colored(' >> ', 'blue')))

match options:

    case 1:

        check_system()
        banner(2)

        host = input(termcolor.colored('\nEnter IP address',
                     'red')+termcolor.colored(' : ', 'blue'))
        port = input(termcolor.colored(
            '\nPort range [default/ALL/number]', 'red')+termcolor.colored(' : ', 'blue'))
        count = int(input(termcolor.colored('\nThread count', 'red') +
                    termcolor.colored(' : ', 'blue')))

        # If port value is None it means we need to assign defalut value to the port variable.
        if port == '':

            port_scanner.main(count, host, 1000)

        # If port is not 'ALL' we change port variable type into int.
        elif port != 'ALL':

            port_scanner.main(count, host, int(port))

    case 2:

        check_system()
        banner(3)

        host = input(termcolor.colored('\nEnter domain name', 'red') +
                     termcolor.colored(' : ', 'blue'))
        whois.main(host)

    case 3:

        check_system()
        banner(4)

        print(termcolor.colored('''

+-----------------------+
| Available DoS attacks |
+-----------------------+

{1} SYN flood
{2} ICMP flood
{3} UDP flood
{0} Exit''', 'yellow'))

        attacks = int(input(termcolor.colored(
            '\nEnter', 'red') + termcolor.colored(' >> ', 'blue')))

        match attacks:

            case 1:

                host = input(termcolor.colored('\nEnter IP address',
                             'red')+termcolor.colored(' : ', 'blue'))
                time_frame = input(termcolor.colored(
                    '\nTime frame (default -> packet per 0.1 sec)', 'red')+termcolor.colored(' : ', 'blue'))

                # If time frame is empty, it means we need to set a default value.
                if time_frame == '':

                    dos.syn_flood(host)

                else:

                    dos.syn_flood(host, time_frame)

            case 2:

                host = input(termcolor.colored('\nEnter IP address',
                             'red')+termcolor.colored(' : ', 'blue'))
                dos.icmp_flood(host)

            case 3:

                host = input(termcolor.colored('\nEnter IP address',
                             'red')+termcolor.colored(' : ', 'blue'))
                dos.udp_flood(host)

            case 0:

                print(termcolor.colored('\nHappy hacking!', 'blue'))
                sys.exit()

            case _:

                print(termcolor.colored('\nTry again!', 'red'))
    case 0:

        print(termcolor.colored('\nHappy hacking!', 'blue'))
        sys.exit()

    case _:

        print(termcolor.colored('\nTry again!', 'red'))
