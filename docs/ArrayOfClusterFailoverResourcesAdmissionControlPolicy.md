# ArrayOfClusterFailoverResourcesAdmissionControlPolicy

A boxed array of *ClusterFailoverResourcesAdmissionControlPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterFailoverResourcesAdmissionControlPolicy]**](ClusterFailoverResourcesAdmissionControlPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_failover_resources_admission_control_policy import ArrayOfClusterFailoverResourcesAdmissionControlPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterFailoverResourcesAdmissionControlPolicy from a JSON string
array_of_cluster_failover_resources_admission_control_policy_instance = ArrayOfClusterFailoverResourcesAdmissionControlPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterFailoverResourcesAdmissionControlPolicy.to_json()

# convert the object into a dict
array_of_cluster_failover_resources_admission_control_policy_dict = array_of_cluster_failover_resources_admission_control_policy_instance.to_dict()
# create an instance of ArrayOfClusterFailoverResourcesAdmissionControlPolicy from a dict
array_of_cluster_failover_resources_admission_control_policy_form_dict = array_of_cluster_failover_resources_admission_control_policy.from_dict(array_of_cluster_failover_resources_admission_control_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


