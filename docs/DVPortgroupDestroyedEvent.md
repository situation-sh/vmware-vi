# DVPortgroupDestroyedEvent

Two distributed virtual portgroup was destroyed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dv_portgroup_destroyed_event import DVPortgroupDestroyedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupDestroyedEvent from a JSON string
dv_portgroup_destroyed_event_instance = DVPortgroupDestroyedEvent.from_json(json)
# print the JSON string representation of the object
print DVPortgroupDestroyedEvent.to_json()

# convert the object into a dict
dv_portgroup_destroyed_event_dict = dv_portgroup_destroyed_event_instance.to_dict()
# create an instance of DVPortgroupDestroyedEvent from a dict
dv_portgroup_destroyed_event_form_dict = dv_portgroup_destroyed_event.from_dict(dv_portgroup_destroyed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


