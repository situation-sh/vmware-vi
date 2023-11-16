# UpdateInternetScsiIPPropertiesRequestType

The parameters of *HostStorageSystem.UpdateInternetScsiIPProperties*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter.  | 
**ip_properties** | [**HostInternetScsiHbaIPProperties**](HostInternetScsiHbaIPProperties.md) |  | 

## Example

```python
from vmware_vi.models.update_internet_scsi_ip_properties_request_type import UpdateInternetScsiIPPropertiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInternetScsiIPPropertiesRequestType from a JSON string
update_internet_scsi_ip_properties_request_type_instance = UpdateInternetScsiIPPropertiesRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateInternetScsiIPPropertiesRequestType.to_json()

# convert the object into a dict
update_internet_scsi_ip_properties_request_type_dict = update_internet_scsi_ip_properties_request_type_instance.to_dict()
# create an instance of UpdateInternetScsiIPPropertiesRequestType from a dict
update_internet_scsi_ip_properties_request_type_form_dict = update_internet_scsi_ip_properties_request_type.from_dict(update_internet_scsi_ip_properties_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


