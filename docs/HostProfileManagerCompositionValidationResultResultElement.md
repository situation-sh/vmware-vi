# HostProfileManagerCompositionValidationResultResultElement

The host profile composition validation result for a specific target host profile.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**status** | **str** | The composition validation status.  See *HostProfileManagerCompositionValidationResultResultElementStatus_enum* for details of supported values.  ***Since:*** vSphere API 6.5  | 
**errors** | [**List[LocalizableMessage]**](LocalizableMessage.md) | The composition validation errors.  ***Since:*** vSphere API 6.5  | [optional] 
**source_diff_for_to_be_merged** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**target_diff_for_to_be_merged** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_be_added** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_be_deleted** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_be_disabled** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_be_enabled** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_be_reenable_cc** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_manager_composition_validation_result_result_element import HostProfileManagerCompositionValidationResultResultElement

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileManagerCompositionValidationResultResultElement from a JSON string
host_profile_manager_composition_validation_result_result_element_instance = HostProfileManagerCompositionValidationResultResultElement.from_json(json)
# print the JSON string representation of the object
print HostProfileManagerCompositionValidationResultResultElement.to_json()

# convert the object into a dict
host_profile_manager_composition_validation_result_result_element_dict = host_profile_manager_composition_validation_result_result_element_instance.to_dict()
# create an instance of HostProfileManagerCompositionValidationResultResultElement from a dict
host_profile_manager_composition_validation_result_result_element_form_dict = host_profile_manager_composition_validation_result_result_element.from_dict(host_profile_manager_composition_validation_result_result_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


