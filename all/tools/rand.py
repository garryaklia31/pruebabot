import time
from faker import Faker
import pycountry
from all.configs._def_main_ import *


@Techie('rand')
async def generate_fake_info(client, message):
    tiempoinicio = time.perf_counter()
    input_data = message.text.split()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    usuario = collection.find_one({"_id": message.from_user.id})
    if len(input_data) != 2:
        return await message.reply("<b>⚠️ Estás usando el comando incorrectamente, utiliza <code>/rand pais</code>.</b>")

    country_name = input_data[1].lower()

    try:
        country = pycountry.countries.lookup(country_name)
        country_code = country.alpha_2.lower()
        english_country_name = country.name
    except LookupError:
        return await message.reply("<b>⚠️ El país proporcionado no estpa registrado en mi base de datos.</b>")

  
    faker = Faker()


    fake_name = faker.name()
    fake_address = faker.address()
    fake_phone_number = faker.phone_number()
    fake_postal_code = faker.postcode()

    message_text = f"""<b><b>━━━━━「ELAINA」━━━━━</b>
<b><i> Random Address Generator</i></b>
━━━━━「DATA」━━━━━
<b>País ➣</b> <code>{english_country_name}</code>
<b>Nombre ➣</b> <code>{fake_name}</code>
<b>Dirección ➣</b> <code>{fake_address}</code>
<b>Número de Teléfono ➣</b> <code>{fake_phone_number}</code>
<b>Código Postal ➣</b> </code>{fake_postal_code}</code>
━━━━━「ELAINA」━━━━━
Tiempo de ejecución ➣ {time.perf_counter() - tiempoinicio:.2f} segundos
<i>Checked by</i> ➣ <a href="tg://user?id={ID}">{FIRST}</a> [<code>{usuario["apodo"]}</code>]
━━━━━「ELAINA」━━━━━</b>"""

    await message.reply(message_text)
