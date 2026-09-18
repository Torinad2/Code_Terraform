component_pressure_sensor = get_component("preesure_sensor")

pressure = component_pressure_sensor.get_value()

if ((pressure % 2) != 0): 
    component_pressure_sensor.stabilize(pressure + 1)
else:
    component_pressure_sensor.stabilize(pressure)
