# InvalidEditionLicense

An ExpiredEditionLicense fault is thrown if an attempt to acquire an Edition license 'feature failed for count 'count'.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** |  | 

## Example

```python
from vmware_vi.models.invalid_edition_license import InvalidEditionLicense

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidEditionLicense from a JSON string
invalid_edition_license_instance = InvalidEditionLicense.from_json(json)
# print the JSON string representation of the object
print InvalidEditionLicense.to_json()

# convert the object into a dict
invalid_edition_license_dict = invalid_edition_license_instance.to_dict()
# create an instance of InvalidEditionLicense from a dict
invalid_edition_license_form_dict = invalid_edition_license.from_dict(invalid_edition_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


