# HostInternetScsiHbaSendTarget

The iSCSI send target. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address or hostname of the storage device.  | 
**port** | **int** | The TCP port of the storage device.  If not specified, the standard default of 3260 is used.  | [optional] 
**authentication_properties** | [**HostInternetScsiHbaAuthenticationProperties**](HostInternetScsiHbaAuthenticationProperties.md) |  | [optional] 
**digest_properties** | [**HostInternetScsiHbaDigestProperties**](HostInternetScsiHbaDigestProperties.md) |  | [optional] 
**supported_advanced_options** | [**List[OptionDef]**](OptionDef.md) | A list of supported key/value pair advanced options for the host bus adapter including their type information.  ***Since:*** vSphere API 4.0  | [optional] 
**advanced_options** | [**List[HostInternetScsiHbaParamValue]**](HostInternetScsiHbaParamValue.md) | A list of the current options settings for the host bus adapter.  ***Since:*** vSphere API 4.0  | [optional] 
**parent** | **str** | The device name of the host bus adapter from which settings can be inherited.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_hba_send_target import HostInternetScsiHbaSendTarget

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiHbaSendTarget from a JSON string
host_internet_scsi_hba_send_target_instance = HostInternetScsiHbaSendTarget.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiHbaSendTarget.to_json()

# convert the object into a dict
host_internet_scsi_hba_send_target_dict = host_internet_scsi_hba_send_target_instance.to_dict()
# create an instance of HostInternetScsiHbaSendTarget from a dict
host_internet_scsi_hba_send_target_form_dict = host_internet_scsi_hba_send_target.from_dict(host_internet_scsi_hba_send_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


