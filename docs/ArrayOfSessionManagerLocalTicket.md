# ArrayOfSessionManagerLocalTicket

A boxed array of *SessionManagerLocalTicket*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SessionManagerLocalTicket]**](SessionManagerLocalTicket.md) |  | 

## Example

```python
from vmware_vi.models.array_of_session_manager_local_ticket import ArrayOfSessionManagerLocalTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSessionManagerLocalTicket from a JSON string
array_of_session_manager_local_ticket_instance = ArrayOfSessionManagerLocalTicket.from_json(json)
# print the JSON string representation of the object
print ArrayOfSessionManagerLocalTicket.to_json()

# convert the object into a dict
array_of_session_manager_local_ticket_dict = array_of_session_manager_local_ticket_instance.to_dict()
# create an instance of ArrayOfSessionManagerLocalTicket from a dict
array_of_session_manager_local_ticket_form_dict = array_of_session_manager_local_ticket.from_dict(array_of_session_manager_local_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


