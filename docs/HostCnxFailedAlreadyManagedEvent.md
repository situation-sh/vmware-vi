# HostCnxFailedAlreadyManagedEvent

This event records a failure to connect to a host due to the host being managed by a different VirtualCenter server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_name** | **str** | The name of the VirtualCenter server that manages the host.  | 

## Example

```python
from vmware_vi.models.host_cnx_failed_already_managed_event import HostCnxFailedAlreadyManagedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostCnxFailedAlreadyManagedEvent from a JSON string
host_cnx_failed_already_managed_event_instance = HostCnxFailedAlreadyManagedEvent.from_json(json)
# print the JSON string representation of the object
print HostCnxFailedAlreadyManagedEvent.to_json()

# convert the object into a dict
host_cnx_failed_already_managed_event_dict = host_cnx_failed_already_managed_event_instance.to_dict()
# create an instance of HostCnxFailedAlreadyManagedEvent from a dict
host_cnx_failed_already_managed_event_form_dict = host_cnx_failed_already_managed_event.from_dict(host_cnx_failed_already_managed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


