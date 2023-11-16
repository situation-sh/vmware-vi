# UpdateLicenseRequestType

The parameters of *LicenseManager.UpdateLicense*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** | A license. E.g. a serial license.  | 
**labels** | [**List[KeyValue]**](KeyValue.md) | array of key-value labels.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.update_license_request_type import UpdateLicenseRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLicenseRequestType from a JSON string
update_license_request_type_instance = UpdateLicenseRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateLicenseRequestType.to_json()

# convert the object into a dict
update_license_request_type_dict = update_license_request_type_instance.to_dict()
# create an instance of UpdateLicenseRequestType from a dict
update_license_request_type_form_dict = update_license_request_type.from_dict(update_license_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


