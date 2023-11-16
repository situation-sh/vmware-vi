# ArrayOfHostGatewaySpec

A boxed array of *HostGatewaySpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostGatewaySpec]**](HostGatewaySpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_gateway_spec import ArrayOfHostGatewaySpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostGatewaySpec from a JSON string
array_of_host_gateway_spec_instance = ArrayOfHostGatewaySpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostGatewaySpec.to_json()

# convert the object into a dict
array_of_host_gateway_spec_dict = array_of_host_gateway_spec_instance.to_dict()
# create an instance of ArrayOfHostGatewaySpec from a dict
array_of_host_gateway_spec_form_dict = array_of_host_gateway_spec.from_dict(array_of_host_gateway_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


