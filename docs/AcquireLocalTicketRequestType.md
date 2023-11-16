# AcquireLocalTicketRequestType

The parameters of *SessionManager.AcquireLocalTicket*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | User requesting one-time password.  | 

## Example

```python
from vmware_vi.models.acquire_local_ticket_request_type import AcquireLocalTicketRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AcquireLocalTicketRequestType from a JSON string
acquire_local_ticket_request_type_instance = AcquireLocalTicketRequestType.from_json(json)
# print the JSON string representation of the object
print AcquireLocalTicketRequestType.to_json()

# convert the object into a dict
acquire_local_ticket_request_type_dict = acquire_local_ticket_request_type_instance.to_dict()
# create an instance of AcquireLocalTicketRequestType from a dict
acquire_local_ticket_request_type_form_dict = acquire_local_ticket_request_type.from_dict(acquire_local_ticket_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


