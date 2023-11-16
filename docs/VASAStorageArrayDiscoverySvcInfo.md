# VASAStorageArrayDiscoverySvcInfo

Discovery service information of storage array. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_type** | **str** | Port type, string as defined in *VASAStorageArrayBlockEnum_enum*.  | 
**svc_nqn** | **str** | Well-known NQN of discovery service.  | 
**ip_info** | [**VASAStorageArrayDiscoveryIpTransport**](VASAStorageArrayDiscoveryIpTransport.md) |  | [optional] 
**fc_info** | [**VASAStorageArrayDiscoveryFcTransport**](VASAStorageArrayDiscoveryFcTransport.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vasa_storage_array_discovery_svc_info import VASAStorageArrayDiscoverySvcInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VASAStorageArrayDiscoverySvcInfo from a JSON string
vasa_storage_array_discovery_svc_info_instance = VASAStorageArrayDiscoverySvcInfo.from_json(json)
# print the JSON string representation of the object
print VASAStorageArrayDiscoverySvcInfo.to_json()

# convert the object into a dict
vasa_storage_array_discovery_svc_info_dict = vasa_storage_array_discovery_svc_info_instance.to_dict()
# create an instance of VASAStorageArrayDiscoverySvcInfo from a dict
vasa_storage_array_discovery_svc_info_form_dict = vasa_storage_array_discovery_svc_info.from_dict(vasa_storage_array_discovery_svc_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


