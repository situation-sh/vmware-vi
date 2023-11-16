# GetDefaultKmsClusterRequestType

The parameters of *CryptoManagerKmip.GetDefaultKmsCluster*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**defaults_to_parent** | **bool** | \\[in\\] (Optional, default &#x3D; false) If set to true, then get the default kms cluster follow the entity hierarchy. That means if the entity has no default kms cluster, then try to get from its parent.  | [optional] 

## Example

```python
from vmware_vi.models.get_default_kms_cluster_request_type import GetDefaultKmsClusterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GetDefaultKmsClusterRequestType from a JSON string
get_default_kms_cluster_request_type_instance = GetDefaultKmsClusterRequestType.from_json(json)
# print the JSON string representation of the object
print GetDefaultKmsClusterRequestType.to_json()

# convert the object into a dict
get_default_kms_cluster_request_type_dict = get_default_kms_cluster_request_type_instance.to_dict()
# create an instance of GetDefaultKmsClusterRequestType from a dict
get_default_kms_cluster_request_type_form_dict = get_default_kms_cluster_request_type.from_dict(get_default_kms_cluster_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


