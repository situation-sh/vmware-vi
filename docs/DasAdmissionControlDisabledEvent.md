# DasAdmissionControlDisabledEvent

This event records when admission control checks have been disabled in a HA cluster. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.das_admission_control_disabled_event import DasAdmissionControlDisabledEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DasAdmissionControlDisabledEvent from a JSON string
das_admission_control_disabled_event_instance = DasAdmissionControlDisabledEvent.from_json(json)
# print the JSON string representation of the object
print DasAdmissionControlDisabledEvent.to_json()

# convert the object into a dict
das_admission_control_disabled_event_dict = das_admission_control_disabled_event_instance.to_dict()
# create an instance of DasAdmissionControlDisabledEvent from a dict
das_admission_control_disabled_event_form_dict = das_admission_control_disabled_event.from_dict(das_admission_control_disabled_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


