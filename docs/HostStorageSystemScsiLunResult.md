# HostStorageSystemScsiLunResult

Contains the result of SCSI LUN operation requests.  Used as return value by *HostStorageSystem.AttachScsiLunEx_Task*, *HostStorageSystem.DetachScsiLunEx_Task* and *HostStorageSystem.MarkPerenniallyReservedEx_Task*  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | UUID of LUN on which the LUN operation was requested.  ***Since:*** vSphere API 6.0  | 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_storage_system_scsi_lun_result import HostStorageSystemScsiLunResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostStorageSystemScsiLunResult from a JSON string
host_storage_system_scsi_lun_result_instance = HostStorageSystemScsiLunResult.from_json(json)
# print the JSON string representation of the object
print HostStorageSystemScsiLunResult.to_json()

# convert the object into a dict
host_storage_system_scsi_lun_result_dict = host_storage_system_scsi_lun_result_instance.to_dict()
# create an instance of HostStorageSystemScsiLunResult from a dict
host_storage_system_scsi_lun_result_form_dict = host_storage_system_scsi_lun_result.from_dict(host_storage_system_scsi_lun_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


