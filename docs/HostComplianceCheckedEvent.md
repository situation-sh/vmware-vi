# HostComplianceCheckedEvent

This event records that a compliance check was triggered on the host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProfileEventArgument**](ProfileEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.host_compliance_checked_event import HostComplianceCheckedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostComplianceCheckedEvent from a JSON string
host_compliance_checked_event_instance = HostComplianceCheckedEvent.from_json(json)
# print the JSON string representation of the object
print HostComplianceCheckedEvent.to_json()

# convert the object into a dict
host_compliance_checked_event_dict = host_compliance_checked_event_instance.to_dict()
# create an instance of HostComplianceCheckedEvent from a dict
host_compliance_checked_event_form_dict = host_compliance_checked_event.from_dict(host_compliance_checked_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


