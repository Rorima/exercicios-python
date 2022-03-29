"""
Use encapsulation
"""


class User:

    __data = []

    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password
        User.__data.append(f'Name: {self.__user_name}. Password: {self.__password}')
    