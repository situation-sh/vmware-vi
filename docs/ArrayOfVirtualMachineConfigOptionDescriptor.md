# ArrayOfVirtualMachineConfigOptionDescriptor

A boxed array of *VirtualMachineConfigOptionDescriptor*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineConfigOptionDescriptor]**](VirtualMachineConfigOptionDescriptor.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_config_option_descriptor import ArrayOfVirtualMachineConfigOptionDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineConfigOptionDescriptor from a JSON string
array_of_virtual_machine_config_option_descriptor_instance = ArrayOfVirtualMachineConfigOptionDescriptor.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineConfigOptionDescriptor.to_json()

# convert the object into a dict
array_of_virtual_machine_config_option_descriptor_dict = array_of_virtual_machine_config_option_descriptor_instance.to_dict()
# create an instance of ArrayOfVirtualMachineConfigOptionDescriptor from a dict
array_of_virtual_machine_config_option_descriptor_form_dict = array_of_virtual_machine_config_option_descriptor.from_dict(array_of_virtual_machine_config_option_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


