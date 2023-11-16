# ConfigureHostCacheRequestType

The parameters of *HostCacheConfigurationManager.ConfigureHostCache_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostCacheConfigurationSpec**](HostCacheConfigurationSpec.md) |  | 

## Example

```python
from vmware_vi.models.configure_host_cache_request_type import ConfigureHostCacheRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureHostCacheRequestType from a JSON string
configure_host_cache_request_type_instance = ConfigureHostCacheRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureHostCacheRequestType.to_json()

# convert the object into a dict
configure_host_cache_request_type_dict = configure_host_cache_request_type_instance.to_dict()
# create an instance of ConfigureHostCacheRequestType from a dict
configure_host_cache_request_type_form_dict = configure_host_cache_request_type.from_dict(configure_host_cache_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


