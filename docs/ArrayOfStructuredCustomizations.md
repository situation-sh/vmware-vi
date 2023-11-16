# ArrayOfStructuredCustomizations

A boxed array of *StructuredCustomizations*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StructuredCustomizations]**](StructuredCustomizations.md) |  | 

## Example

```python
from vmware_vi.models.array_of_structured_customizations import ArrayOfStructuredCustomizations

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStructuredCustomizations from a JSON string
array_of_structured_customizations_instance = ArrayOfStructuredCustomizations.from_json(json)
# print the JSON string representation of the object
print ArrayOfStructuredCustomizations.to_json()

# convert the object into a dict
array_of_structured_customizations_dict = array_of_structured_customizations_instance.to_dict()
# create an instance of ArrayOfStructuredCustomizations from a dict
array_of_structured_customizations_form_dict = array_of_structured_customizations.from_dict(array_of_structured_customizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


