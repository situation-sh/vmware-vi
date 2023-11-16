# InvalidDeviceBacking

An InvalidDeviceBacking exception is thrown if a device with an incompatible device backing is added or edited. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_device_backing import InvalidDeviceBacking

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDeviceBacking from a JSON string
invalid_device_backing_instance = InvalidDeviceBacking.from_json(json)
# print the JSON string representation of the object
print InvalidDeviceBacking.to_json()

# convert the object into a dict
invalid_device_backing_dict = invalid_device_backing_instance.to_dict()
# create an instance of InvalidDeviceBacking from a dict
invalid_device_backing_form_dict = invalid_device_backing.from_dict(invalid_device_backing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


