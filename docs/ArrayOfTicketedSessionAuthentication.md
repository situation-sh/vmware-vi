# ArrayOfTicketedSessionAuthentication

A boxed array of *TicketedSessionAuthentication*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TicketedSessionAuthentication]**](TicketedSessionAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ticketed_session_authentication import ArrayOfTicketedSessionAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTicketedSessionAuthentication from a JSON string
array_of_ticketed_session_authentication_instance = ArrayOfTicketedSessionAuthentication.from_json(json)
# print the JSON string representation of the object
print ArrayOfTicketedSessionAuthentication.to_json()

# convert the object into a dict
array_of_ticketed_session_authentication_dict = array_of_ticketed_session_authentication_instance.to_dict()
# create an instance of ArrayOfTicketedSessionAuthentication from a dict
array_of_ticketed_session_authentication_form_dict = array_of_ticketed_session_authentication.from_dict(array_of_ticketed_session_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


