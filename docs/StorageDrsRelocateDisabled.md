# StorageDrsRelocateDisabled

This fault is thrown when Storage DRS cannot move disks of a virtual machine because the relocate method of the virtual machine is disabled.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_relocate_disabled import StorageDrsRelocateDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsRelocateDisabled from a JSON string
storage_drs_relocate_disabled_instance = StorageDrsRelocateDisabled.from_json(json)
# print the JSON string representation of the object
print StorageDrsRelocateDisabled.to_json()

# convert the object into a dict
storage_drs_relocate_disabled_dict = storage_drs_relocate_disabled_instance.to_dict()
# create an instance of StorageDrsRelocateDisabled from a dict
storage_drs_relocate_disabled_form_dict = storage_drs_relocate_disabled.from_dict(storage_drs_relocate_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


