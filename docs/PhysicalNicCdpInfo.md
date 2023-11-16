# PhysicalNicCdpInfo

CDP (Cisco Discovery Protocol) is a link level protocol that allows for discovering the CDP-awared network hardware at either end of a DIRECT connection.  It's only good for direct connection because CDP doesn't get forwarded through switches. It's a simple advertisement protocol which beacons information about the switch or host along with some port information. The CDP information allows ESX Server admins to know which Cisco switch port is connected to any given virtual switch uplink (PNIC).  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_version** | **int** | CDP version.  The value is always 1.  ***Since:*** VI API 2.5  | [optional] 
**timeout** | **int** | This is the periodicity of advertisement, the time between two successive CDP message transmissions  ***Since:*** VI API 2.5  | [optional] 
**ttl** | **int** | Time-To-Live.  the amount of time, in seconds, that a receiver should retain the information contained in the CDP packet.  ***Since:*** VI API 2.5  | [optional] 
**samples** | **int** | The number of CDP messages we have received from the device.  ***Since:*** VI API 2.5  | [optional] 
**dev_id** | **str** | Device ID which identifies the device.  By default, the device ID is either the device&#39;s fully-qualified host name (including the domain name) or the device&#39;s hardware serial number in ASCII.  ***Since:*** VI API 2.5  | [optional] 
**address** | **str** | The advertised IP address that is assigned to the interface of the device on which the CDP message is sent.  The device can advertise all addresses for a given protocol suite and, optionally, can advertise one or more loopback IP addresses. But this property only show the first address.  ***Since:*** VI API 2.5  | [optional] 
**port_id** | **str** | Port ID.  An ASCII character string that identifies the port on which the CDP message is sent, e.g. \&quot;FastEthernet0/8\&quot;  ***Since:*** VI API 2.5  | [optional] 
**device_capability** | [**PhysicalNicCdpDeviceCapability**](PhysicalNicCdpDeviceCapability.md) |  | [optional] 
**software_version** | **str** | Software version on the device.  A character string that provides information about the software release version that the device is running. e.g. \&quot;Cisco Internetwork Operating Syscisco WS-C2940-8TT-S\&quot;  ***Since:*** VI API 2.5  | [optional] 
**hardware_platform** | **str** | Hardware platform.  An ASCII character string that describes the hardware platform of the device , e.g. \&quot;cisco WS-C2940-8TT-S\&quot;  ***Since:*** VI API 2.5  | [optional] 
**ip_prefix** | **str** | IP prefix.  Each IP prefix represents one of the directly connected IP network segments of the local route.  ***Since:*** VI API 2.5  | [optional] 
**ip_prefix_len** | **int** | ipPrefix length.  ***Since:*** VI API 2.5  | [optional] 
**vlan** | **int** | The native VLAN of advertising port.  The native VLAN is the VLAN to which a port returns when it is not trunking. Also, the native VLAN is the untagged VLAN on an 802.1Q trunk.  ***Since:*** VI API 2.5  | [optional] 
**full_duplex** | **bool** | Half/full duplex setting of the advertising port.  ***Since:*** VI API 2.5  | [optional] 
**mtu** | **int** | MTU, the maximum transmission unit for the advertising port.  Possible values are 1500 through 18190.  ***Since:*** VI API 2.5  | [optional] 
**system_name** | **str** | The configured SNMP system name of the device.  ***Since:*** VI API 2.5  | [optional] 
**system_oid** | **str** | The configured SNMP system OID of the device.  ***Since:*** VI API 2.5  | [optional] 
**mgmt_addr** | **str** | The configured IP address of the SNMP management interface for the device.  ***Since:*** VI API 2.5  | [optional] 
**location** | **str** | The configured location of the device.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.physical_nic_cdp_info import PhysicalNicCdpInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicCdpInfo from a JSON string
physical_nic_cdp_info_instance = PhysicalNicCdpInfo.from_json(json)
# print the JSON string representation of the object
print PhysicalNicCdpInfo.to_json()

# convert the object into a dict
physical_nic_cdp_info_dict = physical_nic_cdp_info_instance.to_dict()
# create an instance of PhysicalNicCdpInfo from a dict
physical_nic_cdp_info_form_dict = physical_nic_cdp_info.from_dict(physical_nic_cdp_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


