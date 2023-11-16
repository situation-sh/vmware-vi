# ArrayOfNamespaceWriteProtected

A boxed array of *NamespaceWriteProtected*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NamespaceWriteProtected]**](NamespaceWriteProtected.md) |  | 

## Example

```python
from vmware_vi.models.array_of_namespace_write_protected import ArrayOfNamespaceWriteProtected

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNamespaceWriteProtected from a JSON string
array_of_namespace_write_protected_instance = ArrayOfNamespaceWriteProtected.from_json(json)
# print the JSON string representation of the object
print ArrayOfNamespaceWriteProtected.to_json()

# convert the object into a dict
array_of_namespace_write_protected_dict = array_of_namespace_write_protected_instance.to_dict()
# create an instance of ArrayOfNamespaceWriteProtected from a dict
array_of_namespace_write_protected_form_dict = array_of_namespace_write_protected.from_dict(array_of_namespace_write_protected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


