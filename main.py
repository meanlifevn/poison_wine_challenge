import random

from process import generate_data, check_wine, find_poisoned_wine

NUMBER_OF_WINE_BOTTLES = 1000
NUMBER_OF_RATS = 10

if __name__ == '__main__':
    # Generate data if there are not initial data
    # Choose random the index of poisoned wine
    poisoned_wine = random.randint(1, NUMBER_OF_WINE_BOTTLES)
    # Generate data
    wines_list, rats_list = generate_data(NUMBER_OF_WINE_BOTTLES, NUMBER_OF_RATS, poisoned_wine)

    # Take each rat to check wine
    check_wine(wines_list, rats_list)
    # Finding ID poisoned wine by check status of rats
    found_wine, id_wine = find_poisoned_wine(wines_list, rats_list)

    # Show result
    print('The index of poisoned wine is:', poisoned_wine)
    if found_wine != 0:
        # Compare the index of found wine and poisoned wine
        if found_wine == poisoned_wine:
            print('ID found wine is:', id_wine)
            print('The index of found wine is:', found_wine)
        else:
            print('ERRor...')
    else:
        print('Not finding...')

    # Find what wines each rat tried
    # for rat in rats_list:
    #     print(len(rat.get_tried_wlist()))

    # Trying all wine
    # for i in range(1, NUMBER_OF_WINE_BOTTLES + 1):
    #     poisoned_wine = i
    #     wines_list, rats_list = generate_data(NUMBER_OF_WINE_BOTTLES, NUMBER_OF_RATS, poisoned_wine)
    #     check_wine(wines_list, rats_list)
    #     found_wine, index_wines = find_poisoned_wine(wines_list, rats_list)
    #     if poisoned_wine - found_wine != 0:
    #         print('Error')
    #         print(poisoned_wine)
    #         print(found_wine)
    #         break
