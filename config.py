#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6323050956:AAFqpxu7VpiYlXP-x2gdYVJeLL8vDNVmpFs")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22234019"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9afb8b419e497e19477e2ad542f79592")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001975834800"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1731373649"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://raghu1234:raghu1234@raghu123.vcbeecq.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "raghu123")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001979976612"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\n <b>○ Direct Mega Links : <a href='https://t.me/+QPyHEA1xCVtlNTcx'>CLICK HERE</a>\n○ Daily Special Mega Links: <a href='https://t.me/+SNSFScToH4piNTk1'>CLICK HERE</a>\n○ TeraBox unlimited Links : <a href='https://t.me/+S7SN-3vnD1s4YjEx'>CLICK HERE</a>\n○ Special Leak Updates : <a href='https://t.me/+wxDSKyTwAMowZGFl'>CLICK HERE</a>\n○ Main Channel : <a href='https://t.me/+kxI_UMH4ZxljODg1'>CLICK HERE </a>\n</b> Join All And Enjoy")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "1St Join Channel నొక్కి Channel join అవ్వు... Next Try again నొక్కు Videos Ostai🔥❤️")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "Direct Mega Links😊😍 - https://t.me/+G_X_urFv6ZpmNDkx - Daily Special Mega Links🥰 - https://t.me/+SNSFScToH4piNTk1 , TeraBox 🎁 unlimited Links - https://t.me/+S7SN-3vnD1s4YjEx")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = f"<b>○ Direct Mega Links : <a href='https://t.me/+QPyHEA1xCVtlNTcx'>CLICK HERE</a>\n○ Daily Special Mega Links: <a href='https://t.me/+SNSFScToH4piNTk1'>CLICK HERE</a>\n○ TeraBox unlimited Links : <a href='https://t.me/+S7SN-3vnD1s4YjEx'>CLICK HERE</a>\n○ Special Leak Updates : <a href='https://t.me/+wxDSKyTwAMowZGFl'>CLICK HERE</a>\n○ Main Channel : <a href='https://t.me/+kxI_UMH4ZxljODg1'>CLICK HERE</a>\n○ Join Our All Stuff Channels in Single Click : https://t.me/addlist/RPm4cp5PE_Q5MzM1 </b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1731373649)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
