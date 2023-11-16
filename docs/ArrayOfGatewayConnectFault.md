# ArrayOfGatewayConnectFault

A boxed array of *GatewayConnectFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GatewayConnectFault]**](GatewayConnectFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_gateway_connect_fault import ArrayOfGatewayConnectFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGatewayConnectFault from a JSON string
array_of_gateway_connect_fault_instance = ArrayOfGatewayConnectFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfGatewayConnectFault.to_json()

# convert the object into a dict
array_of_gateway_connect_fault_dict = array_of_gateway_connect_fault_instance.to_dict()
# create an instance of ArrayOfGatewayConnectFault from a dict
array_of_gateway_connect_fault_form_dict = array_of_gateway_connect_fault.from_dict(array_of_gateway_connect_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


