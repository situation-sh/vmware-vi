# HostVFlashManagerVFlashResourceConfigSpec

vFlash resource configuration specification.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vffs_uuid** | **str** | The contained VFFS volume uuid.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_v_flash_manager_v_flash_resource_config_spec import HostVFlashManagerVFlashResourceConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVFlashManagerVFlashResourceConfigSpec from a JSON string
host_v_flash_manager_v_flash_resource_config_spec_instance = HostVFlashManagerVFlashResourceConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostVFlashManagerVFlashResourceConfigSpec.to_json()

# convert the object into a dict
host_v_flash_manager_v_flash_resource_config_spec_dict = host_v_flash_manager_v_flash_resource_config_spec_instance.to_dict()
# create an instance of HostVFlashManagerVFlashResourceConfigSpec from a dict
host_v_flash_manager_v_flash_resource_config_spec_form_dict = host_v_flash_manager_v_flash_resource_config_spec.from_dict(host_v_flash_manager_v_flash_resource_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


