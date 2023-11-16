# ArrayOfVirtualMachineFileLayout

A boxed array of *VirtualMachineFileLayout*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineFileLayout]**](VirtualMachineFileLayout.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_file_layout import ArrayOfVirtualMachineFileLayout

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineFileLayout from a JSON string
array_of_virtual_machine_file_layout_instance = ArrayOfVirtualMachineFileLayout.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineFileLayout.to_json()

# convert the object into a dict
array_of_virtual_machine_file_layout_dict = array_of_virtual_machine_file_layout_instance.to_dict()
# create an instance of ArrayOfVirtualMachineFileLayout from a dict
array_of_virtual_machine_file_layout_form_dict = array_of_virtual_machine_file_layout.from_dict(array_of_virtual_machine_file_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


