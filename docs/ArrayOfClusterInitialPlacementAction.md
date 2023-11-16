# ArrayOfClusterInitialPlacementAction

A boxed array of *ClusterInitialPlacementAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterInitialPlacementAction]**](ClusterInitialPlacementAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_initial_placement_action import ArrayOfClusterInitialPlacementAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterInitialPlacementAction from a JSON string
array_of_cluster_initial_placement_action_instance = ArrayOfClusterInitialPlacementAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterInitialPlacementAction.to_json()

# convert the object into a dict
array_of_cluster_initial_placement_action_dict = array_of_cluster_initial_placement_action_instance.to_dict()
# create an instance of ArrayOfClusterInitialPlacementAction from a dict
array_of_cluster_initial_placement_action_form_dict = array_of_cluster_initial_placement_action.from_dict(array_of_cluster_initial_placement_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


