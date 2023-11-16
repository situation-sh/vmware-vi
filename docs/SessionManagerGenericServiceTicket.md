# SessionManagerGenericServiceTicket

This data object represents a ticket which grants access to some service.  The ticket may be used only once and is valid only for the *SessionManagerServiceRequestSpec* with which it was acquired. For HTTP service requests (when spec is of type HttpServiceRequestSpec) the returned ticket must be used by setting *SessionManagerGenericServiceTicket.id* as the value of a special cookie in the HTTP request. For CGI requests the name of this cookie is 'vmware\\_cgi\\_ticket'. The use of the returned ticket for other services is to be defined.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique string identifying the ticket.  ***Since:*** vSphere API 5.0  | 
**host_name** | **str** | The name of the host that the service is running on  ***Since:*** vSphere API 5.1  | [optional] 
**ssl_thumbprint** | **str** | The expected thumbprint of the SSL certificate of the host.  If it is empty, the host must be authenticated by name.  ***Since:*** vSphere API 5.1  | [optional] 
**cert_thumbprint_list** | [**List[VirtualMachineCertThumbprint]**](VirtualMachineCertThumbprint.md) | List of expected thumbprints of the certificate of the host to which we are connecting.  The list can be configured on the host to include only certain hash types. The default configuration includes all hash types that are considered secure. See vmware.com for the current security standards.  | [optional] 
**ticket_type** | **str** | Type of the ticket See { @Vim::SessionManager::GenericServiceTicket::TicketType }  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.session_manager_generic_service_ticket import SessionManagerGenericServiceTicket

# TODO update the JSON string below
json = "{}"
# create an instance of SessionManagerGenericServiceTicket from a JSON string
session_manager_generic_service_ticket_instance = SessionManagerGenericServiceTicket.from_json(json)
# print the JSON string representation of the object
print SessionManagerGenericServiceTicket.to_json()

# convert the object into a dict
session_manager_generic_service_ticket_dict = session_manager_generic_service_ticket_instance.to_dict()
# create an instance of SessionManagerGenericServiceTicket from a dict
session_manager_generic_service_ticket_form_dict = session_manager_generic_service_ticket.from_dict(session_manager_generic_service_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


