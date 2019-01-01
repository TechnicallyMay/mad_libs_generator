import requests
import json
import db


database = db.WordDatabase()
database.add_word("blood", ["noun"])
database.close_database()


# app_id = '7c137a51'
# app_key = 'c9780347b3bfd82980f60867a2e92882'
# language = 'en'
# word_id = 'blood'
# url = 'https://od-api.oxforddictionaries.com:443/api/v1/inflections/' + language + '/' + word_id.lower()
#5
# r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
#
# print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))
