# DeviceNotFound

A DeviceNotFound exception is thrown if a device to be edited or removed cannot be found.  Most likely, the client incorrectly passed the device key. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.device_not_found import DeviceNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceNotFound from a JSON string
device_not_found_instance = DeviceNotFound.from_json(json)
# print the JSON string representation of the object
print DeviceNotFound.to_json()

# convert the object into a dict
device_not_found_dict = device_not_found_instance.to_dict()
# create an instance of DeviceNotFound from a dict
device_not_found_form_dict = device_not_found.from_dict(device_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


