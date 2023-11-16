# HostCacheConfigurationInfo

Host solid state drive cache configuration information.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**swap_size** | **int** | Space allocated on this datastore to implement swap performance enhancements, in MB.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_cache_configuration_info import HostCacheConfigurationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostCacheConfigurationInfo from a JSON string
host_cache_configuration_info_instance = HostCacheConfigurationInfo.from_json(json)
# print the JSON string representation of the object
print HostCacheConfigurationInfo.to_json()

# convert the object into a dict
host_cache_configuration_info_dict = host_cache_configuration_info_instance.to_dict()
# create an instance of HostCacheConfigurationInfo from a dict
host_cache_configuration_info_form_dict = host_cache_configuration_info.from_dict(host_cache_configuration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


