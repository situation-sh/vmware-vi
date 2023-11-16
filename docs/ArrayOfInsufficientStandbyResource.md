# ArrayOfInsufficientStandbyResource

A boxed array of *InsufficientStandbyResource*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InsufficientStandbyResource]**](InsufficientStandbyResource.md) |  | 

## Example

```python
from vmware_vi.models.array_of_insufficient_standby_resource import ArrayOfInsufficientStandbyResource

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInsufficientStandbyResource from a JSON string
array_of_insufficient_standby_resource_instance = ArrayOfInsufficientStandbyResource.from_json(json)
# print the JSON string representation of the object
print ArrayOfInsufficientStandbyResource.to_json()

# convert the object into a dict
array_of_insufficient_standby_resource_dict = array_of_insufficient_standby_resource_instance.to_dict()
# create an instance of ArrayOfInsufficientStandbyResource from a dict
array_of_insufficient_standby_resource_form_dict = array_of_insufficient_standby_resource.from_dict(array_of_insufficient_standby_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


