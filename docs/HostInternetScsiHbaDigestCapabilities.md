# HostInternetScsiHbaDigestCapabilities

The digest capabilities for this host bus adapter.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_digest_settable** | **bool** | True if this host bus adapter supports the configuration of the use of header digest.  Defaults to false, in which case no header digests will be used.  ***Since:*** vSphere API 4.0  | [optional] 
**data_digest_settable** | **bool** | True if this host bus adapter supports the configuration of the use of data digest.  Defaults to false, in which case no data digests will be used.  ***Since:*** vSphere API 4.0  | [optional] 
**target_header_digest_settable** | **bool** | True if configuration of the use of header digest is supported on the targets associated with the host bus adapter.  Defaults to false, in which case no header digests will be used.  ***Since:*** vSphere API 4.0  | [optional] 
**target_data_digest_settable** | **bool** | True if configuration of the use of data digest is supported on the targets associated with the host bus adapter.  Defaults to false, in which case no data digests will be used.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_digest_capabilities import HostInternetScsiHbaDigestCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaDigestCapabilities from a JSON string
host_internet_scsi_hba_digest_capabilities_instance = HostInternetScsiHbaDigestCapabilities.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaDigestCapabilities.to_json()

# convert the object into a dict
host_internet_scsi_hba_digest_capabilities_dict = host_internet_scsi_hba_digest_capabilities_instance.to_dict()
# create an instance of HostInternetScsiHbaDigestCapabilities from a dict
host_internet_scsi_hba_digest_capabilities_form_dict = host_internet_scsi_hba_digest_capabilities.from_dict(host_internet_scsi_hba_digest_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


