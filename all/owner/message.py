from all.configs._def_main_ import *


@Techie('msg')
async def msg_command(client, message):
    permisos = collection.find_one({"_id": message.from_user.id})

    if permisos["role"] == "Owner":
        pass
    else:
        return
    
    if len(message.command) > 1:
        mensaje = " ".join(message.command[1:])

        usuarios = collection.find({})
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Owner", url="tg://resolve?domain=ShylphietteGreyrat"),
                InlineKeyboardButton("Canal", url="https://t.me/+1Pa01JvX_740OTIx"),
               
            ]
        ]
    )
        
        
        text = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Message to All」━━━━━━━━
<i>Message</i> ⇨ <code>{mensaje}</code>
━━━━━━━━「ELAINA」━━━━━━━━
</b>"""
        
        for usuario in usuarios:
            user_id = usuario["_id"]
            try:
                await message._client.send_message(chat_id=user_id, text=text, reply_markup=keyboard)
            except Exception as e:
                print(f"No se pudo enviar el mensaje a {user_id}: {str(e)}")

        await message.reply(text="<b><i>The message has been sent to all registered users.</i></b>", quote=True)
    else:
        await message.reply(text="<b><i>Incorrect usage of the command. Please provide a valid message.</i></b>", quote=True)