from colorama import Back, Fore
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