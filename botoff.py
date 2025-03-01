import subprocess
import threading
import time
import telebot
from mongoDB import * 

from dotenv import load_dotenv


bot_token = '7672617754:AAFWfO4QEi-24adDtdW4JwiRTMVukrYDUUU'
bot = telebot.TeleBot(bot_token)

main_script_process = None

@bot.message_handler(regexp=r'^[./!?¿-]?ready')
def run_main_script(message):
    permisos = collection.find_one({"_id": message.from_user.id})

    if permisos and permisos.get("role") == "Owner":
        global main_script_process

        if main_script_process is None:
            msg = bot.send_message(message.chat.id, "<b><i>Starting Bot By Sylphiette</i></b>", parse_mode="HTML")
            time.sleep(10)

            main_script_process = subprocess.Popen(["python", "eli.py"])

            chk = bot.edit_message_text("<b><i>It Is Starting</i></b>", message.chat.id, msg.message_id, parse_mode="HTML")
            time.sleep(60)

            bot.edit_message_text("<b><i>The Bot Is Already Running</i></b>", message.chat.id, chk.message_id, parse_mode="HTML")
        else:
            bot.reply_to(message, "<b><i>The Process Is Already Running</i></b>", parse_mode="HTML")
    else:
        return

@bot.message_handler(regexp=r'^[./!?¿-]?stop')
def pause_main_script(message):
    permisos = collection.find_one({"_id": message.from_user.id})


    if permisos and permisos.get("role") == "Owner":
        global main_script_process

        if main_script_process:
            msg = bot.send_message(message.chat.id, "<b><i>Pausing Bot By Sylphiette</i></b>", parse_mode="HTML")
            time.sleep(10)
            bot.edit_message_text("<b><i>Bot By Sylphiette Paused</i></b>", message.chat.id, msg.message_id, parse_mode="HTML")
            main_script_process.terminate()
            main_script_process = None
        else:
            bot.reply_to(message, "<b><i>Bot Is Not Running</i></b>", parse_mode="HTML")
    else:
        return

@bot.message_handler(regexp=r'^[./!?¿-]?reboot')
def restart_main_script(message):

    permisos = collection.find_one({"_id": message.from_user.id})

    if permisos and permisos.get("role") == "Owner":
        msg = bot.send_message(message.chat.id, "<b><i>Restarting Bot...</i></b>", parse_mode="HTML")
        time.sleep(3)

        global main_script_process
        if main_script_process:
            main_script_process.terminate()
            main_script_process = None
        main_script_process = subprocess.Popen(["python", "eli.py"])
        time.sleep(15)

        bot.edit_message_text("<b><i>Bot successfully restarted.</i></b>", message.chat.id, msg.message_id, parse_mode="HTML")
    else:
        return

if __name__ == "__main__":
    print("BOT EJECUTÁNDOSE")
    bot.polling(none_stop=True)
