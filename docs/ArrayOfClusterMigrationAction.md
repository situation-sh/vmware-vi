# ArrayOfClusterMigrationAction

A boxed array of *ClusterMigrationAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterMigrationAction]**](ClusterMigrationAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_migration_action import ArrayOfClusterMigrationAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterMigrationAction from a JSON string
array_of_cluster_migration_action_instance = ArrayOfClusterMigrationAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterMigrationAction.to_json()

# convert the object into a dict
array_of_cluster_migration_action_dict = array_of_cluster_migration_action_instance.to_dict()
# create an instance of ArrayOfClusterMigrationAction from a dict
array_of_cluster_migration_action_form_dict = array_of_cluster_migration_action.from_dict(array_of_cluster_migration_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


