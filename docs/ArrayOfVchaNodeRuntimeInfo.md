# ArrayOfVchaNodeRuntimeInfo

A boxed array of *VchaNodeRuntimeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VchaNodeRuntimeInfo]**](VchaNodeRuntimeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vcha_node_runtime_info import ArrayOfVchaNodeRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVchaNodeRuntimeInfo from a JSON string
array_of_vcha_node_runtime_info_instance = ArrayOfVchaNodeRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVchaNodeRuntimeInfo.to_json()

# convert the object into a dict
array_of_vcha_node_runtime_info_dict = array_of_vcha_node_runtime_info_instance.to_dict()
# create an instance of ArrayOfVchaNodeRuntimeInfo from a dict
array_of_vcha_node_runtime_info_form_dict = array_of_vcha_node_runtime_info.from_dict(array_of_vcha_node_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


