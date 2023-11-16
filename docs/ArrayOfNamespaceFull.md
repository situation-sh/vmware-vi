# ArrayOfNamespaceFull

A boxed array of *NamespaceFull*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NamespaceFull]**](NamespaceFull.md) |  | 

## Example

```python
from vmware_vi.models.array_of_namespace_full import ArrayOfNamespaceFull

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNamespaceFull from a JSON string
array_of_namespace_full_instance = ArrayOfNamespaceFull.from_json(json)
# print the JSON string representation of the object
print ArrayOfNamespaceFull.to_json()

# convert the object into a dict
array_of_namespace_full_dict = array_of_namespace_full_instance.to_dict()
# create an instance of ArrayOfNamespaceFull from a dict
array_of_namespace_full_form_dict = array_of_namespace_full.from_dict(array_of_namespace_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


