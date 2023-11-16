# HostNvmeTopology

This data object type describes the NVME topology information.  The data objects in this data object type model the NVME storage objects from a topological point of view. The NVME topological view organizes objects by NVME interface, which contains connected controllers, which in turn contain attached namespaces.  Only storage adapters which support the NVME protocol will be represented as NVME interfaces in this data object. In particular, an NVME interface will be created for each NVME over Fabrics adapter in the system.  Note that it is possible for an adapter to be represented by both an NVME interface in the NVME topology and a SCSI interface in the SCSI topology. This can happen when an adapter supporting the NVME protocol is also presented as a SCSI adapter and SCSI to NVME translation is performed.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter** | [**List[HostNvmeTopologyInterface]**](HostNvmeTopologyInterface.md) | The list of NVME interfaces (could be empty).  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nvme_topology import HostNvmeTopology

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeTopology from a JSON string
host_nvme_topology_instance = HostNvmeTopology.from_json(json)
# print the JSON string representation of the object
print HostNvmeTopology.to_json()

# convert the object into a dict
host_nvme_topology_dict = host_nvme_topology_instance.to_dict()
# create an instance of HostNvmeTopology from a dict
host_nvme_topology_form_dict = host_nvme_topology.from_dict(host_nvme_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


