# ArrayOfHostInternetScsiHbaDiscoveryProperties

A boxed array of *HostInternetScsiHbaDiscoveryProperties*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostInternetScsiHbaDiscoveryProperties]**](HostInternetScsiHbaDiscoveryProperties.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_internet_scsi_hba_discovery_properties import ArrayOfHostInternetScsiHbaDiscoveryProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostInternetScsiHbaDiscoveryProperties from a JSON string
array_of_host_internet_scsi_hba_discovery_properties_instance = ArrayOfHostInternetScsiHbaDiscoveryProperties.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostInternetScsiHbaDiscoveryProperties.to_json()

# convert the object into a dict
array_of_host_internet_scsi_hba_discovery_properties_dict = array_of_host_internet_scsi_hba_discovery_properties_instance.to_dict()
# create an instance of ArrayOfHostInternetScsiHbaDiscoveryProperties from a dict
array_of_host_internet_scsi_hba_discovery_properties_form_dict = array_of_host_internet_scsi_hba_discovery_properties.from_dict(array_of_host_internet_scsi_hba_discovery_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


