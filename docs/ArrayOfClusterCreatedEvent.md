# ArrayOfClusterCreatedEvent

A boxed array of *ClusterCreatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterCreatedEvent]**](ClusterCreatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_created_event import ArrayOfClusterCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterCreatedEvent from a JSON string
array_of_cluster_created_event_instance = ArrayOfClusterCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterCreatedEvent.to_json()

# convert the object into a dict
array_of_cluster_created_event_dict = array_of_cluster_created_event_instance.to_dict()
# create an instance of ArrayOfClusterCreatedEvent from a dict
array_of_cluster_created_event_form_dict = array_of_cluster_created_event.from_dict(array_of_cluster_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


