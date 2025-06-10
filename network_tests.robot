*** Settings ***
Resource    keywords.robot

*** Test Cases ***
Validate Show Version on Device
    ${running_version}    Run Show Version on Device
    Should Contain    ${running_version}    10.3(1)

# Create a new test called Validate BGP Status and call Run BGP Show from the keywords file
Validate BGP Status
    ${bgp_status}    Run BGP Show
    # bgp_status should not contain Idle
    Should Not Contain    ${bgp_status}    Idle

# Create a new test called Test Shut Interface and call Shut Interface from keywords.robot and then run Run BGP Show and make sure output does not contain Idle
Test Shut Interface
    Shut Interface
    ${bgp_status}    Run BGP Show
    Should Not Contain    ${bgp_status}    Idle

# Create a new test called BGP Reset and call Run BGP Reset from keyword.robot and then run Run BGP Show and make sure output does not contain Idle
BGP Reset
    Run BGP Reset
    ${bgp_status}    Run BGP Show
    Should Not Contain    ${bgp_status}    Idle