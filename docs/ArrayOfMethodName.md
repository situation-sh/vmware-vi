# ArrayOfMethodName

A boxed array of *PrimitiveMethodName*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[str]** |  | 

## Example

```python
from vmware_vi.models.array_of_method_name import ArrayOfMethodName

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMethodName from a JSON string
array_of_method_name_instance = ArrayOfMethodName.from_json(json)
# print the JSON string representation of the object
print ArrayOfMethodName.to_json()

# convert the object into a dict
array_of_method_name_dict = array_of_method_name_instance.to_dict()
# create an instance of ArrayOfMethodName from a dict
array_of_method_name_form_dict = array_of_method_name.from_dict(array_of_method_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


