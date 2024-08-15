def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet


def feet_to_meters(feet):
    meters = feet / 3.28084
    return meters


# Test the functions
meters = 10
feet = meters_to_feet(meters)
print(f"{meters} meters is equal to {feet} feet")

feet = 32.8084
meters = feet_to_meters(feet)
print(f"{feet} feet is equal to {meters} meters")
