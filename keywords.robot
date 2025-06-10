*** Settings ***
Library    helper.py

*** Variables ***
${testbed}    testbed.yaml
${device}     Spine-1
# create a variable called interface and set value to eth1/1
${interface}  eth1/1

*** Keywords ***
Run Show Version on Device
    ${version}    Get Show Version    ${testbed}    ${device}
    RETURN    ${version}

# Create keyword called Run BGP Show and call Get Bgp Summary from helper.py and return bgp_status
Run BGP Show
    ${bgp_status}    Get Bgp Summary    ${testbed}    ${device}
    RETURN    ${bgp_status}

# Create a keyword called Shut Interface and call Shut Interface from helper.py and pass in the interface variable
Shut Interface
    Shutdown Interface    ${testbed}    ${device}    ${interface}

# Create a keyword called Run BGP Reset and call Clear Ip Bgp from helper.py and pass in the device variable
Run BGP Reset
    Clear Ip Bgp    ${testbed}    ${device}