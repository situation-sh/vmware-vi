# ClusterClusterInitialPlacementAction

Describes an action for the initial placement of a virtual machine in a cluster.  This action is used by the cross cluster placement API when a virtual machine needs to be placed across a set of given clusters. See *Folder.PlaceVmsXCluster*. This action encapsulates details about the chosen cluster (via the resource pool inside that cluster), the chosen host and the chosen datastores for the disks of the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**config_spec** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_cluster_initial_placement_action import ClusterClusterInitialPlacementAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterClusterInitialPlacementAction from a JSON string
cluster_cluster_initial_placement_action_instance = ClusterClusterInitialPlacementAction.from_json(json)
# print the JSON string representation of the object
print ClusterClusterInitialPlacementAction.to_json()

# convert the object into a dict
cluster_cluster_initial_placement_action_dict = cluster_cluster_initial_placement_action_instance.to_dict()
# create an instance of ClusterClusterInitialPlacementAction from a dict
cluster_cluster_initial_placement_action_form_dict = cluster_cluster_initial_placement_action.from_dict(cluster_cluster_initial_placement_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


