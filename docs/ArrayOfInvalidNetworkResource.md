# ArrayOfInvalidNetworkResource

A boxed array of *InvalidNetworkResource*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidNetworkResource]**](InvalidNetworkResource.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_network_resource import ArrayOfInvalidNetworkResource

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidNetworkResource from a JSON string
array_of_invalid_network_resource_instance = ArrayOfInvalidNetworkResource.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidNetworkResource.to_json()

# convert the object into a dict
array_of_invalid_network_resource_dict = array_of_invalid_network_resource_instance.to_dict()
# create an instance of ArrayOfInvalidNetworkResource from a dict
array_of_invalid_network_resource_form_dict = array_of_invalid_network_resource.from_dict(array_of_invalid_network_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


