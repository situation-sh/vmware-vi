# ClusterStatusChangedEvent

This event records when a cluster's overall status changed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_status** | **str** | The old (*status*).  | 
**new_status** | **str** | The new (*status*).  | 

## Example

```python
from vmware_vi.models.cluster_status_changed_event import ClusterStatusChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatusChangedEvent from a JSON string
cluster_status_changed_event_instance = ClusterStatusChangedEvent.from_json(json)
# print the JSON string representation of the object
print ClusterStatusChangedEvent.to_json()

# convert the object into a dict
cluster_status_changed_event_dict = cluster_status_changed_event_instance.to_dict()
# create an instance of ClusterStatusChangedEvent from a dict
cluster_status_changed_event_form_dict = cluster_status_changed_event.from_dict(cluster_status_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


