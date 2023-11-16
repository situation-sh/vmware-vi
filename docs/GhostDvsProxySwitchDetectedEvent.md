# GhostDvsProxySwitchDetectedEvent

This event records when Virtual Center server found DVS proxy switches on the host that don't match any DVS defined in Virtual Center.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_uuid** | **List[str]** | The list of ghost DVS proxy switch uuids that were found.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ghost_dvs_proxy_switch_detected_event import GhostDvsProxySwitchDetectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GhostDvsProxySwitchDetectedEvent from a JSON string
ghost_dvs_proxy_switch_detected_event_instance = GhostDvsProxySwitchDetectedEvent.from_json(json)
# print the JSON string representation of the object
print GhostDvsProxySwitchDetectedEvent.to_json()

# convert the object into a dict
ghost_dvs_proxy_switch_detected_event_dict = ghost_dvs_proxy_switch_detected_event_instance.to_dict()
# create an instance of GhostDvsProxySwitchDetectedEvent from a dict
ghost_dvs_proxy_switch_detected_event_form_dict = ghost_dvs_proxy_switch_detected_event.from_dict(ghost_dvs_proxy_switch_detected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


