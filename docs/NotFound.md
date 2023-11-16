# NotFound

A NotFound error occurs when a referenced component of a managed object cannot be found.  The referenced component can be a data object type (such as a role or permission) or a primitive (such as a string).  For example, if the missing referenced component is a data object, such as VirtualSwitch, the NotFound error is thrown. The NotFound error is also thrown if the data object is found, but the referenced name (for example, \"vswitch0\") is not. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.not_found import NotFound

# TODO update the JSON string below
json = "{}"
# create an instance of NotFound from a JSON string
not_found_instance = NotFound.from_json(json)
# print the JSON string representation of the object
print NotFound.to_json()

# convert the object into a dict
not_found_dict = not_found_instance.to_dict()
# create an instance of NotFound from a dict
not_found_form_dict = not_found.from_dict(not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


