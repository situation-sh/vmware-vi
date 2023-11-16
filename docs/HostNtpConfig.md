# HostNtpConfig

Configuration information for the NTP (Network Time Protocol) service.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | **List[str]** | List of time servers, specified as either IP addresses or fully qualified domain names (FQDNs).  Each entry may optionally specify one or more space separated &#39;server&#39; ntp.conf command options. Any comments appended to an entry after a &#39;#&#39; will not be retained. To reset any previously configured servers, submit an NtpConfig without the server or configFile property set to method *HostDateTimeSystem.UpdateDateTimeConfig*  ***Since:*** VI API 2.5  | [optional] 
**config_file** | **List[str]** | Content of ntp.conf host configuration file, split by lines for ntpd version 4.2.8.  Comment lines start with comment marker &#39;#&#39; as per ntp.conf are kept. When submitting a new ntp commands to this property via *HostDateTimeSystem.UpdateDateTimeConfig* method, any &#39;restrict&#39; or &#39;drift&#39; commands will be ignored as the those are set to fixed defaults.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_ntp_config import HostNtpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostNtpConfig from a JSON string
host_ntp_config_instance = HostNtpConfig.from_json(json)
# print the JSON string representation of the object
print HostNtpConfig.to_json()

# convert the object into a dict
host_ntp_config_dict = host_ntp_config_instance.to_dict()
# create an instance of HostNtpConfig from a dict
host_ntp_config_form_dict = host_ntp_config.from_dict(host_ntp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


