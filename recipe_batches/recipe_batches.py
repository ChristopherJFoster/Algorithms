#!/usr/bin/python

# We start with batches equal to infinity, and make one pass through ingredients for each key in recipe. If the ingredient is found, then we divide to determine the largest number of batches that could be made if that were the only ingredient (and break the loop for efficiency). If the result is smaller than the current batches value then update batches (this is similar to the stock prices exercise, but tracking the smallest value rather than the largest). If an ingredient is not present (found == False) or yields fewer than one batch, then we know that the ingredients yield 0 batches, and we can return 0 immediately.


def recipe_batches(recipe, ingredients):
    batches = float('inf')
    for rk, rv in recipe.items():
        found = False
        for ik, iv in ingredients.items():
            if ik == rk:
                found = True
                if iv // rv < batches:
                    batches = iv // rv
                    break
        if batches == 0 or found == False:
            return 0
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
