# RemoveNetworkResourcePoolRequestType

The parameters of *DistributedVirtualSwitch.RemoveNetworkResourcePool*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **List[str]** | The network resource pool key.  | 

## Example

```python
from vmware_vi.models.remove_network_resource_pool_request_type import RemoveNetworkResourcePoolRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveNetworkResourcePoolRequestType from a JSON string
remove_network_resource_pool_request_type_instance = RemoveNetworkResourcePoolRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveNetworkResourcePoolRequestType.to_json()

# convert the object into a dict
remove_network_resource_pool_request_type_dict = remove_network_resource_pool_request_type_instance.to_dict()
# create an instance of RemoveNetworkResourcePoolRequestType from a dict
remove_network_resource_pool_request_type_form_dict = remove_network_resource_pool_request_type.from_dict(remove_network_resource_pool_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


