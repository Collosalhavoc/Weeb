from typing import List
 
 
from telegram.ext import run_async
 
from skylee import dispatcher
from skylee.modules.disable import DisableAbleCommandHandler
 
normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    " ",
]
morsefont = [
    "._ ",
    "_... ",
    "_._. ",
    "_.. ",
    ". ",
    ".._. ",
    "__. ",
    ".... ",
    ".. ",
    ".___ ",
    "_._ ",
    "._.. ",
    "__ ",
    "_. ",
    "___ ",
    ".__. ",
    "__._ ",
    "._. ",
    "... ",
    "_ ",
    ".._ ",
    "..._ ",
    ".__ ",
    "_.._ ",
    "_.__ ",
    "__.. ",
    ".____ ",
    "..___ ",
    "...__ ",
    "...._ ",
    "..... ",
    "_.... ",
    "__... ",
    "___.. ",
    "____. ",
    "_____ ",
    "   ",
]
 
 
@run_async
def morse(update,context):
    args= context.args
    string = "  ".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            morsecharacter = morsefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, morsecharacter)
 
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)
 
 
MORSE_HANDLER = DisableAbleCommandHandler("morse", morse, pass_args=True)
 
dispatcher.add_handler(MORSE_HANDLER)
 
__command_list__ = ["morse"]
__handlers__ = [MORSE_HANDLER]
 
 
