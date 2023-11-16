# HostCnxFailedBadCcagentEvent

This event records a failure to connect to a host due to no response being received from the host agent. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_cnx_failed_bad_ccagent_event import HostCnxFailedBadCcagentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCnxFailedBadCcagentEvent from a JSON string
host_cnx_failed_bad_ccagent_event_instance = HostCnxFailedBadCcagentEvent.from_json(json)
# print the JSON string representation of the object
print HostCnxFailedBadCcagentEvent.to_json()

# convert the object into a dict
host_cnx_failed_bad_ccagent_event_dict = host_cnx_failed_bad_ccagent_event_instance.to_dict()
# create an instance of HostCnxFailedBadCcagentEvent from a dict
host_cnx_failed_bad_ccagent_event_form_dict = host_cnx_failed_bad_ccagent_event.from_dict(host_cnx_failed_bad_ccagent_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


