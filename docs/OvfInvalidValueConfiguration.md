# OvfInvalidValueConfiguration

If an malformed ovf:configuration attribute value is found in the Ovf descriptor we throw an OvfInvalidValueConfiguration exception.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_invalid_value_configuration import OvfInvalidValueConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of OvfInvalidValueConfiguration from a JSON string
ovf_invalid_value_configuration_instance = OvfInvalidValueConfiguration.from_json(json)
# print the JSON string representation of the object
print OvfInvalidValueConfiguration.to_json()

# convert the object into a dict
ovf_invalid_value_configuration_dict = ovf_invalid_value_configuration_instance.to_dict()
# create an instance of OvfInvalidValueConfiguration from a dict
ovf_invalid_value_configuration_form_dict = ovf_invalid_value_configuration.from_dict(ovf_invalid_value_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


