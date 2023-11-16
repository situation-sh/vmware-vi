# ArrayOfClusterEvent

A boxed array of *ClusterEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterEvent]**](ClusterEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_event import ArrayOfClusterEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterEvent from a JSON string
array_of_cluster_event_instance = ArrayOfClusterEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterEvent.to_json()

# convert the object into a dict
array_of_cluster_event_dict = array_of_cluster_event_instance.to_dict()
# create an instance of ArrayOfClusterEvent from a dict
array_of_cluster_event_form_dict = array_of_cluster_event.from_dict(array_of_cluster_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


