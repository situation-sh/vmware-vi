# MemorySizeNotRecommended

The memory amount of the virtual machine is not within the recommended memory bounds for the virtual machine's guest OS.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_size_mb** | **int** | The configured memory size of the virtual machine.  ***Since:*** VI API 2.5  | 
**min_memory_size_mb** | **int** | The minimum recommended memory size.  ***Since:*** VI API 2.5  | 
**max_memory_size_mb** | **int** | The maximum recommended memory size.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.memory_size_not_recommended import MemorySizeNotRecommended

# TODO update the JSON string below
json = "{}"
# create an instance of MemorySizeNotRecommended from a JSON string
memory_size_not_recommended_instance = MemorySizeNotRecommended.from_json(json)
# print the JSON string representation of the object
print MemorySizeNotRecommended.to_json()

# convert the object into a dict
memory_size_not_recommended_dict = memory_size_not_recommended_instance.to_dict()
# create an instance of MemorySizeNotRecommended from a dict
memory_size_not_recommended_form_dict = memory_size_not_recommended.from_dict(memory_size_not_recommended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


