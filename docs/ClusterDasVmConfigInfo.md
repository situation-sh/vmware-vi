# ClusterDasVmConfigInfo

The *ClusterDasVmConfigInfo* data object contains the HA configuration for a single virtual machine.  All fields are optional. If you set the <code>modify</code> parameter to <code>true</code> when you call *ComputeResource.ReconfigureComputeResource_Task*, an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set the <code>modify</code> parameter to <code>false</code> when you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**restart_priority** | [**DasVmPriorityEnum**](DasVmPriorityEnum.md) |  | [optional] 
**power_off_on_isolation** | **bool** | Deprecated as of VI API 2.5, use *ClusterDasVmConfigInfo.dasSettings*.*ClusterDasVmSettings.isolationResponse*. If you specify both *ClusterDasVmConfigInfo.powerOffOnIsolation* and *ClusterDasVmSettings.isolationResponse*, the value in *ClusterDasVmSettings.isolationResponse* has precedence.  Flag to indicate whether or not the virtual machine should be powered off if a host determines that it is isolated from the rest of the compute resource.  If there is nothing specified here, then the defaults are picked up from *ClusterDasConfigInfo.defaultVmSettings*.  | [optional] 
**das_settings** | [**ClusterDasVmSettings**](ClusterDasVmSettings.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_vm_config_info import ClusterDasVmConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasVmConfigInfo from a JSON string
cluster_das_vm_config_info_instance = ClusterDasVmConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasVmConfigInfo.to_json()

# convert the object into a dict
cluster_das_vm_config_info_dict = cluster_das_vm_config_info_instance.to_dict()
# create an instance of ClusterDasVmConfigInfo from a dict
cluster_das_vm_config_info_form_dict = cluster_das_vm_config_info.from_dict(cluster_das_vm_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


