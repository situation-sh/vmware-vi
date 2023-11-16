# EvaluationLicenseSource

Deprecated as of vSphere API 4.0, this is not used by the system.  Specify an evaluation license source.  Feature licensing is not required while the remaining hours is greater than zero.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remaining_hours** | **int** | The number of remaining hours before product evaluation expires  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.evaluation_license_source import EvaluationLicenseSource

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationLicenseSource from a JSON string
evaluation_license_source_instance = EvaluationLicenseSource.from_json(json)
# print the JSON string representation of the object
print EvaluationLicenseSource.to_json()

# convert the object into a dict
evaluation_license_source_dict = evaluation_license_source_instance.to_dict()
# create an instance of EvaluationLicenseSource from a dict
evaluation_license_source_form_dict = evaluation_license_source.from_dict(evaluation_license_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


