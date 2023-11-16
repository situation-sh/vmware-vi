# DistributedVirtualSwitchPortStatistics

Statistic data of a DistributedVirtualPort.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packets_in_multicast** | **int** | The number of multicast packets received.  ***Since:*** vSphere API 4.0  | 
**packets_out_multicast** | **int** | The number of multicast packets forwarded.  ***Since:*** vSphere API 4.0  | 
**bytes_in_multicast** | **int** | The number of bytes received from multicast packets.  ***Since:*** vSphere API 4.0  | 
**bytes_out_multicast** | **int** | The number of bytes forwarded from multicast packets.  ***Since:*** vSphere API 4.0  | 
**packets_in_unicast** | **int** | The number of unicast packets received.  ***Since:*** vSphere API 4.0  | 
**packets_out_unicast** | **int** | The number of unicast packets forwarded.  ***Since:*** vSphere API 4.0  | 
**bytes_in_unicast** | **int** | The number of bytes received from unicast packets.  ***Since:*** vSphere API 4.0  | 
**bytes_out_unicast** | **int** | The number of bytes forwarded from unicast packets.  ***Since:*** vSphere API 4.0  | 
**packets_in_broadcast** | **int** | The number of broadcast packets received.  ***Since:*** vSphere API 4.0  | 
**packets_out_broadcast** | **int** | The number of broadcast packets forwarded.  ***Since:*** vSphere API 4.0  | 
**bytes_in_broadcast** | **int** | The number of bytes received from broadcast packets.  ***Since:*** vSphere API 4.0  | 
**bytes_out_broadcast** | **int** | The number of bytes forwarded from broadcast packets.  ***Since:*** vSphere API 4.0  | 
**packets_in_dropped** | **int** | The number of received packets dropped.  ***Since:*** vSphere API 4.0  | 
**packets_out_dropped** | **int** | The number of packets to be forwarded dropped.  ***Since:*** vSphere API 4.0  | 
**packets_in_exception** | **int** | The number of packets received that cause an exception.  ***Since:*** vSphere API 4.0  | 
**packets_out_exception** | **int** | The number of packets to be forwarded that cause an exception.  ***Since:*** vSphere API 4.0  | 
**bytes_in_from_pnic** | **int** | The number of bytes received at a pnic on the behalf of a port&#39;s connectee (inter-host rx).  ***Since:*** vSphere API 6.5  | [optional] 
**bytes_out_to_pnic** | **int** | The number of bytes transmitted at a pnic on the behalf of a port&#39;s connectee (inter-host tx).  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_port_statistics import DistributedVirtualSwitchPortStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchPortStatistics from a JSON string
distributed_virtual_switch_port_statistics_instance = DistributedVirtualSwitchPortStatistics.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchPortStatistics.to_json()

# convert the object into a dict
distributed_virtual_switch_port_statistics_dict = distributed_virtual_switch_port_statistics_instance.to_dict()
# create an instance of DistributedVirtualSwitchPortStatistics from a dict
distributed_virtual_switch_port_statistics_form_dict = distributed_virtual_switch_port_statistics.from_dict(distributed_virtual_switch_port_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


