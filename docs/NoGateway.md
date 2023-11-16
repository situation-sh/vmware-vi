# NoGateway

This error occurs when an operation fails because of vmkernel gateway is unset. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_gateway import NoGateway

# TODO update the JSON string below
json = "{}"
# create an instance of NoGateway from a JSON string
no_gateway_instance = NoGateway.from_json(json)
# print the JSON string representation of the object
print NoGateway.to_json()

# convert the object into a dict
no_gateway_dict = no_gateway_instance.to_dict()
# create an instance of NoGateway from a dict
no_gateway_form_dict = no_gateway.from_dict(no_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


