import json

class Database:
    def get_users(self):
        try:
            with open('db.json', 'r') as f:
                return json.load(f)
        except:
            with open('db.json', 'w') as f:
                json.dump({}, f)
                return {}
    
    def get_user_phone(self, tg_id):
        users = self.get_users()
        return users.get(str(tg_id), None)
    
    def save_user(self, tg_id, username, first_name, last_name, phone):
        users = self.get_users()
        users[str(tg_id)] = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
        }
        
        with open('db.json', 'w') as f:
            json.dump(users, f, indent=4)
        
        

db = Database()