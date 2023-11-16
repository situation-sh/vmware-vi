# OvfMissingAttribute

If the Ovf descriptor is missing an attribute this exception is thrown.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_missing_attribute import OvfMissingAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of OvfMissingAttribute from a JSON string
ovf_missing_attribute_instance = OvfMissingAttribute.from_json(json)
# print the JSON string representation of the object
print OvfMissingAttribute.to_json()

# convert the object into a dict
ovf_missing_attribute_dict = ovf_missing_attribute_instance.to_dict()
# create an instance of OvfMissingAttribute from a dict
ovf_missing_attribute_form_dict = ovf_missing_attribute.from_dict(ovf_missing_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


