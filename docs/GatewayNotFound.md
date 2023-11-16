# GatewayNotFound

Deprecated not used since vSphere 6.5.  GatewayNotFound is thrown by vCenter Server, if no host gateway with the specified type/id and available resources is known to the vCenter Server.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.gateway_not_found import GatewayNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayNotFound from a JSON string
gateway_not_found_instance = GatewayNotFound.from_json(json)
# print the JSON string representation of the object
print GatewayNotFound.to_json()

# convert the object into a dict
gateway_not_found_dict = gateway_not_found_instance.to_dict()
# create an instance of GatewayNotFound from a dict
gateway_not_found_form_dict = gateway_not_found.from_dict(gateway_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


