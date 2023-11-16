# ArrayOfInsufficientStorageSpace

A boxed array of *InsufficientStorageSpace*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InsufficientStorageSpace]**](InsufficientStorageSpace.md) |  | 

## Example

```python
from vmware_vi.models.array_of_insufficient_storage_space import ArrayOfInsufficientStorageSpace

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInsufficientStorageSpace from a JSON string
array_of_insufficient_storage_space_instance = ArrayOfInsufficientStorageSpace.from_json(json)
# print the JSON string representation of the object
print ArrayOfInsufficientStorageSpace.to_json()

# convert the object into a dict
array_of_insufficient_storage_space_dict = array_of_insufficient_storage_space_instance.to_dict()
# create an instance of ArrayOfInsufficientStorageSpace from a dict
array_of_insufficient_storage_space_form_dict = array_of_insufficient_storage_space.from_dict(array_of_insufficient_storage_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


