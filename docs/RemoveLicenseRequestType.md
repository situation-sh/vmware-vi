# RemoveLicenseRequestType

The parameters of *LicenseManager.RemoveLicense*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** | A licenses. E.g. a serial license.  | 

## Example

```python
from vmware_vi.models.remove_license_request_type import RemoveLicenseRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveLicenseRequestType from a JSON string
remove_license_request_type_instance = RemoveLicenseRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveLicenseRequestType.to_json()

# convert the object into a dict
remove_license_request_type_dict = remove_license_request_type_instance.to_dict()
# create an instance of RemoveLicenseRequestType from a dict
remove_license_request_type_form_dict = remove_license_request_type.from_dict(remove_license_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


