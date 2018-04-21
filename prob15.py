def num_ways_from_loc(curr_loc, cache):
    x, y = curr_loc

    # Invalid location
    if x > 0 or y < 0:
        return 0
    # Hit the goal!
    if x == 0 and y == 0:
        return 1
    else:
        next_locs = (x+1, y), (x, y-1)
        total_from_curr = 0

        for next_loc in next_locs:
            if next_loc in cache:
                total_from_curr += cache[next_loc]
            else:
                total_from_curr += num_ways_from_loc(next_loc, cache)

        cache[curr_loc] = total_from_curr
        return total_from_curr

def init_lattice_path_finder(grid_size):
    start_x, start_y = -grid_size, grid_size

    return num_ways_from_loc((start_x, start_y), dict())

print(init_lattice_path_finder(20))