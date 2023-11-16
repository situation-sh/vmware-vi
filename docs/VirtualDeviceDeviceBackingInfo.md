# VirtualDeviceDeviceBackingInfo

The <code>*VirtualDeviceDeviceBackingInfo*</code> data object type defines information about a host device or resource that backs a device in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | The name of the device on the host system.  | 
**use_auto_detect** | **bool** | Indicates whether the device should be auto detected instead of directly specified.  If this value is set to TRUE, deviceName is ignored.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_device_device_backing_info import VirtualDeviceDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceDeviceBackingInfo from a JSON string
virtual_device_device_backing_info_instance = VirtualDeviceDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_device_device_backing_info_dict = virtual_device_device_backing_info_instance.to_dict()
# create an instance of VirtualDeviceDeviceBackingInfo from a dict
virtual_device_device_backing_info_form_dict = virtual_device_device_backing_info.from_dict(virtual_device_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


