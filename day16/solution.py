import re


def isnum(numstr):
    try:
        int(numstr)
    except ValueError:
        return False
    return True


def extract_tickets(lines):
    ticket_strings = [line for line in lines if line and isnum(line[0])]  # get all lines starting with a digit
    tickets = [[int(num) for num in ticket.split(',')] for ticket in ticket_strings]
    return tickets


def extract_rule(line):
    field, min1, max1, min2, max2 = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
    return field, int(min1), int(max1), int(min2), int(max2)


def build_ruleset(lines):
    ruleset = {}
    for line in lines:
        if not line.strip():
            break
        field, min1, max1, min2, max2 = extract_rule(line)
        ruleset[field] = (min1, max1, min2, max2)
    return ruleset


def check_field(number, rule):
    min1, max1, min2, max2 = rule
    if min1 <= number <= max1 or min2 <= number <= max2:
        return True
    return False


def validate_number(number, ruleset):
    return any(check_field(number, rule) for rule in ruleset.values())


def find_ticket_scanning_error_rate(tickets, ruleset):
    tser = 0
    for ticket in tickets:
        for number in ticket:
            if not validate_number(number, ruleset):
                tser += number
    return tser


def get_valid_tickets(tickets, ruleset):
    valid_tickets = []
    for ticket in tickets:
        valid = True
        for number in ticket:
            if not validate_number(number, ruleset):
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)
    return valid_tickets


def find_ticket_fields(tickets, ruleset):
    ticket_fields = [set(ruleset.keys()) for _ in tickets[0]]
    # first pass, process of elimination
    for ticket in tickets:
        for field_i, num in enumerate(ticket):
            for field in list(ticket_fields[field_i]):
                rule = ruleset[field]
                if not check_field(num, rule):
                    # print(f'removing "{field}" from field {field_i} because {num} is not in range {rule[0]}-{rule[1]} or {rule[2]}-{rule[3]}')
                    ticket_fields[field_i].remove(field)

    # second pass, remove all known fields from other options
    new_known_fields = set()
    for field_set in ticket_fields:
        if len(field_set) == 1:  # this field is known as there is only one option that fits
            new_known_fields.update(field_set)  # add it to the set of known fields
    while new_known_fields:  # as long as we have some new information about known fields we do...
        known_fields = new_known_fields
        new_known_fields = set()
        for field_set in ticket_fields:
            if len(field_set) > 1:  # if there is more than one option then this is not a known field
                field_set.difference_update(known_fields)  # remove any fields that are already known
                if len(field_set) == 1:  # if this field is now known add it to the set of known fields
                    new_known_fields.update(field_set)

    if all(len(field_set) == 1 for field_set in ticket_fields):  # all fields should now be known
        return [field_set.pop() for field_set in ticket_fields]  # so we can convert the sets to single values

    raise ValueError('Failed to find distinct sequence of fields.')


def field_product(ticket, fields, startswith='departure'):
    product = 1
    for i, num in enumerate(ticket):
        if fields[i].startswith(startswith):
            product *= num
    return product


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line for line in f.readlines()]

    ruleset = build_ruleset(lines)
    tickets = extract_tickets(lines)

    # part 1
    print(find_ticket_scanning_error_rate(tickets, ruleset))

    # part 2
    your_ticket = tickets[0]
    valid_tickets = get_valid_tickets(tickets, ruleset)
    fields = find_ticket_fields(valid_tickets, ruleset)
    print(field_product(your_ticket, fields))
