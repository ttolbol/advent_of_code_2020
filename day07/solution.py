import re


def extract_bag_color(in_str):
    return re.match(r'\d* ?(\w+ \w+)', in_str).group(1)


def extract_bag_color_and_number(in_str):
    match = re.match(r'(\d+) (\w+ \w+)|(\w+ \w+)', in_str)
    number, color, no_other = match.groups()
    if no_other:
        return 0, no_other
    return int(number), color


def get_rule(line):
    key, bags = line.split(' bags contain ')
    parts = bags.strip().split(', ')
    value = set(extract_bag_color_and_number(part) for part in parts)
    value.discard((0, 'no other'))
    return key, value


def get_rules(in_str):
    lines = [line for line in in_str.split('\n') if line]
    return dict(get_rule(line) for line in lines)


def invert_rules(rules):
    inverted = {}
    for key, val in rules.items():
        for _, bag_color in val:
            if bag_color in inverted:
                inverted[bag_color].add(key)
            else:
                inverted[bag_color] = {key}
    return inverted


def get_possible_bag_colors_containing_bag(inv_rules, bag):
    bag_colors = set()
    if not isinstance(bag, set):
        bag = {bag}
    for bag_color in bag:
        if bag_color in inv_rules:
            parents = inv_rules[bag_color]
            bag_colors.update(parents)
            bag_colors.update(get_possible_bag_colors_containing_bag(inv_rules, parents))
    return bag_colors


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    rules = get_rules(data)
    inverted_rules = invert_rules(rules)
    part1 = get_possible_bag_colors_containing_bag(inverted_rules, 'shiny gold')
    print(len(part1))
