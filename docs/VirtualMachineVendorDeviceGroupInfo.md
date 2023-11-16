# VirtualMachineVendorDeviceGroupInfo

Description of a PCI vendor device group device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_group_name** | **str** | Name of Vendor Device Group.  | 
**device_group_description** | **str** | Description of Vendor Device Group.  | [optional] 
**component_device_info** | [**List[VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo]**](VirtualMachineVendorDeviceGroupInfoComponentDeviceInfo.md) | Array describing component devices of this Vendor Device Group.  There is one entry per componentDevice in the deviceGroupSpec.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_vendor_device_group_info import VirtualMachineVendorDeviceGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVendorDeviceGroupInfo from a JSON string
virtual_machine_vendor_device_group_info_instance = VirtualMachineVendorDeviceGroupInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVendorDeviceGroupInfo.to_json()

# convert the object into a dict
virtual_machine_vendor_device_group_info_dict = virtual_machine_vendor_device_group_info_instance.to_dict()
# create an instance of VirtualMachineVendorDeviceGroupInfo from a dict
virtual_machine_vendor_device_group_info_form_dict = virtual_machine_vendor_device_group_info.from_dict(virtual_machine_vendor_device_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


