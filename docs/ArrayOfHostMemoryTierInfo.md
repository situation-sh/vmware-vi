# ArrayOfHostMemoryTierInfo

A boxed array of *HostMemoryTierInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMemoryTierInfo]**](HostMemoryTierInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_memory_tier_info import ArrayOfHostMemoryTierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMemoryTierInfo from a JSON string
array_of_host_memory_tier_info_instance = ArrayOfHostMemoryTierInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMemoryTierInfo.to_json()

# convert the object into a dict
array_of_host_memory_tier_info_dict = array_of_host_memory_tier_info_instance.to_dict()
# create an instance of ArrayOfHostMemoryTierInfo from a dict
array_of_host_memory_tier_info_form_dict = array_of_host_memory_tier_info.from_dict(array_of_host_memory_tier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


