# HostNasVolume


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_host** | **str** | The host that runs the NFS/CIFS server.  Clients must plan to use remoteHostNames for both NFS v3 as well as NFS v4.1 because this field remoteHost may be deprecated in future.  | 
**remote_path** | **str** | The remote path of NFS/CIFS mount point.  | 
**user_name** | **str** | In case of CIFS, the user name used while connecting to the server.  ***Since:*** VI API 2.5  | [optional] 
**remote_host_names** | **List[str]** | This field will hold host names (or ip addresses) of all remote hosts configured for the datastore.  In case of NFS v3 it will have one hostname which will be the same value as in remoteHost defined above. In case of NFS v4.1 if the NFS Client detects additional hostnames or ip addresses during its negotiations with the NFS server, those additional host names (connections) will be added to this list after the datastore is created. Addition of hostnames to this list is limited to MDS server host names or the IP addresses. In other words, the Data Server host names IP addresses will not be appended to this list.  ***Since:*** vSphere API 6.0  | [optional] 
**security_type** | **str** | Security type the volume is currently using.  See *HostNasVolumeSecurityType_enum*  ***Since:*** vSphere API 6.0  | [optional] 
**protocol_endpoint** | **bool** | Indicates that this NAS volume is protocol endpoint.  This property will be populated if and only if host supports VirtualVolume based Datastore. Check the host capability *HostCapability.virtualVolumeDatastoreSupported*. See *HostProtocolEndpoint*.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nas_volume import HostNasVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HostNasVolume from a JSON string
host_nas_volume_instance = HostNasVolume.from_json(json)
# print the JSON string representation of the object
print HostNasVolume.to_json()

# convert the object into a dict
host_nas_volume_dict = host_nas_volume_instance.to_dict()
# create an instance of HostNasVolume from a dict
host_nas_volume_form_dict = host_nas_volume.from_dict(host_nas_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


