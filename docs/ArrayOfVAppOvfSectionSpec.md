# ArrayOfVAppOvfSectionSpec

A boxed array of *VAppOvfSectionSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppOvfSectionSpec]**](VAppOvfSectionSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_ovf_section_spec import ArrayOfVAppOvfSectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppOvfSectionSpec from a JSON string
array_of_v_app_ovf_section_spec_instance = ArrayOfVAppOvfSectionSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppOvfSectionSpec.to_json()

# convert the object into a dict
array_of_v_app_ovf_section_spec_dict = array_of_v_app_ovf_section_spec_instance.to_dict()
# create an instance of ArrayOfVAppOvfSectionSpec from a dict
array_of_v_app_ovf_section_spec_form_dict = array_of_v_app_ovf_section_spec.from_dict(array_of_v_app_ovf_section_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


