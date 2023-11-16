# VirtualMachineMksTicket

Deprecated as of vSphere API 4.1, use *VirtualMachineTicket* instead.  This data object contains the information needed to establish an MKS (mouse-keyboard-screen) connection to a running virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket** | **str** | The ticket name.  This is used as the username and password for the MKS connection.  | 
**cfg_file** | **str** | The name of the configuration file for the virtual machine.  | 
**host** | **str** | The host with which to establish a connection.  If the host is not specified, it is assumed that the requesting entity knows the appropriate host with which to connect.  | [optional] 
**port** | **int** | The port number to use.  If the port is not specified, it is assumed that the requesting entity knows the appropriate port to use when making a new connection.  | [optional] 
**ssl_thumbprint** | **str** | The expected thumbprint of the SSL cert of the host to which we are connecting.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_mks_ticket import VirtualMachineMksTicket

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMksTicket from a JSON string
virtual_machine_mks_ticket_instance = VirtualMachineMksTicket.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMksTicket.to_json()

# convert the object into a dict
virtual_machine_mks_ticket_dict = virtual_machine_mks_ticket_instance.to_dict()
# create an instance of VirtualMachineMksTicket from a dict
virtual_machine_mks_ticket_form_dict = virtual_machine_mks_ticket.from_dict(virtual_machine_mks_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


