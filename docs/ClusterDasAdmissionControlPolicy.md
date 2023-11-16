# ClusterDasAdmissionControlPolicy

Base class for specifying how admission control should be done for vSphere HA.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_reduction_to_tolerate_percent** | **int** | Percentage of resource reduction that a cluster of VMs can tolerate in case of a failover.  ***Since:*** vSphere API 6.5  | [optional] 
**p_mem_admission_control_enabled** | **bool** | Flag that determines whether strict admission control for persistent memory is enabled.  By default, this value is false. This flag can only be set to true if *ClusterDasConfigInfo.admissionControlEnabled* is set to true. When you use persistent memory admission control, the following operations are prevented, if doing so would violate the *ClusterDasConfigInfo.admissionControlEnabled*. - Creating a virtual machine with persistent memory. - Adding a virtual persistent memory device to a virtual machine. - Increasing the capacity of a virtual persistent memory device.    ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_admission_control_policy import ClusterDasAdmissionControlPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasAdmissionControlPolicy from a JSON string
cluster_das_admission_control_policy_instance = ClusterDasAdmissionControlPolicy.from_json(json)
# print the JSON string representation of the object
print ClusterDasAdmissionControlPolicy.to_json()

# convert the object into a dict
cluster_das_admission_control_policy_dict = cluster_das_admission_control_policy_instance.to_dict()
# create an instance of ClusterDasAdmissionControlPolicy from a dict
cluster_das_admission_control_policy_form_dict = cluster_das_admission_control_policy.from_dict(cluster_das_admission_control_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


