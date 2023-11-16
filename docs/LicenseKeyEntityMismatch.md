# LicenseKeyEntityMismatch

A LicenseKeyEntityMismatch fault is thrown if an assignment operation tries to assign a license that does not apply to an entity.  For example assigning a host license to VirtualCenter.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.license_key_entity_mismatch import LicenseKeyEntityMismatch

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseKeyEntityMismatch from a JSON string
license_key_entity_mismatch_instance = LicenseKeyEntityMismatch.from_json(json)
# print the JSON string representation of the object
print LicenseKeyEntityMismatch.to_json()

# convert the object into a dict
license_key_entity_mismatch_dict = license_key_entity_mismatch_instance.to_dict()
# create an instance of LicenseKeyEntityMismatch from a dict
license_key_entity_mismatch_form_dict = license_key_entity_mismatch.from_dict(license_key_entity_mismatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


