# RDMNotPreserved

The virtual machine is configured with a Raw Disk Mapping.  The host only supports Raw Disk Mappings in a limited fashion. After the migration, the RDM will function correctly, but it will be indistinguishable from a virtual disk when viewing the virtual machine's properties. This change will persist even if the virtual machine is migrated back to a host with full RDM support.  This is a warning only for migrations to ESX 2.1.x hosts. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The name of the disk device using the RDM.  | 

## Example

```python
from vmware_vi.models.rdm_not_preserved import RDMNotPreserved

# TODO update the JSON string below
json = "{}"
# create an instance of RDMNotPreserved from a JSON string
rdm_not_preserved_instance = RDMNotPreserved.from_json(json)
# print the JSON string representation of the object
print RDMNotPreserved.to_json()

# convert the object into a dict
rdm_not_preserved_dict = rdm_not_preserved_instance.to_dict()
# create an instance of RDMNotPreserved from a dict
rdm_not_preserved_form_dict = rdm_not_preserved.from_dict(rdm_not_preserved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


