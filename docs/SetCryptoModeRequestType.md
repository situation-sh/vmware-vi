# SetCryptoModeRequestType

The parameters of *ClusterComputeResource.SetCryptoMode*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_mode** | **str** | The encryption mode for the cluster. See *ClusterCryptoConfigInfoCryptoMode_enum* for supported values.  | 

## Example

```python
from vmware_vi.models.set_crypto_mode_request_type import SetCryptoModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetCryptoModeRequestType from a JSON string
set_crypto_mode_request_type_instance = SetCryptoModeRequestType.from_json(json)
# print the JSON string representation of the object
print SetCryptoModeRequestType.to_json()

# convert the object into a dict
set_crypto_mode_request_type_dict = set_crypto_mode_request_type_instance.to_dict()
# create an instance of SetCryptoModeRequestType from a dict
set_crypto_mode_request_type_form_dict = set_crypto_mode_request_type.from_dict(set_crypto_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


