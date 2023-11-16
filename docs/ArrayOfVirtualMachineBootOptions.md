# ArrayOfVirtualMachineBootOptions

A boxed array of *VirtualMachineBootOptions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineBootOptions]**](VirtualMachineBootOptions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_boot_options import ArrayOfVirtualMachineBootOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineBootOptions from a JSON string
array_of_virtual_machine_boot_options_instance = ArrayOfVirtualMachineBootOptions.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineBootOptions.to_json()

# convert the object into a dict
array_of_virtual_machine_boot_options_dict = array_of_virtual_machine_boot_options_instance.to_dict()
# create an instance of ArrayOfVirtualMachineBootOptions from a dict
array_of_virtual_machine_boot_options_form_dict = array_of_virtual_machine_boot_options.from_dict(array_of_virtual_machine_boot_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


