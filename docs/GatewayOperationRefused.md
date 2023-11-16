# GatewayOperationRefused

Deprecated not used sine vSphere 6.5.  GatewayOperationRefused is thrown by vCenter Server when a gateway server denies to accept more connection due to resource limitation.  The fault may occur due to specific configuration of the Gateway server to work with limited resources or due to physical limitation to handle more host connections.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.gateway_operation_refused import GatewayOperationRefused

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayOperationRefused from a JSON string
gateway_operation_refused_instance = GatewayOperationRefused.from_json(json)
# print the JSON string representation of the object
print GatewayOperationRefused.to_json()

# convert the object into a dict
gateway_operation_refused_dict = gateway_operation_refused_instance.to_dict()
# create an instance of GatewayOperationRefused from a dict
gateway_operation_refused_form_dict = gateway_operation_refused.from_dict(gateway_operation_refused_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


