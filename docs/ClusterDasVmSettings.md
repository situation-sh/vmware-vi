# ClusterDasVmSettings

The *ClusterDasVmSettings* data object contains the HA configuration settings specified for a single virtual machine (identified by *ClusterDasVmConfigInfo*.*ClusterDasVmConfigInfo.key*) or as cluster-wide defaults *ClusterDasConfigInfo*.*ClusterDasConfigInfo.defaultVmSettings*  All fields are optional. If you set the <code>modify</code> parameter to <code>true</code> when you call *ComputeResource.ReconfigureComputeResource_Task*, an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set the <code>modify</code> parameter to <code>false</code> when you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restart_priority** | **str** | Restart priority for a virtual machine.  If not specified at either the cluster level or the virtual machine level, this will default to &lt;code&gt;medium&lt;/code&gt;.  See also *ClusterDasVmSettingsRestartPriority_enum*.  ***Since:*** VI API 2.5  | [optional] 
**restart_priority_timeout** | **int** | This setting is used to specify a maximum time the lower priority VMs should wait for the higher priority VMs to be ready.  If the higher priority Vms are not ready by this time, then the lower priority VMs are restarted irrespective of the VM ready state. This timeout can be used to prevent the failover of lower priority VMs to be stuck infinitely.  This timeout is not used if ready condition is *none*  Timeout specified in seconds. To use cluster setting for a VM override, set to -1 in per-VM. setting.  ***Since:*** vSphere API 6.5  | [optional] 
**isolation_response** | **str** | Indicates whether or not the virtual machine should be powered off if a host determines that it is isolated from the rest of the compute resource.  If not specified at either the cluster level or the virtual machine level, this will default to &lt;code&gt;powerOff&lt;/code&gt;.  See also *ClusterDasVmSettingsIsolationResponse_enum*.  ***Since:*** VI API 2.5  | [optional] 
**vm_tools_monitoring_settings** | [**ClusterVmToolsMonitoringSettings**](ClusterVmToolsMonitoringSettings.md) |  | [optional] 
**vm_component_protection_settings** | [**ClusterVmComponentProtectionSettings**](ClusterVmComponentProtectionSettings.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_vm_settings import ClusterDasVmSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasVmSettings from a JSON string
cluster_das_vm_settings_instance = ClusterDasVmSettings.from_json(json)
# print the JSON string representation of the object
print ClusterDasVmSettings.to_json()

# convert the object into a dict
cluster_das_vm_settings_dict = cluster_das_vm_settings_instance.to_dict()
# create an instance of ClusterDasVmSettings from a dict
cluster_das_vm_settings_form_dict = cluster_das_vm_settings.from_dict(cluster_das_vm_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


