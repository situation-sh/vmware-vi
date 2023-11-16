# VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo

Class describing a component device within this vendor device group. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of this component.  See *VirtualMachineVendorDeviceGroupInfoComponentDeviceInfoComponentType_enum* for supported types.  | 
**vendor_name** | **str** | Name of component device vendor.  | 
**device_name** | **str** | Name of component device.  | 
**is_configurable** | **bool** | True if this device may be configured by user or UI.  | 
**device** | [**VirtualDevice**](VirtualDevice.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_vendor_device_group_info_component_device_info import VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo from a JSON string
virtual_machine_vendor_device_group_info_component_device_info_instance = VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo.to_json()

# convert the object into a dict
virtual_machine_vendor_device_group_info_component_device_info_dict = virtual_machine_vendor_device_group_info_component_device_info_instance.to_dict()
# create an instance of VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo from a dict
virtual_machine_vendor_device_group_info_component_device_info_form_dict = virtual_machine_vendor_device_group_info_component_device_info.from_dict(virtual_machine_vendor_device_group_info_component_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


