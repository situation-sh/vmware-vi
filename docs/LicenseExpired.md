# LicenseExpired

A LicenseExpired fault is thrown if it an operation is unsuccessful because the license used for the operation has expired.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** | License key that has expired  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.license_expired import LicenseExpired

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseExpired from a JSON string
license_expired_instance = LicenseExpired.from_json(json)
# print the JSON string representation of the object
print LicenseExpired.to_json()

# convert the object into a dict
license_expired_dict = license_expired_instance.to_dict()
# create an instance of LicenseExpired from a dict
license_expired_form_dict = license_expired.from_dict(license_expired_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


