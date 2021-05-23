import logging
import telegram
from telegram import Bot
from telegram.ext import Updater, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

API_TOKEN = None # Bot API TOKEN

ibot=Bot(token=API_TOKEN)

# ############################### Main ####################################

def check_isMember(update, context):
    group_id = None #Your_Group_ID
    usr_id = None #Members_TG_ID

    try:
        res=ibot.getChatMember(chat_id=group_id, user_id=usr_id)
        print(res)

    except telegram.error.BadRequest:
        print("The User isn't a member of the group.")

def main():

    updater = Updater(bot=ibot, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("check", check_isMember))

    updater.start_polling()
    logger.info("checking")
    updater.idle()


if __name__ == "__main__":
    main()
