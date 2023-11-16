# HostCacheConfigurationSpec

Host cache configuration specification.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**swap_size** | **int** | Space to allocate on this datastore to implement swap performance enhancements, in MB.  This value should be less or equal to free space capacity on the datastore *DatastoreSummary.freeSpace*.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_cache_configuration_spec import HostCacheConfigurationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostCacheConfigurationSpec from a JSON string
host_cache_configuration_spec_instance = HostCacheConfigurationSpec.from_json(json)
# print the JSON string representation of the object
print HostCacheConfigurationSpec.to_json()

# convert the object into a dict
host_cache_configuration_spec_dict = host_cache_configuration_spec_instance.to_dict()
# create an instance of HostCacheConfigurationSpec from a dict
host_cache_configuration_spec_form_dict = host_cache_configuration_spec.from_dict(host_cache_configuration_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


