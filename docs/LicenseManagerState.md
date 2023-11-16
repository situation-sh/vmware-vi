# LicenseManagerState

A boxed *LicenseManagerState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**LicenseManagerStateEnum**](LicenseManagerStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.license_manager_state import LicenseManagerState

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseManagerState from a JSON string
license_manager_state_instance = LicenseManagerState.from_json(json)
# print the JSON string representation of the object
print LicenseManagerState.to_json()

# convert the object into a dict
license_manager_state_dict = license_manager_state_instance.to_dict()
# create an instance of LicenseManagerState from a dict
license_manager_state_form_dict = license_manager_state.from_dict(license_manager_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


