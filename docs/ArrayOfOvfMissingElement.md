# ArrayOfOvfMissingElement

A boxed array of *OvfMissingElement*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfMissingElement]**](OvfMissingElement.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_missing_element import ArrayOfOvfMissingElement

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfMissingElement from a JSON string
array_of_ovf_missing_element_instance = ArrayOfOvfMissingElement.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfMissingElement.to_json()

# convert the object into a dict
array_of_ovf_missing_element_dict = array_of_ovf_missing_element_instance.to_dict()
# create an instance of ArrayOfOvfMissingElement from a dict
array_of_ovf_missing_element_form_dict = array_of_ovf_missing_element.from_dict(array_of_ovf_missing_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


