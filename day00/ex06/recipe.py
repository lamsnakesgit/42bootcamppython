cookbook = { 'sandwich' : { 'ingredients': ['ham','bread', 'cheese', 'tomatoes'], 'meal':'lunch', 'time' : '10'},
        'cake' : {'ingredients': ['flour', 'sugar', 'eggs'], 'meal':'dessert', 'prep_time':'60'},
        'salad' :{'ingredients':['avocado','arugula','tomatoes'], 'meal' : 'lunch', 'prep_time':'15' }}

def print_recipe(cookbook):
    pass
    # print(cookbook)
    print(cookbook['sandwich'])

print_recipe(cookbook)
