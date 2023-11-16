# DistributedVirtualSwitchPortConnectee

Information about the entity that connects to a DistributedVirtualPort.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**nic_key** | **str** | The key of the virtual NIC that connects to this port.  ***Since:*** vSphere API 4.0  | [optional] 
**type** | **str** | The type of the connectee.  See *ConnecteeType* for valid values.  ***Since:*** vSphere API 4.0  | [optional] 
**address_hint** | **str** | A hint on address information of the NIC that connects to this port.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_port_connectee import DistributedVirtualSwitchPortConnectee

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchPortConnectee from a JSON string
distributed_virtual_switch_port_connectee_instance = DistributedVirtualSwitchPortConnectee.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchPortConnectee.to_json()

# convert the object into a dict
distributed_virtual_switch_port_connectee_dict = distributed_virtual_switch_port_connectee_instance.to_dict()
# create an instance of DistributedVirtualSwitchPortConnectee from a dict
distributed_virtual_switch_port_connectee_form_dict = distributed_virtual_switch_port_connectee.from_dict(distributed_virtual_switch_port_connectee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


