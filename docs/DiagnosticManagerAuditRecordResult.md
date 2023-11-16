# DiagnosticManagerAuditRecordResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | **List[str]** | Zero or more audit records returned.  Each audit record is a UTF-8 string in RFC 5424 format. See RFC 5424, page 8, for the ABNF grammar.  The HOSTNAME and MSGID fields are set to \&quot;-\&quot;, the structured data contains the audit record parameters, no unstructured data will be present, and each record is terminated with an ASCII LF (newline).  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**next_token** | **str** | The token to be used for subsequent read operations.  The string is \&quot;opaque\&quot;; the format of this data changes over time.  ***Since:*** vSphere API 7.0.3.0  | 

## Example

```python
from vmware_vi.models.diagnostic_manager_audit_record_result import DiagnosticManagerAuditRecordResult

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticManagerAuditRecordResult from a JSON string
diagnostic_manager_audit_record_result_instance = DiagnosticManagerAuditRecordResult.from_json(json)
# print the JSON string representation of the object
print DiagnosticManagerAuditRecordResult.to_json()

# convert the object into a dict
diagnostic_manager_audit_record_result_dict = diagnostic_manager_audit_record_result_instance.to_dict()
# create an instance of DiagnosticManagerAuditRecordResult from a dict
diagnostic_manager_audit_record_result_form_dict = diagnostic_manager_audit_record_result.from_dict(diagnostic_manager_audit_record_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


