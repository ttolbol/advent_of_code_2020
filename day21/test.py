from unittest import TestCase
from day21.solution import get_ingredients_and_allergens, map_allergens_to_foods, find_allergen_free_ingredients

with open('day21/test_input.txt') as f:
    test_lines = [line for line in f.readlines()]

test_ingredients_and_allergens = [({'mxmxvkd', 'kfcds', 'sqjhc', 'nhms'}, {'dairy', 'fish'}),
                                  ({'trh', 'fvjkl', 'sbzzf', 'mxmxvkd'}, {'dairy'}),
                                  ({'sqjhc', 'fvjkl'}, {'soy'}),
                                  ({'sqjhc', 'mxmxvkd', 'sbzzf'}, {'fish'})]
test_allergen_food_mapping = {'dairy': (0, 1),
                              'fish': (0, 3),
                              'soy': (2, )}


class TestSolution(TestCase):
    def test_get_ingredients_and_allergens(self):
        for i, expected in enumerate(test_ingredients_and_allergens):
            expected_ingredients, expected_allergens = expected
            actual_ingredients, actual_allergens = get_ingredients_and_allergens(test_lines[i])
            self.assertSetEqual(expected_ingredients, actual_ingredients)
            self.assertSetEqual(expected_allergens, actual_allergens)

    def test_map_allergens_to_foods(self):
        allergen_food_mapping = map_allergens_to_foods(test_ingredients_and_allergens)
        self.assertDictEqual(test_allergen_food_mapping, allergen_food_mapping)

    def test_find_allergen_free_ingredients(self):
        result = find_allergen_free_ingredients(test_ingredients_and_allergens, test_allergen_food_mapping)
        expected = {'kfcds', 'nhms', 'sbzzf', 'trh'}
        self.assertSetEqual(expected, result)
