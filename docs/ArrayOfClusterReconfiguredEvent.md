# ArrayOfClusterReconfiguredEvent

A boxed array of *ClusterReconfiguredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterReconfiguredEvent]**](ClusterReconfiguredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_reconfigured_event import ArrayOfClusterReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterReconfiguredEvent from a JSON string
array_of_cluster_reconfigured_event_instance = ArrayOfClusterReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterReconfiguredEvent.to_json()

# convert the object into a dict
array_of_cluster_reconfigured_event_dict = array_of_cluster_reconfigured_event_instance.to_dict()
# create an instance of ArrayOfClusterReconfiguredEvent from a dict
array_of_cluster_reconfigured_event_form_dict = array_of_cluster_reconfigured_event.from_dict(array_of_cluster_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


