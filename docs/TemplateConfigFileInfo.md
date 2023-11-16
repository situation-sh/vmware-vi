# TemplateConfigFileInfo

This data object type describes a template virtual machine configuration file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.template_config_file_info import TemplateConfigFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateConfigFileInfo from a JSON string
template_config_file_info_instance = TemplateConfigFileInfo.from_json(json)
# print the JSON string representation of the object
print TemplateConfigFileInfo.to_json()

# convert the object into a dict
template_config_file_info_dict = template_config_file_info_instance.to_dict()
# create an instance of TemplateConfigFileInfo from a dict
template_config_file_info_form_dict = template_config_file_info.from_dict(template_config_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


