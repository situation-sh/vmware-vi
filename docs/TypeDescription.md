# TypeDescription

Static strings used for describing an object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Type being described  | 

## Example

```python
from vmware_vi.models.type_description import TypeDescription

# TODO update the JSON string below
json = "{}"
# create an instance of TypeDescription from a JSON string
type_description_instance = TypeDescription.from_json(json)
# print the JSON string representation of the object
print TypeDescription.to_json()

# convert the object into a dict
type_description_dict = type_description_instance.to_dict()
# create an instance of TypeDescription from a dict
type_description_form_dict = type_description.from_dict(type_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


