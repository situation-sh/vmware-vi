# ClusterComputeResourceValidationResultBase

Describes the validation results.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**List[LocalizableMessage]**](LocalizableMessage.md) | Describes the messages relevant to the validation result  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_validation_result_base import ClusterComputeResourceValidationResultBase

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceValidationResultBase from a JSON string
cluster_compute_resource_validation_result_base_instance = ClusterComputeResourceValidationResultBase.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceValidationResultBase.to_json()

# convert the object into a dict
cluster_compute_resource_validation_result_base_dict = cluster_compute_resource_validation_result_base_instance.to_dict()
# create an instance of ClusterComputeResourceValidationResultBase from a dict
cluster_compute_resource_validation_result_base_form_dict = cluster_compute_resource_validation_result_base.from_dict(cluster_compute_resource_validation_result_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


