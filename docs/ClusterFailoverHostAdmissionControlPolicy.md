# ClusterFailoverHostAdmissionControlPolicy

The *ClusterFailoverHostAdmissionControlPolicy* dedicates one or more hosts for use during failover.  When a host fails with this policy in place, vSphere HA attempts to restart its virtual machines on a dedicated failover host. If this is not possible, for example the failover host itself has failed or it has insufficient resources, HA attempts to restart those virtual machines on another host in the cluster.  To support the availabilty of a failover host, the vCenter Server will prevent users from powering on virtual machines on that host, or from using vMotion to migrate virtual machines to the host. Also, DRS does not use the failover host for load balancing.  To obtain the status of a failover host, use the *ClusterFailoverHostAdmissionControlInfo.hostStatus* property (*ClusterComputeResourceSummary*.*ClusterComputeResourceSummary.admissionControlInfo*.*ClusterFailoverHostAdmissionControlInfo.hostStatus*).  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of managed object references to failover hosts.  ***Since:*** vSphere API 4.0  Refers instances of *HostSystem*.  | [optional] 
**failover_level** | **int** | Number of host failures that should be tolerated, still guaranteeing sufficient resources to restart virtual machines on available hosts.  If not set, we assume 1.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.cluster_failover_host_admission_control_policy import ClusterFailoverHostAdmissionControlPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFailoverHostAdmissionControlPolicy from a JSON string
cluster_failover_host_admission_control_policy_instance = ClusterFailoverHostAdmissionControlPolicy.from_json(json)
# print the JSON string representation of the object
print ClusterFailoverHostAdmissionControlPolicy.to_json()

# convert the object into a dict
cluster_failover_host_admission_control_policy_dict = cluster_failover_host_admission_control_policy_instance.to_dict()
# create an instance of ClusterFailoverHostAdmissionControlPolicy from a dict
cluster_failover_host_admission_control_policy_form_dict = cluster_failover_host_admission_control_policy.from_dict(cluster_failover_host_admission_control_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


