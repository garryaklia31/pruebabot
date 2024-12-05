from all.configs._def_main_ import *
import datetime
import pytz

@Techie('link')
async def invite_link(client, message,):
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    permisos = collection.find_one({"_id": message.from_user.id})
    if permisos["role"] == "Owner" or permisos["role"] == "Seller":
        pass
    else:
        return
    ahora = datetime.datetime.now(pytz.timezone('UTC'))
    expireminutes = ahora + datetime.timedelta(minutes=120)
    
    link = await client.create_chat_invite_link(
        chat_id=-4506405469, 
        member_limit=1, 
        expire_date=expireminutes  
    )
    
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton('𝙈𝙚𝙢𝙗𝙚𝙧𝙨 𝙋𝙧𝙚𝙢𝙞𝙪𝙢', url=link.invite_link)]])
    
    textpremium = f"""<b>━━━━━━━━「ELAINA」━━━━━━━━
<i>Elaina</i> ⇨ <code>Administration! </code>👁
━━━━━━━━「Group」━━━━━━━━
Message ⇨ Premium User Group
━━━━━━━━「ELAINA」━━━━━━━━
<i>Create By</i> ⇨ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{permisos['role']}</code>]</b>
"""

    await client.send_message(
        chat_id=message.chat.id,
        text=textpremium,
        reply_markup=keyboard
    )