from all.configs._def_main_ import *


async def perfil(Client, message, update):
    buttons = [[InlineKeyboardButton('Atras', callback_data='start')]]

    reply_markup = InlineKeyboardMarkup(buttons)

    usuario = collection.find_one(
        {"_id": message.reply_to_message.from_user.id})

    if usuario is None:
        caption = await registrar_usuario(message)
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
        if key_ != 'None':
            key_ = plan + " " + "-" + " " + key_.strftime('%Y-%m-%d')
        else:
            key_ = 'No Key Actived'
        creditos = usuario["credits"]
        apodo = usuario["apodo"]

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=nperfil.format(user_name=user_name, id_usuario=id_usuario,
                            creditos=creditos, apodo=apodo, plan=plan, key_=key_),
        reply_markup=reply_markup,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def start(Client, message, update):
    tecaption = gtx

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=tecaption,
        reply_markup=dbre,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def gates(Client, message, update):  # GATESSSSSS
    text = gatestext

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text,
        reply_markup=gatbot,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def tools(Client, message, update):  # TOOLS 1

    text_tools_1 = tooltx

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_tools_1,
        reply_markup=toolsbot,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def tools_2(Client, message, update):  # TOOLS 2

    text_tools_2 = tooltx2

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_tools_2,
        reply_markup=toolsbot2,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def authgatecomand(Client, message, update):
    text_auth = authtx
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_auth,
        reply_markup=atrx2,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def chargedgatecomand(Client, message, update):
    text_charged = chargedtx
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_charged,
        reply_markup=chargebotons,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def chargedgatecomand_2(Client, message, update):
    text_charged = chargedtx_2
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_charged,
        reply_markup=chargebotons_2,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def chargedgatecomand_3(Client, message, update):
    text_charged = chargedtx_3
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_charged,
        reply_markup=chargebotons_3,
        message_id=message.id,
        disable_web_page_preview=True
    )



async def chargedgatecomand_4(Client, message, update):
    text_charged = chargedtx_4
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_charged,
        reply_markup=chargebotons_4,
        message_id=message.id,
        disable_web_page_preview=True
    )

async def chargedgatecomand_5(Client, message, update):
    text_charged = chargedtx_5
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_charged,
        reply_markup=chargebotons_5,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def ccngatecomand(Client, message, update):
    text_ccn = ccntxx
    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_ccn,
        reply_markup=atrx2,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def buypremium(Client, message, update):
    
    text_buy = notpermiso

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=text_buy,
        reply_markup=buypremium,
        message_id=message.id,
        disable_web_page_preview=True
    )

async def buypremium2(Client, message, update):
    
    buypm = buypma

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=buypm,
        reply_markup=buypremium2,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def despedida(Client, message, update):

    txtdes = despedidatxt

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=txtdes,
        reply_markup=reopen,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def admins(Client, message, update):

    adtex = admintxt

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=adtex,
        reply_markup=botadmin,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def admins_2(Client, message, update):

    adtex = admintxt2

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=adtex,
        reply_markup=botadmin2,
        message_id=message.id,
        disable_web_page_preview=True
    )


async def admins_3(Client, message, update):

    adtex = admintxt3

    await Client.edit_message_text(
        chat_id=message.chat.id,
        text=adtex,
        reply_markup=botadmin3,
        message_id=message.id,
        disable_web_page_preview=True
    )

async def genagan(Client, message, update):
    usuario = collection.find_one(
        {"_id": message.reply_to_message.from_user.id})
    ID = message.reply_to_message.from_user.id
    FIRST = message.reply_to_message.from_user.first_name
    if update.message.reply_to_message.reply_to_message:
        VerMessage = re.sub(
            "\n", " ", update.message.reply_to_message.reply_to_message.text)
    else:
        VerMessage = re.sub(
            "\n", " ", update.message.reply_to_message.text[5:])
    try:
        VerMessage = re.sub("[^0-9a-zA-Z]", " ", VerMessage)
        matchcc = re.findall(r"\b[0-9a-zA-Z]{6,16}\b", VerMessage)
        for i in matchcc:
            i = matchcc
        l = i
        for x in range(len(l)):
            list_ = l[x]
            if list_[0:6].isnumeric():
                CCnum = list_
    except:
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
    VerMessage = f'{CCnum}|{mes}|{ano}|{cvv}'
    try:
        x = get_bin_info(VerMessage[0:6])
        brand = x.get("vendor")
        level = x.get("level")
        typea = x.get("type")
        bank = x.get("bank_name")
        country_name = x.get("country")
        country_flag = x.get("flag")
    except:
        return "ERROR"
    if VerMessage:
        finalr = str(await GeneatedCC(VerMessage)).split('-')
        listcc = finalr[0]
        extrapcc = finalr[1]
        fin = '0.001'
        if not message.from_user.username:
            UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
        else:
            UserName = f'@{message.from_user.username}'
        plan = usuario["apodo"]
        txgenmass = f"""<b>━━━━━「CCS GENERATOR」━━━━━
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
        await Client.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.id,
            text=txgenmass,
            reply_markup=regen)


async def genmassformate(Client, message, update):
    usuario = collection.find_one(
        {"_id": message.reply_to_message.from_user.id})
    ID = message.reply_to_message.from_user.id
    FIRST = message.reply_to_message.from_user.first_name
    if update.message.reply_to_message.reply_to_message:
        VerMessage = re.sub(
            "\n", " ", update.message.reply_to_message.reply_to_message.text)
    else:
        VerMessage = re.sub(
            "\n", " ", update.message.reply_to_message.text[5:])
    try:
        VerMessage = re.sub("[^0-9a-zA-Z]", " ", VerMessage)
        matchcc = re.findall(r"\b[0-9a-zA-Z]{6,16}\b", VerMessage)
        for i in matchcc:
            i = matchcc
        l = i
        for x in range(len(l)):
            list_ = l[x]
            if list_[0:6].isnumeric():
                CCnum = list_
    except:
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
    VerMessage = f'{CCnum}|{mes}|{ano}|{cvv}'
    try:
        x = get_bin_info(VerMessage[0:6])
        brand = x.get("vendor")
        level = x.get("level")
        typea = x.get("type")
        bank = x.get("bank_name")
        country_name = x.get("country")
        country_flag = x.get("flag")
    except:
        return "ERROR"
    if VerMessage:
        finalr = str(await GeneatedCC(VerMessage)).split('-')
        listcc = finalr[0]
        extrapcc = finalr[1]
        fin = '0.001'
        if not message.from_user.username:
            UserName = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>"
        else:
            UserName = f'@{message.from_user.username}'
        plan = usuario["apodo"]
        txgenmass2 = f"""<b>━━━「CCS GENERATOR」━━━
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
        await Client.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.id,
            text=txgenmass2,
            reply_markup=regen)



@Client.on_callback_query()
async def button(Client, update):
    cb_data = update.data
    text = '𝑨𝒄𝒄𝒆𝒔𝒔 𝒅𝒆𝒏𝒊𝒆𝒅 🟥'
    try:
        if update.message.reply_to_message.from_user.id == update.from_user.id:
            if "gates" in cb_data:
                await gates(Client, update.message, update)
            elif "start" in cb_data:
                await start(Client, update.message, update)
            elif "tools" in cb_data:
                await tools(Client, update.message, update)
            elif "GenerateAgain" in cb_data:
                await genagan(Client, update.message, update)
            elif "FormateMass" in cb_data:
                await genmassformate(Client, update.message, update)
            elif "Finish" in cb_data:
                await update.message.delete()
            elif "sexo" in cb_data:
                await tools_2(Client, update.message, update)
            elif "admin" in cb_data:
                await admins(Client, update.message, update)
            elif "sexito" in cb_data:
                await admins_2(Client, update.message, update)
            elif "sexmi" in cb_data:
                await admins_3(Client, update.message, update)
            elif "user_perfil" in cb_data:
                await perfil(Client, update.message, update)
            elif "authgate" in cb_data:
                await authgatecomand(Client, update.message, update)
            elif "chargedgate" in cb_data:
                await chargedgatecomand(Client, update.message, update)
            elif "page2" in cb_data:
                await chargedgatecomand_2(Client, update.message, update)
            elif "page3" in cb_data:
                await chargedgatecomand_3(Client, update.message, update)
            elif "page4" in cb_data:
                await chargedgatecomand_4(Client, update.message, update)
            elif "page5" in cb_data:
                await chargedgatecomand_5(Client, update.message, update)
            elif "ccngate" in cb_data:
                await ccngatecomand(Client, update.message, update)
            elif "close" in cb_data:
                await despedida(Client, update.message, update)
            elif "buypremium" in cb_data:
                await buypremium(Client, update.message, update)
            elif "buypremium2" in cb_data:
                await buypremium2(Client, update.message, update)
            
        else:
            await Client.answer_callback_query(
                callback_query_id=update.id,
                text=text,
                show_alert="true"
            )
    except RPCError as e:
        print(e)
    except BadRequest as e:
        print(e)
    except Forbidden as e:
        print(e)
