# ArrayOfExpiredAddonLicense

A boxed array of *ExpiredAddonLicense*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExpiredAddonLicense]**](ExpiredAddonLicense.md) |  | 

## Example

```python
from vmware_vi.models.array_of_expired_addon_license import ArrayOfExpiredAddonLicense

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExpiredAddonLicense from a JSON string
array_of_expired_addon_license_instance = ArrayOfExpiredAddonLicense.from_json(json)
# print the JSON string representation of the object
print ArrayOfExpiredAddonLicense.to_json()

# convert the object into a dict
array_of_expired_addon_license_dict = array_of_expired_addon_license_instance.to_dict()
# create an instance of ArrayOfExpiredAddonLicense from a dict
array_of_expired_addon_license_form_dict = array_of_expired_addon_license.from_dict(array_of_expired_addon_license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


