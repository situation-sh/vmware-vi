# ArrayOfClusterFailoverHostAdmissionControlInfoHostStatus

A boxed array of *ClusterFailoverHostAdmissionControlInfoHostStatus*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterFailoverHostAdmissionControlInfoHostStatus]**](ClusterFailoverHostAdmissionControlInfoHostStatus.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_failover_host_admission_control_info_host_status import ArrayOfClusterFailoverHostAdmissionControlInfoHostStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterFailoverHostAdmissionControlInfoHostStatus from a JSON string
array_of_cluster_failover_host_admission_control_info_host_status_instance = ArrayOfClusterFailoverHostAdmissionControlInfoHostStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterFailoverHostAdmissionControlInfoHostStatus.to_json()

# convert the object into a dict
array_of_cluster_failover_host_admission_control_info_host_status_dict = array_of_cluster_failover_host_admission_control_info_host_status_instance.to_dict()
# create an instance of ArrayOfClusterFailoverHostAdmissionControlInfoHostStatus from a dict
array_of_cluster_failover_host_admission_control_info_host_status_form_dict = array_of_cluster_failover_host_admission_control_info_host_status.from_dict(array_of_cluster_failover_host_admission_control_info_host_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


