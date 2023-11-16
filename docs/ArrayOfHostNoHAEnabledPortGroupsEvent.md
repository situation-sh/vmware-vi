# ArrayOfHostNoHAEnabledPortGroupsEvent

A boxed array of *HostNoHAEnabledPortGroupsEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNoHAEnabledPortGroupsEvent]**](HostNoHAEnabledPortGroupsEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_no_ha_enabled_port_groups_event import ArrayOfHostNoHAEnabledPortGroupsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNoHAEnabledPortGroupsEvent from a JSON string
array_of_host_no_ha_enabled_port_groups_event_instance = ArrayOfHostNoHAEnabledPortGroupsEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNoHAEnabledPortGroupsEvent.to_json()

# convert the object into a dict
array_of_host_no_ha_enabled_port_groups_event_dict = array_of_host_no_ha_enabled_port_groups_event_instance.to_dict()
# create an instance of ArrayOfHostNoHAEnabledPortGroupsEvent from a dict
array_of_host_no_ha_enabled_port_groups_event_form_dict = array_of_host_no_ha_enabled_port_groups_event.from_dict(array_of_host_no_ha_enabled_port_groups_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


