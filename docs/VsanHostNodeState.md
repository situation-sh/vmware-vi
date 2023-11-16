# VsanHostNodeState

A boxed *VsanHostNodeState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VsanHostNodeStateEnum**](VsanHostNodeStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.vsan_host_node_state import VsanHostNodeState

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostNodeState from a JSON string
vsan_host_node_state_instance = VsanHostNodeState.from_json(json)
# print the JSON string representation of the object
print VsanHostNodeState.to_json()

# convert the object into a dict
vsan_host_node_state_dict = vsan_host_node_state_instance.to_dict()
# create an instance of VsanHostNodeState from a dict
vsan_host_node_state_form_dict = vsan_host_node_state.from_dict(vsan_host_node_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


