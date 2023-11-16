# ArrayOfManagedObjectReference

A boxed array of *ManagedObjectReference*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.array_of_managed_object_reference import ArrayOfManagedObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfManagedObjectReference from a JSON string
array_of_managed_object_reference_instance = ArrayOfManagedObjectReference.from_json(json)
# print the JSON string representation of the object
print ArrayOfManagedObjectReference.to_json()

# convert the object into a dict
array_of_managed_object_reference_dict = array_of_managed_object_reference_instance.to_dict()
# create an instance of ArrayOfManagedObjectReference from a dict
array_of_managed_object_reference_form_dict = array_of_managed_object_reference.from_dict(array_of_managed_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


