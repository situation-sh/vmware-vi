# AddNetworkResourcePoolRequestType

The parameters of *DistributedVirtualSwitch.AddNetworkResourcePool*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**List[DVSNetworkResourcePoolConfigSpec]**](DVSNetworkResourcePoolConfigSpec.md) | the network resource pool configuration specification.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.add_network_resource_pool_request_type import AddNetworkResourcePoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddNetworkResourcePoolRequestType from a JSON string
add_network_resource_pool_request_type_instance = AddNetworkResourcePoolRequestType.from_json(json)
# print the JSON string representation of the object
print AddNetworkResourcePoolRequestType.to_json()

# convert the object into a dict
add_network_resource_pool_request_type_dict = add_network_resource_pool_request_type_instance.to_dict()
# create an instance of AddNetworkResourcePoolRequestType from a dict
add_network_resource_pool_request_type_form_dict = add_network_resource_pool_request_type.from_dict(add_network_resource_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


