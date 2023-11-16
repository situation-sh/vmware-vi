# ArrayOfOvfAttribute

A boxed array of *OvfAttribute*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfAttribute]**](OvfAttribute.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_attribute import ArrayOfOvfAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfAttribute from a JSON string
array_of_ovf_attribute_instance = ArrayOfOvfAttribute.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfAttribute.to_json()

# convert the object into a dict
array_of_ovf_attribute_dict = array_of_ovf_attribute_instance.to_dict()
# create an instance of ArrayOfOvfAttribute from a dict
array_of_ovf_attribute_form_dict = array_of_ovf_attribute.from_dict(array_of_ovf_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


