# ObjectUpdateKind

A boxed *ObjectUpdateKind_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ObjectUpdateKindEnum**](ObjectUpdateKindEnum.md) |  | 

## Example

```python
from vmware_vi.models.object_update_kind import ObjectUpdateKind

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectUpdateKind from a JSON string
object_update_kind_instance = ObjectUpdateKind.from_json(json)
# print the JSON string representation of the object
print ObjectUpdateKind.to_json()

# convert the object into a dict
object_update_kind_dict = object_update_kind_instance.to_dict()
# create an instance of ObjectUpdateKind from a dict
object_update_kind_form_dict = object_update_kind.from_dict(object_update_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


