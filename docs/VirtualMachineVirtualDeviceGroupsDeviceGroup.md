# VirtualMachineVirtualDeviceGroupsDeviceGroup

Base device group type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_instance_key** | **int** | Group instance key.  Unique integer referencing device group. During group creation client should use a temporary negative number. Once group is added to the virtual machine, server generates non-negative integer that stays constant during group lifetime. See *VirtualDevice.key* for details.  | 
**device_info** | [**Description**](Description.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_virtual_device_groups_device_group import VirtualMachineVirtualDeviceGroupsDeviceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVirtualDeviceGroupsDeviceGroup from a JSON string
virtual_machine_virtual_device_groups_device_group_instance = VirtualMachineVirtualDeviceGroupsDeviceGroup.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVirtualDeviceGroupsDeviceGroup.to_json()

# convert the object into a dict
virtual_machine_virtual_device_groups_device_group_dict = virtual_machine_virtual_device_groups_device_group_instance.to_dict()
# create an instance of VirtualMachineVirtualDeviceGroupsDeviceGroup from a dict
virtual_machine_virtual_device_groups_device_group_form_dict = virtual_machine_virtual_device_groups_device_group.from_dict(virtual_machine_virtual_device_groups_device_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


