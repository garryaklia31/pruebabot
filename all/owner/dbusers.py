from all.configs._def_main_ import *

@Techie('userp')
async def userinfocmd(_, message):
    permisos = collection.find_one({"_id": message.from_user.id})
    if permisos['role'] == "Owner":
        premium_users = collection.find({"$or": [{"plan": "Premium"}, {"role": "Seller"}, {"role": "Owner"}]})

        with open('premium_users.csv', mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['ID', 'Username', 'Plan', 'Status', 'Key']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for user in premium_users:
                writer.writerow({'ID': user['_id'], 
                                 'Username': user.get('username', ''), 
                                 'Plan': user.get('plan', ''), 
                                 'Status': user.get('status', ''), 
                                 'Key': user.get('key', '')})

        await message.reply_document(document='premium_users.csv', quote=True)
        
        os.remove('premium_users.csv')
    else:
        return
