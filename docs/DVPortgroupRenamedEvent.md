# DVPortgroupRenamedEvent

Two distributed virtual portgroup was renamed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The old portgroup name.  ***Since:*** vSphere API 4.0  | 
**new_name** | **str** | The new portgroup name.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dv_portgroup_renamed_event import DVPortgroupRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupRenamedEvent from a JSON string
dv_portgroup_renamed_event_instance = DVPortgroupRenamedEvent.from_json(json)
# print the JSON string representation of the object
print DVPortgroupRenamedEvent.to_json()

# convert the object into a dict
dv_portgroup_renamed_event_dict = dv_portgroup_renamed_event_instance.to_dict()
# create an instance of DVPortgroupRenamedEvent from a dict
dv_portgroup_renamed_event_form_dict = dv_portgroup_renamed_event.from_dict(dv_portgroup_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


