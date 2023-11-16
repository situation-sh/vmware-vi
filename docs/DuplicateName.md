# DuplicateName

A DuplicateName exception is thrown because a name already exists in the same name space. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name that is already bound in the name space.  | 
**object** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.duplicate_name import DuplicateName

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateName from a JSON string
duplicate_name_instance = DuplicateName.from_json(json)
# print the JSON string representation of the object
print DuplicateName.to_json()

# convert the object into a dict
duplicate_name_dict = duplicate_name_instance.to_dict()
# create an instance of DuplicateName from a dict
duplicate_name_form_dict = duplicate_name.from_dict(duplicate_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


