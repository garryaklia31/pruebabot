from pyrogram.types import *

dbre = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('GATES', callback_data='gates'),
        InlineKeyboardButton('TOOLS', callback_data='tools'),
    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),
    ]
])

regex = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(text='Re Gen 🔄', callback_data='gen_pro')
    ]
])

gatbot = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Auth', callback_data='authgate'),
        InlineKeyboardButton('Charged', callback_data='chargedgate'),
        InlineKeyboardButton('Ccn', callback_data='ccngatecomand')
    ],
    [
        InlineKeyboardButton('HOME', callback_data='start')
    ]
])

atrx = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('HOME', callback_data='start'),
    ]
])

toolsbot = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='start'),
        InlineKeyboardButton('NEXT', callback_data='sexo'),
    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),
    ]
])

toolsbot2 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='tools'),
    ],
    [
        InlineKeyboardButton('HOME', callback_data='start'),
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),
    ]
])


atrx2 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='gates'),
    ]
])

chargebotons = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='gates'),
        InlineKeyboardButton('NEXT', callback_data='page2'),
    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),

    ]
])

chargebotons_2 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='chargedgate'),
        InlineKeyboardButton('NEXT', callback_data='page3'),
    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),

    ]
])

chargebotons_3 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='page2'),
        InlineKeyboardButton('NEXT', callback_data='page4'),
    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),

    ]
])

chargebotons_4 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='page3'),
        InlineKeyboardButton('NEXT', callback_data='page5'),
    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),

    ]
])

chargebotons_5 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='page4'),
    ],
    [
        InlineKeyboardButton('HOME', callback_data='gates'),
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),
    ]
])


botadmin = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='gates'),
        InlineKeyboardButton('PAG 2', callback_data='sexito'),
    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),

    ]
])

botadmin2 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='admin'),
        InlineKeyboardButton('PAG 3', callback_data='sexmi'),

    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),
    ]
])

botadmin3 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('BACK', callback_data='sexito'),
        InlineKeyboardButton('PAG 1', callback_data='admin'),

    ],
    [
        InlineKeyboardButton('CLOSE', callback_data='closecmd'),
    ]
])

regen = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Re Gen 🔄', callback_data="GenerateAgain"),
    ],
])

buypremium = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Owner', url="tg://resolve?domain=ShylphietteGreyrat"),
        InlineKeyboardButton('Seller 1', url="tg://resolve?domain=TheMails02"),
    ],
    [
        InlineKeyboardButton('Seller 2', url="tg://resolve?domain=ByCracker2"),
        InlineKeyboardButton('Seller 3', url="tg://resolve?domain=ShylphietteGreyrat"),
    ],
    
    [
        InlineKeyboardButton("Close", callback_data="Finish")
    ]
])

buypremium2 = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Canal', url="https://t.me/+wt6SsKc5vBw1MGNh"),
        InlineKeyboardButton('Chk Free', url="https://t.me/+mTLQsJhV18o0OGIx"),
    ],
    [
        InlineKeyboardButton("Home", callback_data="start")
    ]
])



reopen = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('RE-OPEN', callback_data='start'),
    ]
])
