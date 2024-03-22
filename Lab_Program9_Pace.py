# Gunner Pace CS101 Week 9
import csv

def load_inventory(file_path):
    with open(file_path, 'r') as file:
        inventory_data = csv.reader(file)
        inventory = {}
        next(inventory_data)
        for entry in inventory_data:
            inventory[f"{entry[0]}_{entry[1]}_{entry[2]}"] = {'Make': entry[0], 'Model': entry[1], 'Year': entry[2], 'Price': entry[3]}
        return inventory

def display_inventory(inventory):
    for key, value in inventory.items():
        print(f"{value['Make']} {value['Model']} ({value['Year']}): ${value['Price']}")

def update_price(inventory, make, model, year, new_price):
    try:
        inventory[f'{make}_{model}_{year}']['Price'] = new_price
        return 'Price successfully updated!'
    except KeyError:
        return 'Vehicle not found in inventory!'

def sort_by_make(inventory):
    return sorted(inventory.values(), key=lambda entry: entry['Make'])

def calculate_price_change(inventory, model):
    filtered = list(filter(

file_path = 'vehicle_inventory.csv'
inventory = load_inventory(file_path)

update_price(inventory, 'Hyundai','Sonata',2024,1000)

display_inventory(inventory)
print(sort_by_make(inventory))
