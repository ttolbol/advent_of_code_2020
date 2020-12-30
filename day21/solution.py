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


if __name__ == '__main__':
    with open('input.txt') as f:
        foods = [get_ingredients_and_allergens(line) for line in f.readlines()]

    allergen_food_mapping = map_allergens_to_foods(foods)
    ingredients = find_allergen_free_ingredients(foods, allergen_food_mapping)

    # part 1
    appearance_count = sum(sum(ingredient in ingr_list for ingr_list, _ in foods) for ingredient in ingredients)
    print(appearance_count)
