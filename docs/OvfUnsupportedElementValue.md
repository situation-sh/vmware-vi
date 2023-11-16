# OvfUnsupportedElementValue

If the Ovf descriptor has an unsupported value of a element in the OVF descriptor.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The unsupported element value  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unsupported_element_value import OvfUnsupportedElementValue

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedElementValue from a JSON string
ovf_unsupported_element_value_instance = OvfUnsupportedElementValue.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedElementValue.to_json()

# convert the object into a dict
ovf_unsupported_element_value_dict = ovf_unsupported_element_value_instance.to_dict()
# create an instance of OvfUnsupportedElementValue from a dict
ovf_unsupported_element_value_form_dict = ovf_unsupported_element_value.from_dict(ovf_unsupported_element_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


