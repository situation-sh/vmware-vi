# HostCnxFailedTimeoutEvent

This event records a failure to connect to a host due to a timeout on the connection attempt. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_cnx_failed_timeout_event import HostCnxFailedTimeoutEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCnxFailedTimeoutEvent from a JSON string
host_cnx_failed_timeout_event_instance = HostCnxFailedTimeoutEvent.from_json(json)
# print the JSON string representation of the object
print HostCnxFailedTimeoutEvent.to_json()

# convert the object into a dict
host_cnx_failed_timeout_event_dict = host_cnx_failed_timeout_event_instance.to_dict()
# create an instance of HostCnxFailedTimeoutEvent from a dict
host_cnx_failed_timeout_event_form_dict = host_cnx_failed_timeout_event.from_dict(host_cnx_failed_timeout_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


