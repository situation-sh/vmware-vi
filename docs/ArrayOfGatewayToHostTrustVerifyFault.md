# ArrayOfGatewayToHostTrustVerifyFault

A boxed array of *GatewayToHostTrustVerifyFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GatewayToHostTrustVerifyFault]**](GatewayToHostTrustVerifyFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_gateway_to_host_trust_verify_fault import ArrayOfGatewayToHostTrustVerifyFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGatewayToHostTrustVerifyFault from a JSON string
array_of_gateway_to_host_trust_verify_fault_instance = ArrayOfGatewayToHostTrustVerifyFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfGatewayToHostTrustVerifyFault.to_json()

# convert the object into a dict
array_of_gateway_to_host_trust_verify_fault_dict = array_of_gateway_to_host_trust_verify_fault_instance.to_dict()
# create an instance of ArrayOfGatewayToHostTrustVerifyFault from a dict
array_of_gateway_to_host_trust_verify_fault_form_dict = array_of_gateway_to_host_trust_verify_fault.from_dict(array_of_gateway_to_host_trust_verify_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


