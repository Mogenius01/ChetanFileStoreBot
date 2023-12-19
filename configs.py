# (c) @Rudraa332

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "28746984"))
	API_HASH = os.environ.get("API_HASH", "354faa96503d19125d47536229cf2ec2")
	BOT_TOKEN = os.environ.get("BOT_TOKEN","6320112707:AAEdEsSrpR1x-vsxxaKJCFHjrhSDPIOcUog")
	BOT_USERNAME = os.environ.get("BOT_USERNAME",'Echo_echo_re_bot')
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL",'-1001669395498'))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1450978328"))
	DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Rudraa:Rudraa2213@cluster0.tj0kh3c.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001824876586")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
I Am **Chetan's** file Store bot! \n You Can Send Me Any Media file, And I Will give you a Permanent Sharable Link\n Also Please join my channel And Support Group!


🤖 **My Name:** [File Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://Heroku.app/)

🧑🏻‍💻 **Developer:** @Fundamental00

👥 **Support Group:** [RRR](https://t.me/joint0t)

📢 **Updates Channel:** [Discovery Projects](https://t.me/bot_channelv1)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Rudraa332

Developer is Excellent. And Learning from Official docs. Please do not Donate the Developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database And You will Be **Banned**. So better don't Store Those Kind of Things.

[Rudraa](https://www.telegram.me/Fundamental00) (Contect Me)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Only Admin Can Use This Bot\nIf You Want this Bot Contact to the Admin Or Use This [Content Store Bot](https://t.me/content_storebot) for store any type of data ! Please Check **About Bot** Button.
"""
