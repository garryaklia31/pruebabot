from all.configs._def_main_ import *

@Techie('toggleall')
async def toggle_all_commands(_, message):
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos["role"] != "Owner":
        return

    comandos_habilitados = cargar_datos()

    if len(message.command) < 2:
        return await message.reply(text='<b><i>Uso: /toggleall [on|off]</i></b>', quote=True)

    estado = message.command[1]

    if estado == 'on':
        for comando, info in comandos_habilitados.items():
            comandos_habilitados[comando]['enabled'] = True

        guardar_datos(comandos_habilitados)

        await message.reply(text='<b><i>Todos los comandos han sido habilitados.</i></b>', quote=True)

    elif estado == 'off':
        for comando, info in comandos_habilitados.items():
            comandos_habilitados[comando]['enabled'] = False

        guardar_datos(comandos_habilitados)

        await message.reply(text='<b><i>Todos los comandos han sido deshabilitados.</i></b>', quote=True)

    else:
        await message.reply(text='<b><i>Uso: /toggleall [on|off]</i></b>', quote=True)
