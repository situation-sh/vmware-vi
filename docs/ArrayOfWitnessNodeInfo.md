# ArrayOfWitnessNodeInfo

A boxed array of *WitnessNodeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[WitnessNodeInfo]**](WitnessNodeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_witness_node_info import ArrayOfWitnessNodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfWitnessNodeInfo from a JSON string
array_of_witness_node_info_instance = ArrayOfWitnessNodeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfWitnessNodeInfo.to_json()

# convert the object into a dict
array_of_witness_node_info_dict = array_of_witness_node_info_instance.to_dict()
# create an instance of ArrayOfWitnessNodeInfo from a dict
array_of_witness_node_info_form_dict = array_of_witness_node_info.from_dict(array_of_witness_node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


