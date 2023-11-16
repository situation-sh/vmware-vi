# HostInternetScsiHbaTargetSet

A collection of one or more static targets or discovery addresses.  At least one of the arrays must be non-empty.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_targets** | [**List[HostInternetScsiHbaStaticTarget]**](HostInternetScsiHbaStaticTarget.md) |  | [optional] 
**send_targets** | [**List[HostInternetScsiHbaSendTarget]**](HostInternetScsiHbaSendTarget.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_target_set import HostInternetScsiHbaTargetSet

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaTargetSet from a JSON string
host_internet_scsi_hba_target_set_instance = HostInternetScsiHbaTargetSet.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaTargetSet.to_json()

# convert the object into a dict
host_internet_scsi_hba_target_set_dict = host_internet_scsi_hba_target_set_instance.to_dict()
# create an instance of HostInternetScsiHbaTargetSet from a dict
host_internet_scsi_hba_target_set_form_dict = host_internet_scsi_hba_target_set.from_dict(host_internet_scsi_hba_target_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


