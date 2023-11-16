# GuestPermissionDenied

A GuestPermissionDenied exception is thrown when an operation fails because the authentication used is insufficient to perform the operation.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_permission_denied import GuestPermissionDenied

# TODO update the JSON string below
json = "{}"
# create an instance of GuestPermissionDenied from a JSON string
guest_permission_denied_instance = GuestPermissionDenied.from_json(json)
# print the JSON string representation of the object
print GuestPermissionDenied.to_json()

# convert the object into a dict
guest_permission_denied_dict = guest_permission_denied_instance.to_dict()
# create an instance of GuestPermissionDenied from a dict
guest_permission_denied_form_dict = guest_permission_denied.from_dict(guest_permission_denied_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


