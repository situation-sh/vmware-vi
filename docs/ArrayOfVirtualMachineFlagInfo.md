# ArrayOfVirtualMachineFlagInfo

A boxed array of *VirtualMachineFlagInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineFlagInfo]**](VirtualMachineFlagInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_flag_info import ArrayOfVirtualMachineFlagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineFlagInfo from a JSON string
array_of_virtual_machine_flag_info_instance = ArrayOfVirtualMachineFlagInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineFlagInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_flag_info_dict = array_of_virtual_machine_flag_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineFlagInfo from a dict
array_of_virtual_machine_flag_info_form_dict = array_of_virtual_machine_flag_info.from_dict(array_of_virtual_machine_flag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


