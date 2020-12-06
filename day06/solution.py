def split_groups(in_str):
    return [group.strip().split('\n') for group in in_str.split('\n\n')]


def get_answers_anyone(group):
    answers = (set(answer) for answer in group)
    return set().union(*answers)


def get_answers_everyone(group):
    answers = (set(answer) for answer in group[1:])
    return set(group[0]).intersection(*answers)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    groups = split_groups(data)
    print(sum(len(get_answers_anyone(group)) for group in groups))
    print(sum(len(get_answers_everyone(group)) for group in groups))
