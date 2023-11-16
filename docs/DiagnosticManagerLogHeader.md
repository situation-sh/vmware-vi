# DiagnosticManagerLogHeader

A header that is returned with a set of log entries.  This header describes where entries are located in the log file. Log files typically grow dynamically, so indexes based on line numbers may become inaccurate. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_start** | **int** | The first line of this log segment.  | 
**line_end** | **int** | The last line of this log segment.  | 
**line_text** | **List[str]** | Log entries, listed by line, for this log segment.  | [optional] 

## Example

```python
from vmware_vi.models.diagnostic_manager_log_header import DiagnosticManagerLogHeader

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticManagerLogHeader from a JSON string
diagnostic_manager_log_header_instance = DiagnosticManagerLogHeader.from_json(json)
# print the JSON string representation of the object
print DiagnosticManagerLogHeader.to_json()

# convert the object into a dict
diagnostic_manager_log_header_dict = diagnostic_manager_log_header_instance.to_dict()
# create an instance of DiagnosticManagerLogHeader from a dict
diagnostic_manager_log_header_form_dict = diagnostic_manager_log_header.from_dict(diagnostic_manager_log_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


