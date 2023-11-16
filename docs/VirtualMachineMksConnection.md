# VirtualMachineMksConnection

The *VirtualMachineMksConnection* object describes an MKS style connection to the virtual machine.  ***Since:*** vSphere API 7.0.1.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_mks_connection import VirtualMachineMksConnection

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineMksConnection from a JSON string
virtual_machine_mks_connection_instance = VirtualMachineMksConnection.from_json(json)
# print the JSON string representation of the object
print VirtualMachineMksConnection.to_json()

# convert the object into a dict
virtual_machine_mks_connection_dict = virtual_machine_mks_connection_instance.to_dict()
# create an instance of VirtualMachineMksConnection from a dict
virtual_machine_mks_connection_form_dict = virtual_machine_mks_connection.from_dict(virtual_machine_mks_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


