# ClusterDasVmConfigSpec

An incremental update to the per-virtual-machine vSphere HA configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ClusterDasVmConfigInfo**](ClusterDasVmConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_vm_config_spec import ClusterDasVmConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasVmConfigSpec from a JSON string
cluster_das_vm_config_spec_instance = ClusterDasVmConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterDasVmConfigSpec.to_json()

# convert the object into a dict
cluster_das_vm_config_spec_dict = cluster_das_vm_config_spec_instance.to_dict()
# create an instance of ClusterDasVmConfigSpec from a dict
cluster_das_vm_config_spec_form_dict = cluster_das_vm_config_spec.from_dict(cluster_das_vm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


