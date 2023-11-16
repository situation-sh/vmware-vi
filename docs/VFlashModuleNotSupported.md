# VFlashModuleNotSupported

vFlash module is not supported due to its configuration is not supported by the host.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | VM name  ***Since:*** vSphere API 5.5  | 
**module_name** | **str** | The vFlash module name.  ***Since:*** vSphere API 5.5  | 
**reason** | **str** | Message of reason.  ***Since:*** vSphere API 5.5  | 
**host_name** | **str** | Host name  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.v_flash_module_not_supported import VFlashModuleNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of VFlashModuleNotSupported from a JSON string
v_flash_module_not_supported_instance = VFlashModuleNotSupported.from_json(json)
# print the JSON string representation of the object
print VFlashModuleNotSupported.to_json()

# convert the object into a dict
v_flash_module_not_supported_dict = v_flash_module_not_supported_instance.to_dict()
# create an instance of VFlashModuleNotSupported from a dict
v_flash_module_not_supported_form_dict = v_flash_module_not_supported.from_dict(v_flash_module_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


