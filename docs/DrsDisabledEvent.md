# DrsDisabledEvent

This event records when DRS is disabled on a cluster. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_disabled_event import DrsDisabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsDisabledEvent from a JSON string
drs_disabled_event_instance = DrsDisabledEvent.from_json(json)
# print the JSON string representation of the object
print DrsDisabledEvent.to_json()

# convert the object into a dict
drs_disabled_event_dict = drs_disabled_event_instance.to_dict()
# create an instance of DrsDisabledEvent from a dict
drs_disabled_event_form_dict = drs_disabled_event.from_dict(drs_disabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


