from all.configs._def_main_ import *


@Techie(['my', 'info', 'me'])
async def perfilcmd(_, message):
    awa = collection.find_one({"_id": message.from_user.id})

    try:
        if message.reply_to_message.from_user.id:
            usuario = collection.find_one(
                {"_id": message.reply_to_message.from_user.id})
    except:
        usuario = collection.find_one({"_id": message.from_user.id})
    ID = message.from_user.id
    FIRST = message.from_user.first_name

    if usuario is None:
        caption = await registrar_usuario(message)
        return await message.reply(text=caption, reply_markup=dbre, quote=True)
    else:
        user_name = usuario["username"]
        id_usuario = usuario["id"]
        plan = usuario["plan"]
        key_ = usuario["key"]
        if key_ != 'None' and key_ < datetime.now():
            collection.update_one({"_id": id_usuario}, {
                                  "$set": {"key": 'None'}})
            collection.update_one({"_id": id_usuario}, {
                                  "$set": {"antispam": 60}})
            collection.update_one({"_id": id_usuario}, {
                "$set": {"plan": 'Free User'}})
            return await message.reply(text='<b><i>Your key has expired. contact @ShylphietteGreyrat to purchase a new one.</i></b>', quote=True)
        if key_ != 'None':
            key_ = key_.strftime('%Y-%m-%d')
        else:
            key_ = 'No Key Actived'
        creditos = usuario["credits"]
        gatesusage = usuario['gates_usage']
        apodo = usuario["apodo"]

        caption = nperfil.format(
            id_usuario=id_usuario, apodo=apodo, creditos=creditos, plan=plan, key_=key_, ID=ID, FIRST=FIRST, gatesusage=gatesusage)
    await Client.send_message(_, chat_id=message.chat.id, text=caption,
                              reply_to_message_id=message.id,)
