from all.configs._def_main_ import *


@Techie('on')
async def habilitar_comando(_, message):
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos["role"] == "Owner":
        # Cargar los datos del archivo datos.json
        comandos_habilitados = cargar_datos()

        # Verificar si se proporcionó un argumento
        if len(message.command) < 1:
            return await message.reply(text='<b><i>Uso: /on [comando]</i></b>', quote=True)

        # Obtener el nombre del comando y la razón, si se proporciona
        comando_y_razon = message.text.split(maxsplit=1)[1]
        comando, razon = comando_y_razon.split(
            '|') if '|' in comando_y_razon else (comando_y_razon, '')

        # Verificar si el comando existe
        if comando not in comandos_habilitados:
            # Si el comando no existe, crear una entrada con el valor predeterminado
            comandos_habilitados[comando] = {
                'enabled': True,
                'reason': '',
                'date': ''
            }

        # Verificar si el comando ya está habilitado
        if comandos_habilitados[comando]['enabled']:
            return await message.reply(text=f'<b><i>El comando {comando} ya está habilitado.</i></b>', quote=True)

        # Habilitar el comando
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        comandos_habilitados[comando] = {
            'enabled': True,
            'date': fecha_actual
        }
        guardar_datos(comandos_habilitados)
        await message.reply(text=f'<b><i>El comando {comando} ha sido habilitado.</i></b>', quote=True)
    else:
        return

@Techie('off')
async def deshabilitar_comando(_, message):
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos["role"] != "Owner":
        return

    comandos_habilitados = cargar_datos()

    if len(message.command) < 2:
        return await message.reply(text='<b><i>Uso: /off [comando|razón]</i></b>', quote=True)

    comando_y_razon = message.text.split(maxsplit=1)[1]
    comando, razon = comando_y_razon.split(
        '|') if '|' in comando_y_razon else (comando_y_razon, '')

    if comando not in comandos_habilitados:
        comandos_habilitados[comando] = {
            'enabled': True,
            'reason': '',
            'date': ''
        }

    if not comandos_habilitados[comando]['enabled']:
        return await message.reply(text=f'<b><i>El comando {comando} ya está deshabilitado.</i></b>', quote=True)

    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    comandos_habilitados[comando] = {
        'enabled': False,
        'reason': razon,
        'date': fecha_actual
    }

    guardar_datos(comandos_habilitados)

    await message.reply(text=f'<b><i>El comando {comando} ha sido deshabilitado.</i></b>', quote=True)
