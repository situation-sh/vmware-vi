# ArrayOfHostServiceTicket

A boxed array of *HostServiceTicket*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostServiceTicket]**](HostServiceTicket.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_service_ticket import ArrayOfHostServiceTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostServiceTicket from a JSON string
array_of_host_service_ticket_instance = ArrayOfHostServiceTicket.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostServiceTicket.to_json()

# convert the object into a dict
array_of_host_service_ticket_dict = array_of_host_service_ticket_instance.to_dict()
# create an instance of ArrayOfHostServiceTicket from a dict
array_of_host_service_ticket_form_dict = array_of_host_service_ticket.from_dict(array_of_host_service_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


