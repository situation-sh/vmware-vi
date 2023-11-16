# ArrayOfOvfPropertyQualifier

A boxed array of *OvfPropertyQualifier*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfPropertyQualifier]**](OvfPropertyQualifier.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_property_qualifier import ArrayOfOvfPropertyQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfPropertyQualifier from a JSON string
array_of_ovf_property_qualifier_instance = ArrayOfOvfPropertyQualifier.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfPropertyQualifier.to_json()

# convert the object into a dict
array_of_ovf_property_qualifier_dict = array_of_ovf_property_qualifier_instance.to_dict()
# create an instance of ArrayOfOvfPropertyQualifier from a dict
array_of_ovf_property_qualifier_form_dict = array_of_ovf_property_qualifier.from_dict(array_of_ovf_property_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


