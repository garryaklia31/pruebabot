from all.configs._def_main_ import *
import time
import requests
import random
from datetime import datetime

@Techie('exti')
async def generate_extra(client, message):
    tiempoinicio = time.perf_counter()
    encontrar_usuario = collection.find_one({"_id": message.from_user.id})
    if encontrar_usuario is None:
        return await message.reply(text='<b>Por favor regístrate con el comando <code>!register</code></b>', quote=True)
    
    if encontrar_usuario["role"] == "ban":
        return await message.reply('<i>Proceso detenido\nMotivo: ¡Usuario Baneado!</i>', quote=True)
    
    encontrar_grupo = collection_tres.find_one({"group": str(message.chat.id)})
    
    if encontrar_usuario['key'] != 'None' or encontrar_grupo is not None:
        if encontrar_usuario['key'] != 'None':
            if encontrar_usuario["key"] < datetime.now():
                collection.update_one({"_id": message.from_user.id}, {"$set": {"key": 'None'}})
                collection.update_one({"_id": message.from_user.id}, {"$set": {"antispam": 50}})
                collection.update_one({"_id": message.from_user.id}, {"$set": {"plan": 'Free'}})
                return await message.reply(text='<b>Suscripción premium concluida!</b>', quote=True)
        elif encontrar_grupo["key"] < datetime.now():
            collection_tres.delete_one({"group": str(message.chat.id)})
        else:
            return await message.reply(text='<b>No tienes permiso para ejecutar este comando.</b>', quote=True)
    
    inputm = message.text.split(None, 1)
    if len(inputm) != 2 or not inputm[1] or len(inputm[1]) != 16:
      
        message_text = "<b>⚠️ Estás usando el comando incorrectamente, utiliza <code>/exti cc</code>.</b>"
        await message.reply_text(
            text=message_text,
        )
        return
    
    BIN = inputm[1]
    req = requests.get(f"https://bins.antipublic.cc/bins/{BIN}").json()
    
    try:
        brand = req['brand']
        country_name = req['country_name']
        country_flag = req['country_flag']
        bank = req['bank']
    except KeyError:
        message_text = "Lo siento, el BIN no está en mi base de datos."
        await message.reply_text(
            text=message_text
        )
        return

    extrap = []
    for _ in range(10):
        random_digits = "".join(random.choice("0123456789") for _ in range(6))
        random_month = random.randint(1, 12)
        random_year = random.randint(2024, 2030)
        extra = f"{BIN}{random_digits}xxxx|{random_month:02d}|{random_year}|rnd"
        extrap.append(f"<code>{extra}</code>")

    tiempofinal = time.perf_counter()

   
    message_text = f"""<b>━━━━━「ELAINA」━━━━━
<i>➣ EXTRA POR INDENTACIÓN</i>
━━━━━「EXTRA」━━━━━
<code>{BIN[:7]}x{BIN[8:10]}xx{BIN[12:14]}x{BIN[15:16]}</code>
━━━━━「ELAINA」━━━━━
<b>Tiempo de ejecución ➣ </b>: <code>{tiempofinal - tiempoinicio:.2f}'s</code>
<b>Checked by ➣ </b>: <code>@{message.from_user.username}</code>  [{encontrar_usuario['plan']}]
━━━━━「ELAINA」━━━━━</b>"""

    await message.reply_text(
        text=message_text,
    )
