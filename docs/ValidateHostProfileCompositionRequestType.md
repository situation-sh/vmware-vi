# ValidateHostProfileCompositionRequestType

The parameters of *HostProfileManager.ValidateHostProfileComposition_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**targets** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The array of target host profiles that the configurations composite into.  ***Since:*** vSphere API 4.0  Refers instances of *Profile*.  | [optional] 
**to_be_merged** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_replace_with** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_be_deleted** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**enable_status_to_be_copied** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**error_only** | **bool** | Indicates that the validation result for each target don&#39;t contain the source-target difference.  | [optional] 

## Example

```python
from vmware_vi.models.validate_host_profile_composition_request_type import ValidateHostProfileCompositionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateHostProfileCompositionRequestType from a JSON string
validate_host_profile_composition_request_type_instance = ValidateHostProfileCompositionRequestType.from_json(json)
# print the JSON string representation of the object
print ValidateHostProfileCompositionRequestType.to_json()

# convert the object into a dict
validate_host_profile_composition_request_type_dict = validate_host_profile_composition_request_type_instance.to_dict()
# create an instance of ValidateHostProfileCompositionRequestType from a dict
validate_host_profile_composition_request_type_form_dict = validate_host_profile_composition_request_type.from_dict(validate_host_profile_composition_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


