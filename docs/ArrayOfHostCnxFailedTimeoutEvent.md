# ArrayOfHostCnxFailedTimeoutEvent

A boxed array of *HostCnxFailedTimeoutEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCnxFailedTimeoutEvent]**](HostCnxFailedTimeoutEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_cnx_failed_timeout_event import ArrayOfHostCnxFailedTimeoutEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCnxFailedTimeoutEvent from a JSON string
array_of_host_cnx_failed_timeout_event_instance = ArrayOfHostCnxFailedTimeoutEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCnxFailedTimeoutEvent.to_json()

# convert the object into a dict
array_of_host_cnx_failed_timeout_event_dict = array_of_host_cnx_failed_timeout_event_instance.to_dict()
# create an instance of ArrayOfHostCnxFailedTimeoutEvent from a dict
array_of_host_cnx_failed_timeout_event_form_dict = array_of_host_cnx_failed_timeout_event.from_dict(array_of_host_cnx_failed_timeout_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


