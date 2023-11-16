# ArrayOfBoolean

A boxed array of *PrimitiveBoolean*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[bool]** |  | 

## Example

```python
from vmware_vi.models.array_of_boolean import ArrayOfBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfBoolean from a JSON string
array_of_boolean_instance = ArrayOfBoolean.from_json(json)
# print the JSON string representation of the object
print ArrayOfBoolean.to_json()

# convert the object into a dict
array_of_boolean_dict = array_of_boolean_instance.to_dict()
# create an instance of ArrayOfBoolean from a dict
array_of_boolean_form_dict = array_of_boolean.from_dict(array_of_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


