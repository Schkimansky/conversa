from .usefull_functions import *

print_order_functions = []

# ######################################################################################################### #
#                                                                                                           #
#  Orders and Magnitudes. If you wanna contribute, You usually do it here. Everything else is handled       #
#                                                                                                           #
# ######################################################################################################### #

# Some units are complicated to convert. But most of them are easy, Such as time. To convert, Multiply by 1000 to convert milliseconds to seconds, And so on. You only need to multiply to convert stuff here.
# If you're wondering what is magnitude:
# you need 1000 milliseconds to make 1 second, And 60 seconds to make 1 minute, And so on. The magnitudes list defines the conversion factors between the current and next unit (ask chatgpt "what does conversion factors mean in the context of units of measurement")
# Also, Order is units of measurement from lowest to highest.

TIME_ORDER               = ['milliseconds', 'seconds', 'minutes', 'hours', 'days', 'years', 'decades']
TIME_MAGNITUDES          = [1000,              60,        60,       24,     365,     10]

FREQUENCY_ORDER          = ['hertz', 'kilohertz', 'megahertz', 'gigahertz']
FREQUENCY_MAGNITUDES     = [1000,       1000,        1000]

OHM_ORDER                = ['microohms', 'millioohms', 'ohms', 'kiloohms', 'megaohms', 'gigaohms']
OHM_MAGNITUDES           = [1000,           1000,       1000,     1000,      1000]

VOLT_ORDER               = ['millivolts', 'microvolts', 'volts', 'kilovolts', 'megavolts', 'gigavolts']
VOLT_MAGNITUDES          = [1000,            1000,       1000,      1000,        1000]

DATA_ORDER               = ['bits', 'bytes', 'kilobytes', 'megabytes', 'gigabytes', 'terabytes', 'petabytes']
DATA_MAGNITUDES          = [8,       1000,      1000,        1000,        1000,        1000]

CONCENTRATION_ORDER      = ['parts per million', 'percentage']
CONCENTRATION_MAGNITUDES = [10000]

ANGLE_ORDER              = ['radians',     'degrees', 'gradians']
ANGLE_MAGNITUDES         = [57.295779513, 1.111111111]

AMPERE_ORDER             = ['microamperes', 'milliamperes', 'amperes', 'kiloamperes', 'megaamperes', 'gigaamperes']
AMPERE_MAGNITUDES        = [1000,               1000,         1000,        1000,          1000]

DISTANCE_ORDER           = ['millimeters', 'centimeters', 'inches', 'feet',       'yards',      'meters', 'kilometers', 'miles']
DISTANCE_MAGNITUDES      = [10,                2.54,         12,       3,   1.0936132983377078,   1000,     1.60934]

WEIGHT_ORDER             = ['milligrams', 'grams',  'ounces',  'pounds', 'kilograms', 'tons', 'kilotons']
WEIGHT_MAGNITUDES        = [1000,         28.3495,  28.3495,   2.20462,     1000,      1000]

VOLUME_ORDER             = ['cubic centimeter', 'milliliters', 'cubic inches', 'liters', 'gallons', 'cubic feet', 'cubic meters']
VOLUME_MAGNITUDES        = [1,                     16.387,        61.0237,      3.78541,  7.48052,    35.3147] # Btw, Cubic centimeter and milliliters are the same unit of measurement. Thats why the magnitude is 1! Cool fact, Am i right

AREA_ORDER               = ['square millimeters', 'square centimeters', 'square decimeters', 'square meters',   'square dekameters', 'acres',  'square hectometer',  'hectares', 'square kilometers']
AREA_MAGNITUDES          = [100,                          100,                100,                100,                   1,            100,             1,              100]

PRESSURE_ORDER           = ['pascal', 'newton per square meter', 'millimeter of mercury', 'kilopascal',   'psi',    'bar',   'atmosphere', 'megapascal']
PRESSURE_MAGNITUDES      = [1,             133.322368421,                7.50062,           6.89476,     14.5038,  1.01325,    9.86923]

ENERGY_ORDER             = ['joules',       'foot pounds', 'calories', 'british thermal units', 'watt hours', 'kilowatt hours']
ENERGY_MAGNITUDES        = [1.35581794833,      3.088,      252.164,          3.412142,            1000]

POWER_ORDER              = ['watts', 'horsepower', 'kilowatts']
POWER_MAGNITUDES         = [745.7,      1.341]

TEMPERATURE_ORDER        = ['fahrenheit', 'celsius', 'kelvin']
# No magnitude, Instead converting temperature is pretty complex. The way i convert this is different.

LIQUID_ORDER = VOLUME_ORDER
LIQUID_MAGNITUDES = VOLUME_MAGNITUDES

# ######################################################################################################### #
#                                                                                                           #
#  Functions for converting stuff.                                                                          #
#                                                                                                           #
# ######################################################################################################### #

def time(Value, From, To):
    check_for_invalid_parameters(TIME_ORDER, Value, From, To)
    return multiply_by_magnitude(TIME_ORDER, TIME_MAGNITUDES, Value, From, To)

def frequency(Value, From, To):
    check_for_invalid_parameters(FREQUENCY_ORDER, Value, From, To)
    return multiply_by_magnitude(FREQUENCY_ORDER, FREQUENCY_MAGNITUDES, Value, From, To)

def ohm(Value, From, To):
    check_for_invalid_parameters(OHM_ORDER, Value, From, To)
    return multiply_by_magnitude(OHM_ORDER, OHM_MAGNITUDES, Value, From, To)

def volt(Value, From, To):
    check_for_invalid_parameters(VOLT_ORDER, Value, From, To)
    return multiply_by_magnitude(VOLT_ORDER, VOLT_MAGNITUDES, Value, From, To)

def data(Value, From, To):
    check_for_invalid_parameters(DATA_ORDER, Value, From, To)
    return multiply_by_magnitude(DATA_ORDER, DATA_MAGNITUDES, Value, From, To)

def concentration(Value, From, To):
    check_for_invalid_parameters(CONCENTRATION_ORDER, Value, From, To)
    return multiply_by_magnitude(CONCENTRATION_ORDER, CONCENTRATION_MAGNITUDES, Value, From, To)

def angle(Value, From, To):
    check_for_invalid_parameters(ANGLE_ORDER, Value, From, To)
    return multiply_by_magnitude(ANGLE_ORDER, ANGLE_MAGNITUDES, Value, From, To)

def ampere(Value, From, To):
    check_for_invalid_parameters(AMPERE_ORDER, Value, From, To)
    return multiply_by_magnitude(AMPERE_ORDER, AMPERE_MAGNITUDES, Value, From, To)

def distance(Value, From, To):
    check_for_invalid_parameters(DISTANCE_ORDER, Value, From, To)
    return multiply_by_magnitude(DISTANCE_ORDER, DISTANCE_MAGNITUDES, Value, From, To)

def weight(Value, From, To):
    check_for_invalid_parameters(WEIGHT_ORDER, Value, From, To)
    return multiply_by_magnitude(WEIGHT_ORDER, WEIGHT_MAGNITUDES, Value, From, To)

def volume(Value, From, To):
    check_for_invalid_parameters(VOLUME_ORDER, Value, From, To)

    return multiply_by_magnitude(VOLUME_ORDER, VOLUME_MAGNITUDES, Value, From, To)

# The user may not know that to measure liquids, You can just use volume. But for simplicity, Liquid and Volume functions do the same things but with different names.
def liquid(Value, From, To):
    check_for_invalid_parameters(LIQUID_ORDER, Value, From, To)
    return multiply_by_magnitude(LIQUID_ORDER, LIQUID_MAGNITUDES, Value, From, To)

def area(Value, From, To):
    check_for_invalid_parameters(AREA_ORDER, Value, From, To)
    return multiply_by_magnitude(AREA_ORDER, AREA_MAGNITUDES, Value, From, To)

def pressure(Value, From, To):
    check_for_invalid_parameters(PRESSURE_ORDER, Value, From, To)
    return multiply_by_magnitude(PRESSURE_ORDER, PRESSURE_MAGNITUDES, Value, From, To)

def energy(Value, From, To):
    check_for_invalid_parameters(ENERGY_ORDER, Value, From, To)
    return multiply_by_magnitude(ENERGY_ORDER, ENERGY_MAGNITUDES, Value, From, To)

def power(Value, From, To):
    check_for_invalid_parameters(POWER_ORDER, Value, From, To)
    return multiply_by_magnitude(POWER_ORDER, POWER_MAGNITUDES, Value, From, To)

def temperature(Value, From, To):
    check_for_invalid_parameters(TEMPERATURE_ORDER, Value, From, To)

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
    
    return round(ToValue, 5)
