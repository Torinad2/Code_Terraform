oxygen_sensor = get_component("oxygen_sensor")

calibrated_value_oxygen = oxygen_sensor.calibrate(oxygen_sensor.get_value() * 100)


