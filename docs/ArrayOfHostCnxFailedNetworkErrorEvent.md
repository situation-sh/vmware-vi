# ArrayOfHostCnxFailedNetworkErrorEvent

A boxed array of *HostCnxFailedNetworkErrorEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostCnxFailedNetworkErrorEvent]**](HostCnxFailedNetworkErrorEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_cnx_failed_network_error_event import ArrayOfHostCnxFailedNetworkErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostCnxFailedNetworkErrorEvent from a JSON string
array_of_host_cnx_failed_network_error_event_instance = ArrayOfHostCnxFailedNetworkErrorEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostCnxFailedNetworkErrorEvent.to_json()

# convert the object into a dict
array_of_host_cnx_failed_network_error_event_dict = array_of_host_cnx_failed_network_error_event_instance.to_dict()
# create an instance of ArrayOfHostCnxFailedNetworkErrorEvent from a dict
array_of_host_cnx_failed_network_error_event_form_dict = array_of_host_cnx_failed_network_error_event.from_dict(array_of_host_cnx_failed_network_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


