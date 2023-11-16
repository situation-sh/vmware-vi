# ArrayOfEncryptionKeyRequired

A boxed array of *EncryptionKeyRequired*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EncryptionKeyRequired]**](EncryptionKeyRequired.md) |  | 

## Example

```python
from vmware_vi.models.array_of_encryption_key_required import ArrayOfEncryptionKeyRequired

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEncryptionKeyRequired from a JSON string
array_of_encryption_key_required_instance = ArrayOfEncryptionKeyRequired.from_json(json)
# print the JSON string representation of the object
print ArrayOfEncryptionKeyRequired.to_json()

# convert the object into a dict
array_of_encryption_key_required_dict = array_of_encryption_key_required_instance.to_dict()
# create an instance of ArrayOfEncryptionKeyRequired from a dict
array_of_encryption_key_required_form_dict = array_of_encryption_key_required.from_dict(array_of_encryption_key_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


