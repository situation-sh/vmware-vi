# CreateDefaultProfileRequestType

The parameters of *HostProfileManager.CreateDefaultProfile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_type** | **str** | Type of profile to create. The profile types are system-defined (*ApplyProfile*.*ApplyProfile.profileTypeName*).  | 
**profile_type_name** | **str** | If specified, the method returns a profile object containing data for the named profile. The type name does not have to be system-defined. A user-defined profile can include various dynamically-defined profiles.  | [optional] 
**profile** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.create_default_profile_request_type import CreateDefaultProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDefaultProfileRequestType from a JSON string
create_default_profile_request_type_instance = CreateDefaultProfileRequestType.from_json(json)
# print the JSON string representation of the object
print CreateDefaultProfileRequestType.to_json()

# convert the object into a dict
create_default_profile_request_type_dict = create_default_profile_request_type_instance.to_dict()
# create an instance of CreateDefaultProfileRequestType from a dict
create_default_profile_request_type_form_dict = create_default_profile_request_type.from_dict(create_default_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


