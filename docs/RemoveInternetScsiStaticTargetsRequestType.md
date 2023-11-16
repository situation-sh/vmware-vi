# RemoveInternetScsiStaticTargetsRequestType

The parameters of *HostStorageSystem.RemoveInternetScsiStaticTargets*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter.  | 
**targets** | [**List[HostInternetScsiHbaStaticTarget]**](HostInternetScsiHbaStaticTarget.md) | An array of iSCSI static targets to remove.  | 

## Example

```python
from vmware_vi.models.remove_internet_scsi_static_targets_request_type import RemoveInternetScsiStaticTargetsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveInternetScsiStaticTargetsRequestType from a JSON string
remove_internet_scsi_static_targets_request_type_instance = RemoveInternetScsiStaticTargetsRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveInternetScsiStaticTargetsRequestType.to_json()

# convert the object into a dict
remove_internet_scsi_static_targets_request_type_dict = remove_internet_scsi_static_targets_request_type_instance.to_dict()
# create an instance of RemoveInternetScsiStaticTargetsRequestType from a dict
remove_internet_scsi_static_targets_request_type_form_dict = remove_internet_scsi_static_targets_request_type.from_dict(remove_internet_scsi_static_targets_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


