from pyrogram import Client
import os
import logging
from mongoDB import *
import asyncio
from datetime import datetime
from pyrogram.errors import RPCError, BadRequest
import aiohttp
from all.proxis.array_proxies import proxies as array_proxies

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Obtener el ID del chat de logs desde las variables de entorno
LOG_CHAT_ID = int(os.getenv("LOG_CHAT_ID"))  # Por defecto, usa un valor fijo

# Función para verificar proxies
async def check_proxy(proxy):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://ipv4.webshare.io//", proxy=proxy, timeout=8) as resp:
                result = await resp.text()
                if result:
                    if "Welcome to Webshare" in result:
                        return "Proxy de pago requerido 🔒", proxy
                    else:
                        return "Proxy live ✅", proxy
        return None
    except aiohttp.ClientResponseError as e:
        if e.status == 402:
            return "Proxy de pago requerido 🔒", proxy
        else:
            print(f"Error durante la verificación del proxy: {e}")
            return None
    except Exception as e:
        print(f"Error durante la verificación del proxy: {e}")
        return None

# Función para verificar múltiples proxies
async def check_proxies():
    results = []
    for proxy in array_proxies:
        result = await check_proxy(proxy)
        if result is not None:
            results.append(result)
    return results

# Tarea periódica para verificar proxies
async def periodic_proxy_check():
    while True:
        results = await check_proxies()
        for result in results:
            print(result)

        with open('all/proxis/array_proxies.py', 'r') as file:
            lines = file.readlines()

        paid_proxies = [result[1] for result in results if result[0] == "Proxy de pago requerido 🔒"]

        filtered_lines = []
        for line in lines:
            proxy_line = line.strip()
            if any(proxy in proxy_line for proxy in paid_proxies):
                print(f"Proxy de pago encontrado y eliminado: {line.strip()}")
            else:
                filtered_lines.append(line)

        with open('all/proxis/array_proxies.py', 'w') as file:
            file.writelines(filtered_lines)

        print("Se han eliminado las proxies de pago del archivo array_proxies.py.")
        await asyncio.sleep(600)

# Tarea periódica para renovar membresías
async def periodic_renewal(bot):
    while True:
        await asyncio.sleep(3600)
        for usuario in collection.find():
            if usuario["key"] != "None":
                if usuario["key"] < datetime.now():
                    collection.update_one({"_id": usuario["_id"]}, {
                        "$set": {"key": "None", "plan": "Free User", "antispam": 60, "apodo": "Free User",}})
                    chat_id = usuario["_id"]
                    mensaje = f"""<b><i>Hello user with the id <code>{chat_id}</code>, your premium membership has expired. Contact a seller to purchase a new one.</i></b>"""
                    mensaje_admin = f"""<b><i>The user with id <code>{chat_id}</code> is no longer premium. Check if they are in the paid premium user group.</i></b>"""
                    mensaje_admin2 = f"""<b><i>The user with id <code>{chat_id}</code> is no longer premium but could not receive the message!</i></b>"""
                    try:
                        await bot.send_message(chat_id, mensaje)
                        await bot.send_message(LOG_CHAT_ID, mensaje_admin)
                    except:
                        await bot.send_message(LOG_CHAT_ID, mensaje_admin2)
                        pass

# Tarea periódica para restablecer contadores
async def resetallcmd():
    while True:
        collection.update_many({"alerts": {"$exists": True}}, {"$set": {"alerts": 0}})
        collection.update_many({"tareas_en_proceso": {"$exists": True}}, {"$set": {"tareas_en_proceso": 0}})
        await asyncio.sleep(180)

# Función principal
async def main():
    # Leer configuración desde las variables de entorno
    bot = Client(
        'Chkbot',
        api_id=int(os.getenv("API_ID")),
        api_hash=os.getenv("API_HASH"),
        bot_token=os.getenv("BOT_TOKEN"),
        plugins=dict(root="all")
    )
    os.system('cls' if os.name == 'nt' else 'clear')
    await bot.start()
    await asyncio.gather(
        periodic_proxy_check(),
        periodic_renewal(bot),
        resetallcmd(),
        asyncio.Event().wait(),
    )

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    asyncio.run(main())
