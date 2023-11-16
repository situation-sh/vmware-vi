# ArrayOfObjectUpdateKind

A boxed array of *ObjectUpdateKind_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ObjectUpdateKindEnum]**](ObjectUpdateKindEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_object_update_kind import ArrayOfObjectUpdateKind

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfObjectUpdateKind from a JSON string
array_of_object_update_kind_instance = ArrayOfObjectUpdateKind.from_json(json)
# print the JSON string representation of the object
print ArrayOfObjectUpdateKind.to_json()

# convert the object into a dict
array_of_object_update_kind_dict = array_of_object_update_kind_instance.to_dict()
# create an instance of ArrayOfObjectUpdateKind from a dict
array_of_object_update_kind_form_dict = array_of_object_update_kind.from_dict(array_of_object_update_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


