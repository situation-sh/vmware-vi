# ArrayOfInsufficientStorageIops

A boxed array of *InsufficientStorageIops*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InsufficientStorageIops]**](InsufficientStorageIops.md) |  | 

## Example

```python
from vmware_vi.models.array_of_insufficient_storage_iops import ArrayOfInsufficientStorageIops

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInsufficientStorageIops from a JSON string
array_of_insufficient_storage_iops_instance = ArrayOfInsufficientStorageIops.from_json(json)
# print the JSON string representation of the object
print ArrayOfInsufficientStorageIops.to_json()

# convert the object into a dict
array_of_insufficient_storage_iops_dict = array_of_insufficient_storage_iops_instance.to_dict()
# create an instance of ArrayOfInsufficientStorageIops from a dict
array_of_insufficient_storage_iops_form_dict = array_of_insufficient_storage_iops.from_dict(array_of_insufficient_storage_iops_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


