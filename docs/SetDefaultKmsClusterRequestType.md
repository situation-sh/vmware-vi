# SetDefaultKmsClusterRequestType

The parameters of *CryptoManagerKmip.SetDefaultKmsCluster*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.set_default_kms_cluster_request_type import SetDefaultKmsClusterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetDefaultKmsClusterRequestType from a JSON string
set_default_kms_cluster_request_type_instance = SetDefaultKmsClusterRequestType.from_json(json)
# print the JSON string representation of the object
print SetDefaultKmsClusterRequestType.to_json()

# convert the object into a dict
set_default_kms_cluster_request_type_dict = set_default_kms_cluster_request_type_instance.to_dict()
# create an instance of SetDefaultKmsClusterRequestType from a dict
set_default_kms_cluster_request_type_form_dict = set_default_kms_cluster_request_type.from_dict(set_default_kms_cluster_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


