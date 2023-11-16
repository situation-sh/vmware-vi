# ArrayOfVirtualMachineConsolePreferences

A boxed array of *VirtualMachineConsolePreferences*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineConsolePreferences]**](VirtualMachineConsolePreferences.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_console_preferences import ArrayOfVirtualMachineConsolePreferences

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineConsolePreferences from a JSON string
array_of_virtual_machine_console_preferences_instance = ArrayOfVirtualMachineConsolePreferences.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineConsolePreferences.to_json()

# convert the object into a dict
array_of_virtual_machine_console_preferences_dict = array_of_virtual_machine_console_preferences_instance.to_dict()
# create an instance of ArrayOfVirtualMachineConsolePreferences from a dict
array_of_virtual_machine_console_preferences_form_dict = array_of_virtual_machine_console_preferences.from_dict(array_of_virtual_machine_console_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


