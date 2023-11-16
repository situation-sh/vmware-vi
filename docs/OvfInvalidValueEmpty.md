# OvfInvalidValueEmpty

If an attribute is found with an empty value where it is not allowed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_invalid_value_empty import OvfInvalidValueEmpty

# TODO update the JSON string below
json = "{}"
# create an instance of OvfInvalidValueEmpty from a JSON string
ovf_invalid_value_empty_instance = OvfInvalidValueEmpty.from_json(json)
# print the JSON string representation of the object
print OvfInvalidValueEmpty.to_json()

# convert the object into a dict
ovf_invalid_value_empty_dict = ovf_invalid_value_empty_instance.to_dict()
# create an instance of OvfInvalidValueEmpty from a dict
ovf_invalid_value_empty_form_dict = ovf_invalid_value_empty.from_dict(ovf_invalid_value_empty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


