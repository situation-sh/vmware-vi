# NetIpStackInfoNetToMedia

Information from an IP stack about known mappings betwwen an IP address and the underlying physical address it maps to as learned by: IPv4: Address Resolution Protocol (ARP) RFC 826 IPv6: Neighbor Discovery Protocol (NDP) RFC 4861  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | A Unicast IP address of another system directly reachable w/o routing.  IPv4 address is specified using dotted decimal notation. For example, \&quot;192.0.2.1\&quot;. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol &#39;::&#39; to represent multiple 16-bit groups of contiguous 0&#39;s only once in an address as described in RFC 2373.  ***Since:*** vSphere API 4.1  | 
**physical_address** | **str** | The media-dependent of the address or empty string if not yet learned.  For Ethernet interfaces this is a MAC address reported in the format: XX:XX:XX:XX:XX:XX where XX are hexadecimal numbers.  ***Since:*** vSphere API 4.1  | 
**device** | **str** | The value will be the name of the interface as reported by the operating system.  ***Since:*** vSphere API 4.1  | 
**type** | **str** | The type/state of this entry as reported by the IP stack.  See *NetIpStackInfoEntryType_enum* for values.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.net_ip_stack_info_net_to_media import NetIpStackInfoNetToMedia

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpStackInfoNetToMedia from a JSON string
net_ip_stack_info_net_to_media_instance = NetIpStackInfoNetToMedia.from_json(json)
# print the JSON string representation of the object
print NetIpStackInfoNetToMedia.to_json()

# convert the object into a dict
net_ip_stack_info_net_to_media_dict = net_ip_stack_info_net_to_media_instance.to_dict()
# create an instance of NetIpStackInfoNetToMedia from a dict
net_ip_stack_info_net_to_media_form_dict = net_ip_stack_info_net_to_media.from_dict(net_ip_stack_info_net_to_media_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


