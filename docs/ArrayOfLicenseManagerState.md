# ArrayOfLicenseManagerState

A boxed array of *LicenseManagerState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseManagerStateEnum]**](LicenseManagerStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_manager_state import ArrayOfLicenseManagerState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseManagerState from a JSON string
array_of_license_manager_state_instance = ArrayOfLicenseManagerState.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseManagerState.to_json()

# convert the object into a dict
array_of_license_manager_state_dict = array_of_license_manager_state_instance.to_dict()
# create an instance of ArrayOfLicenseManagerState from a dict
array_of_license_manager_state_form_dict = array_of_license_manager_state.from_dict(array_of_license_manager_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


