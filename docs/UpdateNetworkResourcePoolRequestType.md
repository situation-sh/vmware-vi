# UpdateNetworkResourcePoolRequestType

The parameters of *DistributedVirtualSwitch.UpdateNetworkResourcePool*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**List[DVSNetworkResourcePoolConfigSpec]**](DVSNetworkResourcePoolConfigSpec.md) | The network resource pool configuration specification.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.update_network_resource_pool_request_type import UpdateNetworkResourcePoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNetworkResourcePoolRequestType from a JSON string
update_network_resource_pool_request_type_instance = UpdateNetworkResourcePoolRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateNetworkResourcePoolRequestType.to_json()

# convert the object into a dict
update_network_resource_pool_request_type_dict = update_network_resource_pool_request_type_instance.to_dict()
# create an instance of UpdateNetworkResourcePoolRequestType from a dict
update_network_resource_pool_request_type_form_dict = update_network_resource_pool_request_type.from_dict(update_network_resource_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


