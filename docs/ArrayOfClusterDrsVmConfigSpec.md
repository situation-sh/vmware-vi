# ArrayOfClusterDrsVmConfigSpec

A boxed array of *ClusterDrsVmConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDrsVmConfigSpec]**](ClusterDrsVmConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_drs_vm_config_spec import ArrayOfClusterDrsVmConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDrsVmConfigSpec from a JSON string
array_of_cluster_drs_vm_config_spec_instance = ArrayOfClusterDrsVmConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDrsVmConfigSpec.to_json()

# convert the object into a dict
array_of_cluster_drs_vm_config_spec_dict = array_of_cluster_drs_vm_config_spec_instance.to_dict()
# create an instance of ArrayOfClusterDrsVmConfigSpec from a dict
array_of_cluster_drs_vm_config_spec_form_dict = array_of_cluster_drs_vm_config_spec.from_dict(array_of_cluster_drs_vm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


