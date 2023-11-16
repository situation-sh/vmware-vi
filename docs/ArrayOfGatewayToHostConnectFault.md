# ArrayOfGatewayToHostConnectFault

A boxed array of *GatewayToHostConnectFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GatewayToHostConnectFault]**](GatewayToHostConnectFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_gateway_to_host_connect_fault import ArrayOfGatewayToHostConnectFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGatewayToHostConnectFault from a JSON string
array_of_gateway_to_host_connect_fault_instance = ArrayOfGatewayToHostConnectFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfGatewayToHostConnectFault.to_json()

# convert the object into a dict
array_of_gateway_to_host_connect_fault_dict = array_of_gateway_to_host_connect_fault_instance.to_dict()
# create an instance of ArrayOfGatewayToHostConnectFault from a dict
array_of_gateway_to_host_connect_fault_form_dict = array_of_gateway_to_host_connect_fault.from_dict(array_of_gateway_to_host_connect_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


