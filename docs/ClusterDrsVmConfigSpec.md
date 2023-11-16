# ClusterDrsVmConfigSpec

Updates the per-virtual-machine DRS configuration.  To update the DRS configuration of a virtual machine, a copy of this object is included in the *ClusterConfigSpecEx* object passed to the method *ComputeResource.ReconfigureComputeResource_Task*.  If _reconfigureEx_ is used to incrementally update the cluster configuration (i.e., the parameter **modify** is true), then three operations are provided for updating the DRS configuration for a virtual machine. These operations are listed below (see *ArrayUpdateSpec* for more information on these operations). - add: add a configuration for the virtual machine, overwritting the existing   configuration if one exists - edit: incrmentally update the existing configuration; an existing configuration   must exist - remove: remove the existing configuration; an existing configuration must exist    If, instead, this method is used to overwrite the cluster configuration (i.e., the parameter **modify** is false) thereby creating a new configuration, only the add operation is allowed. In this case, _add_ creates a DRS configuration for a virtual machine in the new cluster configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ClusterDrsVmConfigInfo**](ClusterDrsVmConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_drs_vm_config_spec import ClusterDrsVmConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDrsVmConfigSpec from a JSON string
cluster_drs_vm_config_spec_instance = ClusterDrsVmConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterDrsVmConfigSpec.to_json()

# convert the object into a dict
cluster_drs_vm_config_spec_dict = cluster_drs_vm_config_spec_instance.to_dict()
# create an instance of ClusterDrsVmConfigSpec from a dict
cluster_drs_vm_config_spec_form_dict = cluster_drs_vm_config_spec.from_dict(cluster_drs_vm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


