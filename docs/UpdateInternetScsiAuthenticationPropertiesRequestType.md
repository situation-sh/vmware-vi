# UpdateInternetScsiAuthenticationPropertiesRequestType

The parameters of *HostStorageSystem.UpdateInternetScsiAuthenticationProperties*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter. associated with the target.  | 
**authentication_properties** | [**HostInternetScsiHbaAuthenticationProperties**](HostInternetScsiHbaAuthenticationProperties.md) |  | 
**target_set** | [**HostInternetScsiHbaTargetSet**](HostInternetScsiHbaTargetSet.md) |  | [optional] 

## Example

```python
from vmware_vi.models.update_internet_scsi_authentication_properties_request_type import UpdateInternetScsiAuthenticationPropertiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInternetScsiAuthenticationPropertiesRequestType from a JSON string
update_internet_scsi_authentication_properties_request_type_instance = UpdateInternetScsiAuthenticationPropertiesRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateInternetScsiAuthenticationPropertiesRequestType.to_json()

# convert the object into a dict
update_internet_scsi_authentication_properties_request_type_dict = update_internet_scsi_authentication_properties_request_type_instance.to_dict()
# create an instance of UpdateInternetScsiAuthenticationPropertiesRequestType from a dict
update_internet_scsi_authentication_properties_request_type_form_dict = update_internet_scsi_authentication_properties_request_type.from_dict(update_internet_scsi_authentication_properties_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


