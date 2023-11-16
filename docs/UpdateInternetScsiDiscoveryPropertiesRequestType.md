# UpdateInternetScsiDiscoveryPropertiesRequestType

The parameters of *HostStorageSystem.UpdateInternetScsiDiscoveryProperties*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_device** | **str** | The device of the Internet SCSI HBA adapter.  | 
**discovery_properties** | [**HostInternetScsiHbaDiscoveryProperties**](HostInternetScsiHbaDiscoveryProperties.md) |  | 

## Example

```python
from vmware_vi.models.update_internet_scsi_discovery_properties_request_type import UpdateInternetScsiDiscoveryPropertiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInternetScsiDiscoveryPropertiesRequestType from a JSON string
update_internet_scsi_discovery_properties_request_type_instance = UpdateInternetScsiDiscoveryPropertiesRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateInternetScsiDiscoveryPropertiesRequestType.to_json()

# convert the object into a dict
update_internet_scsi_discovery_properties_request_type_dict = update_internet_scsi_discovery_properties_request_type_instance.to_dict()
# create an instance of UpdateInternetScsiDiscoveryPropertiesRequestType from a dict
update_internet_scsi_discovery_properties_request_type_form_dict = update_internet_scsi_discovery_properties_request_type.from_dict(update_internet_scsi_discovery_properties_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


