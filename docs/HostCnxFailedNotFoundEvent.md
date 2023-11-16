# HostCnxFailedNotFoundEvent

This event records a failure to connect to a host due to a failure to resolve the host name. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_cnx_failed_not_found_event import HostCnxFailedNotFoundEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCnxFailedNotFoundEvent from a JSON string
host_cnx_failed_not_found_event_instance = HostCnxFailedNotFoundEvent.from_json(json)
# print the JSON string representation of the object
print HostCnxFailedNotFoundEvent.to_json()

# convert the object into a dict
host_cnx_failed_not_found_event_dict = host_cnx_failed_not_found_event_instance.to_dict()
# create an instance of HostCnxFailedNotFoundEvent from a dict
host_cnx_failed_not_found_event_form_dict = host_cnx_failed_not_found_event.from_dict(host_cnx_failed_not_found_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


