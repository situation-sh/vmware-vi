# VirtualSCSIPassthroughDeviceBackingInfo

The VirtualSCSIPassthrough.DeviceBackingInfo data object type contains information about the backing that maps the virtual device onto a physical device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_scsi_passthrough_device_backing_info import VirtualSCSIPassthroughDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSCSIPassthroughDeviceBackingInfo from a JSON string
virtual_scsi_passthrough_device_backing_info_instance = VirtualSCSIPassthroughDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualSCSIPassthroughDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_scsi_passthrough_device_backing_info_dict = virtual_scsi_passthrough_device_backing_info_instance.to_dict()
# create an instance of VirtualSCSIPassthroughDeviceBackingInfo from a dict
virtual_scsi_passthrough_device_backing_info_form_dict = virtual_scsi_passthrough_device_backing_info.from_dict(virtual_scsi_passthrough_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


