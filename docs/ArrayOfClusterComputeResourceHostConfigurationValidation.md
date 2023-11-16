# ArrayOfClusterComputeResourceHostConfigurationValidation

A boxed array of *ClusterComputeResourceHostConfigurationValidation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceHostConfigurationValidation]**](ClusterComputeResourceHostConfigurationValidation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_host_configuration_validation import ArrayOfClusterComputeResourceHostConfigurationValidation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceHostConfigurationValidation from a JSON string
array_of_cluster_compute_resource_host_configuration_validation_instance = ArrayOfClusterComputeResourceHostConfigurationValidation.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceHostConfigurationValidation.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_host_configuration_validation_dict = array_of_cluster_compute_resource_host_configuration_validation_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceHostConfigurationValidation from a dict
array_of_cluster_compute_resource_host_configuration_validation_form_dict = array_of_cluster_compute_resource_host_configuration_validation.from_dict(array_of_cluster_compute_resource_host_configuration_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


