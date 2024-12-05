from all.configs._def_main_ import *

@retry('gkey')
async def gkey(_, message):
    ID = message.from_user.id
    FIRST = message.from_user.first_name

    # Verificar permisos
    permisos = collection.find_one({"_id": ID})
    if not permisos or permisos.get("role") not in ["Owner", "Seller"]:
        return await message.reply("No tienes permisos para usar este comando.")

    ccs = message.text[len('/gkey'):]
    espacios = ccs.split()
    if len(espacios) == 0:
        return await message.reply("""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$gkey</code>
<i>Use</i> ⇨ <code>$gkey days</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)

    days = espacios[0]

    key = f'Key-{str(random.randint(1000, 9999))}-MisterChk-{str(random.randint(1000, 9999))}-{str(random.randint(1000, 9999))}'

    my_dict = {
        "key": key,
        "days": int(days)
    }
    collection_dos.insert_one(my_dict)

    textokeys = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━「Key Created」━━━━━
<i>Key</i> ⇨ <code>{key}</code>
<i>Days</i> ⇨ <code>{days}</code>
<i>Type</i> ⇨ <i><u>Premium</u></i>
<i>Bot</i> ⇨ @ChkElainaBot
━━━━━━━━「ELAINA」━━━━━━━━
<i>Create By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
    await message.reply(textokeys, quote=True)
    textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Key Created」━━━━━━━━
<i>Action</i> ⇨ <code>Key Generation</code>
<i>Key</i> ⇨ <code>{key}</code>
<i>Days</i> ⇨ <code>{days}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>{permisos['role']}</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
  #  await message._client.send_message(LOG_CHAT_ID, textito)


@retry('delkeys')
async def delallkeys(_, message):
    ID = message.from_user.id
    FIRST = message.from_user.first_name

    permisos = collection.find_one({"_id": message.from_user.id})

    if permisos["role"] == "Owner":
        pass
    else:
        return

    result = collection_dos.delete_many({})
    if result.deleted_count == 0:
        return await message.reply("""<b><code>Admin Error's!</code>
━━━━━━━━━━━━━━━━
<code>No keys found in the database❗️</code></b>""", quote=True)

    texto = f"""<b><code>Deleted All Key Successfully! </code>❇️
━━━━━━━━━━━━━━━━
<i>Keys Deleted</i> <code>{result.deleted_count}</code>
━━━━━━━━━━━━━━━━
<i>Deleted By</i> <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
    await message.reply(texto, quote=True)
    textito = f"""<b><code>Administration! </code>👁
━━━━━━━━━━━━━━━━
<i>Action</i> <code>Deleted All Key</code>
<i>Keys</i> <code>{result.deleted_count}</code>
━━━━━━━━━━━━━━━━
<i>Seller</i> <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
  #  await message._client.send_message(LOG_CHAT_ID, textito)



