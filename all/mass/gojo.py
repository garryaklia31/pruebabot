from datetime import datetime
from all.configs._def_main_ import *
from all.functions.func_charged.func_gojo import *

nombregate = "Gojo"
tipogate = "Payflow"
cmdgate = "massgo"


@Techie(f'{cmdgate}')
async def gojocmds(_, message):
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
        if not comandos_habilitados.get('massgo', {}).get('enabled', False):
            reason = comandos_habilitados.get(
                'massgo', {}).get('reason', "Unknown")
            date = comandos_habilitados.get('massgo', {}).get('date', "Unknown")
            _textoff = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Info</i> ➣ The {cmdgate} command is disabled ❗ 
━━━━━━━━「ELAINA」━━━━━━━━</b>"""
            return await message.reply(text=_textoff, quote=True)

    if message.reply_to_message:
        input_lines = str(message.reply_to_message.text).split("\n")
    else:
        input_lines = str(message.text).split("\n")

    vnnotmsg = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Gateways</i> ➣ <i>{nombregate}|{tipogate}</i>
<i>Command</i> ➣ <code>${cmdgate}</code>
<i>Format</i> ➣ <code>${cmdgate} cc|month|year|cvv</code>
━━━━━━━━「ELAINA」━━━━━━━━</b>"""

    if len(input_lines) < 4:
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
            return await message.reply(text=notpermiso, quote=True)

    else:
        return await message.reply(text=notpermiso, quote=True)

    cc_list = []
    for input_line in input_lines:
        input = re.findall(r'[0-9]+', input_line)
        if len(input) < 4:
            continue

        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]

        cc_list.append((cc, mes, ano, cvv))

        if cc[0] in bin_prohibido:
            collection.update_one({"_id": message.from_user.id}, {
                "$inc": {"tareas_en_proceso": -1}})
            return await message.reply(text=vnnotmsg, quote=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://bins.antipublic.cc/bins/{cc[:6]}", ssl=False) as response:
                req = await response.json()

        brand = req.get('brand')
        country_name = req.get('country_name')
        country_flag = req.get('country_flag')
        bank = req.get('bank')
        level = req.get('level')
        typea = req.get('type')

        baneado = f"""<b><i>Bin Banned</i></b>"""

        bin = cc[:6]

        banned_bins = load_banned_bins()

        if bin in banned_bins:
            collection.update_one({"_id": message.from_user.id}, {
                "$inc": {"tareas_en_proceso": -1}})

            return await message.reply(text=baneado, quote=True)

        if cc[0] in bin_prohibido:
            collection.update_one({"_id": message.from_user.id}, {
                "$inc": {"tareas_en_proceso": -1}})
            return await message.reply(text=vnnotmsg, quote=True)

        if usuario["role"] == "Owner":
            pass
        else:
            if len(cc_list) >= 11:
                return await message.reply(text="<b><i>Solo se pueden procesar hasta 10 tarjetas a la vez.</i></b>", quote=True)

    if len(cc_list) == 0:
        return await message.reply(text=vnnotmsg, quote=True)

    if req.get("level") is not None and "PREPAID" in req.get("level"):
        collection.update_one({"_id": message.from_user.id}, {
            "$inc": {"tareas_en_proceso": -1}})

        return await message.reply(text=baneado, quote=True)

    texto_1 = f"""<b>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Comment</i> ➣ <code>Checking Your Cards...</code>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Checked by</i> ➣ <a href="tg://user?id={ID}">{FIRST}</a> [{usuario["apodo"]}]</b>"""

    if usuario["role"] == "Owner":
        pass
    else:
        tiempo_usuario = int(usuario["time_user"])
        spam_time = int(time.time()) - tiempo_usuario
        if spam_time < usuario['antispam']:
            tiempo_restante = usuario['antispam'] - spam_time
            texto_spam = f"""<b><i><Try again after {tiempo_restante}'s</i></b>"""
            return await Client.send_message(_, chat_id=message.chat.id, text=texto_spam, reply_to_message_id=message.id)

        collection.update_one({"_id": message.from_user.id}, {
                              "$set": {"time_user": int(time.time())}})

    l = await message.reply(text=texto_1, quote=True)

    texto_1 = f"""<b>
━━━━━━━━「ELAINA」━━━━━━━━
</b>"""

    texto_2 = f"""<b><i>Info</i> ➣ <code>{brand} {level} {typea}</code>
<i>Bank</i> ➣ <code>{bank}</code>
<i>Country</i> ➣ <code>{country_name} | {country_flag}</code>
<i>Gateways</i> ➣ <i>{nombregate}|{tipogate}</i>
━━━━━━━━「ELAINA」━━━━━━━━
<i>Checked by</i> ➣ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{usuario["apodo"]}</code>]
</b>"""

    cc_output = ""
    for i, cc_data in enumerate(cc_list):
        if not luhn_algorithm(cc_data[0]):
            mensaje = 'Luhn failure'
            status = 'Luhn Failure!'
            logo = '🟥'
        else:
            try:
                resultado = await auth(cc, mes, ano, cvv)
                if resultado == "cvv2 mismatch: 15004-this transaction cannot be processed. please enter a valid credit card verification number.":
                    mensaje = 'CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.'
                    status = 'Approved!'
                    logo = '🟩'
                elif resultado == "declined: 15005-this transaction cannot be processed.":
                    mensaje = 'Declined: 15005-This transaction cannot be processed.'
                    status = 'Declined!'
                    logo = '🟥'
                elif resultado == "invalid expiration date: 10502-this transaction cannot be processed. please use a valid credit card.":
                    mensaje = 'Invalid expiration date: 10502-this transaction cannot be processed. please use a valid credit card.'
                    status = 'Declined!'
                    logo = '🟥'
                elif resultado == "field format error: 12002-this transaction cannot be processed due to either missing, incomplete or invalid 3-d secure authentication values.":
                    mensaje = "Field format error: 12002-this transaction cannot be processed due to either missing, incomplete or invalid 3-d secure authentication values."
                    status = 'Declined!'
                    logo = '🟥'
                elif resultado == "invalid account number: 10535-this transaction cannot be processed. please enter a valid credit card number and type.":
                    mensaje = "invalid account number: 10535-this transaction cannot be processed. please enter a valid credit card number and type."
                    status = 'Declined!'
                    logo = '🟥'
                else:
                    mensaje = resultado
                    status = 'Declined!'
                    logo = '🟥'
            except:
                mensaje = 'proxys'
                status = 'Refused!'
                logo = '🟥'
                
                
                logo = '🟥'
        cc_output += f"<b><i>Card:</i></b> <code>{cc_data[0]}:{cc_data[1]}:{cc_data[2]}:{cc_data[3]}</code>\n"
        cc_output += f"""<b><i>↳  Status:</i></b> <code>#{mensaje}</code> {logo}
━━━━━━━━「ELAINA」━━━━━━━━
</b>"""
        if cc_output != l.text:
            await l.edit(text=texto_1 + cc_output + texto_2)
