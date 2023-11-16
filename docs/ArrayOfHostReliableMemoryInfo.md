# ArrayOfHostReliableMemoryInfo

A boxed array of *HostReliableMemoryInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostReliableMemoryInfo]**](HostReliableMemoryInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_reliable_memory_info import ArrayOfHostReliableMemoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostReliableMemoryInfo from a JSON string
array_of_host_reliable_memory_info_instance = ArrayOfHostReliableMemoryInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostReliableMemoryInfo.to_json()

# convert the object into a dict
array_of_host_reliable_memory_info_dict = array_of_host_reliable_memory_info_instance.to_dict()
# create an instance of ArrayOfHostReliableMemoryInfo from a dict
array_of_host_reliable_memory_info_form_dict = array_of_host_reliable_memory_info.from_dict(array_of_host_reliable_memory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


