# VchaClusterDeploymentSpec

The VchaClusterDeploymentSpec class contains deployment information for creating and configuring a VCHA Cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passive_deployment_spec** | [**PassiveNodeDeploymentSpec**](PassiveNodeDeploymentSpec.md) |  | 
**witness_deployment_spec** | [**NodeDeploymentSpec**](NodeDeploymentSpec.md) |  | 
**active_vc_spec** | [**SourceNodeSpec**](SourceNodeSpec.md) |  | 
**active_vc_network_config** | [**ClusterNetworkConfigSpec**](ClusterNetworkConfigSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vcha_cluster_deployment_spec import VchaClusterDeploymentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VchaClusterDeploymentSpec from a JSON string
vcha_cluster_deployment_spec_instance = VchaClusterDeploymentSpec.from_json(json)
# print the JSON string representation of the object
print VchaClusterDeploymentSpec.to_json()

# convert the object into a dict
vcha_cluster_deployment_spec_dict = vcha_cluster_deployment_spec_instance.to_dict()
# create an instance of VchaClusterDeploymentSpec from a dict
vcha_cluster_deployment_spec_form_dict = vcha_cluster_deployment_spec.from_dict(vcha_cluster_deployment_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


