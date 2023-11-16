# LocalTSMEnabledEvent

Local Tech Support Mode for the host has been enabled.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.local_tsm_enabled_event import LocalTSMEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LocalTSMEnabledEvent from a JSON string
local_tsm_enabled_event_instance = LocalTSMEnabledEvent.from_json(json)
# print the JSON string representation of the object
print LocalTSMEnabledEvent.to_json()

# convert the object into a dict
local_tsm_enabled_event_dict = local_tsm_enabled_event_instance.to_dict()
# create an instance of LocalTSMEnabledEvent from a dict
local_tsm_enabled_event_form_dict = local_tsm_enabled_event.from_dict(local_tsm_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


