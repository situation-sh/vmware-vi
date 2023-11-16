# HostVirtualNicSpec

The *HostVirtualNicSpec* data object describes the *HostVirtualNic* configuration containing both the configured properties on a virtual NIC and identification information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_property** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.  | [optional] 
**ip** | [**HostIpConfig**](HostIpConfig.md) |  | [optional] 
**mac** | **str** | Media access control (MAC) address of the virtual network adapter.  | [optional] 
**distributed_virtual_port** | [**DistributedVirtualSwitchPortConnection**](DistributedVirtualSwitchPortConnection.md) |  | [optional] 
**portgroup** | **str** | Portgroup (*HostPortGroup*) to which the virtual NIC is connected.  When reconfiguring a virtual NIC, this property indicates the new portgroup to which the virtual NIC should connect. You can specify this property only if you do not specify *HostVirtualNicSpec.distributedVirtualPort* and *HostVirtualNicSpec.opaqueNetwork*  ***Since:*** vSphere API 4.0  | [optional] 
**mtu** | **int** | Maximum transmission unit for packets size in bytes for the virtual NIC.  If not specified, the Server will use the system default value.  ***Since:*** vSphere API 4.0  | [optional] 
**tso_enabled** | **bool** | Flag enabling or disabling TCP segmentation offset for a virtual NIC.  If not specified, a default value of true will be used.  ***Since:*** vSphere API 4.0  | [optional] 
**net_stack_instance_key** | **str** | The NetStackInstance that the virtual NIC uses, the value of this property is default to be *defaultTcpipStack*  ***Since:*** vSphere API 5.5  | [optional] 
**opaque_network** | [**HostVirtualNicOpaqueNetworkSpec**](HostVirtualNicOpaqueNetworkSpec.md) |  | [optional] 
**external_id** | **str** | An ID assigned to the vmkernel adapter by external management plane.  The value and format of this property is determined by external management plane, and vSphere doesn&#39;t do any validation. It&#39;s also up to external management plane to set, unset or maintain this property.  This property is applicable only when *HostVirtualNicSpec.opaqueNetwork* property is set, otherwise it&#39;s value is ignored.  ***Since:*** vSphere API 6.0  | [optional] 
**pinned_pnic** | **str** | The physical nic to which the vmkernel adapter is pinned.  Setting this value ensures that the virtual NIC will access external network only via the the specified physical NIC.  This property is applicable only when *HostVirtualNicSpec.opaqueNetwork* property is set. If the vmkernel adapter is connected to a portgroup or dvPort, then such pinning can be achieved by configuring correct teaming policy on the portgroup or dvPort or dvPortgroup that is connected to virtual NIC.  ***Since:*** vSphere API 6.0  | [optional] 
**ip_route_spec** | [**HostVirtualNicIpRouteSpec**](HostVirtualNicIpRouteSpec.md) |  | [optional] 
**system_owned** | **bool** | Set to true when the vmkernel adapter is configured by other system indirectly other than by the user directly.  ***Since:*** vSphere API 7.0  | [optional] 
**dpu_id** | **str** | The identifier of the DPU hosting the vmknic.  If vmknic is on ESX host, dpuId will be unset.  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_nic_spec import HostVirtualNicSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualNicSpec from a JSON string
host_virtual_nic_spec_instance = HostVirtualNicSpec.from_json(json)
# print the JSON string representation of the object
print HostVirtualNicSpec.to_json()

# convert the object into a dict
host_virtual_nic_spec_dict = host_virtual_nic_spec_instance.to_dict()
# create an instance of HostVirtualNicSpec from a dict
host_virtual_nic_spec_form_dict = host_virtual_nic_spec.from_dict(host_virtual_nic_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


