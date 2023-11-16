# ArrayOfHostComplianceCheckedEvent

A boxed array of *HostComplianceCheckedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostComplianceCheckedEvent]**](HostComplianceCheckedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_compliance_checked_event import ArrayOfHostComplianceCheckedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostComplianceCheckedEvent from a JSON string
array_of_host_compliance_checked_event_instance = ArrayOfHostComplianceCheckedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostComplianceCheckedEvent.to_json()

# convert the object into a dict
array_of_host_compliance_checked_event_dict = array_of_host_compliance_checked_event_instance.to_dict()
# create an instance of ArrayOfHostComplianceCheckedEvent from a dict
array_of_host_compliance_checked_event_form_dict = array_of_host_compliance_checked_event.from_dict(array_of_host_compliance_checked_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


