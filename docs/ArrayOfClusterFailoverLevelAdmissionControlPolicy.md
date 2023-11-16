# ArrayOfClusterFailoverLevelAdmissionControlPolicy

A boxed array of *ClusterFailoverLevelAdmissionControlPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterFailoverLevelAdmissionControlPolicy]**](ClusterFailoverLevelAdmissionControlPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_failover_level_admission_control_policy import ArrayOfClusterFailoverLevelAdmissionControlPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterFailoverLevelAdmissionControlPolicy from a JSON string
array_of_cluster_failover_level_admission_control_policy_instance = ArrayOfClusterFailoverLevelAdmissionControlPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterFailoverLevelAdmissionControlPolicy.to_json()

# convert the object into a dict
array_of_cluster_failover_level_admission_control_policy_dict = array_of_cluster_failover_level_admission_control_policy_instance.to_dict()
# create an instance of ArrayOfClusterFailoverLevelAdmissionControlPolicy from a dict
array_of_cluster_failover_level_admission_control_policy_form_dict = array_of_cluster_failover_level_admission_control_policy.from_dict(array_of_cluster_failover_level_admission_control_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


