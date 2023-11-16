# UnregisterKmsClusterRequestType

The parameters of *CryptoManagerKmip.UnregisterKmsCluster*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | 

## Example

```python
from vmware_vi.models.unregister_kms_cluster_request_type import UnregisterKmsClusterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterKmsClusterRequestType from a JSON string
unregister_kms_cluster_request_type_instance = UnregisterKmsClusterRequestType.from_json(json)
# print the JSON string representation of the object
print UnregisterKmsClusterRequestType.to_json()

# convert the object into a dict
unregister_kms_cluster_request_type_dict = unregister_kms_cluster_request_type_instance.to_dict()
# create an instance of UnregisterKmsClusterRequestType from a dict
unregister_kms_cluster_request_type_form_dict = unregister_kms_cluster_request_type.from_dict(unregister_kms_cluster_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


