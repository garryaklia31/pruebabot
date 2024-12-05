import time
import requests
import random
from datetime import datetime
from all.configs._def_main_ import *


@Techie('extra')
async def generate_extra(client, message):
    tiempoinicio = time.perf_counter()
    encontrar_usuario = collection.find_one({"_id": message.from_user.id})
    if encontrar_usuario is None: 
        return await message.reply(text='<b>Por favor, regístrate con el comando <code>!register</code></b>', quote=True)
    
    if encontrar_usuario["role"] == "ban":
        return await message.reply('<i>Proceso detenido\nMotivo: ¡Usuario Baneado!</i>', quote=True)

    encontrar_grupo = collection_tres.find_one({"group": str(message.chat.id)})

    if encontrar_usuario['key'] != 'None' or encontrar_grupo is not None:
        if encontrar_usuario['key'] != 'None':
            if encontrar_usuario["key"] < datetime.now():            
                collection.update_one({"_id": message.from_user.id},{"$set": {"key": 'None'}})
                collection.update_one({"_id": message.from_user.id},{"$set": {"antispam": 50}})
                collection.update_one({"_id": message.from_user.id},{"$set": {"plan": 'Free'}})
                return await message.reply(text='<b>Suscripción premium concluida!</b>', quote=True)
        elif encontrar_grupo["key"] < datetime.now():
            collection_tres.delete_one({"group": str(message.chat.id)})

        else: 
            return await message.reply(text='<b>No tienes permiso para ejecutar este comando.</b>', quote=True)

    inputm = message.text.split(None, 1)
    if len(inputm) != 2 or not inputm[1]:
      
        message_text = "<b>⚠️ Estás usando el comando incorrectamente, utiliza <code>/extra 123456</code>.</b>"
        await message.reply_text(
            text=message_text,
        )
        return

    BIN = inputm[1][:6]

    if BIN[0] in ['1', '2', '6', '7','8', '9']:
        return await message.reply(text="<b>El BIN al que le intentas sacar extra, es inexistente en mi base de datos.</b>", quote=True)

    req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()

    try:
        brand = req['brand']
        country_name = req['country_name']
        country_flag = req['country_flag']
        bank = req['bank']
    except KeyError:
        message_text = "El BIN  al que le intentas sacar extra, es inexistente en mi base de datos."
        await message.reply_text(
            text=message_text
        )
        return

    
    extrap = []
    for _ in range(10):
        random_digits = "".join(random.choice("0123456789") for _ in range(6))
        random_month = random.randint(1, 12)
        random_year = random.randint(2025, 2030)
        extra = f"{BIN}{random_digits}xxxx|{random_month:02d}|{random_year}|rnd"
        extrap.append(f"<code>{BIN}{random_digits}xxxx|{random_month:02d}|{random_year}|rnd</code>")

 
    tiempofinal = time.perf_counter()

    message_text = f"""<b>━━━━━「ELAINA」━━━━━
<i>➣ EXTRAS GENERADAS</i>
━━━━━「EXTRAS」━━━━━
""" + "\n".join(extrap) + f"""<b>
━━━━━「INFO」━━━━━
<b>Tipo</b>: <code>{brand}</code>
<b>Banco</b>:<code> {bank}</code>
<b>País</b>: <code>{country_name}</code><code> {country_flag}</code>
━━━━━「ELAINA」━━━━━
<b>➣ checked by</b>:<code>@{message.from_user.username}</code>  [{encontrar_usuario['plan']}]
<b>➣ Time</b>: <code>{tiempofinal - tiempoinicio:.2f}'s</code></b>
━━━━━「ELAINA」━━━━━</b>"""

    await message.reply_text(
        text=message_text,
    )
