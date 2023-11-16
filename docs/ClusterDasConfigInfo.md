# ClusterDasConfigInfo

The *ClusterDasConfigInfo* data object contains configuration data about the HA service on a cluster.  All fields are optional. If you set the <code>modify</code> parameter to <code>true</code> when you call *ComputeResource.ReconfigureComputeResource_Task*, an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set the <code>modify</code> parameter to <code>false</code> when you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag to indicate whether or not vSphere HA feature is enabled.  | [optional] 
**vm_monitoring** | **str** | Level of HA Virtual Machine Health Monitoring Service.  You can monitor both guest and application heartbeats, guest heartbeats only, or you can disable the service. See *ClusterDasConfigInfoVmMonitoringState_enum*. The default value is *vmMonitoringDisabled*.  The Service level specified for the cluster determines the possible monitoring settings that you can use for individual virtual machines. See *ClusterVmToolsMonitoringSettings*.*ClusterVmToolsMonitoringSettings.vmMonitoring*.  ***Since:*** vSphere API 4.0  | [optional] 
**host_monitoring** | **str** | Determines whether HA restarts virtual machines after a host fails.  The default value is *ClusterDasConfigInfoServiceState_enum*.*enabled*. This property is meaningful only when *ClusterDasConfigInfo*.*ClusterDasConfigInfo.enabled* is &lt;code&gt;true&lt;/code&gt;.  When &lt;code&gt;hostMonitoring&lt;/code&gt; is *enabled*, HA restarts virtual machines after a host fails.  When &lt;code&gt;hostMonitoring&lt;/code&gt; is *disabled*, HA does not restart virtual machines after a host fails. The status of Host Monitoring does not affect other services such as virtual machine Health Monitoring or Fault Tolerance. The rest of the cluster operations follow normal processing. No configuration information is lost and re-enabling the service is a quick operation.  ***Since:*** vSphere API 4.0  | [optional] 
**vm_component_protecting** | **str** | This property indicates if vSphere HA VM Component Protection service is enabled.  The default value is *disabled*.  When &lt;code&gt;vmComponentProtecting&lt;/code&gt; is set to *disabled*, reaction to all types of VM component failures is disabled.  When &lt;code&gt;vmComponentProtecting&lt;/code&gt; is set to *enabled*, VM Component Protection service will detect and react to component failures. The actual reaction is determined by *ClusterVmComponentProtectionSettings* which is referenced by both cluster level configuration (*ClusterDasConfigInfo.defaultVmSettings*) and per-VM override *ClusterConfigInfoEx.dasVmConfig*.  ***Since:*** vSphere API 6.0  | [optional] 
**failover_level** | **int** | Deprecated as of vSphere API 4.0, use *ClusterFailoverLevelAdmissionControlPolicy* to set *ClusterDasConfigInfo.admissionControlPolicy*.  Configured failover level.  This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. Acceptable values range from one to four.  | [optional] 
**admission_control_policy** | [**ClusterDasAdmissionControlPolicy**](ClusterDasAdmissionControlPolicy.md) |  | [optional] 
**admission_control_enabled** | **bool** | Flag that determines whether strict admission control is enabled.  When you use admission control, the following operations are prevented, if doing so would violate the *ClusterDasConfigInfo.admissionControlPolicy*. - Powering on a virtual machine in the cluster. - Migrating a virtual machine into the cluster. - Increasing the CPU or memory reservation of powered-on   virtual machines in the cluster.    With admission control disabled, there is no assurance that all virtual machines in the HA cluster can be restarted after a host failure. VMware recommends that you do not disable admission control, but you might need to do so temporarily, for the following reasons: - If you need to violate the failover constraints when there   are not enough resources to support them (for example,   if you are placing hosts in standby mode to test them   for use with DPM). - If an automated process needs to take actions that might   temporarily violate the failover constraints (for example,   as part of an upgrade directed by VMware Update Manager). - If you need to perform testing or maintenance operations.  | [optional] 
**default_vm_settings** | [**ClusterDasVmSettings**](ClusterDasVmSettings.md) |  | [optional] 
**option** | [**List[OptionValue]**](OptionValue.md) | Advanced settings.  | [optional] 
**heartbeat_datastore** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The list of preferred datastores to use for storage heartbeating.  Each of the specified datastores should be active and mounted by more than one host. There is no limit on the number of specified datastores and no priority among them. The specified datastores will replace those previously specified and an empty list will delete all such earlier specified ones.  vCenter Server chooses the heartbeat datastores for a host from the set specified by *ClusterDasConfigInfo.hBDatastoreCandidatePolicy*. The choice is made based on datastore connectivity and storage array redundancy (in case of VMFS).  The final set of selected heartbeat datastores is reported via *ClusterDasAdvancedRuntimeInfo.heartbeatDatastoreInfo*.  ***Since:*** vSphere API 5.0  Refers instances of *Datastore*.  | [optional] 
**h_b_datastore_candidate_policy** | **str** | The policy on what datastores will be used by vCenter Server to choose heartbeat datastores.  See *ClusterDasConfigInfoHBDatastoreCandidate_enum* for all options. The default value is *allFeasibleDsWithUserPreference*.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_config_info import ClusterDasConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasConfigInfo from a JSON string
cluster_das_config_info_instance = ClusterDasConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasConfigInfo.to_json()

# convert the object into a dict
cluster_das_config_info_dict = cluster_das_config_info_instance.to_dict()
# create an instance of ClusterDasConfigInfo from a dict
cluster_das_config_info_form_dict = cluster_das_config_info.from_dict(cluster_das_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


