# SiteInfo

This data object type represents the external site-related capabilities available in the environment managed by this vCenter.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.site_info import SiteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SiteInfo from a JSON string
site_info_instance = SiteInfo.from_json(json)
# print the JSON string representation of the object
print SiteInfo.to_json()

# convert the object into a dict
site_info_dict = site_info_instance.to_dict()
# create an instance of SiteInfo from a dict
site_info_form_dict = site_info.from_dict(site_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


