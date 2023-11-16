# HostConfigVFlashCacheRequestType

The parameters of *HostVFlashManager.HostConfigVFlashCache*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostVFlashManagerVFlashCacheConfigSpec**](HostVFlashManagerVFlashCacheConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_config_v_flash_cache_request_type import HostConfigVFlashCacheRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigVFlashCacheRequestType from a JSON string
host_config_v_flash_cache_request_type_instance = HostConfigVFlashCacheRequestType.from_json(json)
# print the JSON string representation of the object
print HostConfigVFlashCacheRequestType.to_json()

# convert the object into a dict
host_config_v_flash_cache_request_type_dict = host_config_v_flash_cache_request_type_instance.to_dict()
# create an instance of HostConfigVFlashCacheRequestType from a dict
host_config_v_flash_cache_request_type_form_dict = host_config_v_flash_cache_request_type.from_dict(host_config_v_flash_cache_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


