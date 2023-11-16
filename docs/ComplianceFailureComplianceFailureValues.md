# ComplianceFailureComplianceFailureValues


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_identifier** | **str** | Unique key to a message in the localized message catalog, identifying the fields being compared.  ***Since:*** vSphere API 6.5  | 
**profile_instance** | **str** | Name of the profile instance, in case of non-singleton profiles.  ***Since:*** vSphere API 6.5  | [optional] 
**host_value** | [**Any**](Any.md) |  | [optional] 
**profile_value** | [**Any**](Any.md) |  | [optional] 

## Example

```python
from vmware_vi.models.compliance_failure_compliance_failure_values import ComplianceFailureComplianceFailureValues

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceFailureComplianceFailureValues from a JSON string
compliance_failure_compliance_failure_values_instance = ComplianceFailureComplianceFailureValues.from_json(json)
# print the JSON string representation of the object
print ComplianceFailureComplianceFailureValues.to_json()

# convert the object into a dict
compliance_failure_compliance_failure_values_dict = compliance_failure_compliance_failure_values_instance.to_dict()
# create an instance of ComplianceFailureComplianceFailureValues from a dict
compliance_failure_compliance_failure_values_form_dict = compliance_failure_compliance_failure_values.from_dict(compliance_failure_compliance_failure_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


