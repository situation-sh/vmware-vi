# GatewayNotReachable

Deprecated not used since vSphere 6.5.  GatewayNotReachable is thrown by vCenter Server when it fails to establish a connection to the host gateway server.  This fault may occur due to network connectivity problems or inability to establish secure connection between the gateway server and vCenter Server.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.gateway_not_reachable import GatewayNotReachable

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayNotReachable from a JSON string
gateway_not_reachable_instance = GatewayNotReachable.from_json(json)
# print the JSON string representation of the object
print GatewayNotReachable.to_json()

# convert the object into a dict
gateway_not_reachable_dict = gateway_not_reachable_instance.to_dict()
# create an instance of GatewayNotReachable from a dict
gateway_not_reachable_form_dict = gateway_not_reachable.from_dict(gateway_not_reachable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


