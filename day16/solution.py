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
    for ticket in tickets:
        for field_i, num in enumerate(ticket):
            for field in list(ticket_fields[field_i]):
                rule = ruleset[field]
                if not check_field(num, rule):
                    ticket_fields[field_i].remove(field)
            if len(ticket_fields[field_i]) == 1:
                for i, other_field in enumerate(ticket_fields):
                    if i != field_i:
                        other_field.difference_update(ticket_fields[field_i])
        if all(len(ticket_field) == 1 for ticket_field in ticket_fields):
            return [ticket_field.pop() for ticket_field in ticket_fields]
    print(ticket_fields)
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