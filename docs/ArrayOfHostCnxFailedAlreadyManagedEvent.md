# ArrayOfHostCnxFailedAlreadyManagedEvent

A boxed array of *HostCnxFailedAlreadyManagedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCnxFailedAlreadyManagedEvent]**](HostCnxFailedAlreadyManagedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_cnx_failed_already_managed_event import ArrayOfHostCnxFailedAlreadyManagedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCnxFailedAlreadyManagedEvent from a JSON string
array_of_host_cnx_failed_already_managed_event_instance = ArrayOfHostCnxFailedAlreadyManagedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCnxFailedAlreadyManagedEvent.to_json()

# convert the object into a dict
array_of_host_cnx_failed_already_managed_event_dict = array_of_host_cnx_failed_already_managed_event_instance.to_dict()
# create an instance of ArrayOfHostCnxFailedAlreadyManagedEvent from a dict
array_of_host_cnx_failed_already_managed_event_form_dict = array_of_host_cnx_failed_already_managed_event.from_dict(array_of_host_cnx_failed_already_managed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


