from all.configs._def_main_ import *

@Techie('warn')
async def ban(_,message):
    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos is None: return await message.reply(text='<b>Registrate <code>!register</code></b>',quote=True)
        
    
    if buscar_permisos["role"] == "Owner" or buscar_permisos["role"] == "Co-Owner" or buscar_permisos["role"] == "Seller" or buscar_permisos["role"] == "Dev": pass	
    else: return print('Sin autorización')
		
    user =  message.reply_to_message.from_user.id
    
    buscar = collection.find_one({"_id": user})
    if buscar is None: return await message.reply('<b>El usuario a quien intentas sancionar, no se encuentra registrado.</b>',quote=True)
    
    collection.update_one({"_id": user}, {"$set": {"alerts": '1'}})
 
    
    texto = f'''<b>
El usuario a sido Alertado

</b>'''

    await message.reply(texto,quote=True)
    
    
   