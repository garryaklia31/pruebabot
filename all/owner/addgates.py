from all.configs._def_main_ import *


@Techie('addauth')
async def addauth(client, message: Message):
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos["role"] != "Owner":
        return
    if len(message.command) != 3:
        await message.reply(text="Uso incorrecto del comando. El formato correcto es `/addauth cmd_name gate_name`.", quote=True)
        return

    cmd_name = message.command[1].lower()
    gate_name = message.command[2].title()

    gate_dict = {
        '_id': cmd_name,
        'status': True,
        'status_logo': '✅',
        'gate_type': 'auth',
        'cmd_name': cmd_name,
        'gate_name': gate_name,
        'made_by_id': message.from_user.id,
        'made_by_name': message.from_user.first_name,
        'is_paid': True,
        'date': strftime("%Y-%m-%d", gmtime())
    }

    collection_cuatro.insert_one(gate_dict)

    await message.reply(text=f"Autenticación `{cmd_name}` agregada correctamente con nombre de puerta `{gate_name}`.", quote=True)



@Techie('addcharged')
async def addcharged(client, message: Message):
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos["role"] != "Owner":
        return
    
    if len(message.command) != 3:
        await message.reply(text="Uso incorrecto del comando. El formato correcto es `/addcharged cmd_name gate_name`.", quote=True)
        return

    cmd_name = message.command[1].lower()
    gate_name = message.command[2].title()

    gate_dict = {
        '_id': cmd_name,
        'status': True,
        'status_logo': '✅',
        'gate_type': 'charged',
        'cmd_name': cmd_name,
        'gate_name': gate_name,
        'made_by_id': message.from_user.id,
        'made_by_name': message.from_user.first_name,
        'is_paid': True,
        'date': strftime("%Y-%m-%d", gmtime())
    }

    collection_cuatro.insert_one(gate_dict)

    await message.reply(text=f"Autenticación `{cmd_name}` agregada correctamente con nombre de puerta `{gate_name}`.", quote=True)
