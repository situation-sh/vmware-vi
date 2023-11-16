# DVPortgroupCreatedEvent

Two distributed virtual portgroup was created.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dv_portgroup_created_event import DVPortgroupCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupCreatedEvent from a JSON string
dv_portgroup_created_event_instance = DVPortgroupCreatedEvent.from_json(json)
# print the JSON string representation of the object
print DVPortgroupCreatedEvent.to_json()

# convert the object into a dict
dv_portgroup_created_event_dict = dv_portgroup_created_event_instance.to_dict()
# create an instance of DVPortgroupCreatedEvent from a dict
dv_portgroup_created_event_form_dict = dv_portgroup_created_event.from_dict(dv_portgroup_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


