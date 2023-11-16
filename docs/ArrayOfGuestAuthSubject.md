# ArrayOfGuestAuthSubject

A boxed array of *GuestAuthSubject*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestAuthSubject]**](GuestAuthSubject.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_auth_subject import ArrayOfGuestAuthSubject

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestAuthSubject from a JSON string
array_of_guest_auth_subject_instance = ArrayOfGuestAuthSubject.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestAuthSubject.to_json()

# convert the object into a dict
array_of_guest_auth_subject_dict = array_of_guest_auth_subject_instance.to_dict()
# create an instance of ArrayOfGuestAuthSubject from a dict
array_of_guest_auth_subject_form_dict = array_of_guest_auth_subject.from_dict(array_of_guest_auth_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


