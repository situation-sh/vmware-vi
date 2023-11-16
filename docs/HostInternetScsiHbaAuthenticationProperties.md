# HostInternetScsiHbaAuthenticationProperties

The authentication settings for this host bus adapter or target. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chap_auth_enabled** | **bool** | True if CHAP is currently enabled  | 
**chap_name** | **str** | The CHAP user name if enabled  | [optional] 
**chap_secret** | **str** | The CHAP secret if enabled  | [optional] 
**chap_authentication_type** | **str** | The preference for CHAP or non-CHAP protocol if CHAP is enabled  ***Since:*** vSphere API 4.0  | [optional] 
**chap_inherited** | **bool** | CHAP settings are inherited  ***Since:*** vSphere API 4.0  | [optional] 
**mutual_chap_name** | **str** | When Mutual-CHAP is enabled, the user name that target needs to use to authenticate with the initiator  ***Since:*** vSphere API 4.0  | [optional] 
**mutual_chap_secret** | **str** | When Mutual-CHAP is enabled, the secret that target needs to use to authenticate with the initiator  ***Since:*** vSphere API 4.0  | [optional] 
**mutual_chap_authentication_type** | **str** | The preference for CHAP or non-CHAP protocol if CHAP is enabled  ***Since:*** vSphere API 4.0  | [optional] 
**mutual_chap_inherited** | **bool** | Mutual-CHAP settings are inherited  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_authentication_properties import HostInternetScsiHbaAuthenticationProperties

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaAuthenticationProperties from a JSON string
host_internet_scsi_hba_authentication_properties_instance = HostInternetScsiHbaAuthenticationProperties.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaAuthenticationProperties.to_json()

# convert the object into a dict
host_internet_scsi_hba_authentication_properties_dict = host_internet_scsi_hba_authentication_properties_instance.to_dict()
# create an instance of HostInternetScsiHbaAuthenticationProperties from a dict
host_internet_scsi_hba_authentication_properties_form_dict = host_internet_scsi_hba_authentication_properties.from_dict(host_internet_scsi_hba_authentication_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


