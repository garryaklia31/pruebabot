from pyrogram import *
from pyrogram.errors import RPCError, BadRequest, Forbidden
from pyrogram.types import *
from colorama import *
from faker import Faker
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt
from aiohttp_socks.connector import ProxyConnector
from datetime import datetime, timedelta, date
from datetime import *
import logging
import aiohttp
import time
import datetime
import pytz
import string
import random
import urllib3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import ssl
import certifi
import csv
import uuid
import threading
import time
import asyncio
import json
import os
import aiohttp_proxy
import requests
import re
from random import *
from pymongo.errors import *
from all.configs.botones import *
from all.configs._def_main_ import *
from all.configs.plantillas import *
from all.proxis.array_proxies import *
from all.functions.func_imp import *
from all.functions.func_bin import get_bin_info
from all.functions.func_gen import cc_gen
from all.functions.func_gennew import GeneatedCC
from all.textos import *
from time import strftime, gmtime
from mongoDB import *

PHOTO = 'https://images5.alphacoders.com/111/thumb-1920-1115214.jpg'
LOG_CHAT_ID = -1002416011069
ARCHIVO_DATOS = 'all\json\datos.json'


fake = Faker()
nombre = fake.first_name().lower()
last = fake.last_name().lower()
loca = fake.street_name().lower()
city = fake.city().lower()
state = fake.state().lower()
country = fake.country().lower()
postcode = fake.postcode()
phone = fake.phone_number()


def Techie(bit):
    nix = Client.on_message(filters.command(
        bit, ['.', '!', '/', ',', '-', '$', '%', '#'], case_sensitive=False) & filters.text)
    return nix


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + "\nMain : Dev By ( Techie )\n" + Style.RESET_ALL)

async def registrar_usuario(message):
    mydict = {
        "_id": message.from_user.id,
        "id": message.from_user.id,
        "username": message.from_user.username,
        "plan": "Free User",
        "apodo": "Free User",
        "role": "User",
        "status": "Libre",
        "gates_usage": 0,
        "antispam": 60,
        "credits": 0,
        "time_user": 0,
        "alerts": 0,
        "since": datetime.now(),
        "key": 'None',
        "tareas_en_proceso": 0,
    }
    collection.insert_one(mydict)

    caption = f"""<b>Registro Completo 🟩</b>"""

    return caption



def cargar_datos_json():
    with open('all/admin/keys.json', 'r') as f:
        datos = json.load(f)
    return datos


def save_key_info(key_info):
    with open('all/admin/keys.json', 'r') as f:
        data = json.load(f)
    data.append(key_info)
    with open('all/admin/keys.json', 'w') as f:
        json.dump(data, f)


def luhn_algorithm(card_num):
    card_num = card_num.replace(' ', '').replace('-', '')
    if len(card_num) < 2:
        return False
    digits = [int(d) for d in card_num]

    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] = digits[i] - 9
    total = sum(digits)
    return total % 10 == 0


binsbanned = 'all\\json\\bannedbins.json'


def load_banned_bins():
    binsbanned = 'all\\json\\bannedbins.json'
    try:
        with open(binsbanned, 'r') as f:
            banned_bins = json.load(f)
    except FileNotFoundError:
        banned_bins = []
    return banned_bins


def parseX(data, start, end):
    try:
        star = data.index(start) + len(start)
        last = data.index(end, star)
        return data[star:last]

    except ValueError:
        return "None"


def braintree_generate_correlation_id():
    return str(uuid.uuid4())


def braintree_generate_uuid():
    return str(uuid.uuid4())

def generate_guid():
    return str(uuid.uuid4())

def generate_muid():
    return str(uuid.uuid4())

def generate_sid():
    return str(uuid.uuid4())

guid = generate_guid()
muid = generate_muid()
sid = generate_sid()


def get_email():
    generated_email = str(''.join(random.choices(
        string.ascii_uppercase + string.digits, k=8))) + '@gmail.com'
    return generated_email.capitalize()


def cargar_datos():
    if not os.path.isfile(ARCHIVO_DATOS) or os.path.getsize(ARCHIVO_DATOS) == 0:
        datos = {'comandos_habilitados': {}}
        with open(ARCHIVO_DATOS, 'w') as f:
            json.dump(datos, f)

    with open(ARCHIVO_DATOS, 'r') as f:
        try:
            datos = json.load(f)
        except json.decoder.JSONDecodeError:
            datos = {'comandos_habilitados': {}}
            with open(ARCHIVO_DATOS, 'w') as f:
                json.dump(datos, f)

    comandos_habilitados = datos.get('comandos_habilitados', {})
    return comandos_habilitados


def guardar_datos(comandos_habilitados):
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump({'comandos_habilitados': comandos_habilitados}, f)

def getCards(text=None):
    if not text or type(text) != str:
        return []

    digits = re.findall(r"\d+", text)

    if not digits:
        return []

    cards = []

    cc = None
    mm = None
    yy = None
    cvv = None

    curr = datetime.now()
    curr_mm = curr.month
    curr_yy = str(curr.year)[-2:]

    next_yy = str(int(curr_yy) + 10)

    mm_regex = "([1-9]|0[1-9]|1[012])"
    yy_regex = "(20(" + curr_yy[:1] + "[" + curr_yy[1:] + "-9]|" + next_yy[:1] + "[0-" + next_yy[1:] + \
        "])|(" + curr_yy[:1] + "[" + curr_yy[1:] + "-9]|" + \
        next_yy[:1] + "[0-" + next_yy[1:] + "]))"

    for digit in digits:
        if re.findall(r"^(3\d{14}|[456]\d{15})$", digit):
            cc = digit

            mm = None
            yy = None
            cvv = None

            length = 4 if cc[0] == "3" else 3
        elif cc:
            if not mm and re.findall(f"^{mm_regex}$", digit):
                mm = digit
            elif not yy and re.findall(f"^{yy_regex}$", digit):
                yy = digit
            elif not mm and not yy and (re.findall(f"^{mm_regex}{yy_regex}$", digit) or re.findall(f"^{yy_regex}{mm_regex}$", digit)):
                regex = f"{yy_regex}$" if re.findall(
                    f"^{mm_regex}{yy_regex}$", digit) else f"^{yy_regex}"

                yy = re.findall(regex, digit)[0][0]

                mm = re.sub(regex, '', digit)
            elif not cvv and len(digit) == length:
                cvv = digit

        if None in [cc, mm, yy, cvv] or cc in str(cards):
            continue

        mm = f"0{mm}"[-2:]
        yy = f"20{yy}"[-4:]

        card = [cc, mm, yy, cvv]

        if curr.year == int(yy) and int(curr.month) > int(mm):
            card.append('expired')

        cards.append(card)

        cc = None

    return cards

def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False


huso_horario_mexico = timezone(timedelta(hours=-6))

hora_utc = datetime.now(timezone.utc)

hora_mexico = hora_utc.astimezone(huso_horario_mexico)

hora_en_mexico = hora_mexico.strftime("%H:%M:%S")