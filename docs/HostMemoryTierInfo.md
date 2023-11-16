# HostMemoryTierInfo

Information about a memory tier on this host.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Descriptive name for the memory tier.  ***Since:*** vSphere API 7.0.3.0  | 
**type** | **str** | Type of the memory tier.  See *HostMemoryTierType_enum* for supported values.  ***Since:*** vSphere API 7.0.3.0  | 
**flags** | **List[str]** | Flags pertaining to the memory tier.  See *HostMemoryTierFlags_enum* for supported values.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**size** | **int** | Size of the memory tier in bytes.  ***Since:*** vSphere API 7.0.3.0  | 

## Example

```python
from vmware_vi.models.host_memory_tier_info import HostMemoryTierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostMemoryTierInfo from a JSON string
host_memory_tier_info_instance = HostMemoryTierInfo.from_json(json)
# print the JSON string representation of the object
print HostMemoryTierInfo.to_json()

# convert the object into a dict
host_memory_tier_info_dict = host_memory_tier_info_instance.to_dict()
# create an instance of HostMemoryTierInfo from a dict
host_memory_tier_info_form_dict = host_memory_tier_info.from_dict(host_memory_tier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


