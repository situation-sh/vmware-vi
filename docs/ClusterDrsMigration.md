# ClusterDrsMigration

Describes a single virtual machine migration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique key that identifies this recommendation.  This is used as an argument to ComputeResource.applyRecommendation.  | 
**time** | **datetime** | The time this recommendation was computed.  | 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**cpu_load** | **int** | Current CPU load for the virtual machine, in MHz.  This property is only populated for recommendations.  | [optional] 
**memory_load** | **int** | Current memory load for the virtual machine, in bytes.  This field is only populated for recommendations.  | [optional] 
**source** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**source_cpu_load** | **int** | Current CPU load on the source host, in MHz.  | [optional] 
**source_memory_load** | **int** | Current memory usage on the source host, in bytes.  | [optional] 
**destination** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**destination_cpu_load** | **int** | Current CPU load on the destination host, in MHz.  | [optional] 
**destination_memory_load** | **int** | Current memory usage on the destination host, in bytes.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_drs_migration import ClusterDrsMigration

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDrsMigration from a JSON string
cluster_drs_migration_instance = ClusterDrsMigration.from_json(json)
# print the JSON string representation of the object
print ClusterDrsMigration.to_json()

# convert the object into a dict
cluster_drs_migration_dict = cluster_drs_migration_instance.to_dict()
# create an instance of ClusterDrsMigration from a dict
cluster_drs_migration_form_dict = cluster_drs_migration.from_dict(cluster_drs_migration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


