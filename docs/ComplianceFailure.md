# ComplianceFailure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_type** | **str** | String uniquely identifying the failure.  ***Since:*** vSphere API 4.0  | 
**message** | [**LocalizableMessage**](LocalizableMessage.md) |  | 
**expression_name** | **str** | Name of the Expression which generated the ComplianceFailure  ***Since:*** vSphere API 4.0  | [optional] 
**failure_values** | [**List[ComplianceFailureComplianceFailureValues]**](ComplianceFailureComplianceFailureValues.md) | If complianceStatus is non-compliant, failureValues will contain values of the non-compliant fields on the host and in the profile.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.compliance_failure import ComplianceFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceFailure from a JSON string
compliance_failure_instance = ComplianceFailure.from_json(json)
# print the JSON string representation of the object
print ComplianceFailure.to_json()

# convert the object into a dict
compliance_failure_dict = compliance_failure_instance.to_dict()
# create an instance of ComplianceFailure from a dict
compliance_failure_form_dict = compliance_failure.from_dict(compliance_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


