# RemoteTSMEnabledEvent

Remote Tech Support Mode for the host has been enabled.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.remote_tsm_enabled_event import RemoteTSMEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteTSMEnabledEvent from a JSON string
remote_tsm_enabled_event_instance = RemoteTSMEnabledEvent.from_json(json)
# print the JSON string representation of the object
print RemoteTSMEnabledEvent.to_json()

# convert the object into a dict
remote_tsm_enabled_event_dict = remote_tsm_enabled_event_instance.to_dict()
# create an instance of RemoteTSMEnabledEvent from a dict
remote_tsm_enabled_event_form_dict = remote_tsm_enabled_event.from_dict(remote_tsm_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


