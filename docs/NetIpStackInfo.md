# NetIpStackInfo

Protocol version independent reporting data object for IP stack.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neighbor** | [**List[NetIpStackInfoNetToMedia]**](NetIpStackInfoNetToMedia.md) | Zero, one or more entries of neighbors discovered using ARP or NDP.  This information is used to help diagnose connectivity or performance issues. This property maps to RFC 4293 ipNetToPhysicalTable.  ***Since:*** vSphere API 4.1  | [optional] 
**default_router** | [**List[NetIpStackInfoDefaultRouter]**](NetIpStackInfoDefaultRouter.md) | Zero one or more entries of discovered IP routers that are directly reachable from a an interface on this system.  This property maps to RFC 4293 ipDefaultRouterTable.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_ip_stack_info import NetIpStackInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpStackInfo from a JSON string
net_ip_stack_info_instance = NetIpStackInfo.from_json(json)
# print the JSON string representation of the object
print NetIpStackInfo.to_json()

# convert the object into a dict
net_ip_stack_info_dict = net_ip_stack_info_instance.to_dict()
# create an instance of NetIpStackInfo from a dict
net_ip_stack_info_form_dict = net_ip_stack_info.from_dict(net_ip_stack_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


