import pymongo
import os
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from pymongo.errors import *
from datetime import datetime

# Cargar las variables de entorno
MONGO_URI = os.getenv("MONGO_URI")  # Sin valor por defecto
LOG_CHAT_ID = int(os.getenv("LOG_CHAT_ID"))  # Sin valor por defecto

# Verificar que las variables de entorno existan
if not MONGO_URI:
    raise EnvironmentError("La variable de entorno 'MONGO_URI' no está configurada.")
if not LOG_CHAT_ID:
    raise EnvironmentError("La variable de entorno 'LOG_CHAT_ID' no está configurada.")

# Configurar la conexión a la base de datos
client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
database = client['botchk']

# Colecciones
collection = database['usuarios']
collection_dos = database['keys']
collection_tres = database['groups']
collection_cuatro = database['gates']
collection_cinco = database['alerts']

# Comando para renovar claves
@Client.on_message(filters.command('renovacion', prefixes=['/', ',', '.', '!', '$', '-']))
async def uwu(client, message):
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos and buscar_permisos.get("role") == "Owner":
        for usuario in collection.find():
            if usuario["key"] != "None" and usuario["key"] < datetime.now():
                # Actualizar la clave a "None"
                collection.update_one({"_id": usuario["_id"]}, {
                    "$set": {"key": "None", "plan": "Free User", "antispam": 60, "apodo": "Free User"}
                })
                chat_id = usuario["_id"]
                mensaje = (
                    f"<b><i>Your key has expired. Contact @ShylphietteGreyrat to purchase a new one.</i></b>"
                )
                mensaje_admin = (
                    f"<b><i>The user with ID <code>{chat_id}</code> is no longer premium. "
                    "Check if they are in the premium paid users group.</i></b>"
                )
                try:
                    await client.send_message(chat_id, mensaje)
                    await client.send_message(LOG_CHAT_ID, mensaje_admin)
                except Exception as e:
                    print(f"Error al enviar mensaje: {e}")
        await message.reply(text="<b>The notification has been sent to all registered users.</b>", quote=True)
    else:
        await message.reply("<b>You do not have permission to use this command.</b>", quote=True)
