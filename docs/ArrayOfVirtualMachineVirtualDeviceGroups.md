# ArrayOfVirtualMachineVirtualDeviceGroups

A boxed array of *VirtualMachineVirtualDeviceGroups*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVirtualDeviceGroups]**](VirtualMachineVirtualDeviceGroups.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_virtual_device_groups import ArrayOfVirtualMachineVirtualDeviceGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVirtualDeviceGroups from a JSON string
array_of_virtual_machine_virtual_device_groups_instance = ArrayOfVirtualMachineVirtualDeviceGroups.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVirtualDeviceGroups.to_json()

# convert the object into a dict
array_of_virtual_machine_virtual_device_groups_dict = array_of_virtual_machine_virtual_device_groups_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVirtualDeviceGroups from a dict
array_of_virtual_machine_virtual_device_groups_form_dict = array_of_virtual_machine_virtual_device_groups.from_dict(array_of_virtual_machine_virtual_device_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


