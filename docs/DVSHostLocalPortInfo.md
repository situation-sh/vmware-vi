# DVSHostLocalPortInfo

This data object type describes the information about the host local port.  A host local port is created to resurrect the management network connection on a VMkernel Virtual NIC.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_uuid** | **str** | UUID of the vSphere Distributed Switch that management interface is connected to.  ***Since:*** vSphere API 5.1  | 
**port_key** | **str** | Portkey of the DVPort that management interface is now connected to.  ***Since:*** vSphere API 5.1  | 
**setting** | [**DVPortSetting**](DVPortSetting.md) |  | 
**vnic** | **str** | The Virtual NIC device connected to this port  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.dvs_host_local_port_info import DVSHostLocalPortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DVSHostLocalPortInfo from a JSON string
dvs_host_local_port_info_instance = DVSHostLocalPortInfo.from_json(json)
# print the JSON string representation of the object
print DVSHostLocalPortInfo.to_json()

# convert the object into a dict
dvs_host_local_port_info_dict = dvs_host_local_port_info_instance.to_dict()
# create an instance of DVSHostLocalPortInfo from a dict
dvs_host_local_port_info_form_dict = dvs_host_local_port_info.from_dict(dvs_host_local_port_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


