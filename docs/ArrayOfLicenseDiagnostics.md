# ArrayOfLicenseDiagnostics

A boxed array of *LicenseDiagnostics*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseDiagnostics]**](LicenseDiagnostics.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_diagnostics import ArrayOfLicenseDiagnostics

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseDiagnostics from a JSON string
array_of_license_diagnostics_instance = ArrayOfLicenseDiagnostics.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseDiagnostics.to_json()

# convert the object into a dict
array_of_license_diagnostics_dict = array_of_license_diagnostics_instance.to_dict()
# create an instance of ArrayOfLicenseDiagnostics from a dict
array_of_license_diagnostics_form_dict = array_of_license_diagnostics.from_dict(array_of_license_diagnostics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


