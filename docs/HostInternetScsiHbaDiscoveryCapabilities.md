# HostInternetScsiHbaDiscoveryCapabilities

The discovery capabilities for this host bus adapter.  At least one discovery mode must always be active. Multiple modes may be active at the same time. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_sns_discovery_settable** | **bool** | True if this host bus adapter supports iSNS  | 
**slp_discovery_settable** | **bool** | True if this host bus adapter supports SLP  | 
**static_target_discovery_settable** | **bool** | True if this host bus adapter supports static discovery  | 
**send_targets_discovery_settable** | **bool** | True if this host bus adapter supports changing the configuration state of send targets discovery.  Send targets is mandatory, however some adapters may not allow disabling this discovery method.  | 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_discovery_capabilities import HostInternetScsiHbaDiscoveryCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaDiscoveryCapabilities from a JSON string
host_internet_scsi_hba_discovery_capabilities_instance = HostInternetScsiHbaDiscoveryCapabilities.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaDiscoveryCapabilities.to_json()

# convert the object into a dict
host_internet_scsi_hba_discovery_capabilities_dict = host_internet_scsi_hba_discovery_capabilities_instance.to_dict()
# create an instance of HostInternetScsiHbaDiscoveryCapabilities from a dict
host_internet_scsi_hba_discovery_capabilities_form_dict = host_internet_scsi_hba_discovery_capabilities.from_dict(host_internet_scsi_hba_discovery_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


