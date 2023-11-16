# OvfMissingElement

If the Ovf descriptor is missing an Element this exception is thrown.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_missing_element import OvfMissingElement

# TODO update the JSON string below
json = "{}"
# create an instance of OvfMissingElement from a JSON string
ovf_missing_element_instance = OvfMissingElement.from_json(json)
# print the JSON string representation of the object
print OvfMissingElement.to_json()

# convert the object into a dict
ovf_missing_element_dict = ovf_missing_element_instance.to_dict()
# create an instance of OvfMissingElement from a dict
ovf_missing_element_form_dict = ovf_missing_element.from_dict(ovf_missing_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


