# AddInternetScsiSendTargetsRequestType

The parameters of *HostStorageSystem.AddInternetScsiSendTargets*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter.  | 
**targets** | [**List[HostInternetScsiHbaSendTarget]**](HostInternetScsiHbaSendTarget.md) | An array of iSCSI send targets.  | 

## Example

```python
from vmware_vi.models.add_internet_scsi_send_targets_request_type import AddInternetScsiSendTargetsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddInternetScsiSendTargetsRequestType from a JSON string
add_internet_scsi_send_targets_request_type_instance = AddInternetScsiSendTargetsRequestType.from_json(json)
# print the JSON string representation of the object
print AddInternetScsiSendTargetsRequestType.to_json()

# convert the object into a dict
add_internet_scsi_send_targets_request_type_dict = add_internet_scsi_send_targets_request_type_instance.to_dict()
# create an instance of AddInternetScsiSendTargetsRequestType from a dict
add_internet_scsi_send_targets_request_type_form_dict = add_internet_scsi_send_targets_request_type.from_dict(add_internet_scsi_send_targets_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


