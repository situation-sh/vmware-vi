# DiskCryptoSpec

This data object type contains the crypto information of all disks along the chain  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | [**DiskCryptoSpec**](DiskCryptoSpec.md) |  | [optional] 
**crypto** | [**CryptoSpec**](CryptoSpec.md) |  | 

## Example

```python
from vmware_vi.models.disk_crypto_spec import DiskCryptoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DiskCryptoSpec from a JSON string
disk_crypto_spec_instance = DiskCryptoSpec.from_json(json)
# print the JSON string representation of the object
print DiskCryptoSpec.to_json()

# convert the object into a dict
disk_crypto_spec_dict = disk_crypto_spec_instance.to_dict()
# create an instance of DiskCryptoSpec from a dict
disk_crypto_spec_form_dict = disk_crypto_spec.from_dict(disk_crypto_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


