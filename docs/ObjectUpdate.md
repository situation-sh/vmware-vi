# ObjectUpdate

The *ObjectUpdate* data object type contains information about changes to a particular managed object.  We distinguish updates when an object is created, destroyed, or modified, as well as when the object enters or leaves the set of objects dynamically associated with a filter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**ObjectUpdateKindEnum**](ObjectUpdateKindEnum.md) |  | 
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**change_set** | [**List[PropertyChange]**](PropertyChange.md) | Optional set of changes to the object.  Present only if the \&quot;kind\&quot; is either \&quot;modify\&quot; or \&quot;enter\&quot;.  | [optional] 
**missing_set** | [**List[MissingProperty]**](MissingProperty.md) | Properties whose value could not be retrieved and their associated faults.  Present only if the \&quot;kind\&quot; is either \&quot;modify\&quot; or \&quot;enter\&quot;.  | [optional] 

## Example

```python
from vmware_vi.models.object_update import ObjectUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectUpdate from a JSON string
object_update_instance = ObjectUpdate.from_json(json)
# print the JSON string representation of the object
print ObjectUpdate.to_json()

# convert the object into a dict
object_update_dict = object_update_instance.to_dict()
# create an instance of ObjectUpdate from a dict
object_update_form_dict = object_update.from_dict(object_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


