component_thermometer = get_component("thermometer")
component_transmitter = get_component("transmitter")

value_temperature = component_thermometer.get_value()

component_transmitter.connect("earth")
component_transmitter.transmit("current_temperature", value_temperature)
component_transmitter.disconnect()
