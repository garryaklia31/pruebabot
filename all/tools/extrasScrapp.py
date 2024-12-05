from all.configs._def_main_ import *
import time
import requests
import random
from datetime import datetime

EXTRAPOLATIONS_FILE = os.path.join("extrapolaciones.txt")
BIN_DATA_FILE = os.path.join("bins.csv")

def get_bin_info1(bin_number):
    with open(BIN_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['number'] == bin_number:
                return row
    return None

def format_bin_info(bin_info):
    formatted_info = (
        f"\n<b>━━━━━「INFO」━━━━━</b>\n"
        f"<b>BIN: {bin_info['number']}</b>\n"
        f"<b>COUNTRY: {bin_info['country']} - {bin_info['flag']}</b>\n"
        f"<b>BANK: {bin_info['bank']}</b>\n"
        f"<b>TYPE: {bin_info['vendor']} - {bin_info['type']} - {bin_info['level']}</b>\n<b>━━━━━「ELAINA」━━━━━</b>"
    )
    return formatted_info

@Techie('extra2')
async def generate_extra2(client, message):
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
    
    try:
        numero = message.text.split()[1]
    except IndexError:
        await message.reply("Por favor, proporciona un número después del comando /extra.")
        return

    bin_info = get_bin_info1(numero)

    if bin_info:
        bin_info_formatted = format_bin_info(bin_info)
      
        extrapolaciones = set()
        with open(EXTRAPOLATIONS_FILE, 'r') as file:
            for line in file:
                if line.startswith(numero):
                    extrapolaciones.add(line.strip())
       

        extras_formatted = ""
        if extrapolaciones:
            extras_formatted = "<b>━━━━━「ELAINA」━━━━━\nExtras Encontradas en mi DataBase</b>\n<b>━━━━━「DATA EXTRAS」━━━━━</b>\n"""+ "\n".join(extrapolaciones)

        username = message.from_user.username if message.from_user.username else "Unknown"
        custom_message1 = f"\n<b>checked by ➣ </b><code>@{username}</code> \n<b>━━━━━「ELAINA」━━━━━</b>"

        response = extras_formatted + bin_info_formatted + custom_message1 
        await message.reply(response)
    else:
        await message.reply("No se encontró información para ese número de BIN.")
