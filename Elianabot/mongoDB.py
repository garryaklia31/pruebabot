import pymongo
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pymongo.errors import *
from datetime import datetime

# Conectar a MongoDB Atlas con la URI proporcionada
MONGO_URI = 'mongodb+srv://garry:MEHAKPREET@garry.mn2ay.mongodb.net/?retryWrites=true&w=majority&appName=Garry'
client = pymongo.MongoClient(MONGO_URI)  # Crear la conexión al cliente MongoDB

# Seleccionar la base de datos y las colecciones
database = client['Elaina']
collection = database['usuarios']
collection_dos = database['keys']
collection_tres = database['groups']
collection_cuatro = database['gates']
collection_cinco = database['alerts']

# Reemplaza con el ID del chat donde quieres enviar el registro
LOG_CHAT_ID = -1002228014836

@Client.on_message(filters.command('renovacion', prefixes=['/', ',', '.', '!', '$', '-']))
async def uwu(client, message):
    # Buscar los permisos del usuario en la colección 'usuarios'
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    
    if buscar_permisos and buscar_permisos["role"] == "Owner":  # Verifica si el usuario tiene el rol 'Owner'
        for usuario in collection.find():
            if usuario.get("key") != "None":
                if usuario["key"] < datetime.now():
                    # Actualizar la clave a "None" y establecer otros valores por defecto
                    collection.update_one({"_id": usuario["_id"]}, {
                        "$set": {"key": "None", "plan": "Free User", "antispam": 60, "apodo": "Free User"}})
                    
                    chat_id = usuario["_id"]
                    mensaje = f"""<b><i>Your key has expired. contact @ShylphietteGreyrat to purchase a new one.</i></b>"""
                    mensaje_admin = f"""<b><i>El usuario con el id <code>{chat_id}</code> dejo de ser premium, revisar si esta en grupo de usuarios premium pagados</i></b>"""
                    
                    try:
                        # Enviar mensajes a los usuarios y al administrador
                        await client.send_message(chat_id, mensaje)
                        await client.send_message(LOG_CHAT_ID, mensaje_admin)
                        await message.reply(text='<b>El anuncio ha sido enviado a todos los usuarios registrados.</b>', quote=True)
                    except Exception as e:
                        print(f"Error al enviar mensaje a {chat_id}: {e}")
                else:
                    pass
            else:
                pass
    else:
        return
