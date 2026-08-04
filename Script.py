# Use @Get_emojiIDbot to get the premium emoji ID.
# Example of adding a premium emoji to message: "hello <emoji id='5210956306952758910'>👋</emoji> dear"
# If the ID (5210956306952758910) does not work, the normal emoji (👋) will be used as the default.
# The bot owner must have Telegram Premium to use premium emojis in the bot.

class script(object):

    START_TXT = """👋 <b>Hello {}, <i>{}</i>

<i>Am Just A Advance Auto Filter Bot....😉

Just Add Me To Your Group And Channel And Connect Them And See My Pevers 🔥🔥😝</b>
</i>"""

    MY_ABOUT_TXT = """🤖 <b>System Architecture & Info</b>

🌍 <b>Server</b>: <a href="https://www.heroku.com">Cloud Engine</a>
🗄️ <b>Database</b>: <a href="https://www.mongodb.com">MongoDB Atlas</a>
🐍 <b>Language</b>: <a href="https://www.python.org">Python 3.11+</a>
⚡ <b>Framework</b>: <a href="https://kurigram.icu/">Kurigram Async</a>"""

    MY_OWNER_TXT = """👨‍💻 <b>Developer & Owner Details</b>

🧑‍💻 <b>Lead Developer</b>: Hansaka Anuhas
💬 <b>Telegram</b>: @Hansaka_Anuhas
🙋 <b>Owner</b>: @SreejithSKumar
🛠️ <b>Support</b>: Available 24/7 via Support Group"""

    STATUS_TXT = """📊 <b>Nova Filter System Diagnostics</b>

<b>👥 User & Group Metrics</b>
• 👤 Total Users: <code>{}</code>
• 😎 Premium Users: <code>{}</code>
• 👥 Total Connected Chats: <code>{}</code>

<b>🗄️ Data Database Status</b>
• 📦 DB Storage Used: <code>{}</code>

<b>🗳️ Primary Files Database</b>
• 🗂️ Indexed Files: <code>{}</code>
• 📦 Storage Used: <code>{}</code>

<b>🗳️ Secondary Files Database</b>
• 🗂️ Indexed Files: <code>{}</code>
• 📦 Storage Used: <code>{}</code>

<b>🚀 System Uptime</b>: <code>{}</code>"""

    NEW_GROUP_TXT = """📌 <b>#NewGroup Connected</b>

🏷️ <b>Title</b>: {}
🆔 <b>ID</b>: <code>{}</code>
🔗 <b>Username</b>: {}
👥 <b>Total Members</b>: <code>{}</code>"""

    NEW_USER_TXT = """👤 <b>#NewUser Started Bot</b>

🧑 <b>Name</b>: {}
🆔 <b>ID</b>: <code>{}</code>"""

    NOT_FILE_TXT = """👋 <b>Hello {},</b>

<blockquote>🥲 <b>We couldn't locate any streaming or download files for:</b> <code>{}</code></blockquote>

<b>🔍 Why might this file be missing?</b>

• ✏️ <b>Spelling Error</b>: Check for typos or release year formatting.
• ⏳ <b>Not Released Yet</b>: The movie or season might not have digital availability.

<b>💡 Recommended Next Steps:</b>
• 🌐 Click <b>Search Google</b> below to verify exact movie/series names and release dates.
• 📖 Click <b>Instructions</b> below to see advanced search syntax tips.
• 📝 Type <code>/request Movie Name Year</code> directly in chat to notify our 24/7 upload team!"""
    
    IMDB_TEMPLATE = """<blockquote><i>
<b>►Film : {title}
►Rating : {rating} | IMDB
►Genre : {genres}
►Language : {languages}</b></i></blockquote>

<i><b>©𝐓𝐞𝐚𝐦 𝐔𝐫𝐯𝐚𝐬𝐡𝐢 𝐓𝐡𝐞𝐚𝐭𝐞𝐫𝐬™️</i></b>"""

    FILE_CAPTION = """<i><b><blockquote>📚{file_name}</i></b></blockquote>

    <b><a href="https://t.me/+Ug2OqY7R9PM5Mjg1">©𝐓𝐞𝐚𝐦 𝐔𝐫𝐯𝐚𝐬𝐡𝐢 𝐓𝐡𝐞𝐚𝐭𝐞𝐫𝐬</a></b>"""

    WELCOME_TEXT = """👋 <b>Hello {mention},</b>

<blockquote>✨ Welcome to <b>{title}</b>! We are glad to have you here. Type any movie or series name below to get instant download links! 💞</blockquote>"""

    HELP_TXT = """👋 <b>Hello {},</b>
    
<b><i><u>How To Use Me!?</u></i></b>
<i>
-> Add Me To Any Group And Make Me Admin
-> Add Me To Your Desired Channel
</i>
<b>Bot Commands (Works Only In Admin Groups) :</b>"""

    ADMIN_COMMAND_TXT = """🛡️ <b>Admin Commands Panel</b>

<blockquote><b>⚙️ System & DB</b>
• 📊 /stats - Check system status
• 🔄 /restart - Reboot bot cleanly
• 🛠️ /repair_mode - Maintenance mode
• 🗳️ /index - Index channel files
• 📑 /index_channels - Indexed channels
• 🗑️ /delete - Delete files by query
• 💥 /delete_all - Wipe indexed DB

<b>📢 Broadcast & Groups</b>
• 📢 /broadcast - PM broadcast
• 📣 /grp_broadcast - Group broadcast
• 📌 /pin_broadcast - Pinned PM broadcast
• 📍 /pin_grp_broadcast - Pinned group broadcast
• 👥 /users - PM users stats
• 📁 /chats - Group chats stats
• 🚪 /leave - Leave group chat
• 🔗 /invite_link - Create invite link

<b>💎 VIP Premium & FSub</b>
• 👑 /add_prm - Grant VIP status
• 🚫 /rm_prm - Revoke VIP status
• 🛡️ /set_fsub - Force-Sub channels
• 🔔 /set_req_fsub - Request FSub channel
• 🧹 /delreq - Clear join requests</blockquote>"""
    
    PLAN_TXT = """💎 <b>Upgrade To Nova Premium</b>

<blockquote>Unlock exclusive VIP benefits and experience lightning-fast, ad-free file delivery without limits!</blockquote>

<b>🔥 Exclusive Premium Features:</b>
• 🚫 <b>100% Ad-Free Experience</b> (No shortlink redirects)
• ⚡ <b>Instant Watch & Download</b> (Stream online or fast direct download)
• 🔓 <b>No Force-Subscribe Required</b> (Skip channel joins)
• 🔖 <b>Unlimited Watchlist & Favorites</b>
• 💬 <b>Priority 24/7 Admin Support</b>

<b>🏷️ Available Subscription Tiers:</b>
<blockquote>{}</blockquote>

💬 <b>Ready to Upgrade?</b> Contact our support: @{}"""

    USER_COMMAND_TXT = """👤 <b>Bot User Commands Panel</b>

<b>🎬 Search & Files</b>

• 🚀 /start - Check if bot is alive & active
• 📝 /request - Request a new movie or TV series"""
    
    SOURCE_TXT = """📂 <b>Open Source Repository</b>

🛠️ <b>Project</b>: Nova Auto Filter Bot
🔗 <b>Repository</b>: <a href="https://github.com/xHansaka-Anuhas/Nova-Filter-Bot">GitHub Repo</a>
🧑‍💻 <b>Lead Developer</b>: @Hansaka_Anuhas"""


    NEW_ADDED_TEMPLATE = """✅ <b>New Content Added</b>

<blockquote><i>
<b>►Film : {title}
►Rating : {rating} | IMDB
►Genre : {genres}
►Language : {languages}</b></i></blockquote>

<i><b>©𝐓𝐞𝐚𝐦 𝐔𝐫𝐯𝐚𝐬𝐡𝐢 𝐓𝐡𝐞𝐚𝐭𝐞𝐫𝐬™️</i></b>"""
