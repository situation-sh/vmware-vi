# RegisterKmsClusterRequestType

The parameters of *CryptoManagerKmip.RegisterKmsCluster*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | 
**management_type** | **str** | \\[in\\] Key provider management type See *KmipClusterInfoKmsManagementType_enum* for valid values. By default trustAuthority.  | [optional] 

## Example

```python
from vmware_vi.models.register_kms_cluster_request_type import RegisterKmsClusterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterKmsClusterRequestType from a JSON string
register_kms_cluster_request_type_instance = RegisterKmsClusterRequestType.from_json(json)
# print the JSON string representation of the object
print RegisterKmsClusterRequestType.to_json()

# convert the object into a dict
register_kms_cluster_request_type_dict = register_kms_cluster_request_type_instance.to_dict()
# create an instance of RegisterKmsClusterRequestType from a dict
register_kms_cluster_request_type_form_dict = register_kms_cluster_request_type.from_dict(register_kms_cluster_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


