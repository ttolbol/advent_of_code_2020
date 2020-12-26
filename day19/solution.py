import re


def get_rule(in_str):
    if in_str[0] == '"':
        return in_str[1:2]
    else:
        rule = set()
        parts = in_str.split(' | ')
        for part in parts:
            rule.add(tuple(int(num) for num in part.split(' ')))
        return rule


def build_ruleset(rules):
    ruleset = {}
    for rule in rules:
        if rule.strip() == '':
            break
        key, values = rule.split(': ')
        ruleset[int(key)] = get_rule(values)
    return ruleset


def get_message(lines):
    return [line.strip() for line in lines if line[0] == 'a' or line[0] == 'b']


def build_pattern(ruleset, key=0, recursion_depth=0):
    recursion_limit = 20
    if isinstance(ruleset[key], str):
        return list(ruleset[key])[0]

    options = []
    for rule in ruleset[key]:
        if recursion_depth > recursion_limit and key in rule:  # skip recursive rules when past the recursion limit
            continue
        option = ''.join(build_pattern(ruleset, key=key, recursion_depth=recursion_depth+1) for key in rule)
        options.append(option)
    return '(' + '|'.join(options) + ')'


def match_pattern(pattern, message):
    if re.match('^'+pattern+'$', message):
        return True
    return False


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    # part 1
    ruleset = build_ruleset(lines)
    pattern = build_pattern(ruleset)
    messages = get_message(lines)
    print(sum(match_pattern(pattern, msg) for msg in messages))

    # part 2
    ruleset[8] = get_rule('42 | 42 8')
    ruleset[11] = get_rule('42 31 | 42 11 31')
    pattern = build_pattern(ruleset)
    print(sum(match_pattern(pattern, msg) for msg in messages))
