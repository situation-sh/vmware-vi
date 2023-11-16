# ArrayOfStoragePlacementResult

A boxed array of *StoragePlacementResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StoragePlacementResult]**](StoragePlacementResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_placement_result import ArrayOfStoragePlacementResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStoragePlacementResult from a JSON string
array_of_storage_placement_result_instance = ArrayOfStoragePlacementResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfStoragePlacementResult.to_json()

# convert the object into a dict
array_of_storage_placement_result_dict = array_of_storage_placement_result_instance.to_dict()
# create an instance of ArrayOfStoragePlacementResult from a dict
array_of_storage_placement_result_form_dict = array_of_storage_placement_result.from_dict(array_of_storage_placement_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


