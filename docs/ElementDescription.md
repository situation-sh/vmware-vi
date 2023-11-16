# ElementDescription

Static strings used for describing an object model string or enumeration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Enumeration or literal ID being described.  | 

## Example

```python
from vmware_vi.models.element_description import ElementDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ElementDescription from a JSON string
element_description_instance = ElementDescription.from_json(json)
# print the JSON string representation of the object
print ElementDescription.to_json()

# convert the object into a dict
element_description_dict = element_description_instance.to_dict()
# create an instance of ElementDescription from a dict
element_description_form_dict = element_description.from_dict(element_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


