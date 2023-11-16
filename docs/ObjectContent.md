# ObjectContent

The *ObjectContent* data object type contains the contents retrieved for a single managed object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**prop_set** | [**List[DynamicProperty]**](DynamicProperty.md) | Set of name-value pairs for the properties of the managed object.  | [optional] 
**missing_set** | [**List[MissingProperty]**](MissingProperty.md) | Properties for which values could not be retrieved and the associated fault.  | [optional] 

## Example

```python
from vmware_vi.models.object_content import ObjectContent

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectContent from a JSON string
object_content_instance = ObjectContent.from_json(json)
# print the JSON string representation of the object
print ObjectContent.to_json()

# convert the object into a dict
object_content_dict = object_content_instance.to_dict()
# create an instance of ObjectContent from a dict
object_content_form_dict = object_content.from_dict(object_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


