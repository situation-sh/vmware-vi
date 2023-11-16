# StorageIOAllocationOption

The IOAllocationOption specifies value ranges that can be used to initialize *StorageIOAllocationInfo* object.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_option** | [**LongOption**](LongOption.md) |  | 
**shares_option** | [**SharesOption**](SharesOption.md) |  | 

## Example

```python
from vmware_vi.models.storage_io_allocation_option import StorageIOAllocationOption

# TODO update the JSON string below
json = "{}"
# create an instance of StorageIOAllocationOption from a JSON string
storage_io_allocation_option_instance = StorageIOAllocationOption.from_json(json)
# print the JSON string representation of the object
print StorageIOAllocationOption.to_json()

# convert the object into a dict
storage_io_allocation_option_dict = storage_io_allocation_option_instance.to_dict()
# create an instance of StorageIOAllocationOption from a dict
storage_io_allocation_option_form_dict = storage_io_allocation_option.from_dict(storage_io_allocation_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


