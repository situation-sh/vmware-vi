# ArrayOfSessionManagerGenericServiceTicket

A boxed array of *SessionManagerGenericServiceTicket*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SessionManagerGenericServiceTicket]**](SessionManagerGenericServiceTicket.md) |  | 

## Example

```python
from vmware_vi.models.array_of_session_manager_generic_service_ticket import ArrayOfSessionManagerGenericServiceTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSessionManagerGenericServiceTicket from a JSON string
array_of_session_manager_generic_service_ticket_instance = ArrayOfSessionManagerGenericServiceTicket.from_json(json)
# print the JSON string representation of the object
print ArrayOfSessionManagerGenericServiceTicket.to_json()

# convert the object into a dict
array_of_session_manager_generic_service_ticket_dict = array_of_session_manager_generic_service_ticket_instance.to_dict()
# create an instance of ArrayOfSessionManagerGenericServiceTicket from a dict
array_of_session_manager_generic_service_ticket_form_dict = array_of_session_manager_generic_service_ticket.from_dict(array_of_session_manager_generic_service_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


