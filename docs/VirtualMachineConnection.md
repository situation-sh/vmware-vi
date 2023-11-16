# VirtualMachineConnection

The *VirtualMachineConnection* object describes a connection to the virtual machine.  ***Since:*** vSphere API 7.0.1.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The unique identifier associated with the connection.  The label is a UTF-8 string which specifies a unique identifier for a connection.  ***Since:*** vSphere API 7.0.1.0  | 
**client** | **str** | The client identifer.  This identifier is a UTF-8 string which is semantically meaningful for the connection. Examples of the client identifier are an IP address (V4 or V6) with or without a port specification, a machine name that requires a DNS lookup, or any other network oriented identification scheme.  ***Since:*** vSphere API 7.0.1.0  | 
**user_name** | **str** | The name of the user authorizing the connection.  This is used for auditing.  ***Since:*** vSphere API 7.0.1.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_connection import VirtualMachineConnection

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConnection from a JSON string
virtual_machine_connection_instance = VirtualMachineConnection.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConnection.to_json()

# convert the object into a dict
virtual_machine_connection_dict = virtual_machine_connection_instance.to_dict()
# create an instance of VirtualMachineConnection from a dict
virtual_machine_connection_form_dict = virtual_machine_connection.from_dict(virtual_machine_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


