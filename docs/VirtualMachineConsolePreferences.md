# VirtualMachineConsolePreferences

Preferences for the legacy console application that affect the way it behaves during power operations on the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**power_on_when_opened** | **bool** | Power on the virtual machine when it is opened in the console.  | [optional] 
**enter_full_screen_on_power_on** | **bool** | Enter full screen mode when this virtual machine is powered on.  | [optional] 
**close_on_power_off_or_suspend** | **bool** | Close the console application when the virtual machine is powered off or suspended.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_console_preferences import VirtualMachineConsolePreferences

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConsolePreferences from a JSON string
virtual_machine_console_preferences_instance = VirtualMachineConsolePreferences.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConsolePreferences.to_json()

# convert the object into a dict
virtual_machine_console_preferences_dict = virtual_machine_console_preferences_instance.to_dict()
# create an instance of VirtualMachineConsolePreferences from a dict
virtual_machine_console_preferences_form_dict = virtual_machine_console_preferences.from_dict(virtual_machine_console_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


