# ArrayOfStorageDrsVmConfigInfo

A boxed array of *StorageDrsVmConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageDrsVmConfigInfo]**](StorageDrsVmConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_drs_vm_config_info import ArrayOfStorageDrsVmConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageDrsVmConfigInfo from a JSON string
array_of_storage_drs_vm_config_info_instance = ArrayOfStorageDrsVmConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageDrsVmConfigInfo.to_json()

# convert the object into a dict
array_of_storage_drs_vm_config_info_dict = array_of_storage_drs_vm_config_info_instance.to_dict()
# create an instance of ArrayOfStorageDrsVmConfigInfo from a dict
array_of_storage_drs_vm_config_info_form_dict = array_of_storage_drs_vm_config_info.from_dict(array_of_storage_drs_vm_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


