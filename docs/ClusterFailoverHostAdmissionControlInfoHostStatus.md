# ClusterFailoverHostAdmissionControlInfoHostStatus

Data object containing the status of a failover host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 

## Example

```python
from vmware_vi.models.cluster_failover_host_admission_control_info_host_status import ClusterFailoverHostAdmissionControlInfoHostStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFailoverHostAdmissionControlInfoHostStatus from a JSON string
cluster_failover_host_admission_control_info_host_status_instance = ClusterFailoverHostAdmissionControlInfoHostStatus.from_json(json)
# print the JSON string representation of the object
print ClusterFailoverHostAdmissionControlInfoHostStatus.to_json()

# convert the object into a dict
cluster_failover_host_admission_control_info_host_status_dict = cluster_failover_host_admission_control_info_host_status_instance.to_dict()
# create an instance of ClusterFailoverHostAdmissionControlInfoHostStatus from a dict
cluster_failover_host_admission_control_info_host_status_form_dict = cluster_failover_host_admission_control_info_host_status.from_dict(cluster_failover_host_admission_control_info_host_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


