# AcquireTicketRequestType

The parameters of *VirtualMachine.AcquireTicket*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_type** | **str** | The type of service to acquire, the set of possible values is described in *VirtualMachineTicketType_enum*.  | 

## Example

```python
from vmware_vi.models.acquire_ticket_request_type import AcquireTicketRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AcquireTicketRequestType from a JSON string
acquire_ticket_request_type_instance = AcquireTicketRequestType.from_json(json)
# print the JSON string representation of the object
print AcquireTicketRequestType.to_json()

# convert the object into a dict
acquire_ticket_request_type_dict = acquire_ticket_request_type_instance.to_dict()
# create an instance of AcquireTicketRequestType from a dict
acquire_ticket_request_type_form_dict = acquire_ticket_request_type.from_dict(acquire_ticket_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


