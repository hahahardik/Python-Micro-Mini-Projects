import json


def get_stored_num():
    """Get the stored number or ask for it."""

    filename = 'fav_number_2.json'
    try:
        with open(filename) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num


def print_fav_num():
    """Print the favourite number."""

    num = get_stored_num()
    if num:
        print(f"I know your favourite number. It's {num}.")
    else:
        number = input('What is your favourite number? ')

        filename = 'fav_number_2.json'
        with open(filename, 'w') as f:
            json.dump(number, f)
            print('Yes we got that!')


print_fav_num()
