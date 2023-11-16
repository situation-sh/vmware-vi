# HostOpaqueNetworkInfo

Information on opaque networks that are available on the host.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_property** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future.  | [optional] 
**opaque_network_id** | **str** | The ID of the opaque network.  ***Since:*** vSphere API 5.5  | 
**opaque_network_name** | **str** | The name of the opaque network.  ***Since:*** vSphere API 5.5  | 
**opaque_network_type** | **str** | The type of the opaque network.  ***Since:*** vSphere API 5.5  | 
**pnic_zone** | **List[str]** | IDs of networking zones that back the opaque network.  ***Since:*** vSphere API 6.0  | [optional] 
**capability** | [**OpaqueNetworkCapability**](OpaqueNetworkCapability.md) |  | [optional] 
**extra_config** | [**List[OptionValue]**](OptionValue.md) | Extra NSX specific properties for opaque networks.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_opaque_network_info import HostOpaqueNetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostOpaqueNetworkInfo from a JSON string
host_opaque_network_info_instance = HostOpaqueNetworkInfo.from_json(json)
# print the JSON string representation of the object
print HostOpaqueNetworkInfo.to_json()

# convert the object into a dict
host_opaque_network_info_dict = host_opaque_network_info_instance.to_dict()
# create an instance of HostOpaqueNetworkInfo from a dict
host_opaque_network_info_form_dict = host_opaque_network_info.from_dict(host_opaque_network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


