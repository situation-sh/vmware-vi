# ClusterCryptoConfigInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_mode** | **str** | The cluster encrypton mode.  See *ClusterCryptoConfigInfoCryptoMode_enum* for supported values.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_crypto_config_info import ClusterCryptoConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCryptoConfigInfo from a JSON string
cluster_crypto_config_info_instance = ClusterCryptoConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterCryptoConfigInfo.to_json()

# convert the object into a dict
cluster_crypto_config_info_dict = cluster_crypto_config_info_instance.to_dict()
# create an instance of ClusterCryptoConfigInfo from a dict
cluster_crypto_config_info_form_dict = cluster_crypto_config_info.from_dict(cluster_crypto_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


