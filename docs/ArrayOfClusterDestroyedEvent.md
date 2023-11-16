# ArrayOfClusterDestroyedEvent

A boxed array of *ClusterDestroyedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDestroyedEvent]**](ClusterDestroyedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_destroyed_event import ArrayOfClusterDestroyedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDestroyedEvent from a JSON string
array_of_cluster_destroyed_event_instance = ArrayOfClusterDestroyedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDestroyedEvent.to_json()

# convert the object into a dict
array_of_cluster_destroyed_event_dict = array_of_cluster_destroyed_event_instance.to_dict()
# create an instance of ArrayOfClusterDestroyedEvent from a dict
array_of_cluster_destroyed_event_form_dict = array_of_cluster_destroyed_event.from_dict(array_of_cluster_destroyed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


