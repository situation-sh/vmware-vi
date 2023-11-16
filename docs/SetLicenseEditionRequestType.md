# SetLicenseEditionRequestType

The parameters of *LicenseManager.SetLicenseEdition*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**feature_key** | **str** | Name of edition feature to select. If featureKey is not set or set to empty string, the product becomes unlicensed.  | [optional] 

## Example

```python
from vmware_vi.models.set_license_edition_request_type import SetLicenseEditionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetLicenseEditionRequestType from a JSON string
set_license_edition_request_type_instance = SetLicenseEditionRequestType.from_json(json)
# print the JSON string representation of the object
print SetLicenseEditionRequestType.to_json()

# convert the object into a dict
set_license_edition_request_type_dict = set_license_edition_request_type_instance.to_dict()
# create an instance of SetLicenseEditionRequestType from a dict
set_license_edition_request_type_form_dict = set_license_edition_request_type.from_dict(set_license_edition_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


