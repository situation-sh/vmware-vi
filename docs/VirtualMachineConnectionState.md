# VirtualMachineConnectionState

A boxed *VirtualMachineConnectionState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualMachineConnectionStateEnum**](VirtualMachineConnectionStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_connection_state import VirtualMachineConnectionState

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConnectionState from a JSON string
virtual_machine_connection_state_instance = VirtualMachineConnectionState.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConnectionState.to_json()

# convert the object into a dict
virtual_machine_connection_state_dict = virtual_machine_connection_state_instance.to_dict()
# create an instance of VirtualMachineConnectionState from a dict
virtual_machine_connection_state_form_dict = virtual_machine_connection_state.from_dict(virtual_machine_connection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


