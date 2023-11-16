# ArrayOfClusterActionHistory

A boxed array of *ClusterActionHistory*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterActionHistory]**](ClusterActionHistory.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_action_history import ArrayOfClusterActionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterActionHistory from a JSON string
array_of_cluster_action_history_instance = ArrayOfClusterActionHistory.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterActionHistory.to_json()

# convert the object into a dict
array_of_cluster_action_history_dict = array_of_cluster_action_history_instance.to_dict()
# create an instance of ArrayOfClusterActionHistory from a dict
array_of_cluster_action_history_form_dict = array_of_cluster_action_history.from_dict(array_of_cluster_action_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


