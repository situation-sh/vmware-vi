# DeviceControllerNotSupported

The device in question is supported, but the device-controller combination is not supported.  If this fault is returned as a subfault of DisallowedMigrationDeviceAttached, this indicates that although this device-controller combination may be supported on the destination host, the hosts do not support the requested migration of the virtual machine while using this device and controller.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | **str** | The type of the controller.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.device_controller_not_supported import DeviceControllerNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceControllerNotSupported from a JSON string
device_controller_not_supported_instance = DeviceControllerNotSupported.from_json(json)
# print the JSON string representation of the object
print DeviceControllerNotSupported.to_json()

# convert the object into a dict
device_controller_not_supported_dict = device_controller_not_supported_instance.to_dict()
# create an instance of DeviceControllerNotSupported from a dict
device_controller_not_supported_form_dict = device_controller_not_supported.from_dict(device_controller_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


