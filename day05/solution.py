def decode(input_str):
    row = int(input_str[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(input_str[7:].replace('L', '0').replace('R', '1'), 2)
    return row, col


def seat_id(row, col):
    return row * 8 + col


with open('input.txt') as f:
    seats = f.readlines()

seat_ids = [seat_id(*decode(seat)) for seat in seats]
print(max(seat_ids))
seat_ids.sort()
for i, seat_id in enumerate(seat_ids):
    if i > 0 and seat_id == seat_ids[i-1] + 2:
        print(seat_id - 1)
        break
