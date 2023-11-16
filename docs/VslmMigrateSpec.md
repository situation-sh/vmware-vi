# VslmMigrateSpec

Base specification of moving or copying a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backing_spec** | [**VslmCreateSpecBackingSpec**](VslmCreateSpecBackingSpec.md) |  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Virtual storage object Profile requirement.  If unset, the default behavior will apply.  ***Since:*** vSphere API 6.7  | [optional] 
**consolidate** | **bool** | Flag indicates any delta disk backings will be consolidated during migration.  If unset, delta disk backings will not be consolidated.  ***Since:*** vSphere API 6.5  | [optional] 
**disks_crypto** | [**DiskCryptoSpec**](DiskCryptoSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vslm_migrate_spec import VslmMigrateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VslmMigrateSpec from a JSON string
vslm_migrate_spec_instance = VslmMigrateSpec.from_json(json)
# print the JSON string representation of the object
print VslmMigrateSpec.to_json()

# convert the object into a dict
vslm_migrate_spec_dict = vslm_migrate_spec_instance.to_dict()
# create an instance of VslmMigrateSpec from a dict
vslm_migrate_spec_form_dict = vslm_migrate_spec.from_dict(vslm_migrate_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


