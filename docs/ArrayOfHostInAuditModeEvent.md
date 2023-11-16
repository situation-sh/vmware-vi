# ArrayOfHostInAuditModeEvent

A boxed array of *HostInAuditModeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostInAuditModeEvent]**](HostInAuditModeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_in_audit_mode_event import ArrayOfHostInAuditModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostInAuditModeEvent from a JSON string
array_of_host_in_audit_mode_event_instance = ArrayOfHostInAuditModeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostInAuditModeEvent.to_json()

# convert the object into a dict
array_of_host_in_audit_mode_event_dict = array_of_host_in_audit_mode_event_instance.to_dict()
# create an instance of ArrayOfHostInAuditModeEvent from a dict
array_of_host_in_audit_mode_event_form_dict = array_of_host_in_audit_mode_event.from_dict(array_of_host_in_audit_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


