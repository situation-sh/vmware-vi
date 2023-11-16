# ArrayOfDiagnosticManagerLogHeader

A boxed array of *DiagnosticManagerLogHeader*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DiagnosticManagerLogHeader]**](DiagnosticManagerLogHeader.md) |  | 

## Example

```python
from vmware_vi.models.array_of_diagnostic_manager_log_header import ArrayOfDiagnosticManagerLogHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDiagnosticManagerLogHeader from a JSON string
array_of_diagnostic_manager_log_header_instance = ArrayOfDiagnosticManagerLogHeader.from_json(json)
# print the JSON string representation of the object
print ArrayOfDiagnosticManagerLogHeader.to_json()

# convert the object into a dict
array_of_diagnostic_manager_log_header_dict = array_of_diagnostic_manager_log_header_instance.to_dict()
# create an instance of ArrayOfDiagnosticManagerLogHeader from a dict
array_of_diagnostic_manager_log_header_form_dict = array_of_diagnostic_manager_log_header.from_dict(array_of_diagnostic_manager_log_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


