# ObjectSpec

Within a *PropertyFilterSpec*, the *ObjectSpec* data object type specifies the managed object at which the filter begins to collect the managed object references and properties specified by the associated *PropertySpec* set.  If the \"skip\" property is present and set to true, then the filter does not check to see if the starting object's type matches any of the types listed in the associated sets of *PropertySpec* data objects.  If the *ObjectSpec.selectSet* property is present, then this specifies additional objects to filter. These objects are defined by one or more *SelectionSpec* objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**skip** | **bool** | Flag to specify whether or not to report this managed object&#39;s properties.  If the flag is true, the filter will not report this managed object&#39;s properties.  | [optional] 
**select_set** | [**List[SelectionSpec]**](SelectionSpec.md) | Set of selections to specify additional objects to filter.  | [optional] 

## Example

```python
from vmware_vi.models.object_spec import ObjectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectSpec from a JSON string
object_spec_instance = ObjectSpec.from_json(json)
# print the JSON string representation of the object
print ObjectSpec.to_json()

# convert the object into a dict
object_spec_dict = object_spec_instance.to_dict()
# create an instance of ObjectSpec from a dict
object_spec_form_dict = object_spec.from_dict(object_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


