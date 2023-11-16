# ArrayOfInvalidDeviceBacking

A boxed array of *InvalidDeviceBacking*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidDeviceBacking]**](InvalidDeviceBacking.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_device_backing import ArrayOfInvalidDeviceBacking

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidDeviceBacking from a JSON string
array_of_invalid_device_backing_instance = ArrayOfInvalidDeviceBacking.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidDeviceBacking.to_json()

# convert the object into a dict
array_of_invalid_device_backing_dict = array_of_invalid_device_backing_instance.to_dict()
# create an instance of ArrayOfInvalidDeviceBacking from a dict
array_of_invalid_device_backing_form_dict = array_of_invalid_device_backing.from_dict(array_of_invalid_device_backing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


