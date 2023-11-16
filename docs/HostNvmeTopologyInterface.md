# HostNvmeTopologyInterface

This data object describes the NVME interface that is associated with a list of connected NVME controllers.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier for the NVME interface.  ***Since:*** vSphere API 7.0  | 
**adapter** | [**HostHostBusAdapter**](HostHostBusAdapter.md) |  | 
**connected_controller** | [**List[HostNvmeController]**](HostNvmeController.md) | The list of connected NVME controllers.  This list can be empty if am NVME interface is not connected to any controllers. Each NvmeController object contains a list of its attached NVME namespaces in *HostNvmeController.attachedNamespace*.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nvme_topology_interface import HostNvmeTopologyInterface

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeTopologyInterface from a JSON string
host_nvme_topology_interface_instance = HostNvmeTopologyInterface.from_json(json)
# print the JSON string representation of the object
print HostNvmeTopologyInterface.to_json()

# convert the object into a dict
host_nvme_topology_interface_dict = host_nvme_topology_interface_instance.to_dict()
# create an instance of HostNvmeTopologyInterface from a dict
host_nvme_topology_interface_form_dict = host_nvme_topology_interface.from_dict(host_nvme_topology_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


