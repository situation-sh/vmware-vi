# TraversalSpec

The *TraversalSpec* data object type specifies how to derive a new set of objects to add to the filter.  It specifies a property path whose value is either another managed object or an array of managed objects included in the set of objects for consideration. This data object can also be named, using the \"name\" field in the base type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Name of the object type containing the property.  | 
**path** | **str** | Name of the property to use in order to select additional objects.  | 
**skip** | **bool** | Flag to indicate whether or not to filter the object in the \&quot;path\&quot; field.  | [optional] 
**select_set** | [**List[SelectionSpec]**](SelectionSpec.md) | Optional set of selections to specify additional objects to filter.  | [optional] 

## Example

```python
from vmware_vi.models.traversal_spec import TraversalSpec

# TODO update the JSON string below
json = "{}"
# create an instance of TraversalSpec from a JSON string
traversal_spec_instance = TraversalSpec.from_json(json)
# print the JSON string representation of the object
print TraversalSpec.to_json()

# convert the object into a dict
traversal_spec_dict = traversal_spec_instance.to_dict()
# create an instance of TraversalSpec from a dict
traversal_spec_form_dict = traversal_spec.from_dict(traversal_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


