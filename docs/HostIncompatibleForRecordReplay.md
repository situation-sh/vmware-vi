# HostIncompatibleForRecordReplay

Deprecated as of vSphere API 6.0.  This fault is thrown when an attempt is made record or replay a virtual machine on a host that is incompatible.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** |  | [optional] 
**reason** | **str** | The specific reason why the host does not support record/replay.  Values should come from *HostIncompatibleForRecordReplayReason_enum*.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_incompatible_for_record_replay import HostIncompatibleForRecordReplay

# TODO update the JSON string below
json = "{}"
# create an instance of HostIncompatibleForRecordReplay from a JSON string
host_incompatible_for_record_replay_instance = HostIncompatibleForRecordReplay.from_json(json)
# print the JSON string representation of the object
print HostIncompatibleForRecordReplay.to_json()

# convert the object into a dict
host_incompatible_for_record_replay_dict = host_incompatible_for_record_replay_instance.to_dict()
# create an instance of HostIncompatibleForRecordReplay from a dict
host_incompatible_for_record_replay_form_dict = host_incompatible_for_record_replay.from_dict(host_incompatible_for_record_replay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


