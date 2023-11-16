# VslmTagEntry

Specification of the Tag-Association tuple of Dataservice Tagging package.  This class is a subset of the class dataservice.taggging.TaggingEntry.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_name** | **str** | Associated tag name of the Tag-Association tuple  ***Since:*** vSphere API 6.5  | 
**parent_category_name** | **str** | Associated parent category name of the Tag-Association tuple  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.vslm_tag_entry import VslmTagEntry

# TODO update the JSON string below
json = "{}"
# create an instance of VslmTagEntry from a JSON string
vslm_tag_entry_instance = VslmTagEntry.from_json(json)
# print the JSON string representation of the object
print VslmTagEntry.to_json()

# convert the object into a dict
vslm_tag_entry_dict = vslm_tag_entry_instance.to_dict()
# create an instance of VslmTagEntry from a dict
vslm_tag_entry_form_dict = vslm_tag_entry.from_dict(vslm_tag_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


