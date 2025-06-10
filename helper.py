from genie.conf import Genie
from pyats.topology import loader

# Write a method to load the testbed file, connect to the device passed in and return the device object
def connect_device(testbed_file, device_name):
    # Load the testbed file
    testbed = loader.load(testbed_file)

    # Connect to the device
    device = testbed.devices[device_name]
    device.connect()

    return device

# Write a method to disconnect from the device
def disconnect_device(device):
    device.disconnect()

# Write a method called parse_or_execute_command that takes in the device object, command and parse flag then either executes or parses the command and returns the output
def parse_or_execute_command(device, command, parse):
    if parse:
        return device.parse(command)
    else:
        return device.execute(command)
    
# Write a method called get_show_version that takes in the testbed_file and device_name, calls parse_or_execute_command to get the show version output and returns the output
def get_show_version(testbed_file, device_name):
    device = connect_device(testbed_file, device_name)
    output = parse_or_execute_command(device, 'show version', True)
    disconnect_device(device)
    version = output['platform']['software']['system_version']
    return version

# write a method called get_bgp_summary that takes in the testbed_file and device_name, calls parse_or_execute_command and passes in device object, command='show bgp vrf all all summary' and parse=False then returns the output
def get_bgp_summary(testbed_file, device_name):
    device = connect_device(testbed_file, device_name)
    output = parse_or_execute_command(device, 'show bgp vrf all all summary', False)
    disconnect_device(device)
    return output

# write a method called shutdown_interface that will shut down the interface passed in on a nxos device
def shutdown_interface(testbed_file, device_name, interface):
    device = connect_device(testbed_file, device_name)
    output = parse_or_execute_command(device, f'conf t ; interface {interface} ; shutdown ; end', False)
    disconnect_device(device)
    return output

# write method named clear_ip_bgp that takes in the testbed_file and device_name, calls parse_or_execute_command and passes in device object, command='clear ip bgp *' and parse=False then returns the output
def clear_ip_bgp(testbed_file, device_name):
    device = connect_device(testbed_file, device_name)
    output = parse_or_execute_command(device, 'clear ip bgp *', False)
    disconnect_device(device)
    return output