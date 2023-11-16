# PhysicalNic

This data object type describes the physical network adapter as seen by the primary operating system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The linkable identifier.  | [optional] 
**device** | **str** | The device name of the physical network adapter.  | 
**pci** | **str** | Device hash of the PCI device corresponding to this physical network adapter.  | 
**driver** | **str** | The name of the driver.  From command line: esxcli network nic get  | [optional] 
**driver_version** | **str** | The version of the physical network adapter operating system driver.  | [optional] 
**firmware_version** | **str** | The version of the firmware running in the network adapter.  | [optional] 
**link_speed** | [**PhysicalNicLinkInfo**](PhysicalNicLinkInfo.md) |  | [optional] 
**valid_link_specification** | [**List[PhysicalNicLinkInfo]**](PhysicalNicLinkInfo.md) | The valid combinations of speed and duplexity for this physical network adapter.  The speed and the duplex settings usually must be configured as a pair. This array lists all the valid combinations available for a physical network adapter.  Autonegotiate is not listed as one of the combinations supported. If is implicitly supported by the physical network adapter unless *PhysicalNic.autoNegotiateSupported* is set to false.  | [optional] 
**spec** | [**PhysicalNicSpec**](PhysicalNicSpec.md) |  | 
**wake_on_lan_supported** | **bool** | Flag indicating whether the NIC is wake-on-LAN capable  ***Since:*** VI API 2.5  | 
**mac** | **str** | The media access control (MAC) address of the physical network adapter.  ***Since:*** VI API 2.5  | 
**fcoe_configuration** | [**FcoeConfig**](FcoeConfig.md) |  | [optional] 
**vm_direct_path_gen2_supported** | **bool** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  Flag indicating whether the NIC supports VMDirectPath Gen 2.  Note that this is only an indicator of the capabilities of this NIC, not of the whole host.  If the host software is not capable of VMDirectPath Gen 2, this property will be unset, as the host cannot provide information on the NIC capability.  See also *HostCapability.vmDirectPathGen2Supported*.  ***Since:*** vSphere API 4.1  | [optional] 
**vm_direct_path_gen2_supported_mode** | **str** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *PhysicalNic.vmDirectPathGen2Supported* is true, this property advertises the VMDirectPath Gen 2 mode supported by this NIC (chosen from *PhysicalNicVmDirectPathGen2SupportedMode_enum*).  A mode may require that the associated vSphere Distributed Switch have a particular ProductSpec in order for network passthrough to be possible.  ***Since:*** vSphere API 4.1  | [optional] 
**resource_pool_scheduler_allowed** | **bool** | Flag indicating whether the NIC allows resource pool based scheduling for network I/O control.  ***Since:*** vSphere API 4.1  | [optional] 
**resource_pool_scheduler_disallowed_reason** | **List[str]** | If *PhysicalNic.resourcePoolSchedulerAllowed* is false, this property advertises the reason for disallowing resource scheduling on this NIC.  The reasons may be one of *PhysicalNicResourcePoolSchedulerDisallowedReason_enum*  ***Since:*** vSphere API 4.1  | [optional] 
**auto_negotiate_supported** | **bool** | If set the flag indicates if the physical network adapter supports autonegotiate.  ***Since:*** vSphere API 4.1  | [optional] 
**enhanced_networking_stack_supported** | **bool** | If set the flag indicates whether a physical nic supports Enhanced Networking Stack driver  ***Since:*** vSphere API 6.7  | [optional] 
**ens_interrupt_supported** | **bool** | If set the flag indicates whether a physical nic supports Enhanced Networking Stack interrupt mode  ***Since:*** vSphere API 7.0  | [optional] 
**rdma_device** | [**HostRdmaDevice**](HostRdmaDevice.md) |  | [optional] 
**dpu_id** | **str** | The identifier of the DPU by which the physical NIC is backed.  When physical NIC is not backed by DPU, dpuId will be unset.  | [optional] 

## Example

```python
from vmware_vi.models.physical_nic import PhysicalNic

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNic from a JSON string
physical_nic_instance = PhysicalNic.from_json(json)
# print the JSON string representation of the object
print PhysicalNic.to_json()

# convert the object into a dict
physical_nic_dict = physical_nic_instance.to_dict()
# create an instance of PhysicalNic from a dict
physical_nic_form_dict = physical_nic.from_dict(physical_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


