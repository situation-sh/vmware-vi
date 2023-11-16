# HostDateTimeConfig

This data object represents the dateTime configuration of the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** | The time zone of the host.  Must be one of the values of *HostDateTimeSystemTimeZone.key*  ***Since:*** VI API 2.5  | [optional] 
**ntp_config** | [**HostNtpConfig**](HostNtpConfig.md) |  | [optional] 
**ptp_config** | [**HostPtpConfig**](HostPtpConfig.md) |  | [optional] 
**protocol** | **str** | Specify which network time configuration to discipline vmkernel clock.  See *HostDateTimeInfoProtocol_enum* for supported values.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**enabled** | **bool** | Bring Time services subsystem up or down.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**disable_events** | **bool** | When Network Time service or Precision Time service are enabled any detecteced failures will result in Events being sent to Virtual Center.  Use this setting to disable Time Events.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**disable_fallback** | **bool** | When in PrecisionTimeSync, NTP configuration as set will be running as backup.  Use this setting to prevent NTP from becoming the primary time protocol in the event of a PTP service failure.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**reset_to_factory_defaults** | **bool** | When this property is present and set true the existing configuration for Time Services will be reset to factory default.  The protocol property when set defines the scope of what is reset. If additional configuration beyond protocol is provided host will first perform factory reset followed by applying any configuration present.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_date_time_config import HostDateTimeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostDateTimeConfig from a JSON string
host_date_time_config_instance = HostDateTimeConfig.from_json(json)
# print the JSON string representation of the object
print HostDateTimeConfig.to_json()

# convert the object into a dict
host_date_time_config_dict = host_date_time_config_instance.to_dict()
# create an instance of HostDateTimeConfig from a dict
host_date_time_config_form_dict = host_date_time_config.from_dict(host_date_time_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


