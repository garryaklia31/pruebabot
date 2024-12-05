from all.configs._def_main_ import *
import os
import sys
@Techie('restart')
async def re_start(_, message: Message):

    buscar_permisos = collection.find_one({"_id": message.from_user.id})
    if buscar_permisos is None: return await message.reply(text='<b>Por favor registrate con el comando <code>!register</code></b>',quote=True)
        
    if buscar_permisos["role"] == "Owner": pass	
    else: return await message.reply('<i>No tienes permisos ❌</i>',quote=True)

    q = await message.reply_text("<b>Reiniciando...</b>",quote=True)
    time.sleep(1.9)
    qq = await q.edit("<b>Reiniciando sistema, porfavor espere.</b>")
    time.sleep(6.8)
    qqq = await qq.edit("<b>Sistema restaurado con éxito, espere unos segundos en lo que se términa de iniciar ✅</b>")
    print("Sistema restaurado con éxito, espere unos segundos en lo que se términa de iniciar. ✅")
    os.execv(sys.executable, ['python'] + sys.argv)
    