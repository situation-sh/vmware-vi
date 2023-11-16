# AssociateProfileRequestType

The parameters of *Profile.AssociateProfile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The entity(s) to associate with the profile. If an entity is already associated with the profile, the association is maintained and the vCenter Server does not perform any action.  Refers instances of *ManagedEntity*.  | 

## Example

```python
from vmware_vi.models.associate_profile_request_type import AssociateProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AssociateProfileRequestType from a JSON string
associate_profile_request_type_instance = AssociateProfileRequestType.from_json(json)
# print the JSON string representation of the object
print AssociateProfileRequestType.to_json()

# convert the object into a dict
associate_profile_request_type_dict = associate_profile_request_type_instance.to_dict()
# create an instance of AssociateProfileRequestType from a dict
associate_profile_request_type_form_dict = associate_profile_request_type.from_dict(associate_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


