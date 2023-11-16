# VFlashModuleVersionIncompatible

The vFlash module version of the vFlash cache asscociated with the virtual disk of a VM is not compatible with the supported versions of the specified vFlash module on the host.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_name** | **str** | The vFlash module name.  ***Since:*** vSphere API 5.5  | 
**vm_request_module_version** | **str** | The VM request module version.  ***Since:*** vSphere API 5.5  | 
**host_min_supported_verson** | **str** | The minimum supported version of the specified module on the host.  ***Since:*** vSphere API 5.5  | 
**host_module_version** | **str** | The verson of the specified module on the host.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.v_flash_module_version_incompatible import VFlashModuleVersionIncompatible

# TODO update the JSON string below
json = "{}"
# create an instance of VFlashModuleVersionIncompatible from a JSON string
v_flash_module_version_incompatible_instance = VFlashModuleVersionIncompatible.from_json(json)
# print the JSON string representation of the object
print VFlashModuleVersionIncompatible.to_json()

# convert the object into a dict
v_flash_module_version_incompatible_dict = v_flash_module_version_incompatible_instance.to_dict()
# create an instance of VFlashModuleVersionIncompatible from a dict
v_flash_module_version_incompatible_form_dict = v_flash_module_version_incompatible.from_dict(v_flash_module_version_incompatible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


