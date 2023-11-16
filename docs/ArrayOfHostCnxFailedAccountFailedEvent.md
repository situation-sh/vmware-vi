# ArrayOfHostCnxFailedAccountFailedEvent

A boxed array of *HostCnxFailedAccountFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCnxFailedAccountFailedEvent]**](HostCnxFailedAccountFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_cnx_failed_account_failed_event import ArrayOfHostCnxFailedAccountFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCnxFailedAccountFailedEvent from a JSON string
array_of_host_cnx_failed_account_failed_event_instance = ArrayOfHostCnxFailedAccountFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCnxFailedAccountFailedEvent.to_json()

# convert the object into a dict
array_of_host_cnx_failed_account_failed_event_dict = array_of_host_cnx_failed_account_failed_event_instance.to_dict()
# create an instance of ArrayOfHostCnxFailedAccountFailedEvent from a dict
array_of_host_cnx_failed_account_failed_event_form_dict = array_of_host_cnx_failed_account_failed_event.from_dict(array_of_host_cnx_failed_account_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


