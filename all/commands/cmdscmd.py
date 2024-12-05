from all.configs._def_main_ import *


@Techie(['cm', 'cmd', 'cmds'])
async def cmds(_, message):
    ID = message.from_user.id
    CHATID = message.chat.id
    FIRST = message.from_user.first_name
    usuario = collection.find_one({"_id": message.from_user.id})
    

    if usuario is None:
        caption = await registrar_usuario(message)
        return await message.reply(text=caption, reply_markup=dbre, quote=True)
    else:
        id_usuario = usuario["id"]
        caption = gtx.format(id_usuario=id_usuario,
                            ID=ID, FIRST=FIRST, CHATID=CHATID)
        await Client.send_photo(_, chat_id=message.chat.id, caption=caption,
                                  reply_to_message_id=message.id, reply_markup=dbre, photo=PHOTO)
