#https://www.kaggle.com/datasets/sanjanchaudhari/places-dataset

import csv

def load_places_data(filename):
    data = {
        "States": {},
        "HousingCost": {},
        "Climate": {}
    }

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                city_state = row[0].strip('"')
                climate = int(row[1])
                housing_cost = float(row[2])

                city, state = city_state.rsplit(',', 1)

                if state not in data["States"]:
                    data["States"][state] = []
                data["States"][state].append(city)

                data["HousingCost"][city_state] = housing_cost
                data["Climate"][city_state] = climate
    except Exception as e:
        print(f"Error loading file: {e}")

    return data

def get_valid_input(prompt, valid_options):
    user_input = input(prompt).strip()
    if user_input not in valid_options:
        raise ValueError(f"Invalid input! Choose from {valid_options}")
    return user_input

def compare_places(category, place1, place2, places_data):
    if category == "HousingCost":
        cost1 = places_data["HousingCost"].get(place1)
        cost2 = places_data["HousingCost"].get(place2)
        difference = abs(cost1 - cost2)
        return f"The housing cost difference between {place1} and {place2} is ${difference:.2f}."

    elif category == "Climate":
        climate1 = places_data["Climate"].get(place1)
        climate2 = places_data["Climate"].get(place2)
        if climate1 == climate2:
            return f"{place1} and {place2} have the same climate: {climate1}."
        else:
            return f"{place1} has a climate of {climate1}, while {place2} has a climate of {climate2}."

def main():
    places_data = load_places_data('places.txt')

    try:
        available_states = list(places_data["States"].keys())
        state = get_valid_input(f"Enter a state {available_states}: ", available_states)

        available_cities = places_data["States"][state]
        city1 = get_valid_input(f"Enter a city in {state} {available_cities}: ", available_cities)
        city2 = get_valid_input(f"Enter another city in {state} {available_cities}: ", available_cities)

        category = get_valid_input("Select (HousingCost/Climate): ", ["HousingCost", "Climate"])

        city_state1 = f"{city1},{state}"
        city_state2 = f"{city2},{state}"
        comparison_result = compare_places(category, city_state1, city_state2, places_data)
        print(comparison_result)

    except ValueError as e:
        print(e)
        print("Try again.")

    restart = get_valid_input("Would you like to try again? (yes/no): ", ["yes", "no"])
    if restart == "yes":
        main()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
