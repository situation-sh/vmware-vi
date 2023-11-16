# ArrayOfResourceInUse

A boxed array of *ResourceInUse*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourceInUse]**](ResourceInUse.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_in_use import ArrayOfResourceInUse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourceInUse from a JSON string
array_of_resource_in_use_instance = ArrayOfResourceInUse.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourceInUse.to_json()

# convert the object into a dict
array_of_resource_in_use_dict = array_of_resource_in_use_instance.to_dict()
# create an instance of ArrayOfResourceInUse from a dict
array_of_resource_in_use_form_dict = array_of_resource_in_use.from_dict(array_of_resource_in_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


