# VirtualMachineVirtualDeviceGroupsVendorDeviceGroup

Vendor device group.  These groups are defined in the <code>*VirtualMachineVendorDeviceGroupInfo*</code>. When this group is added, all devices that form the group must be added in the same request. Modification of membership in the group is not allowed, devices cannot be added or removed. When group is removed, all devices that form the group must be removed in the same request. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_group_name** | **str** | The name of the vendor device group from &lt;code&gt;*VirtualMachineVendorDeviceGroupInfo*&lt;/code&gt;.  | 

## Example

```python
from vmware_vi.models.virtual_machine_virtual_device_groups_vendor_device_group import VirtualMachineVirtualDeviceGroupsVendorDeviceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVirtualDeviceGroupsVendorDeviceGroup from a JSON string
virtual_machine_virtual_device_groups_vendor_device_group_instance = VirtualMachineVirtualDeviceGroupsVendorDeviceGroup.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVirtualDeviceGroupsVendorDeviceGroup.to_json()

# convert the object into a dict
virtual_machine_virtual_device_groups_vendor_device_group_dict = virtual_machine_virtual_device_groups_vendor_device_group_instance.to_dict()
# create an instance of VirtualMachineVirtualDeviceGroupsVendorDeviceGroup from a dict
virtual_machine_virtual_device_groups_vendor_device_group_form_dict = virtual_machine_virtual_device_groups_vendor_device_group.from_dict(virtual_machine_virtual_device_groups_vendor_device_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


