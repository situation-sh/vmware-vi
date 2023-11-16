# DrsRecoveredFromFailureEvent

This event records that DRS has recovered from failure.  It is triggered by a successful DRS invocation after repeated failure.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_recovered_from_failure_event import DrsRecoveredFromFailureEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsRecoveredFromFailureEvent from a JSON string
drs_recovered_from_failure_event_instance = DrsRecoveredFromFailureEvent.from_json(json)
# print the JSON string representation of the object
print DrsRecoveredFromFailureEvent.to_json()

# convert the object into a dict
drs_recovered_from_failure_event_dict = drs_recovered_from_failure_event_instance.to_dict()
# create an instance of DrsRecoveredFromFailureEvent from a dict
drs_recovered_from_failure_event_form_dict = drs_recovered_from_failure_event.from_dict(drs_recovered_from_failure_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


