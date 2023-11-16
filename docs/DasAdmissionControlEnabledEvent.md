# DasAdmissionControlEnabledEvent

This event records when admission control checks have been enabled in a HA cluster. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.das_admission_control_enabled_event import DasAdmissionControlEnabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasAdmissionControlEnabledEvent from a JSON string
das_admission_control_enabled_event_instance = DasAdmissionControlEnabledEvent.from_json(json)
# print the JSON string representation of the object
print DasAdmissionControlEnabledEvent.to_json()

# convert the object into a dict
das_admission_control_enabled_event_dict = das_admission_control_enabled_event_instance.to_dict()
# create an instance of DasAdmissionControlEnabledEvent from a dict
das_admission_control_enabled_event_form_dict = das_admission_control_enabled_event.from_dict(das_admission_control_enabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


