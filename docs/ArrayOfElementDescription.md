# ArrayOfElementDescription

A boxed array of *ElementDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ElementDescription]**](ElementDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_element_description import ArrayOfElementDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfElementDescription from a JSON string
array_of_element_description_instance = ArrayOfElementDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfElementDescription.to_json()

# convert the object into a dict
array_of_element_description_dict = array_of_element_description_instance.to_dict()
# create an instance of ArrayOfElementDescription from a dict
array_of_element_description_form_dict = array_of_element_description.from_dict(array_of_element_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


