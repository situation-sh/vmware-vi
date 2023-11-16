# KmipClusterInfo

Data Object representing a cluster of KMIP servers.  All servers in a cluster must provide the same keys.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | 
**servers** | [**List[KmipServerInfo]**](KmipServerInfo.md) | Servers in this cluster.  ***Since:*** vSphere API 6.5  | [optional] 
**use_as_default** | **bool** | Use this cluster as default for system wide, when the optional CryptoKeyId.providerId is not set.  ***Since:*** vSphere API 6.5  | 
**management_type** | **str** | Key provider management type.  See *KmipClusterInfoKmsManagementType_enum* for valid values.  ***Since:*** vSphere API 7.0  | [optional] 
**use_as_entity_default** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Use this cluster as default for the managed entities, when the optional CryptoKeyId.providerId is not set.  See *CryptoManagerKmip.SetDefaultKmsCluster* for supported managed entity type.  ***Since:*** vSphere API 7.0  Refers instances of *ManagedEntity*.  | [optional] 
**has_backup** | **bool** |  | [optional] 
**tpm_required** | **bool** |  | [optional] 
**key_id** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.kmip_cluster_info import KmipClusterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KmipClusterInfo from a JSON string
kmip_cluster_info_instance = KmipClusterInfo.from_json(json)
# print the JSON string representation of the object
print KmipClusterInfo.to_json()

# convert the object into a dict
kmip_cluster_info_dict = kmip_cluster_info_instance.to_dict()
# create an instance of KmipClusterInfo from a dict
kmip_cluster_info_form_dict = kmip_cluster_info.from_dict(kmip_cluster_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


