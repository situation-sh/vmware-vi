# ArrayOfInvalidDeviceSpec

A boxed array of *InvalidDeviceSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidDeviceSpec]**](InvalidDeviceSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_device_spec import ArrayOfInvalidDeviceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidDeviceSpec from a JSON string
array_of_invalid_device_spec_instance = ArrayOfInvalidDeviceSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidDeviceSpec.to_json()

# convert the object into a dict
array_of_invalid_device_spec_dict = array_of_invalid_device_spec_instance.to_dict()
# create an instance of ArrayOfInvalidDeviceSpec from a dict
array_of_invalid_device_spec_form_dict = array_of_invalid_device_spec.from_dict(array_of_invalid_device_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


