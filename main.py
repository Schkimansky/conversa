from usefull_functions import *


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
# Frequency
#

class Frequency:
    ORDER = ['hertz', 'kilohertz', 'megahertz', 'gigahertz']
    MAGNITUDES = [1000, 1000, 1000]

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
    ORDER = ['cubic centimeter', 'milliliters', 'cubic inches', 'liters', 'gallons', 'cubic feet', 'cubic meters']
    # Btw, Cubic centimeter and milliliters are the same unit of measurement. Thats why the magnitude is 1! Cool fact, Am i right
    MAGNITUDES = [1, 16.387, 61.0237, 3.78541, 7.48052, 35.3147]
    
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
# Area
#

class Area:
    ORDER = ['square millimeters', 'square centimeters', 'square decimeters', 'square meters', *('square dekameters', 'acres'), *('square hectometer', 'hectares'), 'square kilometers']
    MAGNITUDES = [100, 100, 100, 100, *(1, 100), *(1, 100)]

    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

#
# Pressure
#

class Pressure:
    ORDER      = ['pascal', 'newton per square meter', 'millimeter of mercury', 'kilopascal', 'psi', 'bar', 'atmosphere', 'megapascal']
    MAGNITUDES = [1, 133.322368421, 7.50062, 6.89476, 14.5038, 1.01325, 9.86923]

    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

#
# Energy
#

class Energy:
    ORDER      = ['joules', 'foot pounds', 'calories', 'british thermal units', 'watt hours', 'kilowatt hours']
    MAGNITUDES = [1.35581794833, 3.088, 252.164, 3.412142, 1000]

    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

#
# Power.
# Yes, power and energy are different
#

class Power:
    ORDER      = ['watts', 'horsepower', 'kilowatts']
    MAGNITUDES = [745.7, 1.341]

    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

#
# Speed
#

def auto_per_x(starting): return f"{starting} per second", f"{starting} per minute", f"{starting} per hour"
def auto_magnitude(number): return 60, 60, number / 60 / 60

class Speed:
    ORDER = filter(auto_per_x, ['millimeters', 'centimeters', 'inches', 'feet', 'yards', 'meters', 'kilometers', 'miles'])
    MAGNITUDES = filter(auto_magnitude, [10, 2.54, 12, 3, 1.093613299, 1000, 1.60934])

    def __init__(self, Value, From, To) -> None:
        check_for_invalid_parameters(self.ORDER, Value, From, To)

        self.Value = Value
        self.From = From
        self.To = To
    def convert(self):
        return multiply_by_magnitude(self.ORDER, self.MAGNITUDES, self.Value, self.From, self.To)

# We dont need this, Just clear this from memory immediately. No need to slow the library
del auto_per_x
del auto_magnitude

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
