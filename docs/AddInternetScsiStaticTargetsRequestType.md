# AddInternetScsiStaticTargetsRequestType

The parameters of *HostStorageSystem.AddInternetScsiStaticTargets*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter.  | 
**targets** | [**List[HostInternetScsiHbaStaticTarget]**](HostInternetScsiHbaStaticTarget.md) | An array of iSCSI static targets to add.  | 

## Example

```python
from vmware_vi.models.add_internet_scsi_static_targets_request_type import AddInternetScsiStaticTargetsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddInternetScsiStaticTargetsRequestType from a JSON string
add_internet_scsi_static_targets_request_type_instance = AddInternetScsiStaticTargetsRequestType.from_json(json)
# print the JSON string representation of the object
print AddInternetScsiStaticTargetsRequestType.to_json()

# convert the object into a dict
add_internet_scsi_static_targets_request_type_dict = add_internet_scsi_static_targets_request_type_instance.to_dict()
# create an instance of AddInternetScsiStaticTargetsRequestType from a dict
add_internet_scsi_static_targets_request_type_form_dict = add_internet_scsi_static_targets_request_type.from_dict(add_internet_scsi_static_targets_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


