# ArrayOfDiagnosticManagerBundleInfo

A boxed array of *DiagnosticManagerBundleInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DiagnosticManagerBundleInfo]**](DiagnosticManagerBundleInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_diagnostic_manager_bundle_info import ArrayOfDiagnosticManagerBundleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDiagnosticManagerBundleInfo from a JSON string
array_of_diagnostic_manager_bundle_info_instance = ArrayOfDiagnosticManagerBundleInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfDiagnosticManagerBundleInfo.to_json()

# convert the object into a dict
array_of_diagnostic_manager_bundle_info_dict = array_of_diagnostic_manager_bundle_info_instance.to_dict()
# create an instance of ArrayOfDiagnosticManagerBundleInfo from a dict
array_of_diagnostic_manager_bundle_info_form_dict = array_of_diagnostic_manager_bundle_info.from_dict(array_of_diagnostic_manager_bundle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


