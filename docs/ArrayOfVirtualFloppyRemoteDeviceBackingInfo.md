# ArrayOfVirtualFloppyRemoteDeviceBackingInfo

A boxed array of *VirtualFloppyRemoteDeviceBackingInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualFloppyRemoteDeviceBackingInfo]**](VirtualFloppyRemoteDeviceBackingInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_floppy_remote_device_backing_info import ArrayOfVirtualFloppyRemoteDeviceBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualFloppyRemoteDeviceBackingInfo from a JSON string
array_of_virtual_floppy_remote_device_backing_info_instance = ArrayOfVirtualFloppyRemoteDeviceBackingInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualFloppyRemoteDeviceBackingInfo.to_json()

# convert the object into a dict
array_of_virtual_floppy_remote_device_backing_info_dict = array_of_virtual_floppy_remote_device_backing_info_instance.to_dict()
# create an instance of ArrayOfVirtualFloppyRemoteDeviceBackingInfo from a dict
array_of_virtual_floppy_remote_device_backing_info_form_dict = array_of_virtual_floppy_remote_device_backing_info.from_dict(array_of_virtual_floppy_remote_device_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


