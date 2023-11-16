# ArrayOfResourceNotAvailable

A boxed array of *ResourceNotAvailable*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourceNotAvailable]**](ResourceNotAvailable.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_not_available import ArrayOfResourceNotAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourceNotAvailable from a JSON string
array_of_resource_not_available_instance = ArrayOfResourceNotAvailable.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourceNotAvailable.to_json()

# convert the object into a dict
array_of_resource_not_available_dict = array_of_resource_not_available_instance.to_dict()
# create an instance of ArrayOfResourceNotAvailable from a dict
array_of_resource_not_available_form_dict = array_of_resource_not_available.from_dict(array_of_resource_not_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


