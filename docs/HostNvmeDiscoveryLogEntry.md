# HostNvmeDiscoveryLogEntry

This data object represents a single entry in the Discovery Log returned by a Discovery controller.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnqn** | **str** | NVME Qualified name of the discovered subsystem.  Corresponds to the SUBNQN field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec.  ***Since:*** vSphere API 7.0  | 
**subsystem_type** | **str** | NVM Subsystem type.  Corresponds to the SUBTYPE field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec. The set of supported values is described in *HostNvmeDiscoveryLogSubsystemType_enum*.  ***Since:*** vSphere API 7.0  | 
**subsystem_port_id** | **int** | NVM subsystem port ID.  Corresponds to the PORTID field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec. For an overview, see: - \&quot;NVM Express over Fabrics 1.0\&quot;, Section 1.5.2,   NVM Subsystem    ***Since:*** vSphere API 7.0  | 
**controller_id** | **int** | NVME Controller ID within the NVM subsystem.  Corresponds to the CNTLID field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec. In the static controller model, this field may be set to a specific controller ID which can be used to connect to that particular controller. It could also be set to 0xFFFE (65534 in decimal), in which case the controller ID will be allocated when a connection is established. In the dynamic controller model, this field shall be set to 0xFFFF (65535 in decimal). Note that this is different from the controllerNumber *HostNvmeController.controllerNumber*, which is the unique identifier of the NVMe controller within the entire host and is allocated only after a connection is established.  ***Since:*** vSphere API 7.0  | 
**admin_queue_max_size** | **int** | The maximum size of the Admin Submission Queue.  Corresponds to the ASQSZ field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec. This applies to all controllers within the NVM Subsystem. When establishing a connection, the value of *HostNvmeConnectSpec.adminQueueSize* may not exceed this value.  ***Since:*** vSphere API 7.0  | 
**transport_parameters** | [**HostNvmeTransportParameters**](HostNvmeTransportParameters.md) |  | 
**transport_requirements** | **str** | The requirements for NVME Transport.  Corresponds to the TREQ field in the Discovery Log Page Entry as specified by the NVME over Fabrics spec The set of possible values is described in *HostNvmeDiscoveryLogTransportRequirements_enum*  ***Since:*** vSphere API 7.0  | 
**connected** | **bool** | Indicates whether the controller represented by this Discovery Log Page Entry is already connected to the adapter through which the discovery is initiated.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.host_nvme_discovery_log_entry import HostNvmeDiscoveryLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeDiscoveryLogEntry from a JSON string
host_nvme_discovery_log_entry_instance = HostNvmeDiscoveryLogEntry.from_json(json)
# print the JSON string representation of the object
print HostNvmeDiscoveryLogEntry.to_json()

# convert the object into a dict
host_nvme_discovery_log_entry_dict = host_nvme_discovery_log_entry_instance.to_dict()
# create an instance of HostNvmeDiscoveryLogEntry from a dict
host_nvme_discovery_log_entry_form_dict = host_nvme_discovery_log_entry.from_dict(host_nvme_discovery_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


