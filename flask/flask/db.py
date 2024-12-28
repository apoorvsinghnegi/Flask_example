import json

class Database:

    def insert(self,name,email,password): #this file inserts data in our users.json file
        with open('users.json','r') as rf:
            users = json.load(rf) #json file se load karke users mai daal dia

            if email in users:
                return 0
            else:
                users[email] = [name,password]

        with open('users.json','w') as wf:
            json.dump(users,wf,indent=4)
            return 1

    def search(self,email,password):
        with open('users.json','r') as rf:
            users = json.load(rf)

            if email in users:
                if users[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0