# ArrayOfStorageDrsVmConfigSpec

A boxed array of *StorageDrsVmConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageDrsVmConfigSpec]**](StorageDrsVmConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_drs_vm_config_spec import ArrayOfStorageDrsVmConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageDrsVmConfigSpec from a JSON string
array_of_storage_drs_vm_config_spec_instance = ArrayOfStorageDrsVmConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageDrsVmConfigSpec.to_json()

# convert the object into a dict
array_of_storage_drs_vm_config_spec_dict = array_of_storage_drs_vm_config_spec_instance.to_dict()
# create an instance of ArrayOfStorageDrsVmConfigSpec from a dict
array_of_storage_drs_vm_config_spec_form_dict = array_of_storage_drs_vm_config_spec.from_dict(array_of_storage_drs_vm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


