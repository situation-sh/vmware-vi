# MissingObject

Used for reporting missing objects that were explicitly referenced by a filter spec.  In other words, any of the objects referenced in *PropertyFilterSpec.objectSet* 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.missing_object import MissingObject

# TODO update the JSON string below
json = "{}"
# create an instance of MissingObject from a JSON string
missing_object_instance = MissingObject.from_json(json)
# print the JSON string representation of the object
print MissingObject.to_json()

# convert the object into a dict
missing_object_dict = missing_object_instance.to_dict()
# create an instance of MissingObject from a dict
missing_object_form_dict = missing_object.from_dict(missing_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


