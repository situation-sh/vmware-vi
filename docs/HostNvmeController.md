# HostNvmeController

This data object represents an NVME controller.  Some terminology is borrowed from the NVM Express over Fabrics and the NVM Express 1.3 specifications, which are available at the following address: https://nvmexpress.org/resources/specifications/  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The linkable identifier.  ***Since:*** vSphere API 7.0  | 
**controller_number** | **int** | The controller number uniquely identifies the NVME Controller within its HostSystem.  This should not be confused with Controller ID (see \&quot;NVM Express over Fabrics 1.0\&quot;, Section 4.2, \&quot;Controller model\&quot; for details), which only serves as an identifier within a particular NVME subsystem.  ***Since:*** vSphere API 7.0  | 
**subnqn** | **str** | The NVME subsystem qualified name.  Each NVME controller is associated with an NVME subsystem which can present a collection of controllers to the adapter. For more details, refer to: - \&quot;NVM Express over Fabrics 1.0\&quot;, Section 1.5.2,   \&quot;NVM Subsystem\&quot;.    ***Since:*** vSphere API 7.0  | 
**name** | **str** | Name of the controller.  Each controller has a name. For NVME over Fabrics controllers, it is generated when the controller is connected to an NVME over Fabrics adapter.  ***Since:*** vSphere API 7.0  | 
**associated_adapter** | [**HostHostBusAdapter**](HostHostBusAdapter.md) |  | 
**transport_type** | **str** | The transport type supported by the controller.  The set of possible values is described in *HostNvmeTransportType_enum*. For details, see: - \&quot;NVM Express over Fabrics 1.0\&quot;, Section 1.5.1,   \&quot;Fabrics and Transports\&quot;.    ***Since:*** vSphere API 7.0  | 
**fused_operation_supported** | **bool** | Indicates whether fused operations are supported by the controller.  An NVME controller may support fused operations. This is required to support shared storage, otherwise data corruption may occur. For more details, see: - \&quot;NVM Express 1.3\&quot;, Section 6.2, \&quot;Fused Operations\&quot;.    ***Since:*** vSphere API 7.0  | 
**number_of_queues** | **int** | The number of I/O queues allocated for the controller.  ***Since:*** vSphere API 7.0  | 
**queue_size** | **int** | The size of each of the I/O queues.  This will not be greater than the Maximum Queue Entries Supported (mqes) value for the controller. For more information, see: - \&quot;NVM Express 1.3\&quot;, section 3.1, \&quot;Register definition\&quot;.    ***Since:*** vSphere API 7.0  | 
**attached_namespace** | [**List[HostNvmeNamespace]**](HostNvmeNamespace.md) | List of NVME namespaces attached to the controller.  Namespaces provide access to a non-volatile storage medium which is part of the NVM subsystem. For an overview, see: - \&quot;NVM Express over Fabrics 1.0\&quot;, Section 1.5.2,   \&quot;NVM Subsystem\&quot;. - \&quot;NVM Express 1.3\&quot;, section 6.1, \&quot;Namespaces\&quot;.    ***Since:*** vSphere API 7.0  | [optional] 
**vendor_id** | **str** | The vendor ID of the controller, if available.  ***Since:*** vSphere API 7.0  | [optional] 
**model** | **str** | The model name of the controller, if available.  ***Since:*** vSphere API 7.0  | [optional] 
**serial_number** | **str** | The serial number of the controller, if available.  ***Since:*** vSphere API 7.0  | [optional] 
**firmware_version** | **str** | The firmware version of the controller, if available.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_nvme_controller import HostNvmeController

# TODO update the JSON string below
json = "{}"
# create an instance of HostNvmeController from a JSON string
host_nvme_controller_instance = HostNvmeController.from_json(json)
# print the JSON string representation of the object
print HostNvmeController.to_json()

# convert the object into a dict
host_nvme_controller_dict = host_nvme_controller_instance.to_dict()
# create an instance of HostNvmeController from a dict
host_nvme_controller_form_dict = host_nvme_controller.from_dict(host_nvme_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


