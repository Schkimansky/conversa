#
# Usefull Functions
#

def get_magnitude(From, To, Classification, Magnitudes):
    # Index distance is the distance (in integer) from (From) to (To) values inside the ORDER list
    index_distance = [Classification.index(From), Classification.index(To)]

    if index_distance[0] > index_distance[1]: # Make sure the value doesnt become something like (2, 1) instead of the usual (1, 2) since (2, 1) doesnt slice a array properly
        index_distance = [index_distance[1], index_distance[0]]

    magnitude = 1

    for value_magnitude in Magnitudes[index_distance[0]:index_distance[1]]:
        magnitude *= value_magnitude

    return magnitude

def multiply_by_magnitude(order, magnitudes, Value, From, To):
    # Check if the user is trying to convert a large unit to a small unit or vice versa
    direction = order.index(To) - order.index(From)

    if direction == 0:
        # User is trying to convert ms to ms or seconds to seconds and vice versa
        return Value # Value doesnt change since from and to are the same

    # Magnitude is the value we have to multiply/divide the value with so that we will get the desired value
    elif direction < 0:
        magnitude = get_magnitude(From, To, order, magnitudes)
        return round((Value * magnitude), 5)
    elif direction > 0:
        magnitude = get_magnitude(From, To, order, magnitudes)
        return round((Value / magnitude), 5)

def check_for_invalid_parameters(order, Value, From, To):
    if not type(Value) in [int, float]: raise ValueError('Invalid value:', Value)
    if not order.__contains__(From): raise ValueError('Invalid unit of measurement:', From)
    if not order.__contains__(To): raise ValueError('Invalid unit of measurement:', To)
