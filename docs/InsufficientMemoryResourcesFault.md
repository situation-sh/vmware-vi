# InsufficientMemoryResourcesFault

Memory resource admission control failed 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unreserved** | **int** | The memory available in the resource pool requested in bytes.  | 
**requested** | **int** | The memory resource amount requested in the failed operation in bytes.  | 

## Example

```python
from vmware_vi.models.insufficient_memory_resources_fault import InsufficientMemoryResourcesFault

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientMemoryResourcesFault from a JSON string
insufficient_memory_resources_fault_instance = InsufficientMemoryResourcesFault.from_json(json)
# print the JSON string representation of the object
print InsufficientMemoryResourcesFault.to_json()

# convert the object into a dict
insufficient_memory_resources_fault_dict = insufficient_memory_resources_fault_instance.to_dict()
# create an instance of InsufficientMemoryResourcesFault from a dict
insufficient_memory_resources_fault_form_dict = insufficient_memory_resources_fault.from_dict(insufficient_memory_resources_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


