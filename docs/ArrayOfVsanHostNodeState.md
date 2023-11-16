# ArrayOfVsanHostNodeState

A boxed array of *VsanHostNodeState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostNodeStateEnum]**](VsanHostNodeStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_node_state import ArrayOfVsanHostNodeState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostNodeState from a JSON string
array_of_vsan_host_node_state_instance = ArrayOfVsanHostNodeState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostNodeState.to_json()

# convert the object into a dict
array_of_vsan_host_node_state_dict = array_of_vsan_host_node_state_instance.to_dict()
# create an instance of ArrayOfVsanHostNodeState from a dict
array_of_vsan_host_node_state_form_dict = array_of_vsan_host_node_state.from_dict(array_of_vsan_host_node_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


