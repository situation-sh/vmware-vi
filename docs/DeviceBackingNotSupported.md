# DeviceBackingNotSupported

The device is backed by a backing type which is not supported for this particular device.  If this fault is returned as a subfault of DisallowedMigrationDeviceAttached, this indicates that although this backing for the device may be supported on the destination host, the hosts do not support the requested migration of the virtual machine while using this device with this backing.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backing** | **str** | The type of the backing.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.device_backing_not_supported import DeviceBackingNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceBackingNotSupported from a JSON string
device_backing_not_supported_instance = DeviceBackingNotSupported.from_json(json)
# print the JSON string representation of the object
print DeviceBackingNotSupported.to_json()

# convert the object into a dict
device_backing_not_supported_dict = device_backing_not_supported_instance.to_dict()
# create an instance of DeviceBackingNotSupported from a dict
device_backing_not_supported_form_dict = device_backing_not_supported.from_dict(device_backing_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


