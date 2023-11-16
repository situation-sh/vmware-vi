# MemorySizeNotSupported

The memory amount of the virtual machine is not within the acceptable guest memory bounds supported by the virtual machine's host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_size_mb** | **int** | The configured memory size of the virtual machine.  ***Since:*** VI API 2.5  | 
**min_memory_size_mb** | **int** | The minimum acceptable memory size.  ***Since:*** VI API 2.5  | 
**max_memory_size_mb** | **int** | The maximum acceptable memory size.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.memory_size_not_supported import MemorySizeNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of MemorySizeNotSupported from a JSON string
memory_size_not_supported_instance = MemorySizeNotSupported.from_json(json)
# print the JSON string representation of the object
print MemorySizeNotSupported.to_json()

# convert the object into a dict
memory_size_not_supported_dict = memory_size_not_supported_instance.to_dict()
# create an instance of MemorySizeNotSupported from a dict
memory_size_not_supported_form_dict = memory_size_not_supported.from_dict(memory_size_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


