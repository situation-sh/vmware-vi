# RecordReplayDisabled

Deprecated as of vSphere API 6.0.  Fault thrown if a record or replay operation cannot be performed because these capabilities have been disabled on the virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.record_replay_disabled import RecordReplayDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of RecordReplayDisabled from a JSON string
record_replay_disabled_instance = RecordReplayDisabled.from_json(json)
# print the JSON string representation of the object
print RecordReplayDisabled.to_json()

# convert the object into a dict
record_replay_disabled_dict = record_replay_disabled_instance.to_dict()
# create an instance of RecordReplayDisabled from a dict
record_replay_disabled_form_dict = record_replay_disabled.from_dict(record_replay_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


