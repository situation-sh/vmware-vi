# AcquireGenericServiceTicketRequestType

The parameters of *SessionManager.AcquireGenericServiceTicket*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**SessionManagerServiceRequestSpec**](SessionManagerServiceRequestSpec.md) |  | 

## Example

```python
from vmware_vi.models.acquire_generic_service_ticket_request_type import AcquireGenericServiceTicketRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AcquireGenericServiceTicketRequestType from a JSON string
acquire_generic_service_ticket_request_type_instance = AcquireGenericServiceTicketRequestType.from_json(json)
# print the JSON string representation of the object
print AcquireGenericServiceTicketRequestType.to_json()

# convert the object into a dict
acquire_generic_service_ticket_request_type_dict = acquire_generic_service_ticket_request_type_instance.to_dict()
# create an instance of AcquireGenericServiceTicketRequestType from a dict
acquire_generic_service_ticket_request_type_form_dict = acquire_generic_service_ticket_request_type.from_dict(acquire_generic_service_ticket_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


