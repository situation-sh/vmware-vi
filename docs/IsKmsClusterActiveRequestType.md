# IsKmsClusterActiveRequestType

The parameters of *CryptoManagerKmip.IsKmsClusterActive*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KeyProviderId**](KeyProviderId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.is_kms_cluster_active_request_type import IsKmsClusterActiveRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of IsKmsClusterActiveRequestType from a JSON string
is_kms_cluster_active_request_type_instance = IsKmsClusterActiveRequestType.from_json(json)
# print the JSON string representation of the object
print IsKmsClusterActiveRequestType.to_json()

# convert the object into a dict
is_kms_cluster_active_request_type_dict = is_kms_cluster_active_request_type_instance.to_dict()
# create an instance of IsKmsClusterActiveRequestType from a dict
is_kms_cluster_active_request_type_form_dict = is_kms_cluster_active_request_type.from_dict(is_kms_cluster_active_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


