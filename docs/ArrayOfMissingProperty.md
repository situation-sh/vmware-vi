# ArrayOfMissingProperty

A boxed array of *MissingProperty*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MissingProperty]**](MissingProperty.md) |  | 

## Example

```python
from vmware_vi.models.array_of_missing_property import ArrayOfMissingProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMissingProperty from a JSON string
array_of_missing_property_instance = ArrayOfMissingProperty.from_json(json)
# print the JSON string representation of the object
print ArrayOfMissingProperty.to_json()

# convert the object into a dict
array_of_missing_property_dict = array_of_missing_property_instance.to_dict()
# create an instance of ArrayOfMissingProperty from a dict
array_of_missing_property_form_dict = array_of_missing_property.from_dict(array_of_missing_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


