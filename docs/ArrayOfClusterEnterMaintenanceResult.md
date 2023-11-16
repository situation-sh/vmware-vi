# ArrayOfClusterEnterMaintenanceResult

A boxed array of *ClusterEnterMaintenanceResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterEnterMaintenanceResult]**](ClusterEnterMaintenanceResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_enter_maintenance_result import ArrayOfClusterEnterMaintenanceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterEnterMaintenanceResult from a JSON string
array_of_cluster_enter_maintenance_result_instance = ArrayOfClusterEnterMaintenanceResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterEnterMaintenanceResult.to_json()

# convert the object into a dict
array_of_cluster_enter_maintenance_result_dict = array_of_cluster_enter_maintenance_result_instance.to_dict()
# create an instance of ArrayOfClusterEnterMaintenanceResult from a dict
array_of_cluster_enter_maintenance_result_form_dict = array_of_cluster_enter_maintenance_result.from_dict(array_of_cluster_enter_maintenance_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


