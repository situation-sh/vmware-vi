# ListKmsClustersRequestType

The parameters of *CryptoManagerKmip.ListKmsClusters*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_kms_servers** | **bool** | \\[in\\] Whether to list KMS servers information in the cluster. By default will not include the KMS servers information.  | [optional] 
**management_type_filter** | **int** | \\[in\\] The KMS cluster management type filter. Bit map values: 0x01 - Return VC managed Key Providers registered in the CryptoManager. 0x02 - Return Trusted Key Providers registered in the CryptoManager. 0x04 - Return Trusted Key Providers which are not registered with the CryptoManager. 0x08 - Return Native Key Providers. others - reserved, will be ignored If omitted or -1, then all kinds of Key Providers will be returned.  | [optional] 
**status_filter** | **int** | \\[in\\] The Key Provider status filter. Bit map values: 0x01 - Return active Key Providers. 0x02 - Return inactive Key Providers. others - reserved, will be ignored If omitted or -1, then all status of Key Providers will be returned.  | [optional] 

## Example

```python
from vmware_vi.models.list_kms_clusters_request_type import ListKmsClustersRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListKmsClustersRequestType from a JSON string
list_kms_clusters_request_type_instance = ListKmsClustersRequestType.from_json(json)
# print the JSON string representation of the object
print ListKmsClustersRequestType.to_json()

# convert the object into a dict
list_kms_clusters_request_type_dict = list_kms_clusters_request_type_instance.to_dict()
# create an instance of ListKmsClustersRequestType from a dict
list_kms_clusters_request_type_form_dict = list_kms_clusters_request_type.from_dict(list_kms_clusters_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


