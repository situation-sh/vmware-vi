# ClusterConfigInfoEx

The *ClusterConfigInfoEx* data object describes a complete cluster configuration.  For information about configuring a cluster, see *ClusterConfigSpecEx*.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_vms_config** | [**ClusterSystemVMsConfigInfo**](ClusterSystemVMsConfigInfo.md) |  | [optional] 
**das_config** | [**ClusterDasConfigInfo**](ClusterDasConfigInfo.md) |  | 
**das_vm_config** | [**List[ClusterDasVmConfigInfo]**](ClusterDasVmConfigInfo.md) | List of virtual machine configurations for the vSphere HA service.  Each entry applies to one virtual machine.  If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.  ***Since:*** VI API 2.5  | [optional] 
**drs_config** | [**ClusterDrsConfigInfo**](ClusterDrsConfigInfo.md) |  | 
**drs_vm_config** | [**List[ClusterDrsVmConfigInfo]**](ClusterDrsVmConfigInfo.md) | List of virtual machine configurations for the VMware DRS service.  Each entry applies to one virtual machine.  If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.  ***Since:*** VI API 2.5  | [optional] 
**rule** | [**List[ClusterRuleInfo]**](ClusterRuleInfo.md) | Cluster-wide rules.  ***Since:*** VI API 2.5  | [optional] 
**orchestration** | [**ClusterOrchestrationInfo**](ClusterOrchestrationInfo.md) |  | [optional] 
**vm_orchestration** | [**List[ClusterVmOrchestrationInfo]**](ClusterVmOrchestrationInfo.md) | List of virtual machine configurations that apply during cluster wide VM orchestration.  Each entry applies to one virtual machine.  If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.  ***Since:*** vSphere API 6.5  | [optional] 
**dpm_config_info** | [**ClusterDpmConfigInfo**](ClusterDpmConfigInfo.md) |  | [optional] 
**dpm_host_config** | [**List[ClusterDpmHostConfigInfo]**](ClusterDpmHostConfigInfo.md) | List of host configurations for the VMware DPM service.  Each entry applies to one host.  If a host is not specified in this array, the service uses the cluster default settings for that host.  ***Since:*** VI API 2.5  | [optional] 
**vsan_config_info** | [**VsanClusterConfigInfo**](VsanClusterConfigInfo.md) |  | [optional] 
**vsan_host_config** | [**List[VsanHostConfigInfo]**](VsanHostConfigInfo.md) | List of host configurations for the VMware VSAN service.  Each entry applies to one host.  If a host is not specified in this array, the service uses the cluster default settings for that host.  ***Since:*** vSphere API 5.5  | [optional] 
**group** | [**List[ClusterGroupInfo]**](ClusterGroupInfo.md) | Cluster-wide groups.  ***Since:*** vSphere API 4.1  | [optional] 
**infra_update_ha_config** | [**ClusterInfraUpdateHaConfigInfo**](ClusterInfraUpdateHaConfigInfo.md) |  | [optional] 
**proactive_drs_config** | [**ClusterProactiveDrsConfigInfo**](ClusterProactiveDrsConfigInfo.md) |  | [optional] 
**crypto_config** | [**ClusterCryptoConfigInfo**](ClusterCryptoConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_config_info_ex import ClusterConfigInfoEx

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterConfigInfoEx from a JSON string
cluster_config_info_ex_instance = ClusterConfigInfoEx.from_json(json)
# print the JSON string representation of the object
print ClusterConfigInfoEx.to_json()

# convert the object into a dict
cluster_config_info_ex_dict = cluster_config_info_ex_instance.to_dict()
# create an instance of ClusterConfigInfoEx from a dict
cluster_config_info_ex_form_dict = cluster_config_info_ex.from_dict(cluster_config_info_ex_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


