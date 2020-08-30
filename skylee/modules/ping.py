import time

from telegram.ext import run_async

from skylee import dispatcher
from skylee.modules.disable import DisableAbleCommandHandler

@run_async 
def ping(update, context):
    args=context.args
    start_time = time.time()
    requests.get('https://api.telegram.org')
    end_time = time.time()
    ping_time = round((end_time - start_time)*1000, 3)
    update.effective_message.reply_text("*Your current ping😶*\n`{}ms`".format(ping_time), parse_mode=ParseMode.MARKDOWN)
    
    
PING_HANDLER = DisableAbleCommandHandler("ping", ping, pass_args=True)
 
dispatcher.add_handler(PING_HANDLER)
 
__command_list__ = ["ping"]
__handlers__ = [PING_HANDLER]
