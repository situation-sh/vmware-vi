# DVPortgroupEvent

DVPortgroup related events.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dv_portgroup_event import DVPortgroupEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupEvent from a JSON string
dv_portgroup_event_instance = DVPortgroupEvent.from_json(json)
# print the JSON string representation of the object
print DVPortgroupEvent.to_json()

# convert the object into a dict
dv_portgroup_event_dict = dv_portgroup_event_instance.to_dict()
# create an instance of DVPortgroupEvent from a dict
dv_portgroup_event_form_dict = dv_portgroup_event.from_dict(dv_portgroup_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


