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
        magnitude = get_magnitude(From, To, order, magnitudes)
        return Value * magnitude
    elif direction > 0:
        magnitude = get_magnitude(From, To, order, magnitudes)
        return Value / magnitude

def check_for_invalid_parameters(order, Value, From, To):
    if type(Value) != int: raise ValueError('Invalid value:', Value)
    if not order.__contains__(From): raise ValueError('Invalid unit of measurement:', From)
    if not order.__contains__(To): raise ValueError('Invalid unit of measurement:', To)



# ###########################################################################################################
#                                                                                                           #
# Classes for converting stuff. If you wanna contribute, You usually do it here. Everything else is handled #
#                                                                                                           #
# ###########################################################################################################

#
# Time
#

class Time:
    # Some units are complicated to convert. But most of them are easy, Such as time. To convert, Multiply by 1000 to convert milliseconds to seconds, And so on. You only need to multiply to convert stuff here.
    ORDER = ['milliseconds', 'seconds', 'minutes', 'hours', 'days', 'years', 'decades']
    MAGNITUDES = [1000, 60, 60, 24, 365, 10] # you need 1000 milliseconds to make 1 second, And 60 seconds to make 1 minute, And so on.
    
    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

#
# Distance
#

class Distance:
    ORDER = ['millimeters', 'centimeters', 'inches', 'feet', 'yards', 'meters', 'kilometers', 'miles']
    MAGNITUDES = [10, 2.54, 12, 3, 1.093613299, 1000, 1.60934]
    
    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

#
# Weight
#

class Weight:
    ORDER = ['milligrams', 'grams', 'ounces', 'pounds', 'kilograms', 'tons', 'kilotons']
    MAGNITUDES = [1000, 28.3495, 28.3495, 2.20462, 1000, 1000]
    
    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

#
# Volume
#

class Volume:
    ORDER = ['cubic centimeter', 'milliliters', 'liters', 'gallons', 'cubic meters']
    # Btw, Cubic centimeter and milliliters are the same unit of measurement. Thats why the magnitude is 1! Cool fact, Am i right
    MAGNITUDES = [1, 1000, 3.78541]
    
    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

# The user may not know that to measure liquids, You can just use volume. But for simplicity, Liquid and Volume classes do the same things but with different names.
Liquid = Volume

#
# Temperature
#

class Temperature:
    ORDER = ['fahrenheit', 'celsius', 'kelvin']
    # No magnitude, Instead converting temperature is pretty complex. The way i convert this is different.

    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To

    def F_to_C(F): return (F - 32) + (5/9)
    def K_to_C(K): return K - 273.15
    def C_to_F(C): return (C * (9 / 5)) + 32
    def C_to_K(C): return C + 273.15

    def convert(self):
        # Check if the user is stupid
        if self.From == self.To: return self.Value

        # First, Convert value to celsius.
        ValueCelsius = None
        if self.From == 'farenheit':
            ValueCelsius = self.F_to_C(self.Value)
        elif self.From == 'celsius':
            ValueCelsius = self.Value # No need to convert, Since we are trying to convert value to celsius.
        elif self.From == 'kelvin':
            ValueCelsius = self.K_to_C(self.Value)
        
        # Then convert value in celsius to what the user wants.
        ToValue = None
        if self.To == 'farenheit':
            ToValue = self.C_to_F(ValueCelsius)
        elif self.To == 'celsius':
            ToValue = ValueCelsius # already
        elif self.To == 'kelvin':
            ToValue = self.C_to_K(ValueCelsius)
        
        return ToValue









#
# Import
#

def convert_time(Value, From, To):
    # Check for invalid values
    if type(Value) != int: raise ValueError('The first argument must be a number. Usage: (60, "seconds", "minutes")')
    if type(From)  != str: raise ValueError('The second argument must be a string. Usage: (60, "seconds", "minutes")')
    if type(To)    != str: raise ValueError('The third argument must be a string. Usage: (60, "seconds", "minutes")')
    if not TIME_ORDER.__contains__(From): raise ValueError(f'Sorry, We dont support "{From}" yet. Usage: (60, "seconds", "minutes")')
    if not TIME_ORDER.__contains__(To):   raise ValueError(f'Sorry, We dont support "{To}" yet. Usage: (60, "seconds", "minutes")')

    return calculate(TIME_ORDER, TIME_MAGNITUDES, Value, From, To)

# Usually, To convert something you can just multiply. But temperature is more complex
def convert_temperature(Value: Int, From: Temperature, To: Time):
    # Check for invalid values
    if type(Value) != int: raise ValueError('The first argument must be a number. Usage: (60, "seconds", "minutes")')
    if type(From)  != str: raise ValueError('The second argument must be a string. Usage: (60, "seconds", "minutes")')
    if type(To)    != str: raise ValueError('The third argument must be a string. Usage: (60, "seconds", "minutes")')
    if not TIME_ORDER.__contains__(From): raise ValueError(f'Sorry, We dont support "{From}" yet. Usage: (60, "seconds", "minutes")')
    if not TIME_ORDER.__contains__(To):   raise ValueError(f'Sorry, We dont support "{To}" yet. Usage: (60, "seconds", "minutes")')

    return calculate(TIME_ORDER, TIME_MAGNITUDES, Value, From, To)
