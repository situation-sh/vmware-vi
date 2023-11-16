# VirtualDeviceBackingInfo

<code>*VirtualDeviceBackingInfo*</code> is a base data object type for information about the backing of a device in a virtual machine.  This base type does not define any properties. It is used as a namespace for general-purpose subtypes. Specific devices are represented by subtypes which define properties for device-specific backing information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_device_backing_info import VirtualDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceBackingInfo from a JSON string
virtual_device_backing_info_instance = VirtualDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_device_backing_info_dict = virtual_device_backing_info_instance.to_dict()
# create an instance of VirtualDeviceBackingInfo from a dict
virtual_device_backing_info_form_dict = virtual_device_backing_info.from_dict(virtual_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


