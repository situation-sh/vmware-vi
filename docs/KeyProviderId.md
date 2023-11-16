# KeyProviderId

Data Object representing a crypto key provider's unique identifier.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Globally unique ID for the crypto key provider.  Servers with the same ID must provide the same keys. Cannot be empty.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.key_provider_id import KeyProviderId

# TODO update the JSON string below
json = "{}"
# create an instance of KeyProviderId from a JSON string
key_provider_id_instance = KeyProviderId.from_json(json)
# print the JSON string representation of the object
print KeyProviderId.to_json()

# convert the object into a dict
key_provider_id_dict = key_provider_id_instance.to_dict()
# create an instance of KeyProviderId from a dict
key_provider_id_form_dict = key_provider_id.from_dict(key_provider_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


