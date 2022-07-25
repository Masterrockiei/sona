class script(object):
    START_TXT = """𝐻𝑒𝑙𝑙𝑜 {},
𝑀𝑦 𝑛𝑎𝑚𝑒 𝑖𝑠 <a href=https://t.me/{}>{}</a>,𝐼 𝑐𝑎𝑛 𝑝𝑟𝑜𝑣𝑖𝑑𝑒 𝑚𝑜𝑣𝑖𝑒𝑠, 𝐽𝑢𝑠𝑡 𝑎𝑑𝑑 𝑚𝑒 𝑡𝑜 𝑦𝑜𝑢𝑟 𝑔𝑟𝑜𝑢𝑝 𝑎𝑛𝑑 𝑒𝑛𝑗𝑜𝑦 💖"""
    HELP_TXT = """𝐻𝑒𝑦 {}
𝐻𝑒𝑟𝑒 𝐼𝑠 𝑇ℎ𝑒 𝐻𝑒𝑙𝑝 𝐹𝑜𝑟 𝑀𝑦 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Unni0240>Amal Nath</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴: <a href=https://github.com/Masterrockiei/source>𝙷𝙴𝚁𝙴</a>
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Sakura is not a open source project. 
- but i will give my movie group link join and enjoy
✯ 🎬 𝑀𝑜𝑣𝑖𝑒 𝐺𝑟𝑜𝑢𝑝:<a href=https://t.me/sakura_movies>𝑇ℎ𝑖𝑠</a>
<b>DEVS:</b>
- <a href=https://t.me/Unni0240>Amal Nath</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and Sakura will respond whenever a keyword is found the message
<b>NOTE:</b>
1. Sakura should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- Sakura Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Sakura supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/amal_nath_05)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    MUSIC_TXT = """Help: <b>you tube</b>
    
Music download modules, for those who love music.
<b>Commands and Usage:</b>
• /song or /mp3 (songname) - download song from yt servers.
• /video or /mp4 (songname) - download video from yt servers.
<b>NOTE:</b>
• These commands works only on pm."""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Eva Maria
<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """⍟ 𝑇𝑜𝑡𝑎𝑙 𝐹𝑖𝑙𝑒𝑠: <code>{}</code>
⍟ 𝑇𝑜𝑡𝑎𝑙 𝑈𝑠𝑒𝑟𝑠: <code>{}</code>
⍟ 𝑇𝑜𝑡𝑎𝑙 𝐶ℎ𝑎𝑡𝑠: <code>{}</code>
⍟ 𝑈𝑠𝑒𝑑 𝑆𝑡𝑜𝑟𝑎𝑔𝑒: <code>{}</code> 𝙼𝙱
⍟ 𝐹𝑟𝑒𝑒 𝑆𝑡𝑜𝑟𝑎𝑔𝑒: <code>{}</code> 𝙼𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
