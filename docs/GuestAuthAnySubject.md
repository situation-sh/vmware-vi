# GuestAuthAnySubject

The ANY subject.  When an in-guest user account is configured to trust an alias using the ANY subject, any vSphere user authenticated by that alias will be allowed to impersonate the in-guest user.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_auth_any_subject import GuestAuthAnySubject

# TODO update the JSON string below
json = "{}"
# create an instance of GuestAuthAnySubject from a JSON string
guest_auth_any_subject_instance = GuestAuthAnySubject.from_json(json)
# print the JSON string representation of the object
print GuestAuthAnySubject.to_json()

# convert the object into a dict
guest_auth_any_subject_dict = guest_auth_any_subject_instance.to_dict()
# create an instance of GuestAuthAnySubject from a dict
guest_auth_any_subject_form_dict = guest_auth_any_subject.from_dict(guest_auth_any_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


