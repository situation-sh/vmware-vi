# VirtualPointingDeviceDeviceBackingInfo

The VirtualPointingDevice.DeviceBackingInfo provides information about the physical mouse backing the VirtualPointingDevice data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_pointing_device** | **str** | This optional property defines the mouse type (two-button, three-button, and so on).  The mouse type determines how the user interacts with the host mouse. The valid values are specified in the *VirtualPointingDeviceHostChoice_enum* list.  **Note**: The value specified by this property must be one of the supported types listed in the hostPointingDevices.value array in the *VirtualPointingDeviceOption* data object type. If this property is not set, then the property defaults to the hostPointingDevices.defaultIndex property in the same data object type.  | 

## Example

```python
from vmware_vi.models.virtual_pointing_device_device_backing_info import VirtualPointingDeviceDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPointingDeviceDeviceBackingInfo from a JSON string
virtual_pointing_device_device_backing_info_instance = VirtualPointingDeviceDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualPointingDeviceDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_pointing_device_device_backing_info_dict = virtual_pointing_device_device_backing_info_instance.to_dict()
# create an instance of VirtualPointingDeviceDeviceBackingInfo from a dict
virtual_pointing_device_device_backing_info_form_dict = virtual_pointing_device_device_backing_info.from_dict(virtual_pointing_device_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


