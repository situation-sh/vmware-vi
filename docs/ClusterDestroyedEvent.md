# ClusterDestroyedEvent

This event records when a cluster is destroyed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cluster_destroyed_event import ClusterDestroyedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDestroyedEvent from a JSON string
cluster_destroyed_event_instance = ClusterDestroyedEvent.from_json(json)
# print the JSON string representation of the object
print ClusterDestroyedEvent.to_json()

# convert the object into a dict
cluster_destroyed_event_dict = cluster_destroyed_event_instance.to_dict()
# create an instance of ClusterDestroyedEvent from a dict
cluster_destroyed_event_form_dict = cluster_destroyed_event.from_dict(cluster_destroyed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


