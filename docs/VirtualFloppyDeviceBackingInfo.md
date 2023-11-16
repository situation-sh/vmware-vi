# VirtualFloppyDeviceBackingInfo

The data object type for device backing of a virtual floppy drive. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_floppy_device_backing_info import VirtualFloppyDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualFloppyDeviceBackingInfo from a JSON string
virtual_floppy_device_backing_info_instance = VirtualFloppyDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualFloppyDeviceBackingInfo.to_json()

# convert the object into a dict
virtual_floppy_device_backing_info_dict = virtual_floppy_device_backing_info_instance.to_dict()
# create an instance of VirtualFloppyDeviceBackingInfo from a dict
virtual_floppy_device_backing_info_form_dict = virtual_floppy_device_backing_info.from_dict(virtual_floppy_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


