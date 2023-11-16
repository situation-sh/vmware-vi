# VirtualAppVAppState

A boxed *VirtualAppVAppState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualAppVAppStateEnum**](VirtualAppVAppStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_app_v_app_state import VirtualAppVAppState

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAppVAppState from a JSON string
virtual_app_v_app_state_instance = VirtualAppVAppState.from_json(json)
# print the JSON string representation of the object
print VirtualAppVAppState.to_json()

# convert the object into a dict
virtual_app_v_app_state_dict = virtual_app_v_app_state_instance.to_dict()
# create an instance of VirtualAppVAppState from a dict
virtual_app_v_app_state_form_dict = virtual_app_v_app_state.from_dict(virtual_app_v_app_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


