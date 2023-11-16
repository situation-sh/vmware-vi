# UpdateLicenseLabelRequestType

The parameters of *LicenseManager.UpdateLicenseLabel*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** | A license.  | 
**label_key** | **str** | A label key.  | 
**label_value** | **str** | Value for the label.  | 

## Example

```python
from vmware_vi.models.update_license_label_request_type import UpdateLicenseLabelRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLicenseLabelRequestType from a JSON string
update_license_label_request_type_instance = UpdateLicenseLabelRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateLicenseLabelRequestType.to_json()

# convert the object into a dict
update_license_label_request_type_dict = update_license_label_request_type_instance.to_dict()
# create an instance of UpdateLicenseLabelRequestType from a dict
update_license_label_request_type_form_dict = update_license_label_request_type.from_dict(update_license_label_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


