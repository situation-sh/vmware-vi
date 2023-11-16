# ArrayOfVirtualAppVAppState

A boxed array of *VirtualAppVAppState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualAppVAppStateEnum]**](VirtualAppVAppStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_app_v_app_state import ArrayOfVirtualAppVAppState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualAppVAppState from a JSON string
array_of_virtual_app_v_app_state_instance = ArrayOfVirtualAppVAppState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualAppVAppState.to_json()

# convert the object into a dict
array_of_virtual_app_v_app_state_dict = array_of_virtual_app_v_app_state_instance.to_dict()
# create an instance of ArrayOfVirtualAppVAppState from a dict
array_of_virtual_app_v_app_state_form_dict = array_of_virtual_app_v_app_state.from_dict(array_of_virtual_app_v_app_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


