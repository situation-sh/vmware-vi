# SelectionSpec

The *SelectionSpec* is the base type for data object types that specify what additional objects to filter.  The base type contains only an optional \"name\" field, which allows a selection to be named for future reference. More information is available in the subtype.  Named selections support recursive specifications on an object hierarchy. When used by a derived object, the \"name\" field allows other *SelectionSpec* objects to refer to the object by name. When used as the base type only, the \"name\" field indicates recursion to the derived object by name.  Names are meaningful only within the same FilterSpec. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the selection specification.  | [optional] 

## Example

```python
from vmware_vi.models.selection_spec import SelectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionSpec from a JSON string
selection_spec_instance = SelectionSpec.from_json(json)
# print the JSON string representation of the object
print SelectionSpec.to_json()

# convert the object into a dict
selection_spec_dict = selection_spec_instance.to_dict()
# create an instance of SelectionSpec from a dict
selection_spec_form_dict = selection_spec.from_dict(selection_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


