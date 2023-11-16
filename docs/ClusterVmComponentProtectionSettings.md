# ClusterVmComponentProtectionSettings

vSphere HA Virtual Machine Component Protection Service settings.  vSphere HA Virtual Machine Component Protection Service detects and reacts to storage failures that do not necessarily cause a virtual machine to go down, but may impact the health or QoS of the virtual machine.  All fields are defined as optional. In case of a reconfiguration, fields left unset are not changed.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_storage_protection_for_apd** | **str** | VM storage protection setting for storage failures categorized as All Paths Down (APD).  APD is a condition where a storage has become inaccessible for unknown reasons. It only indicates loss of connectivity and does not indicate storage device failure or LUN removal (Permenant Device Loss or PDL). The details of APD and PDL are described in *HostMountInfoInaccessibleReason_enum*.  This property is meaningful only when vSphere HA is turned on. Valid values are specified by *ClusterVmComponentProtectionSettingsStorageVmReaction_enum*. The default value is *disabled* for cluster setting and *clusterDefault* for per-VM setting.  When an APD condition happens and the host begins timing out I/Os (@link vim.host.MountInfo.InaccessibleReason#AllPathsDown\\_Timeout}, VM Component Protection service will react based on the specific value of this property: - ***disabled***, no reaction, i.e., no   VM failover and no event reporting for the failures. - ***warning***, service will issue events,   alarms and/or config issues for component failures. - ***restartConservative***, service will   terminate the impacted VMs after a preconfigured time interval   (*ClusterVmComponentProtectionSettings.vmTerminateDelayForAPDSec*) if they are to be restarted. - ***restartAggressive***, service might   terminate the impacted VMs after a preconfigured time interval   (*ClusterVmComponentProtectionSettings.vmTerminateDelayForAPDSec*). In some cases, a VM is terminated   even if it may not able to be restarted or lose Fault Tolerance redundancy. - ***clusterDefault***, service will implement   cluster default.    ***Since:*** vSphere API 6.0  | [optional] 
**enable_apd_timeout_for_hosts** | **bool** | This property indicates if APD timeout will be enabled for all the hosts in the cluster when vSphere HA is configured.  The details of APD timeout are described in *HostMountInfoInaccessibleReason_enum*.  If *ClusterDasConfigInfo.vmComponentProtecting* is *disabled*, the property will be ignored. Otherwise, for each host in the cluster, APD timeout will be enabled. Note that no change will be made for a host if it already had APD timeout enabled.  This property is meaningful only for cluster setting. It is ignored if specified at VM level. The default value is false if not specified.  Note that this property is not persisted by vSphere backend. It does not impact any cluster reconfiguration or host operation (such as adding a host to a cluster) that might happen later.  ***Since:*** vSphere API 6.0  | [optional] 
**vm_terminate_delay_for_apd_sec** | **int** | The time interval after an APD timeout has been declared and before VM Component Protection service will terminate the VM.  The value only applies if *ClusterVmComponentProtectionSettings.vmStorageProtectionForAPD* is set to *restartConservative* or *restartAggressive*.  The default value is 180 seconds if not specified. To use cluster setting for a VM override, set to -1 in per-VM setting.  ***Since:*** vSphere API 6.0  | [optional] 
**vm_reaction_on_apd_cleared** | **str** | Action taken by VM Component Protection service for a powered on VM when APD condition clears after APD timeout.  This property is meaningful only when vSphere HA is turned on. Valid values are specified by *ClusterVmComponentProtectionSettingsVmReactionOnAPDCleared_enum*. The default value is *none* for cluster setting and *useClusterDefault* for per-VM setting.  ***Since:*** vSphere API 6.0  | [optional] 
**vm_storage_protection_for_pdl** | **str** | VM storage protection setting for storage failures categorized as Permenant Device Loss (PDL).  PDL indicates storage device failure or LUN removal. In case of PDL, the failed datastore or device is unlikely to recover. The details of PDL are described in *HostMountInfoInaccessibleReason_enum*.  This property is meaningful only when vSphere HA is turned on. Valid values are *disabled*, *warning*, *restartAggressive* and *clusterDefault*. The default value is *disabled* for cluster setting and *clusterDefault* for per-VM setting.  When set to *restartAggressive*, VM Component Protection service will immediately terminate the VMs impacted by PDL and will attempt to restart the VMs with best effort. When set to the other values, the behavior is the same as described for *ClusterVmComponentProtectionSettings.vmStorageProtectionForAPD*.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_vm_component_protection_settings import ClusterVmComponentProtectionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVmComponentProtectionSettings from a JSON string
cluster_vm_component_protection_settings_instance = ClusterVmComponentProtectionSettings.from_json(json)
# print the JSON string representation of the object
print ClusterVmComponentProtectionSettings.to_json()

# convert the object into a dict
cluster_vm_component_protection_settings_dict = cluster_vm_component_protection_settings_instance.to_dict()
# create an instance of ClusterVmComponentProtectionSettings from a dict
cluster_vm_component_protection_settings_form_dict = cluster_vm_component_protection_settings.from_dict(cluster_vm_component_protection_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


