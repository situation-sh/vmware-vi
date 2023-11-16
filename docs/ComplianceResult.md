# ComplianceResult

DataObject representing the result from a ComplianceCheck  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**compliance_status** | **str** | Indicates the compliance status of the entity.  See @link Status  ***Since:*** vSphere API 4.0  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**check_time** | **datetime** | Time at which compliance check was last run on the entity  ***Since:*** vSphere API 4.0  | [optional] 
**failure** | [**List[ComplianceFailure]**](ComplianceFailure.md) | If complianceStatus is non-compliant, failure will contain additional information about the compliance errors.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.compliance_result import ComplianceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceResult from a JSON string
compliance_result_instance = ComplianceResult.from_json(json)
# print the JSON string representation of the object
print ComplianceResult.to_json()

# convert the object into a dict
compliance_result_dict = compliance_result_instance.to_dict()
# create an instance of ComplianceResult from a dict
compliance_result_form_dict = compliance_result.from_dict(compliance_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


