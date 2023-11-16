# ArrayOfPassiveNodeDeploymentSpec

A boxed array of *PassiveNodeDeploymentSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PassiveNodeDeploymentSpec]**](PassiveNodeDeploymentSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_passive_node_deployment_spec import ArrayOfPassiveNodeDeploymentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPassiveNodeDeploymentSpec from a JSON string
array_of_passive_node_deployment_spec_instance = ArrayOfPassiveNodeDeploymentSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfPassiveNodeDeploymentSpec.to_json()

# convert the object into a dict
array_of_passive_node_deployment_spec_dict = array_of_passive_node_deployment_spec_instance.to_dict()
# create an instance of ArrayOfPassiveNodeDeploymentSpec from a dict
array_of_passive_node_deployment_spec_form_dict = array_of_passive_node_deployment_spec.from_dict(array_of_passive_node_deployment_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


