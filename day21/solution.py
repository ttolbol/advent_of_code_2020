from collections import defaultdict


def get_ingredients_and_allergens(in_str):
    ingredients_str, allergens_str = in_str.strip().split(' (contains ')
    return set(ingredients_str.split(' ')), set(allergens_str[:-1].split(', '))


def map_allergens_to_foods(ingredients_allergens):
    allergen_food_mapping = defaultdict(list)

    for i, food in enumerate(ingredients_allergens):
        _, allergens = food
        for allergen in allergens:
            allergen_food_mapping[allergen].append(i)

    for key, val in allergen_food_mapping.items():
        allergen_food_mapping[key] = tuple(val)

    return allergen_food_mapping


def find_allergen_free_ingredients(foods, allergen_food_mapping):
    possible_allergens = set()
    all_ingredients = set()
    # step 1, find all ingredients
    for ingredients, allergens in foods:
        all_ingredients.update(ingredients)

    # step 2, find possible allergens
    for i, food in enumerate(foods):
        ingredients, allergens = food
        test_ingredients = ingredients.copy()
        for allergen in allergens:
            for food_idx in allergen_food_mapping[allergen]:
                if food_idx != i:
                    other_ingredients, _ = foods[food_idx]
                    test_ingredients.intersection_update(other_ingredients)
        possible_allergens.update(test_ingredients)
    return all_ingredients.difference(possible_allergens)


def find_allergens(foods, allergen_free_ingredients, allergen_food_mapping):
    allergen_map = defaultdict(set)
    for ingredients, allergens in foods:
        for allergen in allergens:
            allergen_map[allergen].update(ingredients.difference(allergen_free_ingredients))

    for allergen in allergen_map:
        for food_idx in allergen_food_mapping[allergen]:
            ingredients, _ = foods[food_idx]
            allergen_map[allergen].intersection_update(ingredients)

    # remove all known allergens from other options
    new_known_ingredients = set()
    for allergen, ingredients in allergen_map.items():
        if len(ingredients) == 1:  # this field is known as there is only one option that fits
            new_known_ingredients.update(ingredients)  # add it to the set of known fields
    while new_known_ingredients:  # as long as we have some new information about known allergens then do...
        known_ingredients = new_known_ingredients
        new_known_ingredients = set()
        for ingredients in allergen_map.values():
            if len(ingredients) > 1:  # if there is more than one option then this is not a known field
                ingredients.difference_update(known_ingredients)  # remove any fields that are already known
                if len(ingredients) == 1:  # if this field is now known add it to the set of known fields
                    new_known_ingredients.update(ingredients)

    if all(len(ingredients) == 1 for ingredients in allergen_map.values()):  # all fields should now be known
        return {allergen: ingredients.pop() for allergen, ingredients in allergen_map.items()}


if __name__ == '__main__':
    with open('input.txt') as f:
        foods = [get_ingredients_and_allergens(line) for line in f.readlines()]

    allergen_food_mapping = map_allergens_to_foods(foods)
    safe_ingredients = find_allergen_free_ingredients(foods, allergen_food_mapping)

    # part 1
    appearance_count = sum(sum(ingredient in ingr_list for ingr_list, _ in foods) for ingredient in safe_ingredients)
    print(appearance_count)

    # part 2
    result = find_allergens(foods,
                            safe_ingredients,
                            allergen_food_mapping)
    print(','.join(result[allergen] for allergen in sorted(result.keys())))