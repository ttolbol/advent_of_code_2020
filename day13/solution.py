def argmin(vals):
    minval = vals[0]
    minarg = 0
    for i, val in enumerate(vals[1:]):
        if val < minval:
            minval = val
            minarg = i+1
    return minarg


def departure_time(current_time, bus_id):
    return (1 + current_time // bus_id) * bus_id


def check_time(t, busses):
    for i, bus in busses:
        if (t + i) % bus != 0:
            return False
    return True


def find_time(busses):
    t = 0
    step = 1
    for i, bus in busses:
        while (t + i) % bus != 0:
            t += step
        step *= bus
    return t


if __name__ == '__main__':
    with open('input.txt') as f:
        time, buslist = f.readlines()
    time = int(time)
    buslist = buslist.split(',')

    # part 1
    busses = [int(bus) for bus in buslist if bus != 'x']
    dtimes = [departure_time(time, bus) for bus in busses]
    i = argmin(dtimes)
    result = (dtimes[i] - time) * busses[i]
    print(result)

    # part 2
    busses = [(i, int(bus)) for i, bus in enumerate(buslist) if bus != 'x']
    t = find_time(busses)
    print(t)
