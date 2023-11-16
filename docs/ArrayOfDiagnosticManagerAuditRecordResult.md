# ArrayOfDiagnosticManagerAuditRecordResult

A boxed array of *DiagnosticManagerAuditRecordResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DiagnosticManagerAuditRecordResult]**](DiagnosticManagerAuditRecordResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_diagnostic_manager_audit_record_result import ArrayOfDiagnosticManagerAuditRecordResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDiagnosticManagerAuditRecordResult from a JSON string
array_of_diagnostic_manager_audit_record_result_instance = ArrayOfDiagnosticManagerAuditRecordResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfDiagnosticManagerAuditRecordResult.to_json()

# convert the object into a dict
array_of_diagnostic_manager_audit_record_result_dict = array_of_diagnostic_manager_audit_record_result_instance.to_dict()
# create an instance of ArrayOfDiagnosticManagerAuditRecordResult from a dict
array_of_diagnostic_manager_audit_record_result_form_dict = array_of_diagnostic_manager_audit_record_result.from_dict(array_of_diagnostic_manager_audit_record_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


