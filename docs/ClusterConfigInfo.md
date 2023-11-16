# ClusterConfigInfo

Deprecated as of VI API 2.5, use *ClusterConfigInfoEx*.  A complete cluster configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**das_config** | [**ClusterDasConfigInfo**](ClusterDasConfigInfo.md) |  | 
**das_vm_config** | [**List[ClusterDasVmConfigInfo]**](ClusterDasVmConfigInfo.md) | List of virtual machine configurations for the vSphere HA service.  Each entry applies to one virtual machine.  If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.  | [optional] 
**drs_config** | [**ClusterDrsConfigInfo**](ClusterDrsConfigInfo.md) |  | 
**drs_vm_config** | [**List[ClusterDrsVmConfigInfo]**](ClusterDrsVmConfigInfo.md) | List of virtual machine configurations for the VMware DRS service.  Each entry applies to one virtual machine.  If a virtual machine is not specified in this array, the service uses the default settings for that virtual machine.  | [optional] 
**rule** | [**List[ClusterRuleInfo]**](ClusterRuleInfo.md) | Cluster-wide rules.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_config_info import ClusterConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterConfigInfo from a JSON string
cluster_config_info_instance = ClusterConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterConfigInfo.to_json()

# convert the object into a dict
cluster_config_info_dict = cluster_config_info_instance.to_dict()
# create an instance of ClusterConfigInfo from a dict
cluster_config_info_form_dict = cluster_config_info.from_dict(cluster_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


