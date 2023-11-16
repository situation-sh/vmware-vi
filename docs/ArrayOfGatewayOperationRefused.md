# ArrayOfGatewayOperationRefused

A boxed array of *GatewayOperationRefused*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GatewayOperationRefused]**](GatewayOperationRefused.md) |  | 

## Example

```python
from vmware_vi.models.array_of_gateway_operation_refused import ArrayOfGatewayOperationRefused

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGatewayOperationRefused from a JSON string
array_of_gateway_operation_refused_instance = ArrayOfGatewayOperationRefused.from_json(json)
# print the JSON string representation of the object
print ArrayOfGatewayOperationRefused.to_json()

# convert the object into a dict
array_of_gateway_operation_refused_dict = array_of_gateway_operation_refused_instance.to_dict()
# create an instance of ArrayOfGatewayOperationRefused from a dict
array_of_gateway_operation_refused_form_dict = array_of_gateway_operation_refused.from_dict(array_of_gateway_operation_refused_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


