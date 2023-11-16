# ArrayOfHostInternetScsiHbaDiscoveryCapabilities

A boxed array of *HostInternetScsiHbaDiscoveryCapabilities*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostInternetScsiHbaDiscoveryCapabilities]**](HostInternetScsiHbaDiscoveryCapabilities.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_internet_scsi_hba_discovery_capabilities import ArrayOfHostInternetScsiHbaDiscoveryCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostInternetScsiHbaDiscoveryCapabilities from a JSON string
array_of_host_internet_scsi_hba_discovery_capabilities_instance = ArrayOfHostInternetScsiHbaDiscoveryCapabilities.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostInternetScsiHbaDiscoveryCapabilities.to_json()

# convert the object into a dict
array_of_host_internet_scsi_hba_discovery_capabilities_dict = array_of_host_internet_scsi_hba_discovery_capabilities_instance.to_dict()
# create an instance of ArrayOfHostInternetScsiHbaDiscoveryCapabilities from a dict
array_of_host_internet_scsi_hba_discovery_capabilities_form_dict = array_of_host_internet_scsi_hba_discovery_capabilities.from_dict(array_of_host_internet_scsi_hba_discovery_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


