# HostIpToShortNameFailedEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that the host's IP address could not be resolved to a short name.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_ip_to_short_name_failed_event import HostIpToShortNameFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpToShortNameFailedEvent from a JSON string
host_ip_to_short_name_failed_event_instance = HostIpToShortNameFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostIpToShortNameFailedEvent.to_json()

# convert the object into a dict
host_ip_to_short_name_failed_event_dict = host_ip_to_short_name_failed_event_instance.to_dict()
# create an instance of HostIpToShortNameFailedEvent from a dict
host_ip_to_short_name_failed_event_form_dict = host_ip_to_short_name_failed_event.from_dict(host_ip_to_short_name_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


