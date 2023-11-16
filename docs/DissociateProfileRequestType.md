# DissociateProfileRequestType

The parameters of *Profile.DissociateProfile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of entities. The vCenter Server will remove the associations that the profile has with the entities in the list. If unset, the Server removes all the associations that the profile has with any managed entities in the inventory. If the specified entity is not associated with the profile, the Server does not perform any action.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.dissociate_profile_request_type import DissociateProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DissociateProfileRequestType from a JSON string
dissociate_profile_request_type_instance = DissociateProfileRequestType.from_json(json)
# print the JSON string representation of the object
print DissociateProfileRequestType.to_json()

# convert the object into a dict
dissociate_profile_request_type_dict = dissociate_profile_request_type_instance.to_dict()
# create an instance of DissociateProfileRequestType from a dict
dissociate_profile_request_type_form_dict = dissociate_profile_request_type.from_dict(dissociate_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


