# ClusterCreatedEvent

This event records when a cluster is created. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**FolderEventArgument**](FolderEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.cluster_created_event import ClusterCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreatedEvent from a JSON string
cluster_created_event_instance = ClusterCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ClusterCreatedEvent.to_json()

# convert the object into a dict
cluster_created_event_dict = cluster_created_event_instance.to_dict()
# create an instance of ClusterCreatedEvent from a dict
cluster_created_event_form_dict = cluster_created_event.from_dict(cluster_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


