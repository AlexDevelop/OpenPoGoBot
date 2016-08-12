# pylint: disable=redefined-builtin
from __future__ import print_function
from builtins import str
import time

from colorama import Fore, Back, Style
from pokemongo_bot.event_manager import manager

# Uncomment for type annotations on Python 3
# from typing import Optional


def log(string, color="white", prefix=None, fire_event=True):
    # type: (str, Optional[str], Optional[str], Optional[bool]) -> None
    if fire_event:
        manager.fire("logging", text=string, color=color, prefix=prefix)
    else:
        _log(text=string, color=color, prefix=prefix)


@manager.on("logging")
def _log(text="", color="white", prefix=None):
    # type: (str, Optional[str], Optional[str]) -> None
    color_hex = {
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'red': Fore.RED,
        'blue': Fore.BLUE,
        'cyan': Fore.CYAN,
        'black': Fore.BLACK,
    }
    string = str(text)
    output = u"[" + time.strftime("%Y-%m-%d %H:%M:%S") + u"] "
    if prefix is not None:
        output += u"[{}] ".format(str(prefix))
    output += string
    if color in color_hex:
        output = color_hex[color] + output + Style.RESET_ALL
    print(output)
