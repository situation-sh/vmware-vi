# ArrayOfOvfPropertyType

A boxed array of *OvfPropertyType*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfPropertyType]**](OvfPropertyType.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_property_type import ArrayOfOvfPropertyType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfPropertyType from a JSON string
array_of_ovf_property_type_instance = ArrayOfOvfPropertyType.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfPropertyType.to_json()

# convert the object into a dict
array_of_ovf_property_type_dict = array_of_ovf_property_type_instance.to_dict()
# create an instance of ArrayOfOvfPropertyType from a dict
array_of_ovf_property_type_form_dict = array_of_ovf_property_type.from_dict(array_of_ovf_property_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


