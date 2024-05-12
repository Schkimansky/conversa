from tkinter import Tk

#
# Usefull Functions
#

def get_dpi():
    return Tk().winfo_fpixels('1i')

def get_magnitude(From, To, Classification, Magnitudes):
    # Index distance is the distance (in integer) from (From) to (To) values inside the ORDER list
    index_distance = (Classification.index(From), Classification.index(To))

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
        magnitude = get_magnitude(To, From, order, magnitudes)
        return Value * magnitude
    elif direction > 0:
        magnitude = get_magnitude(From, To, order, magnitudes)
        return Value / magnitude

def check_for_invalid_parameters(order, Value, From, To):
    if type(Value) != int: raise ValueError('Invalid value:', Value)
    if not order.__contains__(From): raise ValueError('Invalid unit of measurement:', From)
    if not order.__contains__(To): raise ValueError('Invalid unit of measurement:', To)
