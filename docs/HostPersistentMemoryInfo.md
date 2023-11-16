# HostPersistentMemoryInfo

Host Hardware information about configured and available persistent memory on a host.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_in_mb** | **int** | Amount of configured persistent memory available on a host in MB.  ***Since:*** vSphere API 6.7  | [optional] 
**volume_uuid** | **str** | Unique persistent memory host indentifier.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.host_persistent_memory_info import HostPersistentMemoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostPersistentMemoryInfo from a JSON string
host_persistent_memory_info_instance = HostPersistentMemoryInfo.from_json(json)
# print the JSON string representation of the object
print HostPersistentMemoryInfo.to_json()

# convert the object into a dict
host_persistent_memory_info_dict = host_persistent_memory_info_instance.to_dict()
# create an instance of HostPersistentMemoryInfo from a dict
host_persistent_memory_info_form_dict = host_persistent_memory_info.from_dict(host_persistent_memory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


