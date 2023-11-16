# TooManyDevices

Thrown when the number of virtual devices exceeds the maximum for a given controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.too_many_devices import TooManyDevices

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyDevices from a JSON string
too_many_devices_instance = TooManyDevices.from_json(json)
# print the JSON string representation of the object
print TooManyDevices.to_json()

# convert the object into a dict
too_many_devices_dict = too_many_devices_instance.to_dict()
# create an instance of TooManyDevices from a dict
too_many_devices_form_dict = too_many_devices.from_dict(too_many_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


