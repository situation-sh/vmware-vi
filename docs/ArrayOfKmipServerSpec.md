# ArrayOfKmipServerSpec

A boxed array of *KmipServerSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[KmipServerSpec]**](KmipServerSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_kmip_server_spec import ArrayOfKmipServerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfKmipServerSpec from a JSON string
array_of_kmip_server_spec_instance = ArrayOfKmipServerSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfKmipServerSpec.to_json()

# convert the object into a dict
array_of_kmip_server_spec_dict = array_of_kmip_server_spec_instance.to_dict()
# create an instance of ArrayOfKmipServerSpec from a dict
array_of_kmip_server_spec_form_dict = array_of_kmip_server_spec.from_dict(array_of_kmip_server_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


