# OvfInvalidValueFormatMalformed

If an malformed value is found in the Ovf descriptor we throw an OvfInvalidValueFormatMalformed exception.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_invalid_value_format_malformed import OvfInvalidValueFormatMalformed

# TODO update the JSON string below
json = "{}"
# create an instance of OvfInvalidValueFormatMalformed from a JSON string
ovf_invalid_value_format_malformed_instance = OvfInvalidValueFormatMalformed.from_json(json)
# print the JSON string representation of the object
print OvfInvalidValueFormatMalformed.to_json()

# convert the object into a dict
ovf_invalid_value_format_malformed_dict = ovf_invalid_value_format_malformed_instance.to_dict()
# create an instance of OvfInvalidValueFormatMalformed from a dict
ovf_invalid_value_format_malformed_form_dict = ovf_invalid_value_format_malformed.from_dict(ovf_invalid_value_format_malformed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


