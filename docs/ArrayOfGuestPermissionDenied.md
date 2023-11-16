# ArrayOfGuestPermissionDenied

A boxed array of *GuestPermissionDenied*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestPermissionDenied]**](GuestPermissionDenied.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_permission_denied import ArrayOfGuestPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestPermissionDenied from a JSON string
array_of_guest_permission_denied_instance = ArrayOfGuestPermissionDenied.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestPermissionDenied.to_json()

# convert the object into a dict
array_of_guest_permission_denied_dict = array_of_guest_permission_denied_instance.to_dict()
# create an instance of ArrayOfGuestPermissionDenied from a dict
array_of_guest_permission_denied_form_dict = array_of_guest_permission_denied.from_dict(array_of_guest_permission_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


