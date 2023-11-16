# ArrayOfVirtualMachineVirtualDeviceGroupsDeviceGroup

A boxed array of *VirtualMachineVirtualDeviceGroupsDeviceGroup*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVirtualDeviceGroupsDeviceGroup]**](VirtualMachineVirtualDeviceGroupsDeviceGroup.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_virtual_device_groups_device_group import ArrayOfVirtualMachineVirtualDeviceGroupsDeviceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVirtualDeviceGroupsDeviceGroup from a JSON string
array_of_virtual_machine_virtual_device_groups_device_group_instance = ArrayOfVirtualMachineVirtualDeviceGroupsDeviceGroup.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVirtualDeviceGroupsDeviceGroup.to_json()

# convert the object into a dict
array_of_virtual_machine_virtual_device_groups_device_group_dict = array_of_virtual_machine_virtual_device_groups_device_group_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVirtualDeviceGroupsDeviceGroup from a dict
array_of_virtual_machine_virtual_device_groups_device_group_form_dict = array_of_virtual_machine_virtual_device_groups_device_group.from_dict(array_of_virtual_machine_virtual_device_groups_device_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


