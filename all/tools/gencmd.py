from all.configs._def_main_ import *


@Techie('gen')
async def gen(_, message):
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    usuario = collection.find_one({"_id": message.from_user.id})

    if usuario is None:
        caption = await registrar_usuario(message)
        return await message.reply(text=caption, reply_markup=dbre, quote=True)
    else:
        pass

    if usuario['status'] == "Baneado":
        return

    if message.reply_to_message:
        try:
            VerMessage = re.sub("\n", " ", message.reply_to_message.text)
        except TypeError:
            return await _.send_message(chat_id=message.chat.id, text=malgen, reply_to_message_id=message.id)
    else:
        VerMessage = re.sub("\n", " ", message.text[5:])
    if re.sub("[^0-9]", "", VerMessage) == '':
        return await _.send_message(chat_id=message.chat.id, text=malgen, reply_to_message_id=message.id)
    inicio = time.time()
    if message.sender_chat:
        return await _.send_message(chat_id=message.chat.id, text=f"""<b><code>You are forbidden from this bot.</code> ⚠️</b>""", reply_to_message_id=message.id)
    if message.forward_from:
        return await _.send_message(chat_id=message.chat.id, text=f"""<b><code>You are forbidden from this bot.</code> ⚠️</b>""", reply_to_message_id=message.id)
    try:
        VerMessage = ''.join(['x' if c.isalpha() else c for c in VerMessage])
        VerMessage = re.sub("[^0-9a-zA-Z]", " ", VerMessage)
        matchcc = re.findall(r"\b[0-9a-zA-Z]{6,16}\b", VerMessage)
        l = []
        for cc in matchcc:
            if cc[0:6].isnumeric():
                l.append(cc)
        CCnum = l[0] if l else 'xxxxxx'
    except UnboundLocalError:
        CCnum = 'xxxxxx'
    try:
        mes = re.sub("[^0-9]", " ", VerMessage)
        BinCheck = int(CCnum[0:1])
        if 3 <= int(BinCheck) <= 6:
            if 4 <= int(BinCheck) <= 6:
                matchmes = re.findall(r"\b(0[1-9]|1[0-2])\b", mes)
                mes = matchmes[0]
            elif int(BinCheck) == 3:
                matchmes = re.findall(r"\b(0[1-9]|1[0-2])\b", mes)
                mes = matchmes[0]
    except:
        mes = 'xx'
    try:
        ano = re.sub("[^0-9]", " ", VerMessage)
        BinCheck = int(CCnum[0:1])
        if 3 <= int(BinCheck) <= 6:
            if 4 <= int(BinCheck) <= 6:
                matchano = re.findall(
                    r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-1])\b", ano)
                ano = matchano[0]
                if len(ano) == 2:
                    ano = f'20{ano}'
            elif int(BinCheck) == 3:
                matchano = re.findall(
                    r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-1])\b", ano)
                ano = matchano[0]
                if len(ano) == 2:
                    ano = f'20{ano}'
    except:
        ano = 'xxxx'
    try:
        cvv = re.sub("[^0-9a-zA-Z]", " ", VerMessage)
        BinCheck = int(CCnum[0:1])
        if 3 <= int(BinCheck) <= 6:
            if 4 <= int(BinCheck) <= 6:
                matchcvv = re.findall(
                    r"\b[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z]\b", cvv.lower())
                cvv = matchcvv[0]
                cvv = re.sub("[^0-9x]", "x", cvv)
                cvv = cvv.ljust(3, 'x')
                cvv = cvv[0:3]
            elif int(BinCheck) == 3:
                matchcvv = re.findall(
                    r"\b[0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z][0-9a-zA-Z]\b", cvv.lower())
                cvv = matchcvv[0]
                cvv = re.sub("[^0-9x]", "x", cvv)
                cvv = cvv.ljust(4, 'x')
                cvv = cvv[0:4]
    except:
        cvv = 'xxx'
    try:
        VerMessage = f'{CCnum}|{mes}|{ano}|{cvv}'
    except UnboundLocalError as e:
        print(e)
    try:
        x = get_bin_info(VerMessage[0:6])
        brand = x.get("vendor")
        level = x.get("level")
        typea = x.get("type")
        bank = x.get("bank_name")
        country_name = x.get("country")
        country_flag = x.get("flag")
    except:
        return await _.send_message(chat_id=message.chat.id, text=malgen2, reply_to_message_id=message.id)
    if ((brand == 'VISA') or (brand == 'MASTERCARD') or (brand == 'DISCOVER') or (brand == 'AMERICAN EXPRESS')) == False:
        return await _.send_message(chat_id=message.chat.id, text=f"""<b><code>This bot only accepts American, Visa, Mastercard and Discover.</code> ⚠️</b>""", reply_to_message_id=message.id)
    if VerMessage:
        finalr = str(await GeneatedCC(VerMessage)).split('-')
        listcc = finalr[0]
        extrapcc = finalr[1]

        if not message.from_user.username:
            UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
        else:
            UserName = f'@{message.from_user.username}'
        fin = f'{time.time()-inicio}'
        plan = usuario["apodo"]
        txgenmass = f"""<b>━━━━━━「CCS GENERATOR」━━━━━━
{listcc}━ • ━━━━━━━━━━━━ • ━
<i>Bin</i> ➣ <code>{VerMessage[0:6]}</code> 
<i>Info</i> ➣ <code>{brand}</code> - <code>{typea}</code> - <code>{level}</code>
<i>Bank</i> ➣ <code>{bank}</code>
<i>Country</i> ➣ <code>{country_name}</code> | {country_flag}
<i>Input</i> ➣ <code>{extrapcc}|{mes}|{ano}|{cvv}</code>
━ • ━━━━━━━━━━━━ • ━
<i>Time</i> ➣ <code>{fin[0:5]}</code><i>'s</i>
<i>Checked By</i> ➣ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{plan}</code>]
━━━━━━━━「ELAINA」━━━━━━━━</b>"""
    return await _.send_message(chat_id=message.chat.id, text=txgenmass, reply_to_message_id=message.id, reply_markup=regen)
