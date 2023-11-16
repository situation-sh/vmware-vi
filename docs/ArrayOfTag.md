# ArrayOfTag

A boxed array of *Tag*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Tag]**](Tag.md) |  | 

## Example

```python
from vmware_vi.models.array_of_tag import ArrayOfTag

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTag from a JSON string
array_of_tag_instance = ArrayOfTag.from_json(json)
# print the JSON string representation of the object
print ArrayOfTag.to_json()

# convert the object into a dict
array_of_tag_dict = array_of_tag_instance.to_dict()
# create an instance of ArrayOfTag from a dict
array_of_tag_form_dict = array_of_tag.from_dict(array_of_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


