# ArrayOfGatewayToHostAuthFault

A boxed array of *GatewayToHostAuthFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GatewayToHostAuthFault]**](GatewayToHostAuthFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_gateway_to_host_auth_fault import ArrayOfGatewayToHostAuthFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGatewayToHostAuthFault from a JSON string
array_of_gateway_to_host_auth_fault_instance = ArrayOfGatewayToHostAuthFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfGatewayToHostAuthFault.to_json()

# convert the object into a dict
array_of_gateway_to_host_auth_fault_dict = array_of_gateway_to_host_auth_fault_instance.to_dict()
# create an instance of ArrayOfGatewayToHostAuthFault from a dict
array_of_gateway_to_host_auth_fault_form_dict = array_of_gateway_to_host_auth_fault.from_dict(array_of_gateway_to_host_auth_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


