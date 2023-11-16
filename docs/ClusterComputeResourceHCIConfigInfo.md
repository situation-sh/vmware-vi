# ClusterComputeResourceHCIConfigInfo

This data object captures a subset of initial configuration of the cluster, which was configured by calling the *ClusterComputeResource.ConfigureHCI_Task* method.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_state** | **str** | Configuration pertinent to state of the HCI workflow.  Valid values are enumerated by the *HCIWorkflowState* type.  ***Since:*** vSphere API 6.7.1  | 
**dvs_setting** | [**List[ClusterComputeResourceDVSSetting]**](ClusterComputeResourceDVSSetting.md) | Contains DVS related information captured while configuring the cluster.  ***Since:*** vSphere API 6.7.1  | [optional] 
**configured_hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Contains a list of hosts that are currently configured using *ClusterComputeResource.ConfigureHCI_Task* and *ClusterComputeResource.ExtendHCI_Task* method.  A failed host will not be part of this list.  ***Since:*** vSphere API 6.7.1  Refers instances of *HostSystem*.  | [optional] 
**host_config_profile** | [**ClusterComputeResourceHostConfigurationProfile**](ClusterComputeResourceHostConfigurationProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_hci_config_info import ClusterComputeResourceHCIConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceHCIConfigInfo from a JSON string
cluster_compute_resource_hci_config_info_instance = ClusterComputeResourceHCIConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceHCIConfigInfo.to_json()

# convert the object into a dict
cluster_compute_resource_hci_config_info_dict = cluster_compute_resource_hci_config_info_instance.to_dict()
# create an instance of ClusterComputeResourceHCIConfigInfo from a dict
cluster_compute_resource_hci_config_info_form_dict = cluster_compute_resource_hci_config_info.from_dict(cluster_compute_resource_hci_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


