# ReplicationConfigSpec

The ReplicationConfigSpec object type encapsulates the replication configuration parameters for a virtual machine.  It consists of two parts: 1) a set of virtual machine-wide replication properties; 2) a set of properties per replicated virtual disk. ReplicationSetting is passed as an argument for initial replication configuration (@see vim.HbrManager#enableReplication) as well as for re-configuration of a replicated VM's properties (@see vim.HbrManager#reconfigureReplication).  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation** | **int** | A generation number (&amp;gt;&#x3D;0) that reflects the \&quot;freshness\&quot; of the ReplicationConfigSpec on which a re-configuration is based.  The generation number is used to detect and disallow concurrent updates to a VM&#39;s replication settings. For initial replication enablement, generation &#x3D; 0. The replication settings of every replication re-configuration operation must reflect the latest generation number known to the caller. It takes an explicit call to get the latest replication settings to find out what the latest generation number is. The update algorithm of the generation number is opaque to the caller; e.g., the caller cannot assume that the generation numbers are incremented by one every time replication is (re)configured, not even that they are changing monotonically.  ***Since:*** vSphere API 5.0  | 
**vm_replication_id** | **str** | An opaque identifier that uniquely identifies a replicated VM between primary and secondary sites.  ***Since:*** vSphere API 5.0  | 
**destination** | **str** | The IP address of the HBR Server in the secondary site where this VM is replicated to.  Note: If net encryption is enabled, this is the address of the encryption tunnelling agent.  ***Since:*** vSphere API 5.0  | 
**port** | **int** | The port on the HBR Server in the secondary site where this VM is replicated to.  Note: If net encryption is enabled, this is the port of the encryption tunneling agent.  ***Since:*** vSphere API 5.0  | 
**rpo** | **int** | The Recovery Point Objective specified for this VM, in minutes.  Currently, valid values are in the range of 1 minute to 1440 minutes (24 hours).  ***Since:*** vSphere API 5.0  | 
**quiesce_guest_enabled** | **bool** | Flag that indicates whether or not to quiesce the file system or applications in the guest OS before a consistent replica is created.  ***Since:*** vSphere API 5.0  | 
**paused** | **bool** | Flag that indicates whether or not the vm or group has been paused for replication.  ***Since:*** vSphere API 5.0  | 
**opp_updates_enabled** | **bool** | Flag that indicates whether or not to perform opportunistic updates in-between consistent replicas.  ***Since:*** vSphere API 5.0  | 
**net_compression_enabled** | **bool** | Flag that indicates whether or not compression should be used when sending traffic over the network.  The primary will negotiate the best compression with the server on the secondary if this is enabled.  ***Since:*** vSphere API 6.0  | [optional] 
**net_encryption_enabled** | **bool** | Flag that indicates whether or not encription should be used when sending traffic over the network.  The primary will use the remoteCertificateThumbprint to verify the identity of the remote server.  ***Since:*** vSphere API 6.7  | [optional] 
**encryption_destination** | **str** | The IP address of the remote HBR server, target for encrypted LWD.  This field is required when net encryption is enabled, ignored otherwise.  ***Since:*** vSphere API 6.7  | [optional] 
**encryption_port** | **int** | The port on the remote HBR server, target for encrypted LWD.  This field is only relevant when net encryption is enabled.  ***Since:*** vSphere API 6.7  | [optional] 
**remote_certificate_thumbprint** | **str** | The SHA256 thumbprint of the remote server certificate.  This field is only relevant when net encription is enabled.  ***Since:*** vSphere API 6.7  | [optional] 
**data_sets_replication_enabled** | **bool** | Flag that indicates whether DataSets files are replicated or not.  | [optional] 
**disk** | [**List[ReplicationInfoDiskSettings]**](ReplicationInfoDiskSettings.md) | The set of the disks of this VM that are configured for replication.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.replication_config_spec import ReplicationConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationConfigSpec from a JSON string
replication_config_spec_instance = ReplicationConfigSpec.from_json(json)
# print the JSON string representation of the object
print ReplicationConfigSpec.to_json()

# convert the object into a dict
replication_config_spec_dict = replication_config_spec_instance.to_dict()
# create an instance of ReplicationConfigSpec from a dict
replication_config_spec_form_dict = replication_config_spec.from_dict(replication_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


