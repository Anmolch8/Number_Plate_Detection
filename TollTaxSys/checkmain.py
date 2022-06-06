import json
from json import JSONDecodeError
def check_loginstatus():
    with open('D:\\final toll tax system\\TollTaxSys\\access.json') as file:
        status=json.load(file)
    try:

        return status['logged_in'],status['id']
    except JSONDecodeError:
        print('Response content is not in the json format')
def change_loginstatus(status,id):
    with open ('access.json','w') as file:
        json.dump({"logged_in":status,'id':id},file)
   