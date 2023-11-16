# QuerySupportedNetworkOffloadSpecRequestType

The parameters of *DistributedVirtualSwitchManager.QuerySupportedNetworkOffloadSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_product_spec** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | 

## Example

```python
from vmware_vi.models.query_supported_network_offload_spec_request_type import QuerySupportedNetworkOffloadSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySupportedNetworkOffloadSpecRequestType from a JSON string
query_supported_network_offload_spec_request_type_instance = QuerySupportedNetworkOffloadSpecRequestType.from_json(json)
# print the JSON string representation of the object
print QuerySupportedNetworkOffloadSpecRequestType.to_json()

# convert the object into a dict
query_supported_network_offload_spec_request_type_dict = query_supported_network_offload_spec_request_type_instance.to_dict()
# create an instance of QuerySupportedNetworkOffloadSpecRequestType from a dict
query_supported_network_offload_spec_request_type_form_dict = query_supported_network_offload_spec_request_type.from_dict(query_supported_network_offload_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


