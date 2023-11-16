# PhysicalNicCdpDeviceCapability

The capability of the CDP-awared device that connects to a Physical NIC.  *PhysicalNicCdpInfo*  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**router** | **bool** | The CDP-awared device has the capability of a routing for at least one network layer protocol  ***Since:*** VI API 2.5  | 
**transparent_bridge** | **bool** | The CDP-awared device has the capability of transparent bridging  ***Since:*** VI API 2.5  | 
**source_route_bridge** | **bool** | The CDP-awared device has the capability of source-route bridging  ***Since:*** VI API 2.5  | 
**network_switch** | **bool** | The CDP-awared device has the capability of switching.  The difference between this capability and transparentBridge is that a switch does not run the Spanning-Tree Protocol. This device is assumed to be deployed in a physical loop-free topology.  ***Since:*** VI API 2.5  | 
**host** | **bool** | The CDP-awared device has the capability of a host, which Sends and receives packets for at least one network layer protocol.  ***Since:*** VI API 2.5  | 
**igmp_enabled** | **bool** | The CDP-awared device is IGMP-enabled, which does not forward IGMP Report packets on nonrouter ports.  ***Since:*** VI API 2.5  | 
**repeater** | **bool** | The CDP-awared device has the capability of a repeater  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.physical_nic_cdp_device_capability import PhysicalNicCdpDeviceCapability

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicCdpDeviceCapability from a JSON string
physical_nic_cdp_device_capability_instance = PhysicalNicCdpDeviceCapability.from_json(json)
# print the JSON string representation of the object
print PhysicalNicCdpDeviceCapability.to_json()

# convert the object into a dict
physical_nic_cdp_device_capability_dict = physical_nic_cdp_device_capability_instance.to_dict()
# create an instance of PhysicalNicCdpDeviceCapability from a dict
physical_nic_cdp_device_capability_form_dict = physical_nic_cdp_device_capability.from_dict(physical_nic_cdp_device_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


