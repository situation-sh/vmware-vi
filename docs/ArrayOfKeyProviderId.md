# ArrayOfKeyProviderId

A boxed array of *KeyProviderId*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[KeyProviderId]**](KeyProviderId.md) |  | 

## Example

```python
from vmware_vi.models.array_of_key_provider_id import ArrayOfKeyProviderId

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfKeyProviderId from a JSON string
array_of_key_provider_id_instance = ArrayOfKeyProviderId.from_json(json)
# print the JSON string representation of the object
print ArrayOfKeyProviderId.to_json()

# convert the object into a dict
array_of_key_provider_id_dict = array_of_key_provider_id_instance.to_dict()
# create an instance of ArrayOfKeyProviderId from a dict
array_of_key_provider_id_form_dict = array_of_key_provider_id.from_dict(array_of_key_provider_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


