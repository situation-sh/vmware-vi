# ArrayOfVirtualMachineRecordReplayState

A boxed array of *VirtualMachineRecordReplayState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineRecordReplayStateEnum]**](VirtualMachineRecordReplayStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_record_replay_state import ArrayOfVirtualMachineRecordReplayState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineRecordReplayState from a JSON string
array_of_virtual_machine_record_replay_state_instance = ArrayOfVirtualMachineRecordReplayState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineRecordReplayState.to_json()

# convert the object into a dict
array_of_virtual_machine_record_replay_state_dict = array_of_virtual_machine_record_replay_state_instance.to_dict()
# create an instance of ArrayOfVirtualMachineRecordReplayState from a dict
array_of_virtual_machine_record_replay_state_form_dict = array_of_virtual_machine_record_replay_state.from_dict(array_of_virtual_machine_record_replay_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


