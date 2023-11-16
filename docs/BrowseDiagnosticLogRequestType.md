# BrowseDiagnosticLogRequestType

The parameters of *DiagnosticManager.BrowseDiagnosticLog*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**key** | **str** | A string key specifying the key for the log file to browse. Keys can be obtained using the queryDescriptions method.  | 
**start** | **int** | The line number for the first entry to be returned. If the parameter is not specified, then the operation returns with lines starting from the top of the log.  | [optional] 
**lines** | **int** | The number of lines to return. If not specified, then all lines are returned from the start value to the end of the file.  | [optional] 

## Example

```python
from vmware_vi.models.browse_diagnostic_log_request_type import BrowseDiagnosticLogRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseDiagnosticLogRequestType from a JSON string
browse_diagnostic_log_request_type_instance = BrowseDiagnosticLogRequestType.from_json(json)
# print the JSON string representation of the object
print BrowseDiagnosticLogRequestType.to_json()

# convert the object into a dict
browse_diagnostic_log_request_type_dict = browse_diagnostic_log_request_type_instance.to_dict()
# create an instance of BrowseDiagnosticLogRequestType from a dict
browse_diagnostic_log_request_type_form_dict = browse_diagnostic_log_request_type.from_dict(browse_diagnostic_log_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


