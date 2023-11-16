# HostGetVFlashModuleDefaultConfigRequestType

The parameters of *HostVFlashManager.HostGetVFlashModuleDefaultConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_flash_module** | **str** | Name of the vFlash module  | 

## Example

```python
from vmware_vi.models.host_get_v_flash_module_default_config_request_type import HostGetVFlashModuleDefaultConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostGetVFlashModuleDefaultConfigRequestType from a JSON string
host_get_v_flash_module_default_config_request_type_instance = HostGetVFlashModuleDefaultConfigRequestType.from_json(json)
# print the JSON string representation of the object
print HostGetVFlashModuleDefaultConfigRequestType.to_json()

# convert the object into a dict
host_get_v_flash_module_default_config_request_type_dict = host_get_v_flash_module_default_config_request_type_instance.to_dict()
# create an instance of HostGetVFlashModuleDefaultConfigRequestType from a dict
host_get_v_flash_module_default_config_request_type_form_dict = host_get_v_flash_module_default_config_request_type.from_dict(host_get_v_flash_module_default_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


