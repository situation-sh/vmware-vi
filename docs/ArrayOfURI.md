# ArrayOfURI

A boxed array of *PrimitiveURI*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[str]** |  | 

## Example

```python
from vmware_vi.models.array_of_uri import ArrayOfURI

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfURI from a JSON string
array_of_uri_instance = ArrayOfURI.from_json(json)
# print the JSON string representation of the object
print ArrayOfURI.to_json()

# convert the object into a dict
array_of_uri_dict = array_of_uri_instance.to_dict()
# create an instance of ArrayOfURI from a dict
array_of_uri_form_dict = array_of_uri.from_dict(array_of_uri_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


