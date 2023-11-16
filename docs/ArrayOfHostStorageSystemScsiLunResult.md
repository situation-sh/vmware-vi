# ArrayOfHostStorageSystemScsiLunResult

A boxed array of *HostStorageSystemScsiLunResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostStorageSystemScsiLunResult]**](HostStorageSystemScsiLunResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_storage_system_scsi_lun_result import ArrayOfHostStorageSystemScsiLunResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostStorageSystemScsiLunResult from a JSON string
array_of_host_storage_system_scsi_lun_result_instance = ArrayOfHostStorageSystemScsiLunResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostStorageSystemScsiLunResult.to_json()

# convert the object into a dict
array_of_host_storage_system_scsi_lun_result_dict = array_of_host_storage_system_scsi_lun_result_instance.to_dict()
# create an instance of ArrayOfHostStorageSystemScsiLunResult from a dict
array_of_host_storage_system_scsi_lun_result_form_dict = array_of_host_storage_system_scsi_lun_result.from_dict(array_of_host_storage_system_scsi_lun_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


