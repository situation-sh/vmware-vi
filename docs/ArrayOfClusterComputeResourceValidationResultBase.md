# ArrayOfClusterComputeResourceValidationResultBase

A boxed array of *ClusterComputeResourceValidationResultBase*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceValidationResultBase]**](ClusterComputeResourceValidationResultBase.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_validation_result_base import ArrayOfClusterComputeResourceValidationResultBase

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceValidationResultBase from a JSON string
array_of_cluster_compute_resource_validation_result_base_instance = ArrayOfClusterComputeResourceValidationResultBase.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceValidationResultBase.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_validation_result_base_dict = array_of_cluster_compute_resource_validation_result_base_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceValidationResultBase from a dict
array_of_cluster_compute_resource_validation_result_base_form_dict = array_of_cluster_compute_resource_validation_result_base.from_dict(array_of_cluster_compute_resource_validation_result_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


