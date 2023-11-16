# ArrayOfTypeDescription

A boxed array of *TypeDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TypeDescription]**](TypeDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_type_description import ArrayOfTypeDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTypeDescription from a JSON string
array_of_type_description_instance = ArrayOfTypeDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfTypeDescription.to_json()

# convert the object into a dict
array_of_type_description_dict = array_of_type_description_instance.to_dict()
# create an instance of ArrayOfTypeDescription from a dict
array_of_type_description_form_dict = array_of_type_description.from_dict(array_of_type_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


