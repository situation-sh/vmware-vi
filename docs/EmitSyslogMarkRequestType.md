# EmitSyslogMarkRequestType

The parameters of *DiagnosticManager.EmitSyslogMark*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The string to be used.  | 

## Example

```python
from vmware_vi.models.emit_syslog_mark_request_type import EmitSyslogMarkRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EmitSyslogMarkRequestType from a JSON string
emit_syslog_mark_request_type_instance = EmitSyslogMarkRequestType.from_json(json)
# print the JSON string representation of the object
print EmitSyslogMarkRequestType.to_json()

# convert the object into a dict
emit_syslog_mark_request_type_dict = emit_syslog_mark_request_type_instance.to_dict()
# create an instance of EmitSyslogMarkRequestType from a dict
emit_syslog_mark_request_type_form_dict = emit_syslog_mark_request_type.from_dict(emit_syslog_mark_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


