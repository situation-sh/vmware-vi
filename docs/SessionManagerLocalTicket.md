# SessionManagerLocalTicket

This data object type contains the user name and location of the file containing the password that clients can use for one-time logon to a server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | User name to be used for logon.  | 
**password_file_path** | **str** | Absolute local path to the file containing a one-time password.  | 

## Example

```python
from vmware_vi.models.session_manager_local_ticket import SessionManagerLocalTicket

# TODO update the JSON string below
json = "{}"
# create an instance of SessionManagerLocalTicket from a JSON string
session_manager_local_ticket_instance = SessionManagerLocalTicket.from_json(json)
# print the JSON string representation of the object
print SessionManagerLocalTicket.to_json()

# convert the object into a dict
session_manager_local_ticket_dict = session_manager_local_ticket_instance.to_dict()
# create an instance of SessionManagerLocalTicket from a dict
session_manager_local_ticket_form_dict = session_manager_local_ticket.from_dict(session_manager_local_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


