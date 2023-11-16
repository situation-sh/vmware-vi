# VirtualMachineVirtualDeviceGroups

The VirtualDeviceGroups data object type contains information about the backing that maps the virtual device onto a physical device for a Vendor Device Group device.  Vendor Device Groups allow third-parties to define collections of devices that must be allocated to a virtual machine as a unit. Typically, this is because the set of devices are related in a some way, e.g. a physical link connects the devices. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_group** | [**List[VirtualMachineVirtualDeviceGroupsDeviceGroup]**](VirtualMachineVirtualDeviceGroupsDeviceGroup.md) | Information about device groups used by this VM.  When adding a group, all devices that form the group must be added in the same request. When removing group, also all devices participating in the group must be removed. Modifying existing device group membership is not allowed.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_virtual_device_groups import VirtualMachineVirtualDeviceGroups

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVirtualDeviceGroups from a JSON string
virtual_machine_virtual_device_groups_instance = VirtualMachineVirtualDeviceGroups.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVirtualDeviceGroups.to_json()

# convert the object into a dict
virtual_machine_virtual_device_groups_dict = virtual_machine_virtual_device_groups_instance.to_dict()
# create an instance of VirtualMachineVirtualDeviceGroups from a dict
virtual_machine_virtual_device_groups_form_dict = virtual_machine_virtual_device_groups.from_dict(virtual_machine_virtual_device_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


