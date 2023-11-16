# RemoveInternetScsiSendTargetsRequestType

The parameters of *HostStorageSystem.RemoveInternetScsiSendTargets*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter.  | 
**targets** | [**List[HostInternetScsiHbaSendTarget]**](HostInternetScsiHbaSendTarget.md) | An array of iSCSI send targets to remove.  | 
**force** | **bool** | flag for forced removal of iSCSI send targets. If unset, force flag will be treated as false.  | [optional] 

## Example

```python
from vmware_vi.models.remove_internet_scsi_send_targets_request_type import RemoveInternetScsiSendTargetsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveInternetScsiSendTargetsRequestType from a JSON string
remove_internet_scsi_send_targets_request_type_instance = RemoveInternetScsiSendTargetsRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveInternetScsiSendTargetsRequestType.to_json()

# convert the object into a dict
remove_internet_scsi_send_targets_request_type_dict = remove_internet_scsi_send_targets_request_type_instance.to_dict()
# create an instance of RemoveInternetScsiSendTargetsRequestType from a dict
remove_internet_scsi_send_targets_request_type_form_dict = remove_internet_scsi_send_targets_request_type.from_dict(remove_internet_scsi_send_targets_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


