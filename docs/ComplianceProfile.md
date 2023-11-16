# ComplianceProfile

DataObject contains the verifications that need to be done to make sure the entity is in compliance.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | [**List[ProfileExpression]**](ProfileExpression.md) | List of expressions that make up the ComplianceChecks.  ***Since:*** vSphere API 4.0  | 
**root_expression** | **str** | Name of the Expression which is the root of the expression tree.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.compliance_profile import ComplianceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceProfile from a JSON string
compliance_profile_instance = ComplianceProfile.from_json(json)
# print the JSON string representation of the object
print ComplianceProfile.to_json()

# convert the object into a dict
compliance_profile_dict = compliance_profile_instance.to_dict()
# create an instance of ComplianceProfile from a dict
compliance_profile_form_dict = compliance_profile.from_dict(compliance_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


