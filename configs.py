# (c) @MRK_YT

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("MT_BOT_TOKEN")
	BOT_USERNAME = os.environ.get("MT_BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("MT_BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("MT_UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("MT_LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("MO_TECH_YT", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍ **Developer:** @AbirHasan2005

👨‍💻 **Editing:** @beereshbanakards

📺 **Support:** [Join channel](https://t.me/BAGURUJOINAGUUKANNADAMOVIES_17)

🗣️ **Any Doubt:** @BAGURUJOINAGUUKANNADAMOVIES_17

📢 **Updates Channel:** [Discovery Projects](https://t.me/BAGURUJOINAGUUKANNADAMOVIES_17)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍ **Developer:** @AbirHasan2005

💻 **Developer Details:** [Clcik Here](https://github.com/kannadamoviesrequestbot/blob/main/README.md)

👨‍💻 **Editing:** @beereshbanakards

🗣️ **Any Doubt:** @BAGURUJOINAGUUKANNADAMOVIES_17

📺 **Support :** [Join channel](https://t.me/BAGURUJOINAGUUKANNADAMOVIES_17)

📢 **Updates Channel:** [Discovery Projects](https://t.me/BAGURUJOINAGUUKANNADAMOVIES_17)

Donate Now (coming soon)
"""
	HOME_TEXT = """
**👋Hi**, [{}](tg://user?id={})\n\n**This is Permanent** ** FileStoreBot**.

**Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check About Bot Button**.
"""

