# ClusterOvercommittedEvent

This event records when a cluster's host capacity cannot satisfy resource configuration constraints. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cluster_overcommitted_event import ClusterOvercommittedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOvercommittedEvent from a JSON string
cluster_overcommitted_event_instance = ClusterOvercommittedEvent.from_json(json)
# print the JSON string representation of the object
print ClusterOvercommittedEvent.to_json()

# convert the object into a dict
cluster_overcommitted_event_dict = cluster_overcommitted_event_instance.to_dict()
# create an instance of ClusterOvercommittedEvent from a dict
cluster_overcommitted_event_form_dict = cluster_overcommitted_event.from_dict(cluster_overcommitted_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


