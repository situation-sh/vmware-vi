# HostCnxFailedBadVersionEvent

This event records a failure to connect to a host due to an incompatible client version. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_cnx_failed_bad_version_event import HostCnxFailedBadVersionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCnxFailedBadVersionEvent from a JSON string
host_cnx_failed_bad_version_event_instance = HostCnxFailedBadVersionEvent.from_json(json)
# print the JSON string representation of the object
print HostCnxFailedBadVersionEvent.to_json()

# convert the object into a dict
host_cnx_failed_bad_version_event_dict = host_cnx_failed_bad_version_event_instance.to_dict()
# create an instance of HostCnxFailedBadVersionEvent from a dict
host_cnx_failed_bad_version_event_form_dict = host_cnx_failed_bad_version_event.from_dict(host_cnx_failed_bad_version_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


