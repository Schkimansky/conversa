from usefull_functions import *


# ###########################################################################################################
#                                                                                                           #
# Classes for converting stuff. If you wanna contribute, You usually do it here. Everything else is handled #
#                                                                                                           #
# ###########################################################################################################

#
# Time
#

def Time(Value, From, To):
    # Some units are complicated to convert. But most of them are easy, Such as time. To convert, Multiply by 1000 to convert milliseconds to seconds, And so on. You only need to multiply to convert stuff here.
    ORDER = ['milliseconds', 'seconds', 'minutes', 'hours', 'days', 'years', 'decades']
    MAGNITUDES = [1000, 60, 60, 24, 365, 10] # you need 1000 milliseconds to make 1 second, And 60 seconds to make 1 minute, And so on.

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Frequency
#

def Frequency(Value, From, To):
    ORDER = ['hertz', 'kilohertz', 'megahertz', 'gigahertz']
    MAGNITUDES = [1000, 1000, 1000]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Ohm (Resistance)
#

def Ohm(Value, From, To):
    ORDER = ['microohms', 'millioohms', 'ohms', 'kiloohms', 'megaohms', 'gigaohms']
    MAGNITUDES = [1000,      1000,       1000,     1000,      1000]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Volt
#

def Volt(Value, From, To):
    ORDER = ['millivolts', 'microvolts', 'volts', 'kilovolts', 'megavolts', 'gigavolts']
    MAGNITUDES = [1000,      1000,       1000,     1000,      1000]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Data
#

def Data(Value, From, To):
    ORDER      = ['bits', 'bytes', 'kilobytes', 'megabytes', 'gigabytes', 'terabytes', 'petabytes']
    MAGNITUDES = [8,       1000,      1000,        1000,        1000,        1000]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Concentration
#

def Concentration(Value, From, To):
    ORDER      = ['parts per million', 'percentage']
    MAGNITUDES = [10000]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Angle
#

def Angle(Value, From, To):
    ORDER      = ['radians', 'degrees', 'gradians']
    MAGNITUDES = [57.295779513, 1.111111111]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Ampere
#

def Ampere(Value, From, To):
    ORDER = ['microamperes', 'milliamperes', 'amperes', 'kiloamperes', 'megaamperes', 'gigaamperes']
    MAGNITUDES = [1000, 1000, 1000, 1000, 1000]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Distance
#

def Distance(Value, From, To):
    ORDER = ['millimeters', 'centimeters', 'inches', 'feet', 'yards', 'meters', 'kilometers', 'miles']
    MAGNITUDES = [10, 2.54, 12, 3, 1.093613299, 1000, 1.60934]
    
    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Weight
#

def Weight(Value, From, To):
    ORDER = ['milligrams', 'grams', 'ounces', 'pounds', 'kilograms', 'tons', 'kilotons']
    MAGNITUDES = [1000, 28.3495, 28.3495, 2.20462, 1000, 1000]
    
    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Volume
#

def Volume(Value, From, To):
    ORDER = ['cubic centimeter', 'milliliters', 'cubic inches', 'liters', 'gallons', 'cubic feet', 'cubic meters']
    # Btw, Cubic centimeter and milliliters are the same unit of measurement. Thats why the magnitude is 1! Cool fact, Am i right
    MAGNITUDES = [1, 16.387, 61.0237, 3.78541, 7.48052, 35.3147]
    
    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

# The user may not know that to measure liquids, You can just use volume. But for simplicity, Liquid and Volume classes do the same things but with different names.
Liquid = Volume

#
# Area
#

def Area(Value, From, To):
    ORDER = ['square millimeters', 'square centimeters', 'square decimeters', 'square meters', *('square dekameters', 'acres'), *('square hectometer', 'hectares'), 'square kilometers']
    MAGNITUDES = [100, 100, 100, 100, *(1, 100), *(1, 100)]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Pressure
#

def Pressure(Value, From, To):
    ORDER      = ['pascal', 'newton per square meter', 'millimeter of mercury', 'kilopascal', 'psi', 'bar', 'atmosphere', 'megapascal']
    MAGNITUDES = [1, 133.322368421, 7.50062, 6.89476, 14.5038, 1.01325, 9.86923]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Energy
#

def Energy(Value, From, To):
    ORDER      = ['joules', 'foot pounds', 'calories', 'british thermal units', 'watt hours', 'kilowatt hours']
    MAGNITUDES = [1.35581794833, 3.088, 252.164, 3.412142, 1000]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Power.
# Yes, power and energy are different
#

def Power(Value, From, To):
    ORDER      = ['watts', 'horsepower', 'kilowatts']
    MAGNITUDES = [745.7, 1.341]

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

#
# Speed
#

def auto_per_x(starting): return f"{starting} per second", f"{starting} per minute", f"{starting} per hour"
def auto_magnitude(number): return 60, 60, number / 60 / 60

def Speed(Value, From, To):
    ORDER = filter(auto_per_x, ['millimeters', 'centimeters', 'inches', 'feet', 'yards', 'meters', 'kilometers', 'miles'])
    MAGNITUDES = filter(auto_magnitude, [10, 2.54, 12, 3, 1.093613299, 1000, 1.60934])

    check_for_invalid_parameters(ORDER, Value, From, To)

    return multiply_by_magnitude(ORDER, MAGNITUDES, Value, From, To)

# We dont need this, Just clear this from memory immediately. No need to slow the library
del auto_per_x
del auto_magnitude

#
# Temperature
#

def Temperature(Value, From, To):
    ORDER = ['fahrenheit', 'celsius', 'kelvin']
    # No magnitude, Instead converting temperature is pretty complex. The way i convert this is different.

    check_for_invalid_parameters(ORDER, Value, From, To)

    def F_to_C(F): return (F - 32) + (5/9)
    def K_to_C(K): return K - 273.15
    def C_to_F(C): return (C * (9 / 5)) + 32
    def C_to_K(C): return C + 273.15

    # Check if the user is stupid
    if From == To: return Value

    # First, Convert value to celsius.
    ValueCelsius = None
    if From == 'farenheit':
        ValueCelsius = F_to_C(Value)
    elif From == 'celsius':
        ValueCelsius = Value # No need to convert, Since we are trying to convert value to celsius.
    elif From == 'kelvin':
        ValueCelsius = K_to_C(Value)
    
    # Then convert value in celsius to what the user wants. This way, it covers all possible ways the user would wanna convert something to the other. And also because i dont have to write a function for each possible parameter, eg. (C_TO_F, C_TO_K, F_TO_K, F_TO_C, and more). I only gotta write 4 functions with the aproach i am using
    ToValue = None
    if To == 'farenheit':
        ToValue = C_to_F(ValueCelsius)
    elif To == 'celsius':
        ToValue = ValueCelsius # already celsius
    elif To == 'kelvin':
        ToValue = C_to_K(ValueCelsius)
    
    return ToValue

