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


def build_pattern(ruleset, key=0):
    if isinstance(ruleset[key], str):
        return list(ruleset[key])[0]

    pattern = '|'.join(''.join(build_pattern(ruleset, key=key) for key in rule) for rule in ruleset[key])
    return '(' + pattern + ')'


def match_pattern(pattern, message):
    if re.match('^'+pattern+'$', message):
        return True
    return False


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    # part 1
    pattern = build_pattern(build_ruleset(lines))
    messages = get_message(lines)
    print(sum(match_pattern(pattern, msg) for msg in messages))
