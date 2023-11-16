# HostReliableMemoryInfo

Information about reliable memory installed on this host.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_size** | **int** |  | 

## Example

```python
from vmware_vi.models.host_reliable_memory_info import HostReliableMemoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostReliableMemoryInfo from a JSON string
host_reliable_memory_info_instance = HostReliableMemoryInfo.from_json(json)
# print the JSON string representation of the object
print HostReliableMemoryInfo.to_json()

# convert the object into a dict
host_reliable_memory_info_dict = host_reliable_memory_info_instance.to_dict()
# create an instance of HostReliableMemoryInfo from a dict
host_reliable_memory_info_form_dict = host_reliable_memory_info.from_dict(host_reliable_memory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


