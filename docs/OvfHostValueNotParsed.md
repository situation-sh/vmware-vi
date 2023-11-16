# OvfHostValueNotParsed


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | The host property field that could not be parsed.  ***Since:*** vSphere API 4.0  | 
**value** | **str** | Value of the field that could not be parsed.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_host_value_not_parsed import OvfHostValueNotParsed

# TODO update the JSON string below
json = "{}"
# create an instance of OvfHostValueNotParsed from a JSON string
ovf_host_value_not_parsed_instance = OvfHostValueNotParsed.from_json(json)
# print the JSON string representation of the object
print OvfHostValueNotParsed.to_json()

# convert the object into a dict
ovf_host_value_not_parsed_dict = ovf_host_value_not_parsed_instance.to_dict()
# create an instance of OvfHostValueNotParsed from a dict
ovf_host_value_not_parsed_form_dict = ovf_host_value_not_parsed.from_dict(ovf_host_value_not_parsed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


