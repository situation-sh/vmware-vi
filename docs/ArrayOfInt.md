# ArrayOfInt

A boxed array of *PrimitiveInt*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[int]** |  | 

## Example

```python
from vmware_vi.models.array_of_int import ArrayOfInt

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInt from a JSON string
array_of_int_instance = ArrayOfInt.from_json(json)
# print the JSON string representation of the object
print ArrayOfInt.to_json()

# convert the object into a dict
array_of_int_dict = array_of_int_instance.to_dict()
# create an instance of ArrayOfInt from a dict
array_of_int_form_dict = array_of_int.from_dict(array_of_int_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


