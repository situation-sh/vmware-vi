# VirtualMachineImportSpec

A VmImportSpec is used by *ResourcePool.importVApp* when importing entities.  It provides all information needed to import a *VirtualMachine*. So far, this coincides with *VirtualMachineConfigSpec*.  A VmImportSpec can be contained in a *VirtualAppImportSpec* as part of the ImportSpec for an entity.  See also *ImportSpec*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | 
**res_pool_entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_import_spec import VirtualMachineImportSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineImportSpec from a JSON string
virtual_machine_import_spec_instance = VirtualMachineImportSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineImportSpec.to_json()

# convert the object into a dict
virtual_machine_import_spec_dict = virtual_machine_import_spec_instance.to_dict()
# create an instance of VirtualMachineImportSpec from a dict
virtual_machine_import_spec_form_dict = virtual_machine_import_spec.from_dict(virtual_machine_import_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


