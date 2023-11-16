# StorageDrsVmConfigSpec

Updates the per-virtual-machine storage DRS configuration.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**StorageDrsVmConfigInfo**](StorageDrsVmConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.storage_drs_vm_config_spec import StorageDrsVmConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsVmConfigSpec from a JSON string
storage_drs_vm_config_spec_instance = StorageDrsVmConfigSpec.from_json(json)
# print the JSON string representation of the object
print StorageDrsVmConfigSpec.to_json()

# convert the object into a dict
storage_drs_vm_config_spec_dict = storage_drs_vm_config_spec_instance.to_dict()
# create an instance of StorageDrsVmConfigSpec from a dict
storage_drs_vm_config_spec_form_dict = storage_drs_vm_config_spec.from_dict(storage_drs_vm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


