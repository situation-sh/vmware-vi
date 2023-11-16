# LicenseDowngradeDisallowed

A LicenseDowngradeDisallowed fault is thrown if an assignment operation tries to downgrade a license that does have certain licensed features which are in use.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edition** | **str** |  | 
**entity_id** | **str** |  | 
**features** | [**List[KeyAnyValue]**](KeyAnyValue.md) | List of conflicting features that prevent downgrade  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.license_downgrade_disallowed import LicenseDowngradeDisallowed

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseDowngradeDisallowed from a JSON string
license_downgrade_disallowed_instance = LicenseDowngradeDisallowed.from_json(json)
# print the JSON string representation of the object
print LicenseDowngradeDisallowed.to_json()

# convert the object into a dict
license_downgrade_disallowed_dict = license_downgrade_disallowed_instance.to_dict()
# create an instance of LicenseDowngradeDisallowed from a dict
license_downgrade_disallowed_form_dict = license_downgrade_disallowed.from_dict(license_downgrade_disallowed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


