from typing import List
 
 
from telegram.ext import run_async
 
__help__ = """

"*These persons helped me a lot in direct and indirect ways to build my bot*"



    animation_interval = 1

    animation_ttl = range(0, 30)

   # input_str = event.pattern_match.group(1)

   # if input_str == "chu":

    await event.edit("Credits......")

    animation_chars = [
        
            "`Searching throughout Telegram`",
            "`Users Found.`",
            "`user1... dank guy\n@dank_as_fuck`",
            "`user2... Phoenix guy\n@RealPhoenix`",
            "`user3... base repo\n skylee`",    
            "`user4....simp but good coder \n @pokurt`",
           
            "`These were some people who helped me knowimgly and unknowingly `"
        ]


    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 30])
"""

__mod_name__ = "Credits"
