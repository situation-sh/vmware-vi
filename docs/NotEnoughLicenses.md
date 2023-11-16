# NotEnoughLicenses

A NotEnoughLicensesFault occurs when an operation fails because there are not enough licenses installed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.not_enough_licenses import NotEnoughLicenses

# TODO update the JSON string below
json = "{}"
# create an instance of NotEnoughLicenses from a JSON string
not_enough_licenses_instance = NotEnoughLicenses.from_json(json)
# print the JSON string representation of the object
print NotEnoughLicenses.to_json()

# convert the object into a dict
not_enough_licenses_dict = not_enough_licenses_instance.to_dict()
# create an instance of NotEnoughLicenses from a dict
not_enough_licenses_form_dict = not_enough_licenses.from_dict(not_enough_licenses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


