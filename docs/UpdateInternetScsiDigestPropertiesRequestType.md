# UpdateInternetScsiDigestPropertiesRequestType

The parameters of *HostStorageSystem.UpdateInternetScsiDigestProperties*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter.  | 
**target_set** | [**HostInternetScsiHbaTargetSet**](HostInternetScsiHbaTargetSet.md) |  | [optional] 
**digest_properties** | [**HostInternetScsiHbaDigestProperties**](HostInternetScsiHbaDigestProperties.md) |  | 

## Example

```python
from vmware_vi.models.update_internet_scsi_digest_properties_request_type import UpdateInternetScsiDigestPropertiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInternetScsiDigestPropertiesRequestType from a JSON string
update_internet_scsi_digest_properties_request_type_instance = UpdateInternetScsiDigestPropertiesRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateInternetScsiDigestPropertiesRequestType.to_json()

# convert the object into a dict
update_internet_scsi_digest_properties_request_type_dict = update_internet_scsi_digest_properties_request_type_instance.to_dict()
# create an instance of UpdateInternetScsiDigestPropertiesRequestType from a dict
update_internet_scsi_digest_properties_request_type_form_dict = update_internet_scsi_digest_properties_request_type.from_dict(update_internet_scsi_digest_properties_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


