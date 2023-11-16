# Capability

A particular product may or may not support certain features.  This data object indicates whether or not a service instance implements these features. This data object type indicates the circumstances under which an operation throws a *NotSupported* fault.  Support for some features is indicated by the presence or absence of the manager object from the service instance. For example, the AlarmManager manager object indicates collecting alarms is supported. Other features indicate whether or not a given operation on an object throws a *NotSupported* fault.  Some capabilities depend on the host or virtual machine version. These are specified by using the vim.host.Capability and vim.vm.Capability objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioning_supported** | **bool** | Indicates whether or not the service instance supports provisioning.  For example, the *CloneVM* operation.  | 
**multi_host_supported** | **bool** | Indicates whether or not the service instance supports multiple hosts.  | 
**user_shell_access_supported** | **bool** | Flag indicating whether host user accounts should have the option to be granted shell access  ***Since:*** VI API 2.5  | 
**supported_evc_mode** | [**List[EVCMode]**](EVCMode.md) | All supported Enhanced VMotion Compatibility modes.  ***Since:*** vSphere API 4.0  | [optional] 
**supported_evc_graphics_mode** | [**List[FeatureEVCMode]**](FeatureEVCMode.md) | All supported Enhanced VMotion Compatibility Graphics modes.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**network_backup_and_restore_supported** | **bool** | Indicates whether network backup and restore feature is supported.  ***Since:*** vSphere API 5.1  | [optional] 
**ft_drs_without_evc_supported** | **bool** | Is DRS supported for Fault Tolerance VMs without enabling EVC.  ***Since:*** vSphere API 6.7  | [optional] 
**hci_workflow_supported** | **bool** | Specifies if the workflow for setting up a HCI cluster is supported.  ***Since:*** vSphere API 6.7.1  | [optional] 
**compute_policy_version** | **int** | Specifies the supported compute policy version.  ***Since:*** vSphere API 6.8.7  | [optional] 
**cluster_placement_supported** | **bool** |  | [optional] 
**lifecycle_management_supported** | **bool** | Specifies if lifecycle management of a Cluster is supported.  ***Since:*** vSphere API 7.0  | [optional] 
**host_seeding_supported** | **bool** | Specifies if host seeding for a cluster is supported.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**scalable_shares_supported** | **bool** | Specifies if scalable shares for resource pools is supported.  ***Since:*** vSphere API 7.0  | [optional] 
**hadcs_supported** | **bool** | Specifies if highly available distributed clustering service is supported.  ***Since:*** vSphere API 7.0.1.1  | [optional] 
**config_mgmt_supported** | **bool** | Specifies if desired configuration management platform is supported on the cluster.  | [optional] 

## Example

```python
from vmware_vi.models.capability import Capability

# TODO update the JSON string below
json = "{}"
# create an instance of Capability from a JSON string
capability_instance = Capability.from_json(json)
# print the JSON string representation of the object
print Capability.to_json()

# convert the object into a dict
capability_dict = capability_instance.to_dict()
# create an instance of Capability from a dict
capability_form_dict = capability.from_dict(capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


