# ArrayOfExtension

A boxed array of *Extension*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Extension]**](Extension.md) |  | 

## Example

```python
from vmware_vi.models.array_of_extension import ArrayOfExtension

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtension from a JSON string
array_of_extension_instance = ArrayOfExtension.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtension.to_json()

# convert the object into a dict
array_of_extension_dict = array_of_extension_instance.to_dict()
# create an instance of ArrayOfExtension from a dict
array_of_extension_form_dict = array_of_extension.from_dict(array_of_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


