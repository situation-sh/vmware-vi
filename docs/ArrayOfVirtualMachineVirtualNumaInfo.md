# ArrayOfVirtualMachineVirtualNumaInfo

A boxed array of *VirtualMachineVirtualNumaInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVirtualNumaInfo]**](VirtualMachineVirtualNumaInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_virtual_numa_info import ArrayOfVirtualMachineVirtualNumaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVirtualNumaInfo from a JSON string
array_of_virtual_machine_virtual_numa_info_instance = ArrayOfVirtualMachineVirtualNumaInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVirtualNumaInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_virtual_numa_info_dict = array_of_virtual_machine_virtual_numa_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVirtualNumaInfo from a dict
array_of_virtual_machine_virtual_numa_info_form_dict = array_of_virtual_machine_virtual_numa_info.from_dict(array_of_virtual_machine_virtual_numa_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


