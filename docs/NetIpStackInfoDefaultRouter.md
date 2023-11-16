# NetIpStackInfoDefaultRouter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | Unicast IP address of a next-hop router.  ***Since:*** vSphere API 4.1  | 
**device** | **str** | This value will contain the name of the interface as reported by the operationg system.  ***Since:*** vSphere API 4.1  | 
**lifetime** | **datetime** | When this entry will no longer valid.  For IPv6 this value see For IPv6 RFC 2462 sections 4.2 and 6.3.4.  ***Since:*** vSphere API 4.1  | 
**preference** | **str** | Value of this entry compared to others that this IP stack uses when making selection to route traffic on the default route when there are multiple default routers.  Value must be one of *NetIpStackInfoPreference_enum*  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.net_ip_stack_info_default_router import NetIpStackInfoDefaultRouter

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpStackInfoDefaultRouter from a JSON string
net_ip_stack_info_default_router_instance = NetIpStackInfoDefaultRouter.from_json(json)
# print the JSON string representation of the object
print NetIpStackInfoDefaultRouter.to_json()

# convert the object into a dict
net_ip_stack_info_default_router_dict = net_ip_stack_info_default_router_instance.to_dict()
# create an instance of NetIpStackInfoDefaultRouter from a dict
net_ip_stack_info_default_router_form_dict = net_ip_stack_info_default_router.from_dict(net_ip_stack_info_default_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


