# ArrayOfVirtualMachineParallelInfo

A boxed array of *VirtualMachineParallelInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineParallelInfo]**](VirtualMachineParallelInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_parallel_info import ArrayOfVirtualMachineParallelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineParallelInfo from a JSON string
array_of_virtual_machine_parallel_info_instance = ArrayOfVirtualMachineParallelInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineParallelInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_parallel_info_dict = array_of_virtual_machine_parallel_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineParallelInfo from a dict
array_of_virtual_machine_parallel_info_form_dict = array_of_virtual_machine_parallel_info.from_dict(array_of_virtual_machine_parallel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


