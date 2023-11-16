# ArrayOfVirtualMachineTargetInfo

A boxed array of *VirtualMachineTargetInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineTargetInfo]**](VirtualMachineTargetInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_target_info import ArrayOfVirtualMachineTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineTargetInfo from a JSON string
array_of_virtual_machine_target_info_instance = ArrayOfVirtualMachineTargetInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineTargetInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_target_info_dict = array_of_virtual_machine_target_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineTargetInfo from a dict
array_of_virtual_machine_target_info_form_dict = array_of_virtual_machine_target_info.from_dict(array_of_virtual_machine_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


