# LicenseManagerEvaluationInfo

Encapsulates product evaluation information  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**List[KeyAnyValue]**](KeyAnyValue.md) | Evaluation properties  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.license_manager_evaluation_info import LicenseManagerEvaluationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseManagerEvaluationInfo from a JSON string
license_manager_evaluation_info_instance = LicenseManagerEvaluationInfo.from_json(json)
# print the JSON string representation of the object
print LicenseManagerEvaluationInfo.to_json()

# convert the object into a dict
license_manager_evaluation_info_dict = license_manager_evaluation_info_instance.to_dict()
# create an instance of LicenseManagerEvaluationInfo from a dict
license_manager_evaluation_info_form_dict = license_manager_evaluation_info.from_dict(license_manager_evaluation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


