# VirtualAppImportSpec

A VAppImportSpec is used by *ResourcePool.importVApp* when importing vApps (single VM or multi-VM).  It provides all information needed to import a *VirtualApp*.  See also *ImportSpec*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the vApp  ***Since:*** vSphere API 4.0  | 
**v_app_config_spec** | [**VAppConfigSpec**](VAppConfigSpec.md) |  | 
**resource_pool_spec** | [**ResourceConfigSpec**](ResourceConfigSpec.md) |  | 
**child** | [**List[ImportSpec]**](ImportSpec.md) | Contains a list of children (*VirtualMachine*s and *VirtualApp*s).  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_app_import_spec import VirtualAppImportSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAppImportSpec from a JSON string
virtual_app_import_spec_instance = VirtualAppImportSpec.from_json(json)
# print the JSON string representation of the object
print VirtualAppImportSpec.to_json()

# convert the object into a dict
virtual_app_import_spec_dict = virtual_app_import_spec_instance.to_dict()
# create an instance of VirtualAppImportSpec from a dict
virtual_app_import_spec_form_dict = virtual_app_import_spec.from_dict(virtual_app_import_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


