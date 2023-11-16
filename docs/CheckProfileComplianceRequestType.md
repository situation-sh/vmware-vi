# CheckProfileComplianceRequestType

The parameters of *Profile.CheckProfileCompliance_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | If specified, the compliance check is performed on this entity. If the entity is not specified, the vCenter Server runs a compliance check on all the entities associated with the profile. The entity does not have to be associated with the profile.  Refers instances of *ManagedEntity*.  | [optional] 

## Example

```python
from vmware_vi.models.check_profile_compliance_request_type import CheckProfileComplianceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckProfileComplianceRequestType from a JSON string
check_profile_compliance_request_type_instance = CheckProfileComplianceRequestType.from_json(json)
# print the JSON string representation of the object
print CheckProfileComplianceRequestType.to_json()

# convert the object into a dict
check_profile_compliance_request_type_dict = check_profile_compliance_request_type_instance.to_dict()
# create an instance of CheckProfileComplianceRequestType from a dict
check_profile_compliance_request_type_form_dict = check_profile_compliance_request_type.from_dict(check_profile_compliance_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


