# HostInAuditModeEvent

Host is booted in audit mode.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_in_audit_mode_event import HostInAuditModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostInAuditModeEvent from a JSON string
host_in_audit_mode_event_instance = HostInAuditModeEvent.from_json(json)
# print the JSON string representation of the object
print HostInAuditModeEvent.to_json()

# convert the object into a dict
host_in_audit_mode_event_dict = host_in_audit_mode_event_instance.to_dict()
# create an instance of HostInAuditModeEvent from a dict
host_in_audit_mode_event_form_dict = host_in_audit_mode_event.from_dict(host_in_audit_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


