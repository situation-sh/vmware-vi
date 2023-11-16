# DrsEnabledEvent

This event records when DRS is enabled on a cluster. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**behavior** | **str** | The DRS automation level in (*DrsBehavior*)  | 

## Example

```python
from vmware_vi.models.drs_enabled_event import DrsEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsEnabledEvent from a JSON string
drs_enabled_event_instance = DrsEnabledEvent.from_json(json)
# print the JSON string representation of the object
print DrsEnabledEvent.to_json()

# convert the object into a dict
drs_enabled_event_dict = drs_enabled_event_instance.to_dict()
# create an instance of DrsEnabledEvent from a dict
drs_enabled_event_form_dict = drs_enabled_event.from_dict(drs_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


