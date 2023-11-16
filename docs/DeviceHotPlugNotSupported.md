# DeviceHotPlugNotSupported

A DeviceHotPlugNotSupported exception is thrown if the specified device cannot be hot-added or hot-removed from the virtual machine at this time.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.device_hot_plug_not_supported import DeviceHotPlugNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceHotPlugNotSupported from a JSON string
device_hot_plug_not_supported_instance = DeviceHotPlugNotSupported.from_json(json)
# print the JSON string representation of the object
print DeviceHotPlugNotSupported.to_json()

# convert the object into a dict
device_hot_plug_not_supported_dict = device_hot_plug_not_supported_instance.to_dict()
# create an instance of DeviceHotPlugNotSupported from a dict
device_hot_plug_not_supported_form_dict = device_hot_plug_not_supported.from_dict(device_hot_plug_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


