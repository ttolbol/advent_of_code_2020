import re


def validate_year(value, min_year, max_year):
    match = re.match(r'\d{4}$', value)
    if not match:
        return False
    return min_year <= int(value) <= max_year


def validate_birth_year(value):
    return validate_year(value, 1920, 2002)


def validate_issue_year(value):
    return validate_year(value, 2010, 2020)


def validate_expiry_year(value):
    return validate_year(value, 2020, 2030)


def validate_height(value):
    match = re.match(r'(\d+)(in|cm)$', value)
    if not match:
        return False
    height, unit = match.groups()
    if unit == 'cm':
        return 150 <= int(height) <= 193
    elif unit == 'in':
        return 59 <= int(height) <= 76
    return False


def validate_haircolor(value):
    return bool(re.match(r'#[0-9a-f]{6}$', value))


def validate_eyecolor(value):
    valid_eyecolors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    return value in valid_eyecolors


def validate_passport_id(value):
    return bool(re.match(r'\d{9}$', value))


validation_functions = {
    'byr': validate_birth_year,
    'iyr': validate_issue_year,
    'eyr': validate_expiry_year,
    'hgt': validate_height,
    'hcl': validate_haircolor,
    'ecl': validate_eyecolor,
    'pid': validate_passport_id
}
expected_fields = set(validation_functions.keys())


def validate_field(value, field):
    return validation_functions[field](value)


def extract_value(passport, field):
    pattern = field + r':([#\w]+)'
    return re.search(pattern, passport).groups()[0]


def validate_passport(passport, strict=False):
    pattern = r'[a-z]{3}:'
    fields = {field[:3] for field in re.findall(pattern, passport)}
    for field in expected_fields:
        if field not in fields:
            return False

    if strict:
        for field in expected_fields:
            value = extract_value(passport, field)
            if not validate_field(value, field):
                return False
    return True


with open('input.txt') as f:
    data = f.read()
passports = data.split('\n\n')
print(sum(validate_passport(passport, False) for passport in passports))
print(sum(validate_passport(passport, True) for passport in passports))
