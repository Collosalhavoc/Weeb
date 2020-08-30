import time

from skylee.modules.disable import DisableAbleCommandHandler

from skylee import dispatcher

@run_async 
def ping(update, context):
    start_time = time.time()
    requests.get('https://api.telegram.org')
    end_time = time.time()
    ping_time = round((end_time - start_time)*1000, 3)
    update.effective_message.reply_text("*Your current ping😶*\n`{}ms`".format(ping_time), parse_mode=ParseMode.MARKDOWN)
    
    
