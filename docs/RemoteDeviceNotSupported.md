# RemoteDeviceNotSupported

The virtual machine has a currently connected device with a remote backing.  This is an error when migrating a powered-on virtual machine, and can be returned as a subfault of DisallowedMigrationDeviceAttached. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.remote_device_not_supported import RemoteDeviceNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteDeviceNotSupported from a JSON string
remote_device_not_supported_instance = RemoteDeviceNotSupported.from_json(json)
# print the JSON string representation of the object
print RemoteDeviceNotSupported.to_json()

# convert the object into a dict
remote_device_not_supported_dict = remote_device_not_supported_instance.to_dict()
# create an instance of RemoteDeviceNotSupported from a dict
remote_device_not_supported_form_dict = remote_device_not_supported.from_dict(remote_device_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


