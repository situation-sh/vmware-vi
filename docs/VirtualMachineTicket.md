# VirtualMachineTicket

This data object contains the information needed to establish a connection to a running virtual machine.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket** | **str** | The ticket name.  This is used as the username and password for the MKS connection.  ***Since:*** vSphere API 4.1  | 
**cfg_file** | **str** | The name of the configuration file for the virtual machine.  ***Since:*** vSphere API 4.1  | 
**host** | **str** | The host with which to establish a connection.  If the host is not specified, it is assumed that the requesting entity knows the appropriate host with which to connect.  ***Since:*** vSphere API 4.1  | [optional] 
**port** | **int** | The port number to use.  If the port is not specified, it is assumed that the requesting entity knows the appropriate port to use when making a new connection.  ***Since:*** vSphere API 4.1  | [optional] 
**ssl_thumbprint** | **str** | The expected SHA1 thumbprint of the SSL cert of the host to which we are connecting.  This field can be enabled or disabled on the host.  ***Since:*** vSphere API 4.1  | [optional] 
**cert_thumbprint_list** | [**List[VirtualMachineCertThumbprint]**](VirtualMachineCertThumbprint.md) | List of expected thumbprints of the certificate of the host to which we are connecting.  The list can be configured on the host to include only certain hash types. The default configuration includes all hash types that are considered secure. See vmware.com for the current security standards.  | [optional] 
**url** | **str** | Websocket URL.  Some tickets are \&quot;websocket\&quot; tickets and are best expressed as a URL.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_ticket import VirtualMachineTicket

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineTicket from a JSON string
virtual_machine_ticket_instance = VirtualMachineTicket.from_json(json)
# print the JSON string representation of the object
print VirtualMachineTicket.to_json()

# convert the object into a dict
virtual_machine_ticket_dict = virtual_machine_ticket_instance.to_dict()
# create an instance of VirtualMachineTicket from a dict
virtual_machine_ticket_form_dict = virtual_machine_ticket.from_dict(virtual_machine_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


