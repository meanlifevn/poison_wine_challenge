import random

from rat import Rat
from wine import Wine


def generate_data(n_wine_bottles, n_rats, id_poisoned_wine):
    w_list = []
    r_list = []
    id_list = list(range(1, n_wine_bottles + 1))
    for i in range(n_wine_bottles):
        id = random.choice(id_list)
        id_list.remove(id)
        if i == id_poisoned_wine - 1:
            w_list.append(Wine(id, True))
        else:
            w_list.append(Wine(id, False))
    for i in range(n_rats):
        r_list.append(Rat(i, False, []))
    return w_list, r_list


def get_binary_id_wine(index_wine):
    string_binary = ''
    decimal_number = index_wine
    while decimal_number:
        temp = decimal_number % 2
        string_binary += str(temp)
        decimal_number = decimal_number // 2
    return [pos for pos, char in enumerate(string_binary) if char == '1']


def check_wine(w_list, r_list):
    for i, wine in enumerate(w_list):
        list_id_mouses = get_binary_id_wine(i + 1)
        for rat in r_list:
            if rat.get_id() in list_id_mouses:
                rat.tried_wines.append(wine.get_id())
                if wine.get_status():
                    setattr(rat, 'is_poisoned', True)
    return -1


def find_poisoned_wine(w_list, r_list):
    result_wine = 0
    id_wine = 0
    for rat in r_list:
        if rat.get_status():
            # print(rat.get_id())
            result_wine += pow(2, rat.get_id())

    for i, wine in enumerate(w_list):
        if result_wine == i + 1:
            id_wine = wine.get_id()

    return result_wine, id_wine
