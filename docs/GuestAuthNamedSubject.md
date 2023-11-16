# GuestAuthNamedSubject

A named subject.  Grants access to a specific vSphere user with the specified name.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The subject name.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_auth_named_subject import GuestAuthNamedSubject

# TODO update the JSON string below
json = "{}"
# create an instance of GuestAuthNamedSubject from a JSON string
guest_auth_named_subject_instance = GuestAuthNamedSubject.from_json(json)
# print the JSON string representation of the object
print GuestAuthNamedSubject.to_json()

# convert the object into a dict
guest_auth_named_subject_dict = guest_auth_named_subject_instance.to_dict()
# create an instance of GuestAuthNamedSubject from a dict
guest_auth_named_subject_form_dict = guest_auth_named_subject.from_dict(guest_auth_named_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


