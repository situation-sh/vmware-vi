# DVPortStatus

The *DVPortStatus* data object contains runtime information about a *DistributedVirtualPort*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_up** | **bool** | Indicates whether the port is in linkUp status.  ***Since:*** vSphere API 4.0  | 
**blocked** | **bool** | Indicates whether the port is blocked by switch implementation.  ***Since:*** vSphere API 4.0  | 
**vlan_ids** | [**List[NumericRange]**](NumericRange.md) | VLAN ID of the port.  ***Since:*** vSphere API 4.0  | [optional] 
**trunking_mode** | **bool** | True if the port VLAN tagging/stripping is disabled.  ***Since:*** vSphere API 4.0  | [optional] 
**mtu** | **int** | Maximum transmission unit (MTU) of the port.  You can set the MTU only at the switch level (*VMwareDVSConfigSpec*). If you attempt to change it at the portgroup or port level, the Server throws an exception.  ***Since:*** vSphere API 4.0  | [optional] 
**link_peer** | **str** | Name of the connected entity.  ***Since:*** vSphere API 4.0  | [optional] 
**mac_address** | **str** | The MAC address that is used at this port.  ***Since:*** vSphere API 4.0  | [optional] 
**status_detail** | **str** | Additional information regarding the current status of the port.  ***Since:*** vSphere API 4.1  | [optional] 
**vm_direct_path_gen2_active** | **bool** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  Indicates whether VMDirectPath Gen 2 is active on this port.  If false, the reason(s) for inactivity will be provided in one or more of *DVPortStatus.vmDirectPathGen2InactiveReasonNetwork*, *DVPortStatus.vmDirectPathGen2InactiveReasonOther*, and *DVPortStatus.vmDirectPathGen2InactiveReasonExtended*.  If the host software is not capable of VMDirectPath Gen 2, this property will be unset. See *HostCapability*.*HostCapability.vmDirectPathGen2Supported*.  ***Since:*** vSphere API 4.1  | [optional] 
**vm_direct_path_gen2_inactive_reason_network** | **List[str]** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *DVPortStatus.vmDirectPathGen2Active* is false, this array will be populated with reasons for the inactivity that are related to network state or configuration.  The reasons are chosen from the *DVPortStatusVmDirectPathGen2InactiveReasonNetwork_enum* values.  Other reasons for inactivity will be provided in *DVPortStatus.vmDirectPathGen2InactiveReasonOther*. If there is a reason for inactivity that cannot be described by the available constants, *DVPortStatus.vmDirectPathGen2InactiveReasonExtended* will be populated with an additional explanation provided by the platform.  Note that this list of reasons is not guaranteed to be exhaustive.  ***Since:*** vSphere API 4.1  | [optional] 
**vm_direct_path_gen2_inactive_reason_other** | **List[str]** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *DVPortStatus.vmDirectPathGen2Active* is false, this array will be populated with reasons for the inactivity that are not related to network state or configuration.  The reasons are chosen from the *DVPortStatusVmDirectPathGen2InactiveReasonOther_enum* values.  Network-related reasons for inactivity will be provided in *DVPortStatus.vmDirectPathGen2InactiveReasonNetwork*. If there is a reason for inactivity that cannot be described by the available constants, *DVPortStatus.vmDirectPathGen2InactiveReasonExtended* will be populated with an additional explanation provided by the platform.  Note that this list of reasons is not guaranteed to be exhaustive.  See also *HostCapability.vmDirectPathGen2Supported*.  ***Since:*** vSphere API 4.1  | [optional] 
**vm_direct_path_gen2_inactive_reason_extended** | **str** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *DVPortStatus.vmDirectPathGen2Active* is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) listed in *DVPortStatus.vmDirectPathGen2InactiveReasonNetwork* and/or *DVPortStatus.vmDirectPathGen2InactiveReasonOther*.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.dv_port_status import DVPortStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortStatus from a JSON string
dv_port_status_instance = DVPortStatus.from_json(json)
# print the JSON string representation of the object
print DVPortStatus.to_json()

# convert the object into a dict
dv_port_status_dict = dv_port_status_instance.to_dict()
# create an instance of DVPortStatus from a dict
dv_port_status_form_dict = dv_port_status.from_dict(dv_port_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


