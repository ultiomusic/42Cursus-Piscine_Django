import sys

def get_key_from_value(dict: dict, value):
    for key, item in dict.items():
        if item == value:
            return key
    return None

def print_states(value: str):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    value = get_key_from_value(capital_cities, value)
    if not value:
        print("Unknown capital city")
        return
    print(get_key_from_value(states, value))

def main():
    if len(sys.argv) == 2:
        print_states(sys.argv[1])

if __name__ == '__main__':
    main()