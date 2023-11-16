# ArrayOfOvfMissingAttribute

A boxed array of *OvfMissingAttribute*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfMissingAttribute]**](OvfMissingAttribute.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_missing_attribute import ArrayOfOvfMissingAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfMissingAttribute from a JSON string
array_of_ovf_missing_attribute_instance = ArrayOfOvfMissingAttribute.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfMissingAttribute.to_json()

# convert the object into a dict
array_of_ovf_missing_attribute_dict = array_of_ovf_missing_attribute_instance.to_dict()
# create an instance of ArrayOfOvfMissingAttribute from a dict
array_of_ovf_missing_attribute_form_dict = array_of_ovf_missing_attribute.from_dict(array_of_ovf_missing_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


