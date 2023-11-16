# HostInternetScsiHba

This data object type describes the iSCSI host bus adapter interface. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_software_based** | **bool** | True if this host bus adapter is a software based initiator utilizing the hosting system&#39;s existing TCP/IP network connection  | 
**can_be_disabled** | **bool** | Can this adapter be disabled  ***Since:*** vSphere API 5.0  | [optional] 
**network_binding_support** | [**HostInternetScsiHbaNetworkBindingSupportTypeEnum**](HostInternetScsiHbaNetworkBindingSupportTypeEnum.md) |  | [optional] 
**discovery_capabilities** | [**HostInternetScsiHbaDiscoveryCapabilities**](HostInternetScsiHbaDiscoveryCapabilities.md) |  | 
**discovery_properties** | [**HostInternetScsiHbaDiscoveryProperties**](HostInternetScsiHbaDiscoveryProperties.md) |  | 
**authentication_capabilities** | [**HostInternetScsiHbaAuthenticationCapabilities**](HostInternetScsiHbaAuthenticationCapabilities.md) |  | 
**authentication_properties** | [**HostInternetScsiHbaAuthenticationProperties**](HostInternetScsiHbaAuthenticationProperties.md) |  | 
**digest_capabilities** | [**HostInternetScsiHbaDigestCapabilities**](HostInternetScsiHbaDigestCapabilities.md) |  | [optional] 
**digest_properties** | [**HostInternetScsiHbaDigestProperties**](HostInternetScsiHbaDigestProperties.md) |  | [optional] 
**ip_capabilities** | [**HostInternetScsiHbaIPCapabilities**](HostInternetScsiHbaIPCapabilities.md) |  | 
**ip_properties** | [**HostInternetScsiHbaIPProperties**](HostInternetScsiHbaIPProperties.md) |  | 
**supported_advanced_options** | [**List[OptionDef]**](OptionDef.md) | A list of supported key/value pair advanced options for the host bus adapter including their type information.  ***Since:*** vSphere API 4.0  | [optional] 
**advanced_options** | [**List[HostInternetScsiHbaParamValue]**](HostInternetScsiHbaParamValue.md) | A list of the current options settings for the host bus adapter.  ***Since:*** vSphere API 4.0  | [optional] 
**i_scsi_name** | **str** | The iSCSI name of this host bus adapter.  | 
**i_scsi_alias** | **str** | The iSCSI alias of this host bus adapter.  | [optional] 
**configured_send_target** | [**List[HostInternetScsiHbaSendTarget]**](HostInternetScsiHbaSendTarget.md) | The configured iSCSI send target entries.  | [optional] 
**configured_static_target** | [**List[HostInternetScsiHbaStaticTarget]**](HostInternetScsiHbaStaticTarget.md) | The configured iSCSI static target entries.  | [optional] 
**max_speed_mb** | **int** | The maximum supported link speed of the port in megabits per second.  | [optional] 
**current_speed_mb** | **int** | The Current operating link speed of the port in megabits per second.  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba import HostInternetScsiHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHba from a JSON string
host_internet_scsi_hba_instance = HostInternetScsiHba.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHba.to_json()

# convert the object into a dict
host_internet_scsi_hba_dict = host_internet_scsi_hba_instance.to_dict()
# create an instance of HostInternetScsiHba from a dict
host_internet_scsi_hba_form_dict = host_internet_scsi_hba.from_dict(host_internet_scsi_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


