# ArrayOfHostCnxFailedNoAccessEvent

A boxed array of *HostCnxFailedNoAccessEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCnxFailedNoAccessEvent]**](HostCnxFailedNoAccessEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_cnx_failed_no_access_event import ArrayOfHostCnxFailedNoAccessEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCnxFailedNoAccessEvent from a JSON string
array_of_host_cnx_failed_no_access_event_instance = ArrayOfHostCnxFailedNoAccessEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCnxFailedNoAccessEvent.to_json()

# convert the object into a dict
array_of_host_cnx_failed_no_access_event_dict = array_of_host_cnx_failed_no_access_event_instance.to_dict()
# create an instance of ArrayOfHostCnxFailedNoAccessEvent from a dict
array_of_host_cnx_failed_no_access_event_form_dict = array_of_host_cnx_failed_no_access_event.from_dict(array_of_host_cnx_failed_no_access_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


