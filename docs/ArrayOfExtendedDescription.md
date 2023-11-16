# ArrayOfExtendedDescription

A boxed array of *ExtendedDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtendedDescription]**](ExtendedDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_extended_description import ArrayOfExtendedDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtendedDescription from a JSON string
array_of_extended_description_instance = ArrayOfExtendedDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtendedDescription.to_json()

# convert the object into a dict
array_of_extended_description_dict = array_of_extended_description_instance.to_dict()
# create an instance of ArrayOfExtendedDescription from a dict
array_of_extended_description_form_dict = array_of_extended_description.from_dict(array_of_extended_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


