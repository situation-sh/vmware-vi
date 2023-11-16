# InvalidLicense

Thrown when an attempt is made to upload license content that is invalid. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_content** | **str** | The content of the license being reported as invalid.  | 

## Example

```python
from vmware_vi.models.invalid_license import InvalidLicense

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidLicense from a JSON string
invalid_license_instance = InvalidLicense.from_json(json)
# print the JSON string representation of the object
print InvalidLicense.to_json()

# convert the object into a dict
invalid_license_dict = invalid_license_instance.to_dict()
# create an instance of InvalidLicense from a dict
invalid_license_form_dict = invalid_license.from_dict(invalid_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


