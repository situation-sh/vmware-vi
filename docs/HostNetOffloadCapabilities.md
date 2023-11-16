# HostNetOffloadCapabilities

Deprecated as of VI API 4.0, the system defaults will be used.  Offload capabilities are used to optimize virtual machine network performance.  When a virtual machine is transmitting on a network, some operations can be offloaded either to the host or to physical hardware. This data object type defines the set of offload capabilities that may be available on a host.  This data object type is used both to publish the list of offload capabilities and to contain offload capability policy settings. The network policy logic is built on a two-level inheritance scheme which requires that all settings be optional. As a result, all properties on the NetOffloadCapabilities object must be optional.  See also *HostNetworkPolicy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csum_offload** | **bool** | (Optional) The flag to indicate whether or not checksum offloading is supported.  | [optional] 
**tcp_segmentation** | **bool** | (Optional) The flag to indicate whether or not TCP segmentation offloading (TSO) is supported.  | [optional] 
**zero_copy_xmit** | **bool** | (Optional) The flag to indicate whether or not zero copy transmits are supported.  | [optional] 

## Example

```python
from vmware_vi.models.host_net_offload_capabilities import HostNetOffloadCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetOffloadCapabilities from a JSON string
host_net_offload_capabilities_instance = HostNetOffloadCapabilities.from_json(json)
# print the JSON string representation of the object
print HostNetOffloadCapabilities.to_json()

# convert the object into a dict
host_net_offload_capabilities_dict = host_net_offload_capabilities_instance.to_dict()
# create an instance of HostNetOffloadCapabilities from a dict
host_net_offload_capabilities_form_dict = host_net_offload_capabilities.from_dict(host_net_offload_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


