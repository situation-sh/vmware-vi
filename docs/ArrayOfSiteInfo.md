# ArrayOfSiteInfo

A boxed array of *SiteInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SiteInfo]**](SiteInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_site_info import ArrayOfSiteInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSiteInfo from a JSON string
array_of_site_info_instance = ArrayOfSiteInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfSiteInfo.to_json()

# convert the object into a dict
array_of_site_info_dict = array_of_site_info_instance.to_dict()
# create an instance of ArrayOfSiteInfo from a dict
array_of_site_info_form_dict = array_of_site_info.from_dict(array_of_site_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


