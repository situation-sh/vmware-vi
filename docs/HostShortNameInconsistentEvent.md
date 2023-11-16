# HostShortNameInconsistentEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that host name resolution returned different names on the host.  Please check your host's network configuration and your DNS configuration. There may be duplicate entries.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | 
**short_name2** | **str** |  | 

## Example

```python
from vmware_vi.models.host_short_name_inconsistent_event import HostShortNameInconsistentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostShortNameInconsistentEvent from a JSON string
host_short_name_inconsistent_event_instance = HostShortNameInconsistentEvent.from_json(json)
# print the JSON string representation of the object
print HostShortNameInconsistentEvent.to_json()

# convert the object into a dict
host_short_name_inconsistent_event_dict = host_short_name_inconsistent_event_instance.to_dict()
# create an instance of HostShortNameInconsistentEvent from a dict
host_short_name_inconsistent_event_form_dict = host_short_name_inconsistent_event.from_dict(host_short_name_inconsistent_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


