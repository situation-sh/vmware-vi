# EventFilterSpecByUsername

This option specifies users used to filter event history. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_user** | **bool** | filter by system user true for system user event  | 
**user_list** | **List[str]** | all interested username list If this property is not set, then all regular user events are collected  | [optional] 

## Example

```python
from vmware_vi.models.event_filter_spec_by_username import EventFilterSpecByUsername

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilterSpecByUsername from a JSON string
event_filter_spec_by_username_instance = EventFilterSpecByUsername.from_json(json)
# print the JSON string representation of the object
print EventFilterSpecByUsername.to_json()

# convert the object into a dict
event_filter_spec_by_username_dict = event_filter_spec_by_username_instance.to_dict()
# create an instance of EventFilterSpecByUsername from a dict
event_filter_spec_by_username_form_dict = event_filter_spec_by_username.from_dict(event_filter_spec_by_username_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


