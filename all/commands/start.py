from all.configs._def_main_ import *


@Techie('start')
async def start(_, message):
    usuario = collection.find_one({"_id": message.from_user.id})
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    if usuario is None:
        caption = await registrar_usuario(message)
        return await message.reply(text=caption, reply_markup=dbre, quote=True)
    else:
        id_usuario = usuario["id"]

        caption = startx.format(id_usuario=id_usuario,
                                ID=ID, FIRST=FIRST, plan=usuario['plan'], key_=usuario['key'], creditos=usuario['credits'],
                                gatesusage=usuario['gates_usage'], plan2=usuario['apodo'])

    await Client.send_photo(_, chat_id=message.chat.id, caption=caption,
                              reply_to_message_id=message.id, reply_markup=dbre, photo=PHOTO)
