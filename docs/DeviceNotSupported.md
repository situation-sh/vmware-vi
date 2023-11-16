# DeviceNotSupported

The virtual machine uses a device type that is not supported on the host.  If this fault is returned as a subfault of *DisallowedMigrationDeviceAttached*, this indicates that although this device may be supported on the destination host, the hosts do not support the requested migration of the virtual machine while using this device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of the device.  | 
**reason** | **str** | The specific reason why the device is not supported.  Values should come from *DeviceNotSupportedReason_enum*. This might not be set if we&#39;re not sure of the reason, or if this doesn&#39;t make sense in the context. For example, in the *DisallowedMigrationDeviceAttached* context we already know the problem.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.device_not_supported import DeviceNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceNotSupported from a JSON string
device_not_supported_instance = DeviceNotSupported.from_json(json)
# print the JSON string representation of the object
print DeviceNotSupported.to_json()

# convert the object into a dict
device_not_supported_dict = device_not_supported_instance.to_dict()
# create an instance of DeviceNotSupported from a dict
device_not_supported_form_dict = device_not_supported.from_dict(device_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


