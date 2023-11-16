# UpdateInternetScsiNameRequestType

The parameters of *HostStorageSystem.UpdateInternetScsiName*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The current name of the Internet SCSI HBA adapter.  | 
**i_scsi_name** | **str** | The new name for the Internet SCSI HBA adapter  | 

## Example

```python
from vmware_vi.models.update_internet_scsi_name_request_type import UpdateInternetScsiNameRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInternetScsiNameRequestType from a JSON string
update_internet_scsi_name_request_type_instance = UpdateInternetScsiNameRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateInternetScsiNameRequestType.to_json()

# convert the object into a dict
update_internet_scsi_name_request_type_dict = update_internet_scsi_name_request_type_instance.to_dict()
# create an instance of UpdateInternetScsiNameRequestType from a dict
update_internet_scsi_name_request_type_form_dict = update_internet_scsi_name_request_type.from_dict(update_internet_scsi_name_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


