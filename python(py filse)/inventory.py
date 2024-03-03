# Inventory dictionary
hw_inventory={
    "Tomato": {"price": 10, "Qty": 2, "Unit": 'kg'},
    "Onion": {"price": 20, "Qty": 3000, "Unit": 'g'},
    "Rawa":{"price":30,"Qty":2000,"Unit":'g'}
}

# Menu dictionary
hw_menu = {
    "Pizza": {
        "ingredients": ("Tomato", "Onion"),
        "quantities": (300, 2),
        "units": ("g", "kg")
    },
    "Burger": {
        "ingredients": ("Lettuce", "Onion"),
        "quantities": (300, 2),
        "units": ("g", "kg")
    },
    "Pani puri": {
        "ingredients": ("Potato", "Rawa"),
        "quantities": (300, 2),
        "units": ("g", "kg")
    },
}
#item_name = "Burger"



a = input("Enter recipe name:")
def check_in_inventory (item_name):

    ingredients = hw_menu[item_name]["ingredients"]
    quantities = hw_menu[item_name]["quantities"]
    units = hw_menu[item_name]["units"]
    test = ingredients
    doable = False
    for element in ingredients:
        indx = -1
        if element in hw_inventory:
            tmp = 0
            for i in test:
                if i == element:
                    indx=tmp
                else:
                    tmp+=1
            if indx==-1:
                print("not found")
                doable = False
                break
            else:
                print(f'Founded at {indx}')
                relevant_menu_qty= quantities[indx]
                relevant_inventory_qty= hw_inventory[ingredients[indx]]["Qty"]
                if hw_inventory[ingredients[indx]]["Unit"] == 'kg':
                    relevant_menu_qty *= 1000
                if ingredients[indx] not in hw_inventory:
                    print(f"{item_name} cannot be made: Missing {ingredients[0]}.")
                    doable=False
                    break
                if hw_inventory[ingredients[indx]]["Unit"] == 'kg':
                    relevant_inventory_qty *= 1000
                if relevant_inventory_qty<relevant_menu_qty:
                    print(f"{item_name} cannot be made: Insufficient quantity of {ingredients[0]}.")
                    doable=False 
                    break
                else:
                    doable = True
        else:
            print(f"{ingredients[0]} can not be found in inventory")
            doable = False
            break
            
    if doable == True:
        #print("DOable") 
        doable = 'Yes' 
        return doable
    else:
       # print("Not Doable")  
        doable = 'No'
        return doable 

check_in_inventory(a)
            
