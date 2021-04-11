from flask import Flask
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)
# userss = {
#     '1': {
#         'id': '1',
#         'username': 'Pe3oH',
#         'email': 'Pe3oH227@mail.ru',
#         'department': 'ART-Tanks',
#         'age': '26'
#     },
#     '2': {
#         'id': '2',
#         'username': 'yeux',
#         'email': 'pail-max@mail.ru',
#         'department': 'ART-Tanks',
#         'age': '24'
#     },
#     '3': {
#         'id': '3',
#         'username': 'Tanya_5',
#         'email': 'pikriper@gmail.com',
#         'department': 'ART-Tanks',
#         'age': '25'
#     },
#     '4': {
#         'id': '4',
#         'username': 'Steelhanter',
#         'email': 'urets@yandex.ru',
#         'department': 'ART-Tanks',
#         'age': '26'
#     }
# }

#
class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code



# class Users(Resource):
#     # methods go here
#     pass

# class Users(Resource):
#     def get(self):
#         return {'data': userss}, 200

api.add_resource(Users, '/users')
if __name__ == '__main__':
    app.run()  # run our Flask app

