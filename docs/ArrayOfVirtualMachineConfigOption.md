# ArrayOfVirtualMachineConfigOption

A boxed array of *VirtualMachineConfigOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineConfigOption]**](VirtualMachineConfigOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_config_option import ArrayOfVirtualMachineConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineConfigOption from a JSON string
array_of_virtual_machine_config_option_instance = ArrayOfVirtualMachineConfigOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineConfigOption.to_json()

# convert the object into a dict
array_of_virtual_machine_config_option_dict = array_of_virtual_machine_config_option_instance.to_dict()
# create an instance of ArrayOfVirtualMachineConfigOption from a dict
array_of_virtual_machine_config_option_form_dict = array_of_virtual_machine_config_option.from_dict(array_of_virtual_machine_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


