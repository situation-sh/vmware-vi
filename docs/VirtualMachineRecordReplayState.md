# VirtualMachineRecordReplayState

A boxed *VirtualMachineRecordReplayState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualMachineRecordReplayStateEnum**](VirtualMachineRecordReplayStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_record_replay_state import VirtualMachineRecordReplayState

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineRecordReplayState from a JSON string
virtual_machine_record_replay_state_instance = VirtualMachineRecordReplayState.from_json(json)
# print the JSON string representation of the object
print VirtualMachineRecordReplayState.to_json()

# convert the object into a dict
virtual_machine_record_replay_state_dict = virtual_machine_record_replay_state_instance.to_dict()
# create an instance of VirtualMachineRecordReplayState from a dict
virtual_machine_record_replay_state_form_dict = virtual_machine_record_replay_state.from_dict(virtual_machine_record_replay_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


