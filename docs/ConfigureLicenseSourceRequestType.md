# ConfigureLicenseSourceRequestType

The parameters of *LicenseManager.ConfigureLicenseSource*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**license_source** | [**LicenseSource**](LicenseSource.md) |  | 

## Example

```python
from vmware_vi.models.configure_license_source_request_type import ConfigureLicenseSourceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureLicenseSourceRequestType from a JSON string
configure_license_source_request_type_instance = ConfigureLicenseSourceRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureLicenseSourceRequestType.to_json()

# convert the object into a dict
configure_license_source_request_type_dict = configure_license_source_request_type_instance.to_dict()
# create an instance of ConfigureLicenseSourceRequestType from a dict
configure_license_source_request_type_form_dict = configure_license_source_request_type.from_dict(configure_license_source_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


