# ArrayOfOvfUnexpectedElement

A boxed array of *OvfUnexpectedElement*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfUnexpectedElement]**](OvfUnexpectedElement.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_unexpected_element import ArrayOfOvfUnexpectedElement

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfUnexpectedElement from a JSON string
array_of_ovf_unexpected_element_instance = ArrayOfOvfUnexpectedElement.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfUnexpectedElement.to_json()

# convert the object into a dict
array_of_ovf_unexpected_element_dict = array_of_ovf_unexpected_element_instance.to_dict()
# create an instance of ArrayOfOvfUnexpectedElement from a dict
array_of_ovf_unexpected_element_form_dict = array_of_ovf_unexpected_element.from_dict(array_of_ovf_unexpected_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


