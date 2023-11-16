# ArrayOfStorageIOAllocationInfo

A boxed array of *StorageIOAllocationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageIOAllocationInfo]**](StorageIOAllocationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_io_allocation_info import ArrayOfStorageIOAllocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageIOAllocationInfo from a JSON string
array_of_storage_io_allocation_info_instance = ArrayOfStorageIOAllocationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageIOAllocationInfo.to_json()

# convert the object into a dict
array_of_storage_io_allocation_info_dict = array_of_storage_io_allocation_info_instance.to_dict()
# create an instance of ArrayOfStorageIOAllocationInfo from a dict
array_of_storage_io_allocation_info_form_dict = array_of_storage_io_allocation_info.from_dict(array_of_storage_io_allocation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


