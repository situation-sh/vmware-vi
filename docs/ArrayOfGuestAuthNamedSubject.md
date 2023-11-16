# ArrayOfGuestAuthNamedSubject

A boxed array of *GuestAuthNamedSubject*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestAuthNamedSubject]**](GuestAuthNamedSubject.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_auth_named_subject import ArrayOfGuestAuthNamedSubject

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestAuthNamedSubject from a JSON string
array_of_guest_auth_named_subject_instance = ArrayOfGuestAuthNamedSubject.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestAuthNamedSubject.to_json()

# convert the object into a dict
array_of_guest_auth_named_subject_dict = array_of_guest_auth_named_subject_instance.to_dict()
# create an instance of ArrayOfGuestAuthNamedSubject from a dict
array_of_guest_auth_named_subject_form_dict = array_of_guest_auth_named_subject.from_dict(array_of_guest_auth_named_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


