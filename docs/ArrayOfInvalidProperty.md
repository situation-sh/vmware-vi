# ArrayOfInvalidProperty

A boxed array of *InvalidProperty*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidProperty]**](InvalidProperty.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_property import ArrayOfInvalidProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidProperty from a JSON string
array_of_invalid_property_instance = ArrayOfInvalidProperty.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidProperty.to_json()

# convert the object into a dict
array_of_invalid_property_dict = array_of_invalid_property_instance.to_dict()
# create an instance of ArrayOfInvalidProperty from a dict
array_of_invalid_property_form_dict = array_of_invalid_property.from_dict(array_of_invalid_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


