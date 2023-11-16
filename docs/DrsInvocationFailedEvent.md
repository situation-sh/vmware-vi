# DrsInvocationFailedEvent

This event records DRS invocation failure.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_invocation_failed_event import DrsInvocationFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsInvocationFailedEvent from a JSON string
drs_invocation_failed_event_instance = DrsInvocationFailedEvent.from_json(json)
# print the JSON string representation of the object
print DrsInvocationFailedEvent.to_json()

# convert the object into a dict
drs_invocation_failed_event_dict = drs_invocation_failed_event_instance.to_dict()
# create an instance of DrsInvocationFailedEvent from a dict
drs_invocation_failed_event_form_dict = drs_invocation_failed_event.from_dict(drs_invocation_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


