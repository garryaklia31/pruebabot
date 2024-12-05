from all.configs._def_main_ import *


@retry('staff')
async def admin(_, message):
    permisos = collection.find_one({"_id": message.from_user.id})
    usernameowo = message.from_user.username
    ID = message.from_user.id
    FIRST = message.from_user.first_name

    if permisos["role"] == "Owner": #or permisos["role"] == "Seller":
        pass
    else:
        return

    command_args = message.text.split()[1:]

    if len(command_args) < 1:
        atx = admintxt.format(usernameowo=usernameowo)
        await Client.send_photo(_, chat_id=message.chat.id, caption=atx,
                                  reply_to_message_id=message.id, reply_markup=botadmin, photo=PHOTO)
        return

    subcommand = command_args[0]

    if subcommand == 'addcredit':
        # /seller addcredit userid amount
        if len(command_args) < 3:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>addcredit</code>
<i>Use</i> ⇨ <code>$addcredit userid amount</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        amount = int(command_args[2])

        user_to_add_credits = collection.find_one({"_id": userid})

        if user_to_add_credits:
            current_credits = user_to_add_credits.get("credits", 0)
            updated_credits = current_credits + amount

            collection.update_one(
                {"_id": userid},
                {"$set": {"credits": updated_credits}}
            )
            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━「Added Credits」━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Added Credits</i> ⇨ <code>{amount}</code>
<i>Current credits</i> ⇨ <code>{updated_credits}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Added By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━「Added Credits」━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Added Credits</i> ⇨ <code>{amount}</code>
<i>Current credits</i> ⇨ <code>{updated_credits}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Added By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)
    
    
    elif subcommand == 'edit':
        # /seller edit userid amount
        if len(command_args) < 3:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller edit</code>
<i>Use</i> ⇨ <code>$seller edit userid amount</code></b>
━━━━━━━━「ELAINA」━━━━━━━━""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        amount = int(command_args[2])

        user_to_edit_credits = collection.find_one({"_id": userid})

        if user_to_edit_credits:
            current_credits = user_to_edit_credits.get("credits", 0)

            if current_credits < amount:
                await message.reply(f"""<b><i>El usuario con ID <code>{userid}</code>, No tiene suficientes créditos. Créditos actuales: <code>{current_credits}</code></i></b>""", quote=True)
            else:
                updated_credits = current_credits - amount

                collection.update_one(
                    {"_id": userid},
                    {"$set": {"credits": updated_credits}}
                )
                await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Subtracted Credits」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Current credits</i> ⇨ <code>{updated_credits}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Subtracted By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
                textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Subtracted Credits」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Current credits</i> ⇨ <code>{updated_credits}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Subtracted By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
                await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'nick':
        # /seller nick userid new_nick
        if len(command_args) < 3:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller nick</code>
<i>Use</i> ⇨ <code>$seller nick userid new_nick</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        new_nick = command_args[2]

        user_to_modify = collection.find_one({"_id": userid})

        if user_to_modify:
            collection.update_one(
                {"_id": userid},
                {"$set": {"apodo": new_nick}}
            )
            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━「Modified Plan」━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>New Plan</i> ⇨ <code>{new_nick}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Modified By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━「Modified Plan」━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>New Plan</i> ⇨ <code>{new_nick}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Modified By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'ban':
        # /seller ban userid
        if len(command_args) < 2:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller ban</code>
<i>Use</i> ⇨ <code>$seller ban userid</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        user_to_ban = collection.find_one({"_id": userid})

        if user_to_ban:
            collection.update_one(
                {"_id": userid},
                {"$set": {"status": "Banned"}}
            )
            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Ban User」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Time</i> ⇨ <i><u>Permanently</u></i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Banned By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Ban User」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Time</i> ⇨ <i><u>Permanently</u></i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Banned By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'unban':
        # /seller unban userid
        if len(command_args) < 2:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller unban</code>
<i>Use</i> ⇨ <code>$seller unban userid</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        user_to_unban = collection.find_one({"_id": userid})

        if user_to_unban:
            collection.update_one(
                {"_id": userid},
                {"$set": {"status": "Libre"}}
            )
            f"<b>El usuario con ID <code>{userid}</code>, fue desbaneado del bot correctamente.</b>"
            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Ban Removed」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Ban Removed」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'premium':
        # /seller premium userid
        if len(command_args) < 3:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller premium</code>
<i>Use</i> ⇨ <code>$seller premium userid</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        days = command_args[2]
        x = datetime.now() + timedelta(days=int(days))

        user_to_premium = collection.find_one({"_id": userid})

        if user_to_premium:
            collection.update_one(
                {"_id": userid},
                {"$set": {"plan": "Premium", "key": x, "apodo": "Premium"}},
                upsert=True
            )
        
        usuario = collection.find_one(
                {"_id": userid})
        
        if usuario is not None:
            creditos = usuario["credits"]

            
            try: 
                premium_message = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Your Account Has Been Upgraded to Premium</i>
━━━━━━━━「INFO」━━━━━━━━━━
<i>Plan</i> <code>Premium</code>
<i>Days</i> <code>{days}</code>
<i>Credits</i> <code>{creditos}</code>
<i>Userid</i> <code>{userid}</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>"""
                await message._client.send_message(userid, premium_message, )
            except Exception as e:
                print(f"No se pudo enviar el mensaje a {userid}: {str(e)}")
            
            
            
            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Add Premium」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Plan</i> ⇨ <i><u>Premium</u></i>
<i>Days</i> ⇨ <code>{days}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Add Premium」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Plan</i> ⇨ <i><u>Premium</u></i>
<i>Days</i> ⇨ <code>{days}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)
    
    elif subcommand == 'freeuserprem':
        # /seller Free Userprem days
        if len(command_args) < 2:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller freeuserprem</code>
<i>Use</i> ⇨ <code>$seller freeuserprem days</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        days = command_args[1]
        x = datetime.now() + timedelta(days=int(days))

        # Filtrar solo los usuarios con plan "Free User"
        all_users = collection.find({"plan": "Free User"})
        
        users_not_updated = []

        for user in all_users:
            userid = user["_id"]
            collection.update_one(
                {"_id": userid},
                {"$set": {"plan": "Premium", "key": x, "apodo": "Premium"}},
                upsert=True
            )

            creditos = user["credits"]

            premium_message = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Your Account Has Been Upgraded to Premium</i>
━━━━━━━━「INFO」━━━━━━━━━━
<i>Plan</i> <code>Premium</code>
<i>Days</i> <code>{days}</code>
<i>Credits</i> <code>{creditos}</code>
<i>Userid</i> <code>{userid}</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>"""

            try:
                await message._client.send_message(userid, premium_message)
            except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
                # Usuario no recibió el mensaje
                users_not_updated.append(userid)
                print(users_not_updated)

        await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Premium to All」━━━━━━━━
<i>Days</i> ⇨ <code>{days}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
    
        textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Premium to All」━━━━━━━━
<i>Days</i> ⇨ <code>{days}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
    
        await message._client.send_message(LOG_CHAT_ID, textito)
    
    
    elif subcommand == 'id':
        #/seller id group
        if len(command_args) < 2:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller id</code>
<i>Use</i> ⇨ <code>$seller id group</code>
━━━━━━━━「ELAINA」━━━━━━━━
</b>""", quote=True)
            return
        
        await message.reply(text = f"""
<b><i>CHATID <code>{message.chat.id}</code></i></b>
""")


    elif subcommand == 'addgp':
        # /seller addgp days|reason
        print("Command args:", command_args)  
        if len(command_args) < 2:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller addgp</code>
<i>Use</i> ⇨ <code>$seller addgp days|reason</code>
━━━━━━━━「ELAINA」━━━━━━━━
</b>""", quote=True)
            return

        duration_reason = " ".join(command_args[1:])
        duration_reason = duration_reason.split("|")
    
        days = duration_reason[0]
        reason = duration_reason[1] if len(duration_reason) > 1 else "Not Reason"

        
        print(f'Days: {days}')

        if not days.isdigit():
            return await message.reply("""<b>Invalid Number Of Days❗</b>""", quote=True)

        x = datetime.now() + timedelta(days=int(days))

        encontrar_key = collection_tres.find_one(
            {"group": str(message.chat.id)})

        if encontrar_key is None:
            my_dict = {
                "group": str(message.chat.id),
                "days": int(days),
                "key": x,
                "promote": str(message.from_user.username),
                "rango": permisos["role"],
                "type": "Premium Group",
                "reason": reason
            }
            collection_tres.insert_one(my_dict)

            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Add Group」━━━━━━━━
<i>Group ID</i> ⇨ <code>{message.chat.id}</code>
<i>Plan</i> ⇨ <i><u>Premium Group</u></i>
<i>Days</i> ⇨ <code>{days}</code>
<i>Reason</i> ⇨ <i>{reason}</i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Add Group」━━━━━━━━
<i>Group ID</i> ⇨ <code>{message.chat.id}</code>
<i>Plan</i> ⇨ <i>Premium Group</i>
<i>Days</i> ⇨ <code>{days}</code>
<i>Reason</i> ⇨ <i>{reason}</i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply("""<b>This group already has a premium membership❗</b>""", quote=True)



    elif subcommand == 'removeg':
        # /seller removeg idchat
        if len(command_args) < 2:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller removeg</code>
<i>Use</i> ⇨ <code>$seller removeg idchat</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        group_id = command_args[1]

        group = collection_tres.find_one({"group": group_id})

        if group is None:
            return await message.reply(text=f"""<b><code>The group with ID <code>{group_id}</code> is not registered in my database</code>❗</b>""", quote=True)

        collection_tres.delete_one({"group": group_id})

        await message.reply(text=f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━「Group Removed」━━━━━
<i>Group ID</i> ⇨ <code>{message.chat.id}</code>
<i>Plan</i> ⇨ <i><u>Free Group</u></i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
        textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━「Group Removed」━━━━━
<i>Group ID</i> ⇨ <code>{message.chat.id}</code>
<i>Plan</i> ⇨ <i><u>Free Group</u></i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
        await message._client.send_message(LOG_CHAT_ID, textito)

    elif subcommand == 'removep':
        if len(command_args) < 2:
            await message.reply("""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller removep</code>
<i>Use</i> ⇨ <code>$seller removep userid</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        user_to_promote = collection.find_one({"_id": userid})

        if user_to_promote:
            collection.update_one(
                {"_id": userid},
                {"$set": {"plan": "Free User", "key": 'None', "apodo": "Free User"}}
            )

            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━「Premium Removed」━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Plan</i> ⇨ <i><u>Free User</u></i>
<i>Key</i> ⇨ <code>None</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━「Premium Removed」━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Plan</i> ⇨ <i><u>Free User</u></i>
<i>Key</i> ⇨ <code>None</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'kit':
        # /seller kit userid
        if permisos["role"] == "Owner":
            pass
        else:
            return
        if len(command_args) < 2:
            await message.reply("""━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller kit</code>
<i>Use</i> ⇨ <code>$seller kit userid</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        user_to_promote = collection.find_one({"_id": userid})

        if user_to_promote:
            collection.update_one(
                {"_id": userid},
                {"$set": {"role": "User", "plan": "Free User", "key": 'None', "credits": 0, "apodo": "Free User"}}
            )

            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Data Removed」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Plan</i> ⇨ <i><u>Free User</u></i>
<i>Key</i> ⇨ <code>None</code>
<i>credits</i> ⇨ <code>0</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Data Removed」━━━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Plan</i> ⇨ <i><u>Free User</u></i>
<i>Key</i> ⇨ <code>None</code>
<i>credits</i> ⇨ <code>0</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'promote':
        # /seller promote userid
        if permisos["role"] == "Owner":
            pass
        else:
            return
        if len(command_args) < 2:
            await message.reply("""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller seller</code>
<i>Use</i> ⇨ <code>$seller seller userid</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        user_to_promote = collection.find_one({"_id": userid})
        
        
        
        days = 1000000
        x = datetime.now() + timedelta(days=int(days))

        if user_to_promote:
            collection.update_one(
                {"_id": userid},
                {"$set": {"role": "Seller", "plan": "Seller", "credits": 100000000000000, "key": x, "apodo": "Seller"}}
            )

            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━「Seller Promote」━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Role</i> ⇨ <i><u>Seller</u></i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━「Seller Promote」━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Role</i> ⇨ <i><u>Seller</u></i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'removes':
        # /seller removes userid
        if permisos["role"] == "Owner":
            pass
        else:
            return
        if len(command_args) < 2:
            await message.reply("""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller removes</code>
<i>Use</i> ⇨ <code>$seller removes userid</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        user_to_promote = collection.find_one({"_id": userid})

        if user_to_promote:
            collection.update_one(
                {"_id": userid},
                {"$set": {"role": "User", "plan": "Free User", "key": 'None', "credits": 0, "apodo": "Free User"}}
            )

            await message.reply(f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━「Seller Removed」━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Plan</i> ⇨ <i><u>Free User</u></i>
<i>Key</i> ⇨ <code>None</code>
<i>credits</i> ⇨ <code>0</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>""", quote=True)
            textito = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━「Seller Removed」━━━━━━
<i>User ID</i> ⇨ <code>{userid}</code>
<i>Plan</i> ⇨ <i><u>Free User</u></i>
<i>Key</i> ⇨ <code>None</code>
<i>credits</i> ⇨ <code>0</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Removed By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""
            await message._client.send_message(LOG_CHAT_ID, textito)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'user':
        # /seller user userid
        if len(command_args) < 2:
            await message.reply("""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller user</code>
<i>Use</i> ⇨ <code>$seller user userid</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        userid = command_args[1]

        try:
            userid = int(userid)
        except ValueError:
            await message.reply(text=validid, quote=True)
            return

        user_info = collection.find_one({"_id": userid})

        if user_info:
            username = user_info.get("username")
            id_usuario = user_info.get("id")
            credits = user_info.get("credits")
            plan = user_info.get("plan")
            key_ = user_info.get("key")
            if key_ != 'None':
                key_ = key_.strftime('%Y-%m-%d %H:%M:%S')
            else:
                key_ = 'No Key Actived'

            response = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「User Search」━━━━━━━━
<i>Plan</i> ⇨ <code>{plan}</code> 
<i>Date</i> ⇨ <code>{key_}</code>
<i>User Id</i> ⇨ <code>{id_usuario}</code>
<i>Credits</i> ⇨ <code>{credits}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Requested By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>"""

            await message.reply(response, quote=True)
        else:
            await message.reply(text=notexistid, quote=True)

    elif subcommand == 'group':
        # /seller group info
        if len(command_args) < 2:
            await message.reply("""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Command</i> ⇨ <code>$seller group</code>
<i>Use</i> ⇨ <code>$seller group info</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>""", quote=True)
            return

        encontrar_grupo = collection_tres.find_one(
            {"group": str(message.chat.id)})

        if encontrar_grupo is None:
            return await message.reply(text=f"""<b>This group does not have a membership, contact seller to buy a premium membership❗</b>""", reply_markup=buypremium, quote=True)

        prom = encontrar_grupo["promote"]
        dios = encontrar_grupo["rango"]
        lol = encontrar_grupo["days"]
        owo = encontrar_grupo["type"]

        await message.reply(text=f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Group」━━━━━━━━
<i>Chat ID</i> ⇨ <code>{message.chat.id}</code>
<i>Plan</i> ⇨ <i><u>{owo}</u></i>
<i>Days</i> ⇨ <code>{lol}</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Promote By</i> ⇨ @{prom}</i> [<code>{dios}</code>]</b>""", quote=True)
       
    else:
        await message.reply("""<b>Ingresa un subcomando existente, para saber cuales son ejecuta: /seller</b>""", quote=True)







