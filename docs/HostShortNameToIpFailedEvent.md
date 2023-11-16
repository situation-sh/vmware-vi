# HostShortNameToIpFailedEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that the host's short name could not be resolved to an IP address.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | 

## Example

```python
from vmware_vi.models.host_short_name_to_ip_failed_event import HostShortNameToIpFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostShortNameToIpFailedEvent from a JSON string
host_short_name_to_ip_failed_event_instance = HostShortNameToIpFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostShortNameToIpFailedEvent.to_json()

# convert the object into a dict
host_short_name_to_ip_failed_event_dict = host_short_name_to_ip_failed_event_instance.to_dict()
# create an instance of HostShortNameToIpFailedEvent from a dict
host_short_name_to_ip_failed_event_form_dict = host_short_name_to_ip_failed_event.from_dict(host_short_name_to_ip_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


