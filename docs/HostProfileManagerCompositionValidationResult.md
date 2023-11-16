# HostProfileManagerCompositionValidationResult

The data class for the host profile composition validation results.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HostProfileManagerCompositionValidationResultResultElement]**](HostProfileManagerCompositionValidationResultResultElement.md) | The array of *HostProfileManagerCompositionValidationResultResultElement* for all the target host profiles.  ***Since:*** vSphere API 6.5  | [optional] 
**errors** | [**List[LocalizableMessage]**](LocalizableMessage.md) | The common error happened at validation.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_profile_manager_composition_validation_result import HostProfileManagerCompositionValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostProfileManagerCompositionValidationResult from a JSON string
host_profile_manager_composition_validation_result_instance = HostProfileManagerCompositionValidationResult.from_json(json)
# print the JSON string representation of the object
print HostProfileManagerCompositionValidationResult.to_json()

# convert the object into a dict
host_profile_manager_composition_validation_result_dict = host_profile_manager_composition_validation_result_instance.to_dict()
# create an instance of HostProfileManagerCompositionValidationResult from a dict
host_profile_manager_composition_validation_result_form_dict = host_profile_manager_composition_validation_result.from_dict(host_profile_manager_composition_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


