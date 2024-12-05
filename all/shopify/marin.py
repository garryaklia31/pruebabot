from datetime import datetime
from all.configs._def_main_ import *
from all.functions.func_shopi.func_marin import auto_sho_async

nombregate = "Marin"
tipogate = "Sh + Payeezy"
cargogate = "($10.82)"
cmdgate = "mar"


@Techie(f'{cmdgate}')
async def yamadacmds(_, message):
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

    comandos_habilitados = cargar_datos()

    if usuario is not None and usuario.get("role") == "Owner":
        pass
    else:
        if not comandos_habilitados.get('mar', {}).get('enabled', False):
            reason = comandos_habilitados.get(
                'mar', {}).get('reason', "Unknown")
            date = comandos_habilitados.get('mar', {}).get('date', "Unknown")
            _textoff = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>This command is under maintenance. Please wait until it's fixed.</i> ❗ 
━━━━━━━━「ELAINA」━━━━━━━━</b>"""
            return await message.reply(text=_textoff, quote=True)

    if message.reply_to_message:
        input = getCards(str(message.reply_to_message.text))
    else:
        input = getCards(str(message.text))

    vnnotmsg = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Gateways</i> ➣ <i>{nombregate}|{tipogate}</i>
<i>Command</i> ➣ <code>${cmdgate}</code>
<i>Format</i> ➣ <code>${cmdgate} cc|month|year|cvv</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>"""

    if not input:
        return await message.reply(text=vnnotmsg, quote=True)

    if usuario['key'] != 'None':
        if usuario['key'] != 'None':
            if usuario["key"] < datetime.now():
                collection.update_one({"_id": message.from_user.id}, {
                                      "$set": {"key": 'None'}})
                collection.update_one({"_id": message.from_user.id}, {
                                      "$set": {"antispam": 60}})
                collection.update_one({"_id": message.from_user.id}, {
                                      "$set": {"plan": 'Free'}})
                return await message.reply(text=expiracion, quote=True)
        else:
            return await message.reply(text=notpermiso, reply_markup=buypremium, quote=True)

    else:
        return await message.reply(text=notpermiso, reply_markup=buypremium, quote=True)
    
    cc = input[0][0]
    mes = input[0][1]
    ano = input[0][2]
    cvv = input[0][3]

    if len(input[0]) > 4:
        estado = input[0][4]
        if estado == "expired":
            return await message.reply(text=expiredmsg, quote=True)
    else:
        estado = None

    vlunh = checkLuhn(cc)

    if vlunh == False:
        return await message.reply(text=noluhn, quote=True)
    
    credits = usuario['credits']
    
    
    if credits == 0 or credits < 2:
        notcredits = """<b>You don't have enough credit, contact @ShylphietteGreyrat to buy❗</b>"""
        return await message.reply(text=notcredits, quote=True)

    if usuario['plan'] == 'Premium':
        max_tareas = 2
    elif usuario['role'] == 'Seller':
        max_tareas = 4
    elif usuario['plan'] == 'Free':
        max_tareas = 1
    elif usuario['plan'] == 'Free User':
        max_tareas = 1
    elif usuario['role'] == 'Owner':
        max_tareas = float('inf')
    else:
        max_tareas = 1

    if max_tareas == 0:
        return

    tareas_en_proceso = usuario.get('tareas_en_proceso', 0)

    if tareas_en_proceso >= max_tareas:
        await Client.send_message(_, chat_id=message.chat.id, text=texto_spam, reply_to_message_id=message.id)
        return

    collection.update_one({"_id": message.from_user.id}, {
                          "$set": {"tareas_en_proceso": tareas_en_proceso + 1}})

    if cc[0] in bin_prohibido:
        collection.update_one({"_id": message.from_user.id}, {
            "$inc": {"tareas_en_proceso": -1}})
        return await message.reply(text=vnnotmsg, quote=True)

    if cc[0] in bin_prohibido:
        collection.update_one({"_id": message.from_user.id}, {
            "$inc": {"tareas_en_proceso": -1}})
        return await message.reply(text=vnnotmsg, quote=True)

    x = get_bin_info(cc[0:6])

    brand = x.get("vendor")
    level = x.get("level")
    typea = x.get("type")
    bank = x.get("bank_name")
    country_name = x.get("country")
    country_flag = x.get("flag")
    req = x

    baneado = f"""<b><i>Bin Banned</i></b>"""

    bin = cc[:6]

    banned_bins = load_banned_bins()

    if bin in banned_bins:
        collection.update_one({"_id": message.from_user.id}, {
            "$inc": {"tareas_en_proceso": -1}})

        if usuario['role'] == 'Owner':
            pass
        else:
            return await message.reply(text=baneado, quote=True)

    if req.get("level") is not None and "PREPAID" in req.get("level"):
        collection.update_one({"_id": message.from_user.id}, {
            "$inc": {"tareas_en_proceso": -1}})

        if usuario['role'] == 'Owner':
            pass
        else:
            return await message.reply(text=baneado, quote=True)

    texto_1 = carga1.format(cc=cc, mes=mes, ano=ano, cvv=cvv, brand=brand, level=level, typea=typea,
                            country_flag=country_flag, nombregate=nombregate, ID=ID, FIRST=FIRST, tipogate=tipogate, user_plan=usuario["apodo"])

    ñ = await message.reply(text=texto_1, quote=True)

    try:
        resultado = await auto_sho_async(cc, mes, ano, cvv)
        if resultado == 'Charged':
            mensaje = 'Charged $10.82 USD'
            status = 'Approved!'
            logo = '🟩'
            usuario['credits'] -= 2
            collection.update_one({"_id": usuario['_id']}, {"$set": {"credits": usuario['credits']}})
        elif resultado == 'Address not Verified - Approved':
            mensaje = 'Address not Verified - Approved'
            status = 'Approved!'
            logo = '🟩'
            usuario['credits'] -= 2
            collection.update_one({"_id": usuario['_id']}, {"$set": {"credits": usuario['credits']}})
        elif resultado == 'Address not Verified - Insufficient Funds':
            mensaje = 'Address not Verified - Insufficient Funds'
            status = 'Approved!'
            logo = '🟩'
            usuario['credits'] -= 2
            collection.update_one({"_id": usuario['_id']}, {"$set": {"credits": usuario['credits']}})
        elif resultado == 'Transaction Normal - Insufficient Funds':
            mensaje = 'Transaction Normal - Insufficient Funds'
            status = 'Approved!'
            logo = '🟩'
            usuario['credits'] -= 2
            collection.update_one({"_id": usuario['_id']}, {"$set": {"credits": usuario['credits']}})
        elif resultado == 'Data within the transaction is incorrect - Approved':
            mensaje = 'Data within the transaction is incorrect - Approved'
            status = 'Approved!'
            logo = '🟩'
            usuario['credits'] -= 2
            collection.update_one({"_id": usuario['_id']}, {"$set": {"credits": usuario['credits']}})
        elif resultado == 'Transaction Normal - Invalid CC Number':
            mensaje = 'Transaction Normal - Invalid CC Number'
            status = 'Declined!'
            logo = '🟥'
        elif resultado == 'Transaction Normal - Suspected Fraud':
            mensaje = 'Transaction Normal - Suspected Fraud'
            status = 'Declined!'
            logo = '🟥'
        elif resultado == 'Transaction Normal - Other Error':
            mensaje = 'Transaction Normal - Other Error'
            status = 'Declined!'
            logo = '🟥'
        elif resultado == 'Transaction Normal - Declined':
            mensaje = 'Transaction Normal - Declined'
            status = 'Declined!'
            logo = '🟥'
        elif resultado == 'Address not Verified - Account Closed':
            mensaje = 'Address not Verified - Account Closed'
            status = 'Declined!'
            logo = '🟥'
        elif resultado == 'Transaction Normal - Pickup':
            mensaje = 'Transaction Normal - Pickup'
            status = 'Declined!'
            logo = '🟥'
        elif resultado == 'There was a problem processing the payment. Try refreshing this page or check your internet connection.':
            mensaje = 'There was a problem processing the payment. Try refreshing this page or check your internet connection.'
            status = 'Declined!'
            logo = '🟥'
        else:
            mensaje = resultado
            status = 'Declined!'
            logo = '🟥'
    except:
        mensaje = 'Proxys'
        status = 'Try again!'
        logo = '🟥'

    texto_final = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Card</i> ➣ <code>{cc}|{mes}|{ano}|{cvv}</code>
<i>Status</i> ➣ <i>{status}</i> {logo}
<i>Result</i> ➣ <i>{mensaje}</i>
━━━━━━━━「RESULT」━━━━━━━━
<i>Bank</i> ➣ <code>{bank}</code>
<i>Country</i> ➣ <code>{country_name} | {country_flag}</code>
<i>Info</i> ➣ <code>{brand} {level} {typea}</code>
━━━━━━━━「INFO」━━━━━━━━━━
<i>Time</i> ➣ <code>{get_time_taken(tiempo)}</code>'s
<i>Gateways</i> ➣ <i>{nombregate}|{tipogate}</i>
<i>Checked by</i> ➣ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{usuario["apodo"]}</code>]
━━━━━━━━「ELAINA」━━━━━━━━</b>"""

    collection.update_one({"_id": message.from_user.id}, {
                          "$inc": {"tareas_en_proceso": -1}})
    collection.update_one({"_id": message.from_user.id}, {
                          "$inc": {"gates_usage": 1}})
    await ñ.edit(texto_final)
