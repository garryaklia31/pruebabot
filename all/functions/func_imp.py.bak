# YA QUEDO

import time
import random
import string
import re
import aiohttp
import asyncio
from aiohttp_socks.connector import ProxyConnector
import urllib.parse
import base64
import json


def xor(data, key):
    return bytes([datum ^ key for datum in data])


def auto_ext(checkout:str):

    urltodecode = checkout.split('#')[1]
    basetodecode = urllib.parse.unquote(urltodecode)
    xortodecode = base64.b64decode(basetodecode).decode('utf-8')
    pk = (xor(xortodecode.encode('utf-8'), 5))
    cs = checkout.split('#')[0].split('/')[-1]

    cadena_datos = pk.decode('utf-8')
    datos_decodificados = json.loads(cadena_datos)
    api_key = datos_decodificados['apiKey']
    return api_key,cs


def find_between(data: str, first: str, last: str) -> str:
    # Busca una subcadena dentro de una cadena, dados dos marcadores
    if not isinstance(data, str):
        raise TypeError("El primer argumento debe ser una cadena de texto.")
    
    try:
        start_index = data.index(first) + len(first)
        end_index = data.index(last, start_index)
        return data[start_index:end_index]
    except ValueError:
        return ''


def get_time_taken(val):
    current_time = time.time()
    time_taken = current_time - val
    return str(time_taken)[:4]


def find_between_str( data, first, last ):
    try:
        start = data.index( first ) + len( first )
        end = data.index( last, start )
        return data[start:end]
    except ValueError:
        return None



async def make_order():

    async with aiohttp.ClientSession() as session:

        API_KEY = 'bd3af3218920bd82cbe93f7bc6623853'

        req = await session.get(url=f'https://juicysms.com/api/makeorder?key={API_KEY}&serviceId=5&country=UK')

        x = await req.text()
        print(x)

        if 'ORDER_ID_' in x:
            order_id = find_between_str(x,'ORDER_ID_','_NUMBER_')
            numero = x[len(f'ORDER_ID_{order_id}_NUMBER_')::]
        elif 'NO_PHONE_AVAILABLE' in x: order_id = None
        elif 'ORDER_ALREADY_OPEN_' in x: order_id = None
        elif 'NO_BALANCE' in x: order_id = None
        else: order_id = None

        if order_id != None:
            return order_id,numero
        else: return



async def get_sms(order_id):

    async with aiohttp.ClientSession() as session:

        tiempo = time.time()

        orderid = str(order_id)

        API_KEY = 'bd3af3218920bd82cbe93f7bc6623853'

        while time.time() - tiempo < 200:

            req = await session.get(url=f'https://juicysms.com/api/getsms?key={API_KEY}&orderId={orderid}')

            x = await req.text()

            if 'SUCCESS' in x: return x

            await asyncio.sleep(1)

            print(x)

        return None




def get_email(): 
    generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))) + '@gmail.com'
    return generated_email.lower()




def expresion_url(url):
    pattern = r'https?://[^/]+\.[^/]+'

    match = re.search(pattern, url)
    if match:
        return match.group(0)
    else:
        None



def get_random_string(length):
    # Genera una cadena de texto aleatoria.
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


