# FetchAuditRecordsRequestType

The parameters of *DiagnosticManager.FetchAuditRecords*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token to be used for the operation. The first call must be made without a token. All subsequent calls use the token returned in AuditRecordStatus.  | [optional] 

## Example

```python
from vmware_vi.models.fetch_audit_records_request_type import FetchAuditRecordsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FetchAuditRecordsRequestType from a JSON string
fetch_audit_records_request_type_instance = FetchAuditRecordsRequestType.from_json(json)
# print the JSON string representation of the object
print FetchAuditRecordsRequestType.to_json()

# convert the object into a dict
fetch_audit_records_request_type_dict = fetch_audit_records_request_type_instance.to_dict()
# create an instance of FetchAuditRecordsRequestType from a dict
fetch_audit_records_request_type_form_dict = fetch_audit_records_request_type.from_dict(fetch_audit_records_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


