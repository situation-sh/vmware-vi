# GatewayHostNotReachable

Deprecated not used since vSphere 6.5.  GatewayHostNotReachable is thrown by the gateway used to connect to a host, if an error occurs while establishing a connection to that host.  The fault may provide a more detailed message of what caused the problem.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.gateway_host_not_reachable import GatewayHostNotReachable

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayHostNotReachable from a JSON string
gateway_host_not_reachable_instance = GatewayHostNotReachable.from_json(json)
# print the JSON string representation of the object
print GatewayHostNotReachable.to_json()

# convert the object into a dict
gateway_host_not_reachable_dict = gateway_host_not_reachable_instance.to_dict()
# create an instance of GatewayHostNotReachable from a dict
gateway_host_not_reachable_form_dict = gateway_host_not_reachable.from_dict(gateway_host_not_reachable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


