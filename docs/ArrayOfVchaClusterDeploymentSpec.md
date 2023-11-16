# ArrayOfVchaClusterDeploymentSpec

A boxed array of *VchaClusterDeploymentSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VchaClusterDeploymentSpec]**](VchaClusterDeploymentSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vcha_cluster_deployment_spec import ArrayOfVchaClusterDeploymentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVchaClusterDeploymentSpec from a JSON string
array_of_vcha_cluster_deployment_spec_instance = ArrayOfVchaClusterDeploymentSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVchaClusterDeploymentSpec.to_json()

# convert the object into a dict
array_of_vcha_cluster_deployment_spec_dict = array_of_vcha_cluster_deployment_spec_instance.to_dict()
# create an instance of ArrayOfVchaClusterDeploymentSpec from a dict
array_of_vcha_cluster_deployment_spec_form_dict = array_of_vcha_cluster_deployment_spec.from_dict(array_of_vcha_cluster_deployment_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


