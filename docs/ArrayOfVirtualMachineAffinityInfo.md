# ArrayOfVirtualMachineAffinityInfo

A boxed array of *VirtualMachineAffinityInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineAffinityInfo]**](VirtualMachineAffinityInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_affinity_info import ArrayOfVirtualMachineAffinityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineAffinityInfo from a JSON string
array_of_virtual_machine_affinity_info_instance = ArrayOfVirtualMachineAffinityInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineAffinityInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_affinity_info_dict = array_of_virtual_machine_affinity_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineAffinityInfo from a dict
array_of_virtual_machine_affinity_info_form_dict = array_of_virtual_machine_affinity_info.from_dict(array_of_virtual_machine_affinity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


