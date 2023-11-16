# ArrayOfDiskCryptoSpec

A boxed array of *DiskCryptoSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DiskCryptoSpec]**](DiskCryptoSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_disk_crypto_spec import ArrayOfDiskCryptoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDiskCryptoSpec from a JSON string
array_of_disk_crypto_spec_instance = ArrayOfDiskCryptoSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfDiskCryptoSpec.to_json()

# convert the object into a dict
array_of_disk_crypto_spec_dict = array_of_disk_crypto_spec_instance.to_dict()
# create an instance of ArrayOfDiskCryptoSpec from a dict
array_of_disk_crypto_spec_form_dict = array_of_disk_crypto_spec.from_dict(array_of_disk_crypto_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


