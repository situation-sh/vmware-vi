# AddLicenseRequestType

The parameters of *LicenseManager.AddLicense*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** | A license. E.g. a serial license.  | 
**labels** | [**List[KeyValue]**](KeyValue.md) | array of key-value labels. Ignored by ESX Server.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.add_license_request_type import AddLicenseRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddLicenseRequestType from a JSON string
add_license_request_type_instance = AddLicenseRequestType.from_json(json)
# print the JSON string representation of the object
print AddLicenseRequestType.to_json()

# convert the object into a dict
add_license_request_type_dict = add_license_request_type_instance.to_dict()
# create an instance of AddLicenseRequestType from a dict
add_license_request_type_form_dict = add_license_request_type.from_dict(add_license_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


