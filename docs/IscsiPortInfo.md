# IscsiPortInfo

The *IscsiPortInfo* data object describes the Virtual NIC that are bound to an iSCSI adapter and also it describes the candidate Virtual NICs that can be bound to a given iSCSI adapter.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** | Virtual NIC Name.  Contains the name of the Virtual NIC device. This may be unset in case where the bound Virtual NIC doesn&#39;t have the system object or where a candidate Physical NIC isn&#39;t associated with any Virtual NIC.  ***Since:*** vSphere API 5.0  | [optional] 
**vnic** | [**HostVirtualNic**](HostVirtualNic.md) |  | [optional] 
**pnic_device** | **str** | Physical NIC Name.  ***Since:*** vSphere API 5.0  | [optional] 
**pnic** | [**PhysicalNic**](PhysicalNic.md) |  | [optional] 
**switch_name** | **str** | Name of the virtual switch this Physical/Virtual NIC belongs.  May be unset if the vnicDevice and/or pnicDevice do not have a virtual switch associated with them.  ***Since:*** vSphere API 5.0  | [optional] 
**switch_uuid** | **str** | UUID of the virtual switch this Physical/Virtual NIC belongs.  May be unset if the vnicDevice and/or pnicDevice do not have a virtual switch associated with them or the associated switch is not VDS.  ***Since:*** vSphere API 5.0  | [optional] 
**portgroup_name** | **str** | Name of the portgroup to which this Virtual NIC belongs.  May be unset if the vnicDevice and/or pnicDevice do not have a Portgroup associated with them.  ***Since:*** vSphere API 5.0  | [optional] 
**portgroup_key** | **str** | Portgroup key to which this Virtual NIC belongs.  May be unset if the vnicDevice and/or pnicDevice do not have a Portgroup associated with them or the associated portgroup does is not of VDS type.  ***Since:*** vSphere API 5.0  | [optional] 
**port_key** | **str** | portkey to which this Virtual NIC belongs.  May be unset if the vnicDevice is not assigned to a specific port or the switch is not VDS.  ***Since:*** vSphere API 5.0  | [optional] 
**opaque_network_id** | **str** | ID of the Opaque network to which the virtual NIC is connected.  This property is set only when vnicDevice is associated with an opaque network.  ***Since:*** vSphere API 6.5  | [optional] 
**opaque_network_type** | **str** | Type of the Opaque network to which the virtual NIC is connected.  This property is set only when vnicDevice is associated with an opaque network.  ***Since:*** vSphere API 6.5  | [optional] 
**opaque_network_name** | **str** | Name of the Opaque network to which the virtual NIC is connected.  This property is set only when vnicDevice is associated with an opaque network.  ***Since:*** vSphere API 6.5  | [optional] 
**external_id** | **str** | An ID assigned to the vmkernel adapter by external management plane or controller.  This property is set only when vnicDevice is associated with an opaque network.  ***Since:*** vSphere API 6.5  | [optional] 
**compliance_status** | [**IscsiStatus**](IscsiStatus.md) |  | [optional] 
**path_status** | **str** | A status, as defined in *IscsiPortInfoPathStatus_enum*, indicating the existing storage paths dependency level on a given Virtual NIC.  May be unset in the candidate NIC list.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.iscsi_port_info import IscsiPortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiPortInfo from a JSON string
iscsi_port_info_instance = IscsiPortInfo.from_json(json)
# print the JSON string representation of the object
print IscsiPortInfo.to_json()

# convert the object into a dict
iscsi_port_info_dict = iscsi_port_info_instance.to_dict()
# create an instance of IscsiPortInfo from a dict
iscsi_port_info_form_dict = iscsi_port_info.from_dict(iscsi_port_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


