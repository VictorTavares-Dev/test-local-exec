from script import meters_to_feet, feet_to_meters


def test_meters_to_feet():
    # Test case 1: meters = 0
    meters = 0
    expected_feet = 0
    assert meters_to_feet(meters) == expected_feet

    # Test case 2: meters = 1
    meters = 1
    expected_feet = 3.28084
    assert meters_to_feet(meters) == expected_feet

    # Test case 3: meters = -10
    meters = -10
    expected_feet = -32.8084
    assert meters_to_feet(meters) == expected_feet

    # Test case 4: meters = 100
    meters = 100
    expected_feet = 328.084
    assert meters_to_feet(meters) == expected_feet

    # Test case 5: meters = 2.5
    meters = 2.5
    expected_feet = 8.2021
    assert meters_to_feet(meters) == expected_feet


def test_feet_to_meters():
    # Test case 1: feet = 0
    feet = 0
    expected_meters = 0
    assert feet_to_meters(feet) == expected_meters

    # Test case 2: feet = 1
    feet = 1
    expected_meters = 0.3048
    assert round(feet_to_meters(feet), 4) == expected_meters

    # Test case 3: feet = -10
    feet = -10
    expected_meters = -3.048
    assert round(feet_to_meters(feet), 3) == expected_meters

    # Test case 4: feet = 100
    feet = 100
    expected_meters = 30.48
    assert round(feet_to_meters(feet), 2) == expected_meters

    # Test case 5: feet = 2.5
    feet = 2.5
    expected_meters = 0.762
    assert round(feet_to_meters(feet), 3) == expected_meters
