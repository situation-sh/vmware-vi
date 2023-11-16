# ArrayOfManagedObjectNotFound

A boxed array of *ManagedObjectNotFound*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ManagedObjectNotFound]**](ManagedObjectNotFound.md) |  | 

## Example

```python
from vmware_vi.models.array_of_managed_object_not_found import ArrayOfManagedObjectNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfManagedObjectNotFound from a JSON string
array_of_managed_object_not_found_instance = ArrayOfManagedObjectNotFound.from_json(json)
# print the JSON string representation of the object
print ArrayOfManagedObjectNotFound.to_json()

# convert the object into a dict
array_of_managed_object_not_found_dict = array_of_managed_object_not_found_instance.to_dict()
# create an instance of ArrayOfManagedObjectNotFound from a dict
array_of_managed_object_not_found_form_dict = array_of_managed_object_not_found.from_dict(array_of_managed_object_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


