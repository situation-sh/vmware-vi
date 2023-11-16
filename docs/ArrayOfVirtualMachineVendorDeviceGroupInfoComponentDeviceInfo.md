# ArrayOfVirtualMachineVendorDeviceGroupInfoComponentDeviceInfo

A boxed array of *VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo]**](VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_vendor_device_group_info_component_device_info import ArrayOfVirtualMachineVendorDeviceGroupInfoComponentDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVendorDeviceGroupInfoComponentDeviceInfo from a JSON string
array_of_virtual_machine_vendor_device_group_info_component_device_info_instance = ArrayOfVirtualMachineVendorDeviceGroupInfoComponentDeviceInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVendorDeviceGroupInfoComponentDeviceInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_vendor_device_group_info_component_device_info_dict = array_of_virtual_machine_vendor_device_group_info_component_device_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVendorDeviceGroupInfoComponentDeviceInfo from a dict
array_of_virtual_machine_vendor_device_group_info_component_device_info_form_dict = array_of_virtual_machine_vendor_device_group_info_component_device_info.from_dict(array_of_virtual_machine_vendor_device_group_info_component_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


