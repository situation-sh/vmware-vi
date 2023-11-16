# DasDisabledEvent

This event records when a cluster has been disabled for HA. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.das_disabled_event import DasDisabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasDisabledEvent from a JSON string
das_disabled_event_instance = DasDisabledEvent.from_json(json)
# print the JSON string representation of the object
print DasDisabledEvent.to_json()

# convert the object into a dict
das_disabled_event_dict = das_disabled_event_instance.to_dict()
# create an instance of DasDisabledEvent from a dict
das_disabled_event_form_dict = das_disabled_event.from_dict(das_disabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


