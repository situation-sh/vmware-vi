# ArrayOfRetrieveOptions

A boxed array of *RetrieveOptions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RetrieveOptions]**](RetrieveOptions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_retrieve_options import ArrayOfRetrieveOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRetrieveOptions from a JSON string
array_of_retrieve_options_instance = ArrayOfRetrieveOptions.from_json(json)
# print the JSON string representation of the object
print ArrayOfRetrieveOptions.to_json()

# convert the object into a dict
array_of_retrieve_options_dict = array_of_retrieve_options_instance.to_dict()
# create an instance of ArrayOfRetrieveOptions from a dict
array_of_retrieve_options_form_dict = array_of_retrieve_options.from_dict(array_of_retrieve_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


