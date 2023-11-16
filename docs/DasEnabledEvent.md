# DasEnabledEvent

This event records when a cluster has been enabled for HA. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.das_enabled_event import DasEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasEnabledEvent from a JSON string
das_enabled_event_instance = DasEnabledEvent.from_json(json)
# print the JSON string representation of the object
print DasEnabledEvent.to_json()

# convert the object into a dict
das_enabled_event_dict = das_enabled_event_instance.to_dict()
# create an instance of DasEnabledEvent from a dict
das_enabled_event_form_dict = das_enabled_event.from_dict(das_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


