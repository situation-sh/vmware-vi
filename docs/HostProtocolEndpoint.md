# HostProtocolEndpoint

ProtocolEndpoint is configured LUN or NFS directory This is used for io path to actual virtual disks (VVols)  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pe_type** | **str** | Deprecated from all vmodl version above @released(\&quot;6.0\&quot;) Use type instead.  Type of ProtocolEndpoint See *HostProtocolEndpointPEType_enum*  ***Since:*** vSphere API 6.0  | 
**type** | **str** | Type of ProtocolEndpoint See *HostProtocolEndpointProtocolEndpointType_enum*  ***Since:*** vSphere API 6.5  | [optional] 
**uuid** | **str** | Identifier for PE assigned by VASA Provider  ***Since:*** vSphere API 6.0  | 
**host_key** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Set of ESX hosts which can see the same PE  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | [optional] 
**storage_array** | **str** | Associated Storage Array  ***Since:*** vSphere API 6.0  | [optional] 
**nfs_server** | **str** | NFSv3 and NFSv4x PE will contain information about NFS Server For NFSv4x this field may contain comma separated list of IP addresses which are associated with the NFS Server  ***Since:*** vSphere API 6.0  | [optional] 
**nfs_dir** | **str** | NFSv3 and NFSv4x PE will contain information about NFS directory  ***Since:*** vSphere API 6.0  | [optional] 
**nfs_server_scope** | **str** | NFSv4x PE will contain information about NFSv4x Server Scope  ***Since:*** vSphere API 6.5  | [optional] 
**nfs_server_major** | **str** | NFSv4x PE will contain information about NFSv4x Server Major  ***Since:*** vSphere API 6.5  | [optional] 
**nfs_server_auth_type** | **str** | NFSv4x PE will contain information about NFSv4x Server Auth-type  ***Since:*** vSphere API 6.5  | [optional] 
**nfs_server_user** | **str** | NFSv4x PE will contain information about NFSv4x Server User  ***Since:*** vSphere API 6.5  | [optional] 
**device_id** | **str** | SCSI PE will contain information about SCSI device ID  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_protocol_endpoint import HostProtocolEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of HostProtocolEndpoint from a JSON string
host_protocol_endpoint_instance = HostProtocolEndpoint.from_json(json)
# print the JSON string representation of the object
print HostProtocolEndpoint.to_json()

# convert the object into a dict
host_protocol_endpoint_dict = host_protocol_endpoint_instance.to_dict()
# create an instance of HostProtocolEndpoint from a dict
host_protocol_endpoint_form_dict = host_protocol_endpoint.from_dict(host_protocol_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


