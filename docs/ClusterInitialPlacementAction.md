# ClusterInitialPlacementAction

Describes an initial placement of a single virtual machine  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_initial_placement_action import ClusterInitialPlacementAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInitialPlacementAction from a JSON string
cluster_initial_placement_action_instance = ClusterInitialPlacementAction.from_json(json)
# print the JSON string representation of the object
print ClusterInitialPlacementAction.to_json()

# convert the object into a dict
cluster_initial_placement_action_dict = cluster_initial_placement_action_instance.to_dict()
# create an instance of ClusterInitialPlacementAction from a dict
cluster_initial_placement_action_form_dict = cluster_initial_placement_action.from_dict(cluster_initial_placement_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


