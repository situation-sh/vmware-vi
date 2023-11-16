# ArrayOfByte

A boxed array of *PrimitiveByte*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[int]** |  | 

## Example

```python
from vmware_vi.models.array_of_byte import ArrayOfByte

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfByte from a JSON string
array_of_byte_instance = ArrayOfByte.from_json(json)
# print the JSON string representation of the object
print ArrayOfByte.to_json()

# convert the object into a dict
array_of_byte_dict = array_of_byte_instance.to_dict()
# create an instance of ArrayOfByte from a dict
array_of_byte_form_dict = array_of_byte.from_dict(array_of_byte_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


