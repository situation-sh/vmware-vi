# ArrayOfDiagnosticManagerLogDescriptor

A boxed array of *DiagnosticManagerLogDescriptor*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DiagnosticManagerLogDescriptor]**](DiagnosticManagerLogDescriptor.md) |  | 

## Example

```python
from vmware_vi.models.array_of_diagnostic_manager_log_descriptor import ArrayOfDiagnosticManagerLogDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDiagnosticManagerLogDescriptor from a JSON string
array_of_diagnostic_manager_log_descriptor_instance = ArrayOfDiagnosticManagerLogDescriptor.from_json(json)
# print the JSON string representation of the object
print ArrayOfDiagnosticManagerLogDescriptor.to_json()

# convert the object into a dict
array_of_diagnostic_manager_log_descriptor_dict = array_of_diagnostic_manager_log_descriptor_instance.to_dict()
# create an instance of ArrayOfDiagnosticManagerLogDescriptor from a dict
array_of_diagnostic_manager_log_descriptor_form_dict = array_of_diagnostic_manager_log_descriptor.from_dict(array_of_diagnostic_manager_log_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


