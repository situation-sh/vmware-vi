# DvsPortJoinPortgroupEvent

A port was moved into the distributed virtual portgroup.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **str** | The port key.  ***Since:*** vSphere API 4.0  | 
**portgroup_key** | **str** | The portgroup key.  ***Since:*** vSphere API 4.0  | 
**portgroup_name** | **str** | The portgroup name.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dvs_port_join_portgroup_event import DvsPortJoinPortgroupEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsPortJoinPortgroupEvent from a JSON string
dvs_port_join_portgroup_event_instance = DvsPortJoinPortgroupEvent.from_json(json)
# print the JSON string representation of the object
print DvsPortJoinPortgroupEvent.to_json()

# convert the object into a dict
dvs_port_join_portgroup_event_dict = dvs_port_join_portgroup_event_instance.to_dict()
# create an instance of DvsPortJoinPortgroupEvent from a dict
dvs_port_join_portgroup_event_form_dict = dvs_port_join_portgroup_event.from_dict(dvs_port_join_portgroup_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


