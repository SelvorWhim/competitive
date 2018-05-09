def cakes(recipe, available):
    return min(available.get(ing,0)//amount for ing,amount in recipe.items()) # integer division because of the setup and examples. In case of recipe that can be done fractionally, switch // to /
