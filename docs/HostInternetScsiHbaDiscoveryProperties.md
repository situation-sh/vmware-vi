# HostInternetScsiHbaDiscoveryProperties

The discovery settings for this host bus adapter.  At least one discovery mode must always be active. Multiple modes may be active at the same time. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_sns_discovery_enabled** | **bool** | True if iSNS is currently enabled  | 
**i_sns_discovery_method** | **str** | The iSNS discovery method in use when iSNS is enabled.  Must be one of the values of *InternetScsiSnsDiscoveryMethod_enum*  | [optional] 
**i_sns_host** | **str** | For STATIC iSNS, this is the iSNS server address  | [optional] 
**slp_discovery_enabled** | **bool** | True if SLP is enabled  | 
**slp_discovery_method** | **str** | The current SLP discovery method when SLP is enabled.  Must be one of the values of *SlpDiscoveryMethod_enum*  | [optional] 
**slp_host** | **str** | When the SLP discovery method is set to MANUAL, this property reflects the hostname, and optionally port number of the SLP DA.  | [optional] 
**static_target_discovery_enabled** | **bool** | True if static target discovery is enabled  | 
**send_targets_discovery_enabled** | **bool** | True if send targets discovery is enabled  | 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_discovery_properties import HostInternetScsiHbaDiscoveryProperties

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaDiscoveryProperties from a JSON string
host_internet_scsi_hba_discovery_properties_instance = HostInternetScsiHbaDiscoveryProperties.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaDiscoveryProperties.to_json()

# convert the object into a dict
host_internet_scsi_hba_discovery_properties_dict = host_internet_scsi_hba_discovery_properties_instance.to_dict()
# create an instance of HostInternetScsiHbaDiscoveryProperties from a dict
host_internet_scsi_hba_discovery_properties_form_dict = host_internet_scsi_hba_discovery_properties.from_dict(host_internet_scsi_hba_discovery_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


