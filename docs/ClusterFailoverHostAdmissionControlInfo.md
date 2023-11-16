# ClusterFailoverHostAdmissionControlInfo

The current admission control related information if the cluster was configured with a FailoverHostAdmissionControlPolicy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_status** | [**List[ClusterFailoverHostAdmissionControlInfoHostStatus]**](ClusterFailoverHostAdmissionControlInfoHostStatus.md) | Status of the failover hosts in the cluster.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_failover_host_admission_control_info import ClusterFailoverHostAdmissionControlInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFailoverHostAdmissionControlInfo from a JSON string
cluster_failover_host_admission_control_info_instance = ClusterFailoverHostAdmissionControlInfo.from_json(json)
# print the JSON string representation of the object
print ClusterFailoverHostAdmissionControlInfo.to_json()

# convert the object into a dict
cluster_failover_host_admission_control_info_dict = cluster_failover_host_admission_control_info_instance.to_dict()
# create an instance of ClusterFailoverHostAdmissionControlInfo from a dict
cluster_failover_host_admission_control_info_form_dict = cluster_failover_host_admission_control_info.from_dict(cluster_failover_host_admission_control_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


