# ExpiredEditionLicense

An ExpiredEditionLicense fault is thrown if an attempt to acquire an Edition license 'feature failed for count 'count'.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.expired_edition_license import ExpiredEditionLicense

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiredEditionLicense from a JSON string
expired_edition_license_instance = ExpiredEditionLicense.from_json(json)
# print the JSON string representation of the object
print ExpiredEditionLicense.to_json()

# convert the object into a dict
expired_edition_license_dict = expired_edition_license_instance.to_dict()
# create an instance of ExpiredEditionLicense from a dict
expired_edition_license_form_dict = expired_edition_license.from_dict(expired_edition_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


