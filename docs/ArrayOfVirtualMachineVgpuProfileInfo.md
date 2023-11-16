# ArrayOfVirtualMachineVgpuProfileInfo

A boxed array of *VirtualMachineVgpuProfileInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVgpuProfileInfo]**](VirtualMachineVgpuProfileInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_vgpu_profile_info import ArrayOfVirtualMachineVgpuProfileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVgpuProfileInfo from a JSON string
array_of_virtual_machine_vgpu_profile_info_instance = ArrayOfVirtualMachineVgpuProfileInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVgpuProfileInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_vgpu_profile_info_dict = array_of_virtual_machine_vgpu_profile_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVgpuProfileInfo from a dict
array_of_virtual_machine_vgpu_profile_info_form_dict = array_of_virtual_machine_vgpu_profile_info.from_dict(array_of_virtual_machine_vgpu_profile_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


