# ArrayOfObjectContent

A boxed array of *ObjectContent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ObjectContent]**](ObjectContent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_object_content import ArrayOfObjectContent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfObjectContent from a JSON string
array_of_object_content_instance = ArrayOfObjectContent.from_json(json)
# print the JSON string representation of the object
print ArrayOfObjectContent.to_json()

# convert the object into a dict
array_of_object_content_dict = array_of_object_content_instance.to_dict()
# create an instance of ArrayOfObjectContent from a dict
array_of_object_content_form_dict = array_of_object_content.from_dict(array_of_object_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


