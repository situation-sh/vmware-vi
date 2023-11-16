# ArrayOfMethodDescription

A boxed array of *MethodDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MethodDescription]**](MethodDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_method_description import ArrayOfMethodDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMethodDescription from a JSON string
array_of_method_description_instance = ArrayOfMethodDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfMethodDescription.to_json()

# convert the object into a dict
array_of_method_description_dict = array_of_method_description_instance.to_dict()
# create an instance of ArrayOfMethodDescription from a dict
array_of_method_description_form_dict = array_of_method_description.from_dict(array_of_method_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


