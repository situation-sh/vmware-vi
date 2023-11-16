# ArrayOfInvalidBundle

A boxed array of *InvalidBundle*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidBundle]**](InvalidBundle.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_bundle import ArrayOfInvalidBundle

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidBundle from a JSON string
array_of_invalid_bundle_instance = ArrayOfInvalidBundle.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidBundle.to_json()

# convert the object into a dict
array_of_invalid_bundle_dict = array_of_invalid_bundle_instance.to_dict()
# create an instance of ArrayOfInvalidBundle from a dict
array_of_invalid_bundle_form_dict = array_of_invalid_bundle.from_dict(array_of_invalid_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


