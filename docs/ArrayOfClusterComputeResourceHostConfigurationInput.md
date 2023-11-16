# ArrayOfClusterComputeResourceHostConfigurationInput

A boxed array of *ClusterComputeResourceHostConfigurationInput*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceHostConfigurationInput]**](ClusterComputeResourceHostConfigurationInput.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_host_configuration_input import ArrayOfClusterComputeResourceHostConfigurationInput

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceHostConfigurationInput from a JSON string
array_of_cluster_compute_resource_host_configuration_input_instance = ArrayOfClusterComputeResourceHostConfigurationInput.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceHostConfigurationInput.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_host_configuration_input_dict = array_of_cluster_compute_resource_host_configuration_input_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceHostConfigurationInput from a dict
array_of_cluster_compute_resource_host_configuration_input_form_dict = array_of_cluster_compute_resource_host_configuration_input.from_dict(array_of_cluster_compute_resource_host_configuration_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


