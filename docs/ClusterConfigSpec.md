# ClusterConfigSpec

Deprecated as of VI API 2.5, use *ClusterConfigSpecEx*.  A complete cluster configuration.  All fields are defined as optional. In case of a reconfiguration, unset fields are unchanged. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**das_config** | [**ClusterDasConfigInfo**](ClusterDasConfigInfo.md) |  | [optional] 
**das_vm_config_spec** | [**List[ClusterDasVmConfigSpec]**](ClusterDasVmConfigSpec.md) | Changes to the per-virtual-machine vSphere HA settings.  | [optional] 
**drs_config** | [**ClusterDrsConfigInfo**](ClusterDrsConfigInfo.md) |  | [optional] 
**drs_vm_config_spec** | [**List[ClusterDrsVmConfigSpec]**](ClusterDrsVmConfigSpec.md) | Changes to the per-virtual-machine DRS settings.  | [optional] 
**rules_spec** | [**List[ClusterRuleSpec]**](ClusterRuleSpec.md) | Changes to the set of rules.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_config_spec import ClusterConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterConfigSpec from a JSON string
cluster_config_spec_instance = ClusterConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterConfigSpec.to_json()

# convert the object into a dict
cluster_config_spec_dict = cluster_config_spec_instance.to_dict()
# create an instance of ClusterConfigSpec from a dict
cluster_config_spec_form_dict = cluster_config_spec.from_dict(cluster_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


