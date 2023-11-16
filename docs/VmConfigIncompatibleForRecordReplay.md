# VmConfigIncompatibleForRecordReplay

Deprecated as of vSphere API 6.0.  Thrown when a virtual machine's existing or requested configuration is incompatible for record and replay.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_config_incompatible_for_record_replay import VmConfigIncompatibleForRecordReplay

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigIncompatibleForRecordReplay from a JSON string
vm_config_incompatible_for_record_replay_instance = VmConfigIncompatibleForRecordReplay.from_json(json)
# print the JSON string representation of the object
print VmConfigIncompatibleForRecordReplay.to_json()

# convert the object into a dict
vm_config_incompatible_for_record_replay_dict = vm_config_incompatible_for_record_replay_instance.to_dict()
# create an instance of VmConfigIncompatibleForRecordReplay from a dict
vm_config_incompatible_for_record_replay_form_dict = vm_config_incompatible_for_record_replay.from_dict(vm_config_incompatible_for_record_replay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


