# HostCompliantEvent

This event records that host is in compliance.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_compliant_event import HostCompliantEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCompliantEvent from a JSON string
host_compliant_event_instance = HostCompliantEvent.from_json(json)
# print the JSON string representation of the object
print HostCompliantEvent.to_json()

# convert the object into a dict
host_compliant_event_dict = host_compliant_event_instance.to_dict()
# create an instance of HostCompliantEvent from a dict
host_compliant_event_form_dict = host_compliant_event.from_dict(host_compliant_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


