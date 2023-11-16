# HostDevice

This data object type defines a device on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | The name of the device on the host.  For example, /dev/cdrom or \\\\\\\\serverX\\\\device\\_name.  | 
**device_type** | **str** | Device type when available: floppy, mouse, cdrom, disk, scsi device, or adapter.  | 

## Example

```python
from vmware_vi.models.host_device import HostDevice

# TODO update the JSON string below
json = "{}"
# create an instance of HostDevice from a JSON string
host_device_instance = HostDevice.from_json(json)
# print the JSON string representation of the object
print HostDevice.to_json()

# convert the object into a dict
host_device_dict = host_device_instance.to_dict()
# create an instance of HostDevice from a dict
host_device_form_dict = host_device.from_dict(host_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


