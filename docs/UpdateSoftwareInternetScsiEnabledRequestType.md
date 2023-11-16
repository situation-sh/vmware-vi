# UpdateSoftwareInternetScsiEnabledRequestType

The parameters of *HostStorageSystem.UpdateSoftwareInternetScsiEnabled*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | True to enable the iSCSI; false to disable it  | 

## Example

```python
from vmware_vi.models.update_software_internet_scsi_enabled_request_type import UpdateSoftwareInternetScsiEnabledRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSoftwareInternetScsiEnabledRequestType from a JSON string
update_software_internet_scsi_enabled_request_type_instance = UpdateSoftwareInternetScsiEnabledRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateSoftwareInternetScsiEnabledRequestType.to_json()

# convert the object into a dict
update_software_internet_scsi_enabled_request_type_dict = update_software_internet_scsi_enabled_request_type_instance.to_dict()
# create an instance of UpdateSoftwareInternetScsiEnabledRequestType from a dict
update_software_internet_scsi_enabled_request_type_form_dict = update_software_internet_scsi_enabled_request_type.from_dict(update_software_internet_scsi_enabled_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


