# ArrayOfPassiveNodeNetworkSpec

A boxed array of *PassiveNodeNetworkSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PassiveNodeNetworkSpec]**](PassiveNodeNetworkSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_passive_node_network_spec import ArrayOfPassiveNodeNetworkSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPassiveNodeNetworkSpec from a JSON string
array_of_passive_node_network_spec_instance = ArrayOfPassiveNodeNetworkSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfPassiveNodeNetworkSpec.to_json()

# convert the object into a dict
array_of_passive_node_network_spec_dict = array_of_passive_node_network_spec_instance.to_dict()
# create an instance of ArrayOfPassiveNodeNetworkSpec from a dict
array_of_passive_node_network_spec_form_dict = array_of_passive_node_network_spec.from_dict(array_of_passive_node_network_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


