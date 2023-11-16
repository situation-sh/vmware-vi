# OvfInvalidValue

If an invalid value is found in the Ovf descriptor we throw an OvfInvalidValue exception.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Attribute value  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_invalid_value import OvfInvalidValue

# TODO update the JSON string below
json = "{}"
# create an instance of OvfInvalidValue from a JSON string
ovf_invalid_value_instance = OvfInvalidValue.from_json(json)
# print the JSON string representation of the object
print OvfInvalidValue.to_json()

# convert the object into a dict
ovf_invalid_value_dict = ovf_invalid_value_instance.to_dict()
# create an instance of OvfInvalidValue from a dict
ovf_invalid_value_form_dict = ovf_invalid_value.from_dict(ovf_invalid_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


