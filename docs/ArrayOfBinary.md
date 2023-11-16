# ArrayOfBinary

A boxed array of *PrimitiveBinary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[bytearray]** |  | 

## Example

```python
from vmware_vi.models.array_of_binary import ArrayOfBinary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfBinary from a JSON string
array_of_binary_instance = ArrayOfBinary.from_json(json)
# print the JSON string representation of the object
print ArrayOfBinary.to_json()

# convert the object into a dict
array_of_binary_dict = array_of_binary_instance.to_dict()
# create an instance of ArrayOfBinary from a dict
array_of_binary_form_dict = array_of_binary.from_dict(array_of_binary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


