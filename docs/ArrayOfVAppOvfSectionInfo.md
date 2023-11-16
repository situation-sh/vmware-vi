# ArrayOfVAppOvfSectionInfo

A boxed array of *VAppOvfSectionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppOvfSectionInfo]**](VAppOvfSectionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_ovf_section_info import ArrayOfVAppOvfSectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppOvfSectionInfo from a JSON string
array_of_v_app_ovf_section_info_instance = ArrayOfVAppOvfSectionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppOvfSectionInfo.to_json()

# convert the object into a dict
array_of_v_app_ovf_section_info_dict = array_of_v_app_ovf_section_info_instance.to_dict()
# create an instance of ArrayOfVAppOvfSectionInfo from a dict
array_of_v_app_ovf_section_info_form_dict = array_of_v_app_ovf_section_info.from_dict(array_of_v_app_ovf_section_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


