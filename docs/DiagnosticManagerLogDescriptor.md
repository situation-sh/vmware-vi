# DiagnosticManagerLogDescriptor

Describes a log file that is available on a server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A key to identify the log file for browsing and download operations.  | 
**file_name** | **str** | The filename of the log.  | 
**creator** | **str** | The application that generated the log file.  For more information on currently supported creators, see *DiagnosticManagerLogCreator_enum*.  | 
**format** | **str** | Describes the format of the log file.  For more information on currently supported formats, see *DiagnosticManagerLogFormat_enum*.  | 
**mime_type** | **str** | Describes the mime-type of the returned file.  Typical mime-types include: - text/plain - for a plain log file  | 
**info** | [**Description**](Description.md) |  | 

## Example

```python
from vmware_vi.models.diagnostic_manager_log_descriptor import DiagnosticManagerLogDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of DiagnosticManagerLogDescriptor from a JSON string
diagnostic_manager_log_descriptor_instance = DiagnosticManagerLogDescriptor.from_json(json)
# print the JSON string representation of the object
print DiagnosticManagerLogDescriptor.to_json()

# convert the object into a dict
diagnostic_manager_log_descriptor_dict = diagnostic_manager_log_descriptor_instance.to_dict()
# create an instance of DiagnosticManagerLogDescriptor from a dict
diagnostic_manager_log_descriptor_form_dict = diagnostic_manager_log_descriptor.from_dict(diagnostic_manager_log_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


