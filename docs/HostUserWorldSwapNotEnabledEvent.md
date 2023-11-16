# HostUserWorldSwapNotEnabledEvent

Deprecated as of vSphere API 5.0, the event is no longer relevant.  This event records that the userworld swap is not enabled on the host.  HA needs userworld swap to be configured on embedded ESX hosts to function.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_user_world_swap_not_enabled_event import HostUserWorldSwapNotEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostUserWorldSwapNotEnabledEvent from a JSON string
host_user_world_swap_not_enabled_event_instance = HostUserWorldSwapNotEnabledEvent.from_json(json)
# print the JSON string representation of the object
print HostUserWorldSwapNotEnabledEvent.to_json()

# convert the object into a dict
host_user_world_swap_not_enabled_event_dict = host_user_world_swap_not_enabled_event_instance.to_dict()
# create an instance of HostUserWorldSwapNotEnabledEvent from a dict
host_user_world_swap_not_enabled_event_form_dict = host_user_world_swap_not_enabled_event.from_dict(host_user_world_swap_not_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


