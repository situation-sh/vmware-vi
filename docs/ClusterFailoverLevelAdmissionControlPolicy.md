# ClusterFailoverLevelAdmissionControlPolicy

The *ClusterFailoverLevelAdmissionControlPolicy* defines the number of host failures that should be tolerated and still guarantee enough unfragmented resources to failover all powered on virtual machines on those failed hosts.  When you use the failover level policy, vSphere HA partitions resources into slots. A slot represents the minimum CPU and memory resources that are required to support any powered-on virtual machine in the cluster.  With the failover level policy in place, HA uses the following slot calculations to control virtual machine migration within the cluster: 1. Calculate the slot size from CPU and memory reservations.    The CPU value is the largest CPU reservation for all powered-on    virtual machines in the cluster. The memory value is the largest    memory reservation (plus memory overhead).        If your cluster contains any virtual machines that have much larger    reservations than the others, they will distort slot size calculation.    To avoid this, you can specify an upper bound for slot sizes;    use the configuration editor in the vSphere Client to set the    das.slotCpuInMHz and das.slotMemInMB attributes. When you use these    attributes, there is a risk that resource fragmentation will cause    virtual machines with resource requirements larger than the slot size    to be assigned multiple slots. In a cluster that is close to capacity,    there might be enough slots in aggregate for HA to successfully    failover a virtual machine. However, if those slots are located    on multiple hosts, a virtual machine assigned multiple slots cannot    use them because a virtual machine can run on only a single host    at a time. 2. Determine how many slots each host in the cluster can hold.    HA uses the CPU and memory resources in a host's root resource pool    to determine host slot capacity, not the total physical resources    of the host. Resources used for virtualization purposes are not    included. HA uses connected hosts that are not in maintenance mode    and that do not have any HA errors.        The CPU slot resource is the host CPU resource amount divided    by the CPU component of the slot size; the result is rounded down.    HA makes the same calculation for host memory resource amount.    HA compares the results; the lower of the two numbers is the    host slot capacity. 3. Determine the current failover capacity of the cluster. This is the    number of hosts (starting from the largest) that can fail and still    leave enough slots to satisfy all of the powered-on virtual machines. 4. Compare the current failover capacity to the configured    *ClusterFailoverLevelAdmissionControlPolicy.failoverLevel*.    If the current failover capacity is less than the configured    failover level, HA disallows the operation.     ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_level** | **int** | Number of host failures that should be tolerated, still guaranteeing sufficient resources to restart virtual machines on available hosts.  ***Since:*** vSphere API 4.0  | 
**slot_policy** | [**ClusterSlotPolicy**](ClusterSlotPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_failover_level_admission_control_policy import ClusterFailoverLevelAdmissionControlPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFailoverLevelAdmissionControlPolicy from a JSON string
cluster_failover_level_admission_control_policy_instance = ClusterFailoverLevelAdmissionControlPolicy.from_json(json)
# print the JSON string representation of the object
print ClusterFailoverLevelAdmissionControlPolicy.to_json()

# convert the object into a dict
cluster_failover_level_admission_control_policy_dict = cluster_failover_level_admission_control_policy_instance.to_dict()
# create an instance of ClusterFailoverLevelAdmissionControlPolicy from a dict
cluster_failover_level_admission_control_policy_form_dict = cluster_failover_level_admission_control_policy.from_dict(cluster_failover_level_admission_control_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


