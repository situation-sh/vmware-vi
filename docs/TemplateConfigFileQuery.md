# TemplateConfigFileQuery

This data object type describes the query specification for a template virtual machine configuration file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.template_config_file_query import TemplateConfigFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateConfigFileQuery from a JSON string
template_config_file_query_instance = TemplateConfigFileQuery.from_json(json)
# print the JSON string representation of the object
print TemplateConfigFileQuery.to_json()

# convert the object into a dict
template_config_file_query_dict = template_config_file_query_instance.to_dict()
# create an instance of TemplateConfigFileQuery from a dict
template_config_file_query_form_dict = template_config_file_query.from_dict(template_config_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


