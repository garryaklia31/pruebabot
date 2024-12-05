from all.configs._def_main_ import *


@Techie('all')
async def allinfocmd(_, message):
    permisos = collection.find_one({"_id": message.from_user.id})
    if permisos['role'] == "Owner":
        total_users = collection.count_documents({})
        premium_users = collection.count_documents({"plan": "Premium"})
        seller_users = collection.count_documents({"role": "Seller"})
        ban_users = collection.count_documents({"status": "Baneado"})
        authorized_groups = collection_tres.count_documents({})
        banned_bins = len(load_banned_bins())
        _text = f"""<b><code>Db Info</code>
━━━━━━━━━━━━━━━━
<i>Registered Users</i> ➵ <code>{total_users}</code>
<i>Premium Users</i> ➵ <code>{premium_users}</code>
<i>Banned Users</i> ➵ <code>{ban_users}</code>
<i>Authorized Groups</i> ➵ <code>{authorized_groups}</code>
<i>Banned Bins</i> ➵ <code>{banned_bins}</code>
<i>Sellers</i> ➵ <code>{seller_users}</code></b>"""
        await message.reply(_text, quote=True)
    else:
        return

@Techie('resetall')
async def resetallcmd(_, message):
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos is None:
        return 

    if buscar_permisos["role"] == "Owner":
        collection.update_many({"alerts": {"$exists": True}}, {
                               "$set": {"alerts": 0}})
        collection.update_many({"tareas_en_proceso": {"$exists": True}}, {
                               "$set": {"tareas_en_proceso": 0}})
        _text = f"""
<b><i>¡Se han restablecido los valores de alertas y tareas en proceso!</i></b>
        """

        await message.reply(_text, quote=True)
    else:
        return