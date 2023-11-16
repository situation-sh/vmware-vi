# GhostDvsProxySwitchRemovedEvent

This event records when the ghost DVS proxy switches (a.k.a host proxy switches that don't match any DVS defined in Virtual Center) were removed on the host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_uuid** | **List[str]** | The list of ghost DVS proxy switch uuid that were removed.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ghost_dvs_proxy_switch_removed_event import GhostDvsProxySwitchRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GhostDvsProxySwitchRemovedEvent from a JSON string
ghost_dvs_proxy_switch_removed_event_instance = GhostDvsProxySwitchRemovedEvent.from_json(json)
# print the JSON string representation of the object
print GhostDvsProxySwitchRemovedEvent.to_json()

# convert the object into a dict
ghost_dvs_proxy_switch_removed_event_dict = ghost_dvs_proxy_switch_removed_event_instance.to_dict()
# create an instance of GhostDvsProxySwitchRemovedEvent from a dict
ghost_dvs_proxy_switch_removed_event_form_dict = ghost_dvs_proxy_switch_removed_event.from_dict(ghost_dvs_proxy_switch_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


