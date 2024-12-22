"""Functions to prevent a nuclear meltdown."""

# The first thing a control system has to do is check if the reactor is balanced in criticality.
# A reactor is said to be critical if it satisfies the following conditions:
#
# - The temperature is less than 800 K.
# - The number of neutrons emitted per second is greater than 500.
# - The product of temperature and neutrons emitted per second is less than 500000.
#
# Implement the function `is_criticality_balanced()` that takes `temperature` measured in kelvin and `neutrons_emitted`
# as parameters, and returns `True` if the criticality conditions are met, `False` if not.
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    temperature_is_lower_than_800 = temperature < 800
    neutron_count_gt_500 = neutrons_emitted > 500
    product_of_neutrons_and_temperature_emitted_per_second_is_less_than_500000 = temperature * neutrons_emitted < 500000

    if temperature_is_lower_than_800 and neutron_count_gt_500 and product_of_neutrons_and_temperature_emitted_per_second_is_less_than_500000:
        return True


    return False


# 1. `green` -> efficiency of 80% or more,
# 2. `orange` -> efficiency of less than 80% but at least 60%,
# 3. `red` -> efficiency below 60%, but still 30% or more,
# 4. `black` ->  less than 30% efficient.
#
# The percentage value can be calculated as `(generated_power/theoretical_max_power)*100`
# where `generated_power` = `voltage` * `current`.
# Note that the percentage value is usually not an integer number, so make sure to consider the
# proper use of the `<` and `<=` comparisons.
#
# Implement the function `reactor_efficiency(<voltage>, <current>, <theoretical_max_power>)`, with three parameters: `voltage`,
# `current`, and `theoretical_max_power`.
# This function should return the efficiency band of the reactor : 'green', 'orange', 'red', or 'black'.
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency_percentage = (generated_power / theoretical_max_power) * 100

    if efficiency_percentage >= 80:
        return 'green'
    if efficiency_percentage >= 60:
        return 'orange'
    if efficiency_percentage >= 30:
        return 'red'
    return 'black'


# Your final task involves creating a fail-safe mechanism to avoid overload and meltdown.
# This mechanism will determine if the reactor is below, at, or above the ideal criticality threshold.
# Criticality can then be increased, decreased, or stopped by inserting (or removing) control rods into the reactor.
#
# Implement the function called `fail_safe()`, which takes 3 parameters: `temperature` measured in kelvin,
# `neutrons_produced_per_second`, and `threshold`, and outputs a status code for the reactor.
#
# - If `temperature * neutrons_produced_per_second` < 90% of `threshold`, output a status code of 'LOW'
#   indicating that control rods must be removed to produce power.
#
# - If the value `temperature * neutrons_produced_per_second` is within 10% of the
#   `threshold` (so either 0-10% less than the threshold, at the threshold, or 0-10% greater
#   than the threshold), the reactor is in _criticality_ and the status code of 'NORMAL' should be output,
#   indicating that the reactor is in optimum condition and control rods are in an ideal position.
#
# - If `temperature * neutrons_produced_per_second` is not in the above-stated ranges, the reactor is
#   going into meltdown and a status code of 'DANGER' must be passed to immediately shut down the reactor.
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    result = temperature * neutrons_produced_per_second
    percentage = (result / threshold) * 100

    is_low = percentage < 90
    is_critical = percentage >= 90 and percentage > 110

    if is_low:
        return 'LOW'
    if is_critical:
        return 'DANGER'

    return 'NORMAL'
