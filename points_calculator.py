# The official F1 points system; used as a reference
points_table = {
    '1': 25,
    '2': 18,
    '3': 15,
    '4': 12,
    '5': 10,
    '6': 8,
    '7': 6,
    '8': 4,
    '9': 2,
    '10': 1
}


def calculate_points(total_positions: int):
    new_points_table = {}
    
    # All positions beyond 10th are "residual positions", we add '0' points to them later
    residue = None
    if total_positions > 10:
        residue = total_positions - 10
        total_positions = 10
        print('Residue found;', residue)
    
    # Determining the points for the first position based on the total number of positons here
    leader_points = points_table[str(10 - (total_positions - 1))]

    # Determining the points for all the non-residual positions and addimg them to the table
    for position in range(1, total_positions + 1):
        ratio = points_table['1'] / points_table[str(position)]
        calculated_points = round(leader_points / ratio)
        
        new_points_table[str(position)] = calculated_points

    # Taking care of the residual positions; assigning 0 points to them and adding them to the table
    if residue is not None:
        for residual_position_index in range(1, residue + 1):
            residual_position = residual_position_index + 10

            new_points_table[str(residual_position)] = 0

    # The table is good to be dispatched!
    return new_points_table
