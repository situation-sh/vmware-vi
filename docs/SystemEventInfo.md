# SystemEventInfo

IPMI System Event Log (SEL) provides a history of hardware sensor states.  This is defined in IPMI specification, section 32.1 SEL Event Records. CLI:: esxcli hardware ipmi sel list  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **int** | The recordId uniquely identifies an entry in IPMI System Event Log.  ***Since:*** vSphere API 6.5  | 
**when** | **str** | A ISO 8601 timestamp when the event was added to IPMI System Event Log.  This timestamp comes from the IPMI subsystem clock and may not be the same as hypervisor&#39;s clock.  ***Since:*** vSphere API 6.5  | 
**sel_type** | **int** | The IPMI SEL type defines the if the SEL event uses the system event format format or is OEM defined.  A value of 2 indicates system event. Values 0xC0-0xDF, 0xE0-0xFF are OEM event ranges.  ***Since:*** vSphere API 6.5  | 
**message** | **str** | A description of what the event is about.  ***Since:*** vSphere API 6.5  | 
**sensor_number** | **int** | The IPMI Sensor/probe that is reporting this event.  A value of zero (0) indicates event has no related sensor.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.system_event_info import SystemEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemEventInfo from a JSON string
system_event_info_instance = SystemEventInfo.from_json(json)
# print the JSON string representation of the object
print SystemEventInfo.to_json()

# convert the object into a dict
system_event_info_dict = system_event_info_instance.to_dict()
# create an instance of SystemEventInfo from a dict
system_event_info_form_dict = system_event_info.from_dict(system_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


