# MemorySizeNotSupportedByDatastore

The memory amount of the virtual machine is not within the acceptable guest memory bounds supported by the virtual machine's datastore.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**memory_size_mb** | **int** | The configured memory size of the virtual machine.  ***Since:*** vSphere API 5.0  | 
**max_memory_size_mb** | **int** | The maximum acceptable memory size supported by the datastore.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.memory_size_not_supported_by_datastore import MemorySizeNotSupportedByDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of MemorySizeNotSupportedByDatastore from a JSON string
memory_size_not_supported_by_datastore_instance = MemorySizeNotSupportedByDatastore.from_json(json)
# print the JSON string representation of the object
print MemorySizeNotSupportedByDatastore.to_json()

# convert the object into a dict
memory_size_not_supported_by_datastore_dict = memory_size_not_supported_by_datastore_instance.to_dict()
# create an instance of MemorySizeNotSupportedByDatastore from a dict
memory_size_not_supported_by_datastore_form_dict = memory_size_not_supported_by_datastore.from_dict(memory_size_not_supported_by_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


