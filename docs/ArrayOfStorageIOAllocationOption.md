# ArrayOfStorageIOAllocationOption

A boxed array of *StorageIOAllocationOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageIOAllocationOption]**](StorageIOAllocationOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_io_allocation_option import ArrayOfStorageIOAllocationOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageIOAllocationOption from a JSON string
array_of_storage_io_allocation_option_instance = ArrayOfStorageIOAllocationOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageIOAllocationOption.to_json()

# convert the object into a dict
array_of_storage_io_allocation_option_dict = array_of_storage_io_allocation_option_instance.to_dict()
# create an instance of ArrayOfStorageIOAllocationOption from a dict
array_of_storage_io_allocation_option_form_dict = array_of_storage_io_allocation_option.from_dict(array_of_storage_io_allocation_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


