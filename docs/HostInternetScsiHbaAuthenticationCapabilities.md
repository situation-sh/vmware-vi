# HostInternetScsiHbaAuthenticationCapabilities

The authentication capabilities for this host bus adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chap_auth_settable** | **bool** | True if this host bus adapter supports changing the configuration state of CHAP authentication.  CHAP is mandatory, however some adapter may not allow disabling this authentication method.  | 
**krb5_auth_settable** | **bool** | Always false in this version of the API.  | 
**srp_auth_settable** | **bool** | Always false in this version of the API.  | 
**spkm_auth_settable** | **bool** | Always false in this version of the API.  | 
**mutual_chap_settable** | **bool** | When chapAuthSettable is TRUE, this describes if Mutual CHAP configuration is allowed as well.  ***Since:*** vSphere API 4.0  | [optional] 
**target_chap_settable** | **bool** | When targetChapSettable is TRUE, this describes if CHAP configuration is allowed on targets associated with the adapter.  ***Since:*** vSphere API 4.0  | [optional] 
**target_mutual_chap_settable** | **bool** | When targetMutualChapSettable is TRUE, this describes if Mutual CHAP configuration is allowed on targets associated with the adapter.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_authentication_capabilities import HostInternetScsiHbaAuthenticationCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaAuthenticationCapabilities from a JSON string
host_internet_scsi_hba_authentication_capabilities_instance = HostInternetScsiHbaAuthenticationCapabilities.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaAuthenticationCapabilities.to_json()

# convert the object into a dict
host_internet_scsi_hba_authentication_capabilities_dict = host_internet_scsi_hba_authentication_capabilities_instance.to_dict()
# create an instance of HostInternetScsiHbaAuthenticationCapabilities from a dict
host_internet_scsi_hba_authentication_capabilities_form_dict = host_internet_scsi_hba_authentication_capabilities.from_dict(host_internet_scsi_hba_authentication_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


