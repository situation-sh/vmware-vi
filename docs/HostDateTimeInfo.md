# HostDateTimeInfo

This data object represents the dateTime configuration of the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | [**HostDateTimeSystemTimeZone**](HostDateTimeSystemTimeZone.md) |  | 
**system_clock_protocol** | **str** | The system clock synchronization protocol.  See *HostDateTimeInfoProtocol_enum* for possible values.  ***Since:*** vSphere API 7.0  | [optional] 
**ntp_config** | [**HostNtpConfig**](HostNtpConfig.md) |  | [optional] 
**ptp_config** | [**HostPtpConfig**](HostPtpConfig.md) |  | [optional] 
**enabled** | **bool** | Present state of the time services subsystem.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**disable_events** | **bool** | When not disabled Network Time service or Precision Time service will send events to Virtual Center when service fails or recovers.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**disable_fallback** | **bool** | When not disabled, if PrecisionTimeSync is configured, then the NTP configuration can run as backup.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**in_fallback_state** | **bool** | Tracks if NTP is providing time to ESXi due to PTP service failure.  This is set only if disableFallback is set to false.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**service_sync** | **bool** | Report true if time is synchronized with remote time source For PrecisionTimeSync this is obtained from PTP Port Status value.  For NetworkTimeProtocol this obtained from Leap Indicator value.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**last_sync_time** | **datetime** | Timestamp when time services were last in sync with remote clock.  If not set, time services have never established synchronization.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**remote_ntp_server** | **str** | Provides the NTP server that the host is synced with from the set of servers configured.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**ntp_run_time** | **int** | Provides the total seconds ntpd process has been running for.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**ptp_run_time** | **int** | Provides the total seconds ptpd process has been running for.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**ntp_duration** | **str** | Provides a duration in simplified, human-readable form for the lifetime of the ntp service.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**ptp_duration** | **str** | Provides a duration in simplified, human-readable form for the lifetime of the ptp service.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_date_time_info import HostDateTimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDateTimeInfo from a JSON string
host_date_time_info_instance = HostDateTimeInfo.from_json(json)
# print the JSON string representation of the object
print HostDateTimeInfo.to_json()

# convert the object into a dict
host_date_time_info_dict = host_date_time_info_instance.to_dict()
# create an instance of HostDateTimeInfo from a dict
host_date_time_info_form_dict = host_date_time_info.from_dict(host_date_time_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


