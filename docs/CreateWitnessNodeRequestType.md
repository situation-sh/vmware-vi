# CreateWitnessNodeRequestType

The parameters of *FailoverClusterConfigurator.createWitnessNode_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**witness_deployment_spec** | [**NodeDeploymentSpec**](NodeDeploymentSpec.md) |  | 
**source_vc_spec** | [**SourceNodeSpec**](SourceNodeSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_witness_node_request_type import CreateWitnessNodeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWitnessNodeRequestType from a JSON string
create_witness_node_request_type_instance = CreateWitnessNodeRequestType.from_json(json)
# print the JSON string representation of the object
print CreateWitnessNodeRequestType.to_json()

# convert the object into a dict
create_witness_node_request_type_dict = create_witness_node_request_type_instance.to_dict()
# create an instance of CreateWitnessNodeRequestType from a dict
create_witness_node_request_type_form_dict = create_witness_node_request_type.from_dict(create_witness_node_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


