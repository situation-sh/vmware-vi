# CreatePassiveNodeRequestType

The parameters of *FailoverClusterConfigurator.createPassiveNode_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passive_deployment_spec** | [**PassiveNodeDeploymentSpec**](PassiveNodeDeploymentSpec.md) |  | 
**source_vc_spec** | [**SourceNodeSpec**](SourceNodeSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_passive_node_request_type import CreatePassiveNodeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePassiveNodeRequestType from a JSON string
create_passive_node_request_type_instance = CreatePassiveNodeRequestType.from_json(json)
# print the JSON string representation of the object
print CreatePassiveNodeRequestType.to_json()

# convert the object into a dict
create_passive_node_request_type_dict = create_passive_node_request_type_instance.to_dict()
# create an instance of CreatePassiveNodeRequestType from a dict
create_passive_node_request_type_form_dict = create_passive_node_request_type.from_dict(create_passive_node_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


