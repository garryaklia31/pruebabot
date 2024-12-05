from all.configs._def_main_ import *

@Techie(['claim', 'redeem'])
async def claim(_, message):
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    usuario = collection.find_one({"_id": message.from_user.id})
    if usuario is None:
        caption = await registrar_usuario(message)
        return await message.reply(text=caption, reply_markup=dbre, quote=True)
    else:
        pass

    ccs = message.text[len('/claim'):]
    ccs = message.text[len('/redeem'):]
    espacios = ccs.split()

    if len(espacios) == 0:
        return await message.reply("""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$claim</code>
<i>Use</i> ⇨ <code>$claim Key-XXXX-MisterChk-XXXX-XXXX</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)

    key = espacios[0]

    if usuario['plan'] == "Premium" or usuario['role'] == "Seller":
        return await message.reply(text="""<b>You already have a premium membership❗️</b>""", quote=True)

    if usuario['status'] == "Banned":
        return await message.reply(text="""<b>🚫Usuario Baneado✋❌</b>""", quote=True)

    datos = cargar_datos_json()

    if key in [dato['key'] for dato in datos]:
        return await message.reply(text="""<b>This Key has already been claimed, please do not retry or you will be banned❗️</b>""", quote=True)

    encontrar_key = collection_dos.find_one({"key": key})
    if encontrar_key is None:
        collection.update_one({"_id": message.from_user.id}, {
                              "$inc": {"alerts": 1}})
        alerts = collection.find_one(
            {"_id": message.from_user.id}).get('alerts', 0)
        if alerts >= 5:
            collection.update_one({"_id": message.from_user.id}, {"$set": {
                                  "status": 'Banned'}})
            return await message.reply(text="""<b>You have been banned for trying to claim a non-existent key❗️</b>""", quote=True)
        else:
            return await message.reply(text="""<b>You are trying to redeem a non-existent key, if you keep trying you will be banned❗️</b>""", quote=True)

    dias = encontrar_key['days']
    x = datetime.now() + timedelta(days=dias)

    collection.update_one({"_id": message.from_user.id}, {"$set": {"key": x}})
    collection.update_one({"_id": message.from_user.id},
                          {"$set": {"plan": 'Premium', "apodo": 'Premium'}})
    collection_dos.delete_one({"key": key})

    key_info = {'key': key}
    save_key_info(key_info)

    caption = claimtxt.format(KEY=key, ID=ID, FIRST=FIRST,
                              plan=usuario['plan'], apodo=usuario["apodo"], dias=dias, final=x.strftime('%Y-%m-%d %H:%M:%S'))

    return await message.reply(text=caption, quote=True)