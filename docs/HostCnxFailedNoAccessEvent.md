# HostCnxFailedNoAccessEvent

This event records a failure to connect to a host due to insufficient account privileges. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_cnx_failed_no_access_event import HostCnxFailedNoAccessEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCnxFailedNoAccessEvent from a JSON string
host_cnx_failed_no_access_event_instance = HostCnxFailedNoAccessEvent.from_json(json)
# print the JSON string representation of the object
print HostCnxFailedNoAccessEvent.to_json()

# convert the object into a dict
host_cnx_failed_no_access_event_dict = host_cnx_failed_no_access_event_instance.to_dict()
# create an instance of HostCnxFailedNoAccessEvent from a dict
host_cnx_failed_no_access_event_form_dict = host_cnx_failed_no_access_event.from_dict(host_cnx_failed_no_access_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


