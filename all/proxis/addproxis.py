from all.configs._def_main_ import *
from all.proxis.array_proxies import *


async def check_proxy(user, rotate, password):
    try:
        rotate_proxy = f"http://{user}-{rotate}:{password}@p.webshare.io:80"
        
        async with aiohttp.ClientSession() as session:
            for _ in range(3):
                async with session.get("https://ipv4.webshare.io//", proxy=rotate_proxy, timeout=8) as resp:
                    result = await resp.text()
                    if result:
                        if "Welcome to Webshare" in result:
                            return "Proxy de pago requerido 🔒", rotate_proxy
                        else:
                            return "Proxy live ✅", rotate_proxy
        
        return None
    except aiohttp.ClientResponseError as e:
        if e.status == 402:
            return "Proxy de pago requerido 🔒", rotate_proxy
        else:
            print(f"Error durante la verificación del proxy: {e}")
            return None
    except Exception as e:
        print(f"Error durante la verificación del proxy: {e}")
        return None
    
def save_proxy(proxy):
    try:
        with open("all/proxis/array_proxies.py", "r") as file:
            lines = file.readlines()

        lines.pop()

        lines.append(f"    '{proxy}',\n")

        lines.append("]\n")

        with open("all/proxis/array_proxies.py", "w") as file:
            file.writelines(lines)

    except Exception as e:
        print("Error al guardar el proxy:", e)



@Techie('addproxy')
async def process_proxy(_, message):
    proxy_data = message.text.split(' ')[1:]
    if len(proxy_data) != 2:
        await message.reply(text="Formato incorrecto. Debe ser /addproxy usuario-rotate contraseña", quote=True)
        return

    user_rotate = proxy_data[0]
    password = proxy_data[1]
    user, rotate = user_rotate.split('-')

    result = await check_proxy(user, rotate, password)
    if result:
        status, proxy = result
        await message.reply(f"Resultado: {status}\nProxy: {proxy}", quote=True)
        if "requerido" not in status:
            save_proxy(proxy)
    else:
        await message.reply(text="La verificación del proxy ha fallado. Verifique si la proxy es de pago.", quote=True)