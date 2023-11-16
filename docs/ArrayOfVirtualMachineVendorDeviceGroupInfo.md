# ArrayOfVirtualMachineVendorDeviceGroupInfo

A boxed array of *VirtualMachineVendorDeviceGroupInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVendorDeviceGroupInfo]**](VirtualMachineVendorDeviceGroupInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_vendor_device_group_info import ArrayOfVirtualMachineVendorDeviceGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVendorDeviceGroupInfo from a JSON string
array_of_virtual_machine_vendor_device_group_info_instance = ArrayOfVirtualMachineVendorDeviceGroupInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVendorDeviceGroupInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_vendor_device_group_info_dict = array_of_virtual_machine_vendor_device_group_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVendorDeviceGroupInfo from a dict
array_of_virtual_machine_vendor_device_group_info_form_dict = array_of_virtual_machine_vendor_device_group_info.from_dict(array_of_virtual_machine_vendor_device_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


