# OvfInvalidValueReference

If a value refer to something that is not found is found in the Ovf descriptor we throw an OvfInvalidValueReference exception.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_invalid_value_reference import OvfInvalidValueReference

# TODO update the JSON string below
json = "{}"
# create an instance of OvfInvalidValueReference from a JSON string
ovf_invalid_value_reference_instance = OvfInvalidValueReference.from_json(json)
# print the JSON string representation of the object
print OvfInvalidValueReference.to_json()

# convert the object into a dict
ovf_invalid_value_reference_dict = ovf_invalid_value_reference_instance.to_dict()
# create an instance of OvfInvalidValueReference from a dict
ovf_invalid_value_reference_form_dict = ovf_invalid_value_reference.from_dict(ovf_invalid_value_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


