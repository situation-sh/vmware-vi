# DistributedVirtualPort

The *DistributedVirtualPort* data object represents a port in a *DistributedVirtualSwitch*.  Virtual ports are part of a distributed virtual portgroup. Servers create virtual ports according to the portgroup type (*DistributedVirtualPortgroup*.*DistributedVirtualPortgroup.config*.*DVPortgroupConfigInfo.type*). See *DistributedVirtualPortgroupPortgroupType_enum*. - To configure host network access by port, set the distributed virtual port   in the host virtual NIC specification   (*HostVirtualNicSpec*.*HostVirtualNicSpec.distributedVirtualPort*.*DistributedVirtualSwitchPortConnection.portKey*). - To configure virtual machine network access by port, set the port   in the virtual Ethernet card backing   (*VirtualEthernetCard*.*VirtualDevice.backing*.*VirtualEthernetCardDistributedVirtualPortBackingInfo.port*.*DistributedVirtualSwitchPortConnection.portKey*).    ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Port key.  ***Since:*** vSphere API 4.0  | 
**config** | [**DVPortConfigInfo**](DVPortConfigInfo.md) |  | 
**dvs_uuid** | **str** | UUID of the *DistributedVirtualSwitch* to which the port belongs.  ***Since:*** vSphere API 4.0  | 
**portgroup_key** | **str** | Key of the portgroup *DistributedVirtualPortgroup* to which the port belongs, if any.  ***Since:*** vSphere API 4.0  | [optional] 
**proxy_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**connectee** | [**DistributedVirtualSwitchPortConnectee**](DistributedVirtualSwitchPortConnectee.md) |  | [optional] 
**conflict** | **bool** | Specifies whether the port is a conflict port.  A port could be marked as conflict if an entity is discovered connecting to a port that is already occupied, or if the host creates a port without conferring with vCenter Server.  The distributed virtual switch does not persist the runtime state of a conflict port. Also, the port cannot move away from the host. vCenter Server will not move a virtual machine (VMotion) that is using a conflict port.  ***Since:*** vSphere API 4.0  | 
**conflict_port_key** | **str** | If the port is marked conflict in the case of two entities connecting to the same port (see *DistributedVirtualPort.conflict*), this is the key of the port which the connected entity is contending for.  ***Since:*** vSphere API 4.0  | [optional] 
**state** | [**DVPortState**](DVPortState.md) |  | [optional] 
**connection_cookie** | **int** | Cookie representing the current instance of association between a port and a virtual or physical NIC.  See *DistributedVirtualSwitchPortConnection*. The same cookie is present in the physical or virtual NIC configuration (*DistributedVirtualSwitchPortConnection*.*DistributedVirtualSwitchPortConnection.connectionCookie*) so that the Server can verify that the entity is the rightful connectee of the port.  ***Since:*** vSphere API 4.0  | [optional] 
**last_status_change** | **datetime** | The last time the *DistributedVirtualPort.state*.*DVPortState.runtimeInfo* value was changed.  ***Since:*** vSphere API 4.0  | 
**host_local_port** | **bool** | Specifies whether the port is a host local port.  A host local port is created to resurrect the management network connection on a VMkernel virtual NIC. You cannot use vCenter Server to reconfigure this port and you cannot reassign the port.  ***Since:*** vSphere API 5.1  | [optional] 
**external_id** | **str** | Populate the Id assigned to vmknic or vnic by external management plane to port, if the port is connected to the nics.  ***Since:*** vSphere API 7.0  | [optional] 
**segment_port_id** | **str** | Populate the segmentPortId assigned to LSP.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_port import DistributedVirtualPort

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualPort from a JSON string
distributed_virtual_port_instance = DistributedVirtualPort.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualPort.to_json()

# convert the object into a dict
distributed_virtual_port_dict = distributed_virtual_port_instance.to_dict()
# create an instance of DistributedVirtualPort from a dict
distributed_virtual_port_form_dict = distributed_virtual_port.from_dict(distributed_virtual_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


