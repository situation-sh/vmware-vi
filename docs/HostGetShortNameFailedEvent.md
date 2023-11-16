# HostGetShortNameFailedEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that hostname -s failed or returned a name containing '.'.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_get_short_name_failed_event import HostGetShortNameFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostGetShortNameFailedEvent from a JSON string
host_get_short_name_failed_event_instance = HostGetShortNameFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostGetShortNameFailedEvent.to_json()

# convert the object into a dict
host_get_short_name_failed_event_dict = host_get_short_name_failed_event_instance.to_dict()
# create an instance of HostGetShortNameFailedEvent from a dict
host_get_short_name_failed_event_form_dict = host_get_short_name_failed_event.from_dict(host_get_short_name_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


