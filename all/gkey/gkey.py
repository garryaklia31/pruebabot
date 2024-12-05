from all.configs._def_main_ import*

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
