from enum import Enum


from enum import Enum
from unicodedata import decomposition

class Who_Are_You(Enum):
    CLIENT = 1
    OFICIAL =2

class Clients_type(Enum):
    REGULAR = 1
    PREMIUM = 2
    VIP = 3

class Clients_action(Enum):
    ATTRACTION = 1
    DEPOSIT = 2
    BALANCECHECK = 3
    PRINT = 4
    EXIT = 5

class Oficail_type(Enum):
    OFICIAL1 = 1
    OFICIAL2 = 2
    OFICIAL3 =3

class Oficial_actions(Enum):
    ADD_NEW_CLIENT = 1
    SEACH_CLIENT = 2
    REMOVE_CLIENT = 3
    PRINT = 4
    EXIT = 5

def menu():
    print("Welcome Who Are You?")
    for action in User_Actions
        print(f'{action.value} - {action.name})')
    return int( input("select action"))
    
