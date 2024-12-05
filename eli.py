from pyrogram import Client
import os
import logging
from aiohttp import web
from mongoDB import *
import asyncio
from datetime import datetime
from all.proxis.array_proxies import proxies as array_proxies

logging.basicConfig(level=logging.INFO)

LOG_CHAT_ID = -1002416011069

# Servidor HTTP para Render
async def handle(request):
    return web.Response(text="Bot de Telegram está en ejecución")

async def start_http_server():
    port = int(os.environ.get("PORT", 8080))
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logging.info(f"Servidor HTTP ejecutándose en el puerto {port}")

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
    except Exception as e:
        logging.error(f"Error durante la verificación del proxy: {e}")
        return None

# Verificar múltiples proxies
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
            logging.info(result)

        with open('all/proxis/array_proxies.py', 'r') as file:
            lines = file.readlines()

        paid_proxies = [result[1] for result in results if result[0] == "Proxy de pago requerido 🔒"]

        filtered_lines = []
        for line in lines:
            proxy_line = line.strip()
            if any(proxy in proxy_line for proxy in paid_proxies):
                logging.info(f"Proxy de pago encontrado y eliminado: {line.strip()}")
            else:
                filtered_lines.append(line)

        with open('all/proxis/array_proxies.py', 'w') as file:
            file.writelines(filtered_lines)

        logging.info("Se han eliminado las proxies de pago del archivo array_proxies.py.")
        await asyncio.sleep(600)

# Tarea periódica para renovar membresías
async def periodic_renewal(bot):
    while True:
        await asyncio.sleep(3600)
        for usuario in collection.find():
            if usuario["key"] != "None":
                if usuario["key"] < datetime.now():
                    collection.update_one({"_id": usuario["_id"]}, {
                        "$set": {"key": "None", "plan": "Free User", "antispam": 60, "apodo": "Free User"}})
                    chat_id = usuario["_id"]
                    mensaje = f"""<b><i>Hello user with the id <code>{chat_id}</code> your premium membership has expired, contact a seller to purchase a new one.</i></b>"""
                    mensaje_admin = f"""<b><i>El usuario con el id <code>{chat_id}</code> dejó de ser premium, revisar si está en grupo de usuarios premium pagados</i></b>"""
                    mensaje_admin2 = f"""<b><i>El usuario con el id <code>{chat_id}</code> dejó de ser premium, pero no pudo recibir el mensaje!</i></b>"""
                    try:
                        await bot.send_message(chat_id, mensaje)
                        await bot.send_message(LOG_CHAT_ID, mensaje_admin)
                    except:
                        await bot.send_message(LOG_CHAT_ID, mensaje_admin2)
                        pass

# Tarea periódica para restablecer alertas y tareas
async def resetallcmd():
    while True:
        collection.update_many({"alerts": {"$exists": True}}, {"$set": {"alerts": 0}})
        collection.update_many({"tareas_en_proceso": {"$exists": True}}, {"$set": {"tareas_en_proceso": 0}})
        await asyncio.sleep(180)

# Función principal
async def main():
    bot = Client(
        'Chkbot',
        api_id=29114806,
        api_hash="8a26d0ca9df972e7d5ad165e8e0745f8",
        bot_token="7727039084:AAGcxYDuVbj0tzdAhd9JBa7GXsx9U96j3qE",
        plugins=dict(root="all")
    )
    os.system('cls')
    await bot.start()
    await asyncio.gather(
        start_http_server(),  # Inicia el servidor HTTP
        periodic_proxy_check(),
        periodic_renewal(bot),
        resetallcmd(),
        asyncio.Event().wait(),
    )

if __name__ == "__main__":
    os.system('clear')
    asyncio.run(main())
