# ArrayOfLicenseManagerEvaluationInfo

A boxed array of *LicenseManagerEvaluationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseManagerEvaluationInfo]**](LicenseManagerEvaluationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_manager_evaluation_info import ArrayOfLicenseManagerEvaluationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseManagerEvaluationInfo from a JSON string
array_of_license_manager_evaluation_info_instance = ArrayOfLicenseManagerEvaluationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseManagerEvaluationInfo.to_json()

# convert the object into a dict
array_of_license_manager_evaluation_info_dict = array_of_license_manager_evaluation_info_instance.to_dict()
# create an instance of ArrayOfLicenseManagerEvaluationInfo from a dict
array_of_license_manager_evaluation_info_form_dict = array_of_license_manager_evaluation_info.from_dict(array_of_license_manager_evaluation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


