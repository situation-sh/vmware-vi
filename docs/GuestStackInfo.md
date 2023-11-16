# GuestStackInfo

Information about the Internet Protocol stack as configured in the guest operating system.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_config** | [**NetDnsConfigInfo**](NetDnsConfigInfo.md) |  | [optional] 
**ip_route_config** | [**NetIpRouteConfigInfo**](NetIpRouteConfigInfo.md) |  | [optional] 
**ip_stack_config** | [**List[KeyValue]**](KeyValue.md) | Report Kernel IP configuration settings.  The key part contains a unique number in the report. The value part contains the &#39;key&#x3D;value&#39; as provided by the underlying provider. For example on Linux, BSD, the systcl -a output would be reported as: key&#x3D;&#39;5&#39;, value&#x3D;&#39;net.ipv4.tcp\\_keepalive\\_time &#x3D; 7200&#39;  ***Since:*** vSphere API 4.1  | [optional] 
**dhcp_config** | [**NetDhcpConfigInfo**](NetDhcpConfigInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.guest_stack_info import GuestStackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestStackInfo from a JSON string
guest_stack_info_instance = GuestStackInfo.from_json(json)
# print the JSON string representation of the object
print GuestStackInfo.to_json()

# convert the object into a dict
guest_stack_info_dict = guest_stack_info_instance.to_dict()
# create an instance of GuestStackInfo from a dict
guest_stack_info_form_dict = guest_stack_info.from_dict(guest_stack_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


