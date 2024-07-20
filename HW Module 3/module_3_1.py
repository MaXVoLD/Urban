calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string


def is_contains(string: str, list_to_search: list):
    count_calls()
    string = string.lower()
    list_to_search = (str(list_to_search))
    list_to_search = list_to_search.lower()
    if string in list_to_search:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
