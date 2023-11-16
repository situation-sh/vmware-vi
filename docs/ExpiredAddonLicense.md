# ExpiredAddonLicense

An ExpiredAddonLicense fault is thrown if an attempt to acquire an Addon license 'feature failed for count 'count'.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.expired_addon_license import ExpiredAddonLicense

# TODO update the JSON string below
json = "{}"
# create an instance of ExpiredAddonLicense from a JSON string
expired_addon_license_instance = ExpiredAddonLicense.from_json(json)
# print the JSON string representation of the object
print ExpiredAddonLicense.to_json()

# convert the object into a dict
expired_addon_license_dict = expired_addon_license_instance.to_dict()
# create an instance of ExpiredAddonLicense from a dict
expired_addon_license_form_dict = expired_addon_license.from_dict(expired_addon_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


