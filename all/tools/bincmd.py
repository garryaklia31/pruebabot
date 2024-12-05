from all.configs._def_main_ import *


@Techie('bin')
async def bin(_, message):
    tiempo = time.time()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    usuario = collection.find_one({"_id": message.from_user.id})

    if usuario is None:
        caption = await registrar_usuario(message)
        return await message.reply(text=caption, reply_markup=dbre, quote=True)
    else:
        pass

    if usuario['status'] == "Banned":
        return

    if message.reply_to_message:
        search_bin = re.findall(r'[0-9]+', str(message.reply_to_message.text))
    else:
        search_bin = re.findall(r'[0-9]+', str(message.text))

    grupo = collection_tres.find_one({"group": str(message.chat.id)})   

    if usuario['key'] != 'None' or grupo != None:
        if usuario['key'] != 'None':
            if usuario["key"] < datetime.now():
                collection.update_one({"_id": message.from_user.id}, {
                                      "$set": {"key": 'None'}})
                collection.update_one({"_id": message.from_user.id}, {
                                      "$set": {"plan": 'Free User'}})
                return await message.reply(text=expiracion, quote=True)
        elif grupo["key"] < datetime.now():
            collection_tres.delete_one({"group": str(message.chat.id)})

    else:
        return await message.reply(text=notpermiso, quote=True)

    try:
        BIN = search_bin[0][0:6]
    except IndexError:
        return await message.reply(text=malbin, quote=True)
    x = get_bin_info(BIN)

    if not x:
        return await message.reply(text=malbin, quote=True)

    caption = binpx.format(name=x.get("bank_name"), BIN=BIN, coun=x.get("country"), flag=x.get("flag"), info1=x.get(
        "vendor"), info2=x.get("type"), info3=x.get("level"), tiem=get_time_taken(tiempo), ID=ID, FIRST=FIRST, plan=usuario["apodo"])

    return await message.reply(text=caption, quote=True)
