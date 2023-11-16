# StorageDrsDisabledOnVm

This fault is thrown when Storage DRS cannot move disks of a virtual machine because Storage DRS is disabled on it.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_disabled_on_vm import StorageDrsDisabledOnVm

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsDisabledOnVm from a JSON string
storage_drs_disabled_on_vm_instance = StorageDrsDisabledOnVm.from_json(json)
# print the JSON string representation of the object
print StorageDrsDisabledOnVm.to_json()

# convert the object into a dict
storage_drs_disabled_on_vm_dict = storage_drs_disabled_on_vm_instance.to_dict()
# create an instance of StorageDrsDisabledOnVm from a dict
storage_drs_disabled_on_vm_form_dict = storage_drs_disabled_on_vm.from_dict(storage_drs_disabled_on_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


