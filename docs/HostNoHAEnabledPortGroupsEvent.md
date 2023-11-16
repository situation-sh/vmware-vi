# HostNoHAEnabledPortGroupsEvent

This event records the fact that a host does not have any HA-enabled port groups  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_no_ha_enabled_port_groups_event import HostNoHAEnabledPortGroupsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostNoHAEnabledPortGroupsEvent from a JSON string
host_no_ha_enabled_port_groups_event_instance = HostNoHAEnabledPortGroupsEvent.from_json(json)
# print the JSON string representation of the object
print HostNoHAEnabledPortGroupsEvent.to_json()

# convert the object into a dict
host_no_ha_enabled_port_groups_event_dict = host_no_ha_enabled_port_groups_event_instance.to_dict()
# create an instance of HostNoHAEnabledPortGroupsEvent from a dict
host_no_ha_enabled_port_groups_event_form_dict = host_no_ha_enabled_port_groups_event.from_dict(host_no_ha_enabled_port_groups_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


