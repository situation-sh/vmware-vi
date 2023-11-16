# ArrayOfSourceNodeSpec

A boxed array of *SourceNodeSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SourceNodeSpec]**](SourceNodeSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_source_node_spec import ArrayOfSourceNodeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSourceNodeSpec from a JSON string
array_of_source_node_spec_instance = ArrayOfSourceNodeSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfSourceNodeSpec.to_json()

# convert the object into a dict
array_of_source_node_spec_dict = array_of_source_node_spec_instance.to_dict()
# create an instance of ArrayOfSourceNodeSpec from a dict
array_of_source_node_spec_form_dict = array_of_source_node_spec.from_dict(array_of_source_node_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


